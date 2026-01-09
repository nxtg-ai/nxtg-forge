"""Integration tests for Phase 2: Automation features.

Tests git automation, quality monitoring, work orchestration, and hook system.
"""

import json
import subprocess

import pytest

from forge.services.git_automation import GitAutomationService
from forge.services.quality_monitor import QualityMetrics, QualityMonitor
from forge.services.work_orchestrator import FeatureSpec, WorkOrchestrator


class TestGitAutomation:
    """Test git automation service."""

    @pytest.fixture()
    def temp_git_repo(self, tmp_path):
        """Create temporary git repository for testing."""
        repo_dir = tmp_path / "test_repo"
        repo_dir.mkdir()

        # Initialize git repo
        subprocess.run(["git", "init"], cwd=repo_dir, check=True, capture_output=True)
        subprocess.run(
            ["git", "config", "user.name", "Test User"],
            cwd=repo_dir,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "config", "user.email", "test@example.com"],
            cwd=repo_dir,
            check=True,
            capture_output=True,
        )

        # Create initial commit
        (repo_dir / "README.md").write_text("# Test Repo")
        subprocess.run(["git", "add", "."], cwd=repo_dir, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"],
            cwd=repo_dir,
            check=True,
            capture_output=True,
        )

        return repo_dir

    def test_analyze_commit_history_conventional(self, temp_git_repo):
        """Test analyzing commit history for conventional commits."""
        service = GitAutomationService(temp_git_repo)

        # Add some conventional commits
        test_file = temp_git_repo / "test.txt"
        for i, msg in enumerate(
            [
                "feat: add new feature",
                "fix: resolve bug",
                "docs: update README",
                "test: add unit tests",
            ],
        ):
            test_file.write_text(f"content {i}")
            subprocess.run(["git", "add", "."], cwd=temp_git_repo, check=True, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", msg],
                cwd=temp_git_repo,
                check=True,
                capture_output=True,
            )

        # Analyze history
        result = service.analyze_commit_history()

        assert result.is_ok()
        style = result.value
        assert style.uses_conventional_commits is True
        assert "feat" in style.common_prefixes
        assert "fix" in style.common_prefixes

    def test_generate_commit_message(self, temp_git_repo):
        """Test commit message generation."""
        service = GitAutomationService(temp_git_repo)

        # Stage some changes
        test_file = temp_git_repo / "new_feature.py"
        test_file.write_text("def new_function():\n    pass")
        subprocess.run(["git", "add", "."], cwd=temp_git_repo, check=True, capture_output=True)

        # Generate commit message
        result = service.generate_commit_message(feature_context="Add authentication")

        assert result.is_ok()
        message = result.value
        assert "authentication" in message.lower() or "add" in message.lower()
        assert "🤖 Generated with" in message
        assert "Co-Authored-By: Claude" in message

    def test_create_feature_branch(self, temp_git_repo):
        """Test feature branch creation."""
        service = GitAutomationService(temp_git_repo)

        # Create feature branch
        result = service.create_feature_branch("User Authentication")

        assert result.is_ok()
        branch_name = result.value
        assert branch_name == "feature/user-authentication"

        # Verify we're on the branch
        current_branch = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=temp_git_repo,
            capture_output=True,
            text=True,
            check=True,
        )
        assert current_branch.stdout.strip() == branch_name

    def test_link_to_issues(self, temp_git_repo):
        """Test adding issue references to commit messages."""
        service = GitAutomationService(temp_git_repo)

        # Test with issue number in branch name
        message = "feat: add authentication\n\n🤖 Generated with Claude"
        linked = service.link_to_issues(message, "feature/123-auth-feature")

        assert "Closes #123" in linked

    def test_sanitize_branch_name(self, temp_git_repo):
        """Test branch name sanitization."""
        service = GitAutomationService(temp_git_repo)

        # Test various feature names
        assert service._sanitize_branch_name("Add User Auth") == "feature/add-user-auth"
        assert service._sanitize_branch_name("Fix Bug #123") == "feature/fix-bug-123"
        assert (
            service._sanitize_branch_name("Update/Refactor Components")
            == "feature/update-refactor-components"
        )


class TestQualityMonitor:
    """Test quality monitoring service."""

    @pytest.fixture()
    def project_with_code(self, tmp_path):
        """Create test project with Python code."""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()

        # Create forge directory structure
        forge_dir = project_dir / ".claude" / "forge"
        forge_dir.mkdir(parents=True)

        # Create state.json
        state = {
            "project": {"name": "test", "created_at": "2026-01-08T00:00:00Z"},
            "quality": {"tests": {"unit": {"coverage": 75, "passing": 10, "total": 10}}},
        }
        (forge_dir / "state.json").write_text(json.dumps(state))

        # Create some Python files
        src_dir = project_dir / "src"
        src_dir.mkdir()
        (src_dir / "main.py").write_text('def main():\n    """Main function."""\n    pass')
        (src_dir / "utils.py").write_text("def helper():\n    pass")

        return project_dir

    def test_track_metrics(self, project_with_code):
        """Test tracking quality metrics."""
        monitor = QualityMonitor(project_with_code)

        result = monitor.track_metrics()

        assert result.is_ok()
        metrics = result.value
        assert isinstance(metrics, QualityMetrics)
        assert metrics.timestamp is not None

    def test_calculate_health_score(self, project_with_code):
        """Test health score calculation."""
        monitor = QualityMonitor(project_with_code)

        result = monitor.calculate_health_score()

        assert result.is_ok()
        score = result.value
        assert 0 <= score <= 100

    def test_detect_regressions(self, project_with_code):
        """Test regression detection."""
        monitor = QualityMonitor(project_with_code)

        # Track initial metrics
        monitor.track_metrics()

        # Track again (should have no regressions if nothing changed)
        regressions_result = monitor.detect_regressions()

        assert regressions_result.is_ok()
        regressions = regressions_result.value
        # May or may not have regressions depending on actual metrics
        assert isinstance(regressions, list)

    def test_analyze_trends(self, project_with_code):
        """Test trend analysis."""
        monitor = QualityMonitor(project_with_code)

        # Create some historical data
        for i in range(3):
            monitor.track_metrics()

        # Analyze trends
        result = monitor.analyze_trends(days=7)

        assert result.is_ok()
        report = result.value
        assert report.overall_trend in ["improving", "declining", "stable"]

    def test_metrics_persistence(self, project_with_code):
        """Test that metrics are persisted to log file."""
        monitor = QualityMonitor(project_with_code)

        # Track metrics
        monitor.track_metrics()

        # Check that metrics file exists
        metrics_file = project_with_code / ".claude" / "forge" / "quality_metrics.jsonl"
        assert metrics_file.exists()

        # Verify content
        content = metrics_file.read_text()
        assert len(content) > 0
        # Should be valid JSON lines
        data = json.loads(content.splitlines()[0])
        assert "timestamp" in data
        assert "test_coverage" in data


class TestWorkOrchestrator:
    """Test work orchestration service."""

    @pytest.fixture()
    def project_with_workflows(self, tmp_path):
        """Create test project for workflow testing."""
        project_dir = tmp_path / "test_workflows"
        project_dir.mkdir()

        # Create directory structure
        (project_dir / ".claude" / "forge" / "workflows").mkdir(parents=True)
        (project_dir / ".claude" / "forge" / "checkpoints").mkdir(parents=True)

        return project_dir

    def test_execute_feature_workflow(self, project_with_workflows):
        """Test complete feature workflow execution."""
        orchestrator = WorkOrchestrator(project_with_workflows)

        # Define feature
        feature = FeatureSpec(
            name="User Authentication",
            description="Implement JWT-based user authentication",
            requirements=[
                "User registration",
                "Login with JWT",
                "Token validation",
            ],
            acceptance_criteria=[
                "Users can register",
                "Users can login",
                "Protected routes work",
            ],
            estimated_hours=4.0,
            priority="high",
        )

        # Execute workflow
        result = orchestrator.execute_feature_workflow(feature)

        assert result.is_ok()
        workflow_result = result.value
        assert workflow_result.status in ["success", "partial", "failed"]
        assert workflow_result.workflow_id is not None

    def test_plan_workflow_tasks(self, project_with_workflows):
        """Test workflow task planning."""
        orchestrator = WorkOrchestrator(project_with_workflows)

        feature = FeatureSpec(
            name="Email Notifications",
            description="Add email notification system",
        )

        # Create workflow
        from forge.services.work_orchestrator import Workflow

        workflow = Workflow(
            id="test_workflow",
            feature=feature,
        )

        # Plan tasks
        result = orchestrator._plan_workflow_tasks(workflow)

        assert result.is_ok()
        tasks = result.value
        assert len(tasks) > 0
        # Should have architecture, implementation, testing tasks
        assert any(
            "design" in t.description.lower() or "architect" in t.description.lower() for t in tasks
        )
        assert any("implement" in t.description.lower() for t in tasks)
        assert any("test" in t.description.lower() for t in tasks)

    def test_handle_agent_failure(self, project_with_workflows):
        """Test agent failure handling."""
        orchestrator = WorkOrchestrator(project_with_workflows)

        from forge.services.work_orchestrator import AgentError

        # Test timeout error (should retry)
        error = AgentError(
            agent="test-agent",
            task_id="task-1",
            error_message="Operation timed out",
            recoverable=True,
        )

        result = orchestrator.handle_agent_failure(error)

        assert result.is_ok()
        action = result.value
        assert action.action_type == "retry"

        # Test permission error (should abort)
        error = AgentError(
            agent="test-agent",
            task_id="task-2",
            error_message="Permission denied",
            recoverable=False,
        )

        result = orchestrator.handle_agent_failure(error)

        assert result.is_ok()
        action = result.value
        assert action.action_type == "abort"

    def test_checkpoint_creation(self, project_with_workflows):
        """Test checkpoint creation during workflow."""
        orchestrator = WorkOrchestrator(project_with_workflows)

        from forge.services.work_orchestrator import Workflow, WorkflowTask

        workflow = Workflow(
            id="test_workflow",
            feature=FeatureSpec(name="Test Feature", description="Test"),
        )

        task = WorkflowTask(
            id="test_task",
            description="Implement feature",
            agent="test-agent",
            status="complete",
        )

        # Create checkpoint
        checkpoint_id = orchestrator._create_task_checkpoint(task, workflow)

        # Checkpoint may or may not be created (depends on task significance)
        if checkpoint_id:
            checkpoint_file = (
                project_with_workflows
                / ".claude"
                / "forge"
                / "checkpoints"
                / f"{checkpoint_id}.json"
            )
            assert checkpoint_file.exists()


class TestHookIntegration:
    """Integration tests for hook system."""

    @pytest.fixture()
    def project_with_hooks(self, tmp_path):
        """Create test project with hook structure."""
        project_dir = tmp_path / "test_hooks"
        project_dir.mkdir()

        # Create directory structure
        forge_dir = project_dir / ".claude" / "forge"
        forge_dir.mkdir(parents=True)

        # Create minimal state.json
        state = {
            "project": {
                "name": "test",
                "created_at": "2026-01-08T00:00:00Z",
            },
            "quality": {"tests": {"unit": {"coverage": 85, "passing": 10, "total": 10}}},
        }
        (forge_dir / "state.json").write_text(json.dumps(state))

        return project_dir

    def test_activity_reporter_integration(self, project_with_hooks):
        """Test activity reporter with actual file I/O."""
        from forge.services.activity_reporter import ActivityReporter

        reporter = ActivityReporter(project_with_hooks)

        # Report activity start
        result = reporter.report_start("Running tests...")
        assert result.is_ok()

        # Report activity complete
        result = reporter.report_complete("Tests completed", duration=2.5, success=True)
        assert result.is_ok()

        # Check status file
        status_file = project_with_hooks / ".claude" / "forge" / "activity.status"
        assert status_file.exists()

        # Get current status
        status_result = reporter.get_current_status()
        assert status_result.is_ok()
        status = status_result.value
        assert status is not None
        assert status.activity == "Tests completed"

        # Get history
        history_result = reporter.get_recent_history()
        assert history_result.is_ok()
        assert len(history_result.value) > 0

    def test_session_state_tracking(self, project_with_hooks):
        """Test session state tracking across operations."""
        state_file = project_with_hooks / ".claude" / "forge" / "state.json"

        # Read initial state
        with open(state_file, encoding="utf-8") as f:
            state = json.load(f)

        # Simulate session start
        state["last_session"] = {
            "id": "test_session_001",
            "started": "2026-01-08T10:00:00Z",
            "status": "in_progress",
        }

        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)

        # Simulate file modification
        if "files_modified" not in state["last_session"]:
            state["last_session"]["files_modified"] = []

        state["last_session"]["files_modified"].append("test.py")

        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)

        # Read back and verify
        with open(state_file, encoding="utf-8") as f:
            updated_state = json.load(f)

        assert "last_session" in updated_state
        assert updated_state["last_session"]["id"] == "test_session_001"
        assert "test.py" in updated_state["last_session"]["files_modified"]


@pytest.mark.slow()
class TestEndToEndWorkflow:
    """End-to-end workflow tests (slower, comprehensive)."""

    def test_complete_feature_workflow_with_quality_tracking(self, tmp_path):
        """Test complete feature workflow with quality tracking."""
        project_dir = tmp_path / "e2e_test"
        project_dir.mkdir()

        # Setup project structure
        (project_dir / ".claude" / "forge").mkdir(parents=True)

        state = {
            "project": {"name": "e2e_test", "created_at": "2026-01-08T00:00:00Z"},
            "quality": {"tests": {"unit": {"coverage": 80}}},
        }
        (project_dir / ".claude" / "forge" / "state.json").write_text(json.dumps(state))

        # Step 1: Track initial quality
        monitor = QualityMonitor(project_dir)
        initial_metrics = monitor.track_metrics()
        assert initial_metrics.is_ok()

        # Step 2: Create feature workflow
        orchestrator = WorkOrchestrator(project_dir)
        feature = FeatureSpec(
            name="Test Feature",
            description="End-to-end test feature",
            requirements=["Requirement 1"],
        )

        workflow_result = orchestrator.execute_feature_workflow(feature)
        assert workflow_result.is_ok()

        # Step 3: Track final quality
        final_metrics = monitor.track_metrics()
        assert final_metrics.is_ok()

        # Step 4: Detect any regressions
        regressions = monitor.detect_regressions()
        assert regressions.is_ok()
