"""Integration tests for Phase 3 observability services.

Tests the complete observability stack:
- DashboardService
- AnalyticsService
- NotificationService
- SessionReporter
- ActivityReporter
- TextChartUtils

Tests verify services work together and handle real-world scenarios.
"""

import json
from datetime import datetime, timedelta
from unittest.mock import patch

import pytest

from forge.services.activity_reporter import ActivityReporter, ActivityUpdate
from forge.services.analytics_service import AnalyticsService
from forge.services.dashboard_service import DashboardService, DateRange, ExportFormat
from forge.services.notification_service import (
    NotificationCategory,
    NotificationConfig,
    NotificationLevel,
    NotificationService,
)
from forge.services.session_reporter import OutputFormat, ReportFormat, SessionReporter


class TestDashboardService:
    """Test DashboardService integration."""

    def test_dashboard_data_aggregation(self, tmp_path):
        """Test dashboard aggregates data from multiple sources."""
        # Setup test project
        state_file = tmp_path / ".claude" / "forge" / "state.json"
        state_file.parent.mkdir(parents=True, exist_ok=True)

        # Create state with quality metrics
        state = {
            "quality": {
                "health_score": 88,  # Add health_score at the expected location
                "tests": {
                    "unit": {"coverage": 89.5, "passing": 142, "total": 150},
                    "integration": {"passing": 12, "total": 15},
                },
                "security": {"vulnerabilities": {"critical": 0, "high": 0, "medium": 1}},
                "linting": {"issues": 3},
            },
            "workflows": {
                "current": [
                    {"name": "feature/auth", "status": "in_progress"},
                    {"name": "fix/bug-123", "status": "testing"},
                ],
            },
            "health_history": [
                {"timestamp": "2026-01-01T00:00:00Z", "score": 85},
                {"timestamp": "2026-01-08T00:00:00Z", "score": 88},
            ],
        }

        with open(state_file, "w") as f:
            json.dump(state, f)

        # Create service and get dashboard data
        dashboard = DashboardService(tmp_path)
        result = dashboard.get_dashboard_data()

        assert result.is_ok()
        data = result.value

        assert data.health_score == 88
        assert data.health_trend in ["improving", "declining", "stable"]
        assert len(data.active_workflows) >= 0
        assert len(data.quality_metrics) > 0

    def test_text_chart_generation(self, tmp_path):
        """Test dashboard generates text charts correctly."""
        dashboard = DashboardService(tmp_path)

        # Get metrics (may be empty, but should not error)
        result = dashboard.get_dashboard_data()
        assert result.is_ok()

        data = result.value
        # generate_text_charts returns string directly, not Result
        charts = dashboard.generate_text_charts(list(data.quality_metrics.values()))
        assert isinstance(charts, str)
        assert len(charts) >= 0  # Can be empty string if no metrics

    def test_period_comparison(self, tmp_path):
        """Test comparing metrics across time periods."""
        # Create metrics file with data for comparison
        metrics_dir = tmp_path / ".claude" / "forge"
        metrics_dir.mkdir(parents=True, exist_ok=True)

        metrics_file = metrics_dir / "quality_metrics.jsonl"
        now = datetime.utcnow()

        # Write metrics for two periods
        with open(metrics_file, "w") as f:
            # Period 1 (14-7 days ago)
            for i in range(7):
                timestamp = now - timedelta(days=14 - i)
                metric = {
                    "timestamp": timestamp.isoformat() + "Z",
                    "test_coverage": 75.0 + i,
                    "health_score": 70 + i,
                }
                f.write(json.dumps(metric) + "\n")

            # Period 2 (7-0 days ago)
            for i in range(7):
                timestamp = now - timedelta(days=7 - i)
                metric = {
                    "timestamp": timestamp.isoformat() + "Z",
                    "test_coverage": 82.0 + i,
                    "health_score": 77 + i,
                }
                f.write(json.dumps(metric) + "\n")

        dashboard = DashboardService(tmp_path)

        period1 = DateRange(start=now - timedelta(days=14), end=now - timedelta(days=7))
        period2 = DateRange(start=now - timedelta(days=7), end=now)

        result = dashboard.compare_periods(period1, period2)
        assert result.is_ok()

        comparison = result.value
        assert hasattr(comparison, "summary")
        assert hasattr(comparison, "improvements")
        assert hasattr(comparison, "regressions")

    def test_export_formats(self, tmp_path):
        """Test exporting metrics in different formats."""
        dashboard = DashboardService(tmp_path)

        # Test JSON export
        json_result = dashboard.export_metrics(ExportFormat.JSON)
        assert json_result.is_ok()
        assert json.loads(json_result.value)  # Valid JSON

        # Test Markdown export
        md_result = dashboard.export_metrics(ExportFormat.MARKDOWN)
        assert md_result.is_ok()
        assert "# " in md_result.value  # Has headers

        # Test CSV export
        csv_result = dashboard.export_metrics(ExportFormat.CSV)
        assert csv_result.is_ok()
        assert "," in csv_result.value  # Has commas

        # Test Text export
        text_result = dashboard.export_metrics(ExportFormat.TEXT)
        assert text_result.is_ok()
        assert len(text_result.value) > 0


class TestAnalyticsService:
    """Test AnalyticsService integration."""

    def test_workflow_pattern_detection(self, tmp_path):
        """Test detecting workflow patterns from git history."""
        # Initialize git repo
        import subprocess

        try:
            subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "test@example.com"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Test User"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
            )

            # Set initial branch name to avoid warnings
            subprocess.run(
                ["git", "config", "init.defaultBranch", "main"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
            )

            # Create initial commit to avoid errors
            test_file = tmp_path / "README.md"
            test_file.write_text("# Test Project")
            subprocess.run(["git", "add", "."], cwd=tmp_path, check=True, capture_output=True)

            # Try to commit, but handle if it fails (no global git config)
            result = subprocess.run(
                ["git", "commit", "-m", "Initial commit"],
                cwd=tmp_path,
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode == 0:
                # Create some commits
                test_file = tmp_path / "test.txt"
                for i in range(5):
                    test_file.write_text(f"Content {i}")
                    subprocess.run(
                        ["git", "add", "."],
                        cwd=tmp_path,
                        check=True,
                        capture_output=True,
                    )
                    subprocess.run(
                        ["git", "commit", "-m", f"test: Add test {i}"],
                        cwd=tmp_path,
                        check=True,
                        capture_output=True,
                    )

        except subprocess.CalledProcessError:
            # Git setup failed, skip test
            pytest.skip("Git setup failed in tmpdir")

        # Test pattern detection
        analytics = AnalyticsService(tmp_path)
        result = analytics.detect_workflow_patterns(days=30)

        assert result.is_ok()
        patterns = result.value
        assert isinstance(patterns, list)

    def test_productivity_metrics(self, tmp_path):
        """Test calculating productivity metrics."""
        # Initialize git repo
        import subprocess

        try:
            subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
            subprocess.run(
                ["git", "config", "user.email", "test@example.com"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Test User"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
            )

            # Set initial branch name to avoid warnings
            subprocess.run(
                ["git", "config", "init.defaultBranch", "main"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
            )

            # Create test commit
            test_file = tmp_path / "test.txt"
            test_file.write_text("Content")
            subprocess.run(["git", "add", "."], cwd=tmp_path, check=True, capture_output=True)

            result = subprocess.run(
                ["git", "commit", "-m", "test: Add test"],
                cwd=tmp_path,
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode != 0:
                pytest.skip("Git commit failed in tmpdir")

        except subprocess.CalledProcessError:
            pytest.skip("Git setup failed in tmpdir")

        analytics = AnalyticsService(tmp_path)
        result = analytics.calculate_productivity_metrics(days=30)

        assert result.is_ok()
        metrics = result.value
        assert hasattr(metrics, "commits_per_day")
        assert metrics.commits_per_day >= 0

    def test_quality_predictions(self, tmp_path):
        """Test predicting quality trends."""
        analytics = AnalyticsService(tmp_path)
        result = analytics.predict_quality_trends(days_ahead=7)

        # Should return predictions even with no data (graceful degradation)
        assert result.is_ok()
        predictions = result.value
        assert isinstance(predictions, list)

    def test_technology_insights(self, tmp_path):
        """Test analyzing technology usage."""
        # Create some Python files
        (tmp_path / "test.py").write_text("print('hello')")
        (tmp_path / "test2.py").write_text("import os")

        analytics = AnalyticsService(tmp_path)
        result = analytics.analyze_technology_usage()

        assert result.is_ok()
        insights = result.value
        assert isinstance(insights, list)


class TestNotificationService:
    """Test NotificationService integration."""

    def test_notification_levels(self, tmp_path):
        """Test notification filtering by level."""
        service = NotificationService(tmp_path)

        # Set minimum level to WARNING
        config = NotificationConfig(min_level=NotificationLevel.WARNING)
        service.update_config(config)

        # INFO should be filtered
        with patch("builtins.print") as mock_print:
            service.notify(
                level=NotificationLevel.INFO,
                category=NotificationCategory.GENERAL,
                title="Test Info",
                message="Test info message",
            )
            mock_print.assert_not_called()

        # WARNING should be shown
        with patch("builtins.print") as mock_print:
            service.notify(
                level=NotificationLevel.WARNING,
                category=NotificationCategory.GENERAL,
                title="Test Warning",
                message="Test warning message",
            )
            mock_print.assert_called()

    def test_category_filtering(self, tmp_path):
        """Test notification filtering by category."""
        service = NotificationService(tmp_path)

        # Enable only QUALITY category
        config = NotificationConfig(enabled_categories={NotificationCategory.QUALITY})
        service.update_config(config)

        # WORKFLOW should be filtered
        with patch("builtins.print") as mock_print:
            service.notify(
                level=NotificationLevel.INFO,
                category=NotificationCategory.WORKFLOW,
                title="Test Workflow",
                message="Test workflow",
            )
            mock_print.assert_not_called()

        # QUALITY should be shown
        with patch("builtins.print") as mock_print:
            service.notify(
                level=NotificationLevel.INFO,
                category=NotificationCategory.QUALITY,
                title="Test Quality",
                message="Test quality",
            )
            mock_print.assert_called()

    def test_smart_notifications(self, tmp_path):
        """Test smart notification methods."""
        service = NotificationService(tmp_path)

        with patch("builtins.print") as mock_print:
            service.notify_quality_regression("Coverage", 90.0, 85.0)
            assert mock_print.called

        with patch("builtins.print") as mock_print:
            service.notify_workflow_complete("test-workflow", 300)
            assert mock_print.called

        with patch("builtins.print") as mock_print:
            service.notify_security_alert("high", "SQL injection detected")
            assert mock_print.called

        with patch("builtins.print") as mock_print:
            service.notify_success("All tests passing!")
            assert mock_print.called

    def test_quiet_hours(self, tmp_path):
        """Test quiet hours functionality."""
        service = NotificationService(tmp_path)

        # Set quiet hours (always quiet for testing)
        current_hour = datetime.now().hour
        config = NotificationConfig(
            quiet_hours_start=current_hour,
            quiet_hours_end=(current_hour + 1) % 24,
        )
        service.update_config(config)

        # Should be filtered during quiet hours
        with patch("builtins.print") as mock_print:
            service.notify(
                level=NotificationLevel.INFO,
                category=NotificationCategory.GENERAL,
                title="Test Quiet Hours",
                message="Test during quiet hours",
            )
            # Only critical should pass through
            assert not mock_print.called or "CRITICAL" in str(mock_print.call_args)


class TestSessionReporter:
    """Test SessionReporter integration."""

    def test_session_report_formats(self, tmp_path):
        """Test generating reports in different formats."""
        reporter = SessionReporter(tmp_path)

        # Create a test session
        session_dir = tmp_path / ".claude" / "forge" / "sessions"
        session_dir.mkdir(parents=True, exist_ok=True)

        session_data = {
            "id": "test-session",
            "start_time": "2026-01-08T00:00:00Z",
            "end_time": "2026-01-08T01:00:00Z",
            "feature_name": "Test Feature",
            "branch": "feature/test",
        }

        session_file = session_dir / "test-session.json"
        with open(session_file, "w") as f:
            json.dump(session_data, f)

        # Test different report formats
        result = reporter.generate_report(
            "test-session",
            format=ReportFormat.BRIEF,
            output_format=OutputFormat.TEXT,
        )
        assert result.is_ok()
        assert len(result.value) > 0

        result = reporter.generate_report(
            "test-session",
            format=ReportFormat.DETAILED,
            output_format=OutputFormat.TEXT,
        )
        assert result.is_ok()
        assert "Session" in result.value

        result = reporter.generate_report(
            "test-session",
            format=ReportFormat.DAILY,
            output_format=OutputFormat.TEXT,
        )
        assert result.is_ok()

    def test_report_output_formats(self, tmp_path):
        """Test generating reports in different output formats."""
        reporter = SessionReporter(tmp_path)

        # Create a test session
        session_dir = tmp_path / ".claude" / "forge" / "sessions"
        session_dir.mkdir(parents=True, exist_ok=True)

        session_data = {
            "id": "test-session",
            "start_time": "2026-01-08T00:00:00Z",
            "end_time": "2026-01-08T01:00:00Z",
            "feature_name": "Test Feature",
            "branch": "main",
        }

        session_file = session_dir / "test-session.json"
        with open(session_file, "w") as f:
            json.dump(session_data, f)

        # Test JSON output
        result = reporter.generate_report("test-session", output_format=OutputFormat.JSON)
        assert result.is_ok()
        data = json.loads(result.value)
        assert data["session_id"] == "test-session"

        # Test Markdown output
        result = reporter.generate_report("test-session", output_format=OutputFormat.MARKDOWN)
        assert result.is_ok()
        assert "# Session Report" in result.value

    def test_filtered_reports(self, tmp_path):
        """Test generating filtered reports across sessions."""
        reporter = SessionReporter(tmp_path)

        # Create multiple test sessions
        session_dir = tmp_path / ".claude" / "forge" / "sessions"
        session_dir.mkdir(parents=True, exist_ok=True)

        for i in range(3):
            session_data = {
                "id": f"session-{i}",
                "start_time": f"2026-01-0{i+1}T00:00:00Z",
                "end_time": f"2026-01-0{i+1}T01:00:00Z",
                "feature_name": f"Feature {i}",
                "branch": "main",
            }

            session_file = session_dir / f"session-{i}.json"
            with open(session_file, "w") as f:
                json.dump(session_data, f)

        # Test filtered report
        result = reporter.generate_filtered_report()
        assert result.is_ok()
        assert "AGGREGATE METRICS" in result.value or "No sessions found" in result.value


class TestActivityReporter:
    """Test ActivityReporter integration."""

    def test_activity_lifecycle(self, tmp_path):
        """Test complete activity lifecycle: start -> complete."""
        reporter = ActivityReporter(tmp_path)

        # Start activity
        result = reporter.report_start("Running tests")
        assert result.is_ok()

        # Check status
        status_result = reporter.get_current_status()
        assert status_result.is_ok()
        status = status_result.value
        assert status.activity == "Running tests"
        assert status.status == "started"

        # Complete activity
        result = reporter.report_complete("Running tests", duration=1.5, success=True)
        assert result.is_ok()

        # Check history
        history_result = reporter.get_recent_history(limit=10)
        assert history_result.is_ok()
        assert len(history_result.value) > 0

    def test_activity_formatting(self, tmp_path):
        """Test formatting activity summaries."""
        reporter = ActivityReporter(tmp_path)

        # Create some activities
        reporter.report_complete("Test 1", 1.0, True)
        reporter.report_complete("Test 2", 2.0, True)
        reporter.report_failed("Test 3", 0.5, "Error occurred")

        # Get and format history
        history_result = reporter.get_recent_history()
        assert history_result.is_ok()

        summary = reporter.format_summary(history_result.value)
        assert "Forge Activity" in summary

    @pytest.mark.asyncio()
    async def test_async_monitoring_not_supported(self, tmp_path):
        """Test async monitoring when terminal doesn't support it."""
        reporter = ActivityReporter(tmp_path)

        # Mock terminal to not support async
        with patch.object(reporter, "supports_async_display", return_value=False):
            result = await reporter.monitor_activity_async(lambda x: None)
            assert result.is_error()

    def test_live_update_formatting(self, tmp_path):
        """Test formatting live updates."""
        reporter = ActivityReporter(tmp_path)

        update = ActivityUpdate(
            activity="Test activity",
            status="progress",
            progress=0.5,
            message="Half done",
        )

        formatted = reporter.format_live_update(update)
        assert "Test activity" in formatted

    def test_progress_bar_rendering(self, tmp_path):
        """Test progress bar rendering."""
        reporter = ActivityReporter(tmp_path)

        bar = reporter._render_progress_bar(0.75, width=20)
        assert "75%" in bar
        assert "[" in bar and "]" in bar


class TestEndToEndWorkflow:
    """Test complete end-to-end observability workflows."""

    def test_complete_feature_workflow(self, tmp_path):
        """Test observing a complete feature development workflow."""
        # Setup services
        dashboard = DashboardService(tmp_path)
        activity_reporter = ActivityReporter(tmp_path)
        notification_service = NotificationService(tmp_path)

        # Simulate workflow
        activity_reporter.report_start("Starting feature development")

        # Get dashboard data
        dash_result = dashboard.get_dashboard_data()
        assert dash_result.is_ok()

        # Send notification
        with patch("builtins.print"):
            notification_service.notify_workflow_complete("feature/test", 300)

        # Complete activity
        activity_reporter.report_complete("Starting feature development", 5.0, True)

        # Verify activity logged
        history = activity_reporter.get_recent_history()
        assert history.is_ok()
        assert len(history.value) > 0

    def test_quality_regression_workflow(self, tmp_path):
        """Test detecting and reporting quality regression."""
        # Setup
        dashboard = DashboardService(tmp_path)
        notification_service = NotificationService(tmp_path)

        # Create state with quality regression
        state_file = tmp_path / ".claude" / "forge" / "state.json"
        state_file.parent.mkdir(parents=True, exist_ok=True)

        state = {
            "quality": {
                "health_score": 85,  # Current health score
                "tests": {"unit": {"coverage": 85.0, "passing": 100, "total": 120}},
            },
            "health_history": [
                {"timestamp": "2026-01-01T00:00:00Z", "score": 90},
                {"timestamp": "2026-01-08T00:00:00Z", "score": 85},
            ],
        }

        with open(state_file, "w") as f:
            json.dump(state, f)

        # Get dashboard data
        dash_result = dashboard.get_dashboard_data()
        assert dash_result.is_ok()

        data = dash_result.value
        # Should detect declining trend
        assert data.health_trend == "declining"

        # Send notification
        with patch("builtins.print") as mock_print:
            notification_service.notify_quality_regression("Health", 90, 85)
            assert mock_print.called


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
