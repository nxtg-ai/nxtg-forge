"""Tests for refactored CLI architecture.

Validates:
- Command pattern implementation
- Dependency injection
- Result type usage
- Service layer separation
"""

from pathlib import Path
from unittest.mock import Mock

import pytest

from forge.cli_refactored import ForgeCLI
from forge.commands import CommandContext, StatusCommand
from forge.result import Ok
from forge.services import StatusService


class TestCLIArchitecture:
    """Test CLI architecture and patterns."""

    def test_cli_creates_di_container(self):
        """Test that CLI creates DI container."""
        cli = ForgeCLI()
        assert cli.container is not None

    def test_cli_registers_services(self):
        """Test that services are registered in container."""
        cli = ForgeCLI()

        # Check that services can be resolved
        assert cli.container.has(StatusService)

    def test_command_pattern_with_result_types(self):
        """Test command returns Result type."""
        # Mock service
        mock_service = Mock(spec=StatusService)
        mock_service.get_project_status.return_value = Ok(
            Mock(
                project_name="Test",
                project_type="test",
                forge_version="1.0",
                current_phase="development",
                features_completed=0,
                features_in_progress=0,
                features_planned=0,
                active_agents=[],
                health_score=100,
                has_interrupted_session=False,
            ),
        )
        mock_service.get_full_state.return_value = Ok({})

        # Create command with mock
        command = StatusCommand(mock_service)

        # Create context
        args = Mock()
        args.json = False
        args.detail = None
        context = CommandContext(project_root=Path.cwd(), args=args)

        # Execute
        result = command.execute(context)

        # Verify Result type returned
        assert result.is_ok()
        assert result.value == 0


class TestDependencyInjection:
    """Test dependency injection container."""

    def test_singleton_registration(self):
        """Test singleton registration and resolution."""
        from forge.container import DIContainer

        container = DIContainer()
        instance = Path.cwd()

        container.register_singleton(Path, instance)
        resolved = container.resolve(Path)

        assert resolved == instance
        assert resolved is instance  # Same object

    def test_factory_registration(self):
        """Test factory registration."""
        from forge.container import DIContainer

        container = DIContainer()
        container.register_singleton(Path, Path.cwd())

        # Register factory that depends on Path
        container.register_factory(StatusService, lambda c: StatusService(Mock()))

        service = container.resolve(StatusService)
        assert isinstance(service, StatusService)


class TestServiceLayer:
    """Test service layer separation."""

    def test_service_returns_result_types(self):
        """Test that services return Result types."""
        from forge.services import CheckpointService

        mock_state_manager = Mock()
        mock_state_manager.checkpoint.return_value = "checkpoint-123"

        service = CheckpointService(mock_state_manager)
        result = service.create_checkpoint("Test checkpoint")

        assert result.is_ok()
        assert result.value == "checkpoint-123"

    def test_service_handles_errors_with_result(self):
        """Test that services handle errors using Result."""
        from forge.services import CheckpointService

        mock_state_manager = Mock()
        mock_state_manager.checkpoint.side_effect = Exception("Failed")

        service = CheckpointService(mock_state_manager)
        result = service.create_checkpoint("Test checkpoint")

        assert result.is_error()
        assert "Failed" in result.error.message


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
