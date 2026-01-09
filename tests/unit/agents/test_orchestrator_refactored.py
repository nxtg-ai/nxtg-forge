"""Tests for refactored agent orchestrator."""

import pytest

from forge.agents.domain.agent import AgentType
from forge.agents.domain.task import TaskPriority, TaskStatus
from forge.agents.orchestrator_refactored import AgentOrchestrator
from forge.agents.selection.strategy import KeywordStrategy


class TestAgentOrchestrator:
    """Test suite for AgentOrchestrator."""

    @pytest.fixture()
    def orchestrator(self, tmp_path):
        """Create orchestrator for testing."""
        return AgentOrchestrator(project_root=tmp_path)

    def test_initialization(self, orchestrator):
        """Test orchestrator initializes correctly."""
        assert orchestrator is not None
        assert orchestrator.task_service is not None
        assert orchestrator.executor is not None
        assert isinstance(orchestrator.selection_strategy, KeywordStrategy)

    def test_create_task(self, orchestrator):
        """Test task creation."""
        task = orchestrator.create_task(
            description="Implement user authentication",
            task_type="feature",
            priority="high",
        )

        assert task is not None
        assert task.description == "Implement user authentication"
        assert task.task_type == "feature"
        assert task.priority == TaskPriority.HIGH
        assert task.assigned_agent is not None
        assert task.status == TaskStatus.PENDING

    def test_agent_selection_backend(self, orchestrator):
        """Test backend tasks assigned to backend master."""
        task = orchestrator.create_task(
            description="Create API endpoint for user management",
            task_type="feature",
        )

        assert task.assigned_agent == AgentType.BACKEND_MASTER.value

    def test_agent_selection_cli(self, orchestrator):
        """Test CLI tasks assigned to CLI artisan."""
        task = orchestrator.create_task(
            description="Add CLI command for status display",
            task_type="feature",
        )

        assert task.assigned_agent == AgentType.CLI_ARTISAN.value

    def test_agent_selection_qa(self, orchestrator):
        """Test testing tasks assigned to QA sentinel."""
        task = orchestrator.create_task(
            description="Write tests for authentication",
            task_type="testing",
        )

        assert task.assigned_agent == AgentType.QA_SENTINEL.value

    def test_task_decomposition_feature(self, orchestrator):
        """Test feature task decomposition."""
        task = orchestrator.create_task(
            description="Add user registration",
            task_type="feature",
        )

        subtasks = orchestrator.decompose_task(task)

        assert len(subtasks) == 3
        assert subtasks[0].description.startswith("Design architecture for:")
        assert subtasks[1].description.startswith("Implement:")
        assert subtasks[2].description.startswith("Test:")

        # Check dependencies
        assert len(subtasks[0].dependencies) == 0
        assert subtasks[1].dependencies == (f"{task.id}-arch",)
        assert subtasks[2].dependencies == (f"{task.id}-impl",)

    def test_task_decomposition_bugfix(self, orchestrator):
        """Test bugfix task decomposition."""
        task = orchestrator.create_task(
            description="Fix login timeout",
            task_type="bugfix",
        )

        subtasks = orchestrator.decompose_task(task)

        assert len(subtasks) == 3
        assert "Diagnose" in subtasks[0].description
        assert "Fix" in subtasks[1].description
        assert "Verify" in subtasks[2].description

    def test_execute_task(self, orchestrator):
        """Test task execution."""
        task = orchestrator.create_task(
            description="Simple task",
            task_type="feature",
        )

        # Execute (will use default callback)
        result = orchestrator.execute_task(task)

        assert result.is_ok()
        assert "status" in result.value

        # Check task was updated
        updated_task = orchestrator.get_task(task.id)
        assert updated_task.status == TaskStatus.COMPLETED
        assert updated_task.started_at is not None
        assert updated_task.completed_at is not None

    def test_execute_task_with_callback(self, orchestrator):
        """Test task execution with custom callback."""

        def custom_callback(task):
            return {"status": "completed", "custom": "result"}

        orchestrator.register_agent_callback(
            AgentType.BACKEND_MASTER,
            custom_callback,
        )

        task = orchestrator.create_task(
            description="Create API endpoint",
            task_type="feature",
        )

        result = orchestrator.execute_task(task)

        assert result.is_ok()
        assert result.value["custom"] == "result"

    def test_list_tasks(self, orchestrator):
        """Test listing tasks."""
        # Create several tasks
        orchestrator.create_task("Task 1", priority="high")
        orchestrator.create_task("Task 2", priority="low")
        orchestrator.create_task("Task 3", priority="medium")

        # List all tasks
        tasks = orchestrator.list_tasks()
        assert len(tasks) == 3

        # Check sorting by priority
        assert tasks[0].priority == TaskPriority.HIGH
        assert tasks[1].priority == TaskPriority.MEDIUM
        assert tasks[2].priority == TaskPriority.LOW

    def test_list_tasks_by_status(self, orchestrator):
        """Test filtering tasks by status."""
        task1 = orchestrator.create_task("Task 1")
        task2 = orchestrator.create_task("Task 2")

        # Execute one task
        orchestrator.execute_task(task1)

        # List pending tasks
        pending = orchestrator.list_tasks("pending")
        assert len(pending) == 1
        assert pending[0].id == task2.id

        # List completed tasks
        completed = orchestrator.list_tasks("completed")
        assert len(completed) == 1
        assert completed[0].id == task1.id

    def test_get_task(self, orchestrator):
        """Test retrieving specific task."""
        task = orchestrator.create_task("Test task")

        retrieved = orchestrator.get_task(task.id)
        assert retrieved is not None
        assert retrieved.id == task.id
        assert retrieved.description == task.description

    def test_get_agent_context(self, orchestrator):
        """Test getting agent context."""
        context = orchestrator.get_agent_context(AgentType.BACKEND_MASTER)
        assert context is not None
        assert "backend-master" in context.lower()


class TestAsyncExecution:
    """Test async execution capabilities."""

    @pytest.fixture()
    def async_orchestrator(self, tmp_path):
        """Create orchestrator with async executor."""
        return AgentOrchestrator(project_root=tmp_path, use_async=True)

    @pytest.mark.asyncio()
    async def test_execute_task_async(self, async_orchestrator):
        """Test async task execution."""
        task = async_orchestrator.create_task("Async task")

        result = await async_orchestrator.execute_task_async(task)

        assert result.is_ok()
        updated_task = async_orchestrator.get_task(task.id)
        assert updated_task.status == TaskStatus.COMPLETED

    @pytest.mark.asyncio()
    async def test_execute_parallel(self, async_orchestrator):
        """Test parallel task execution."""
        tasks = [async_orchestrator.create_task(f"Task {i}") for i in range(5)]

        results = await async_orchestrator.execute_parallel(tasks)

        assert len(results) == 5
        assert all(r.is_ok() for r in results)

        # Check all tasks completed
        for task in tasks:
            updated = async_orchestrator.get_task(task.id)
            assert updated.status == TaskStatus.COMPLETED
