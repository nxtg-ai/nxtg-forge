"""
Pytest configuration and shared fixtures
"""

import json
import tempfile
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture()
def temp_project_dir():
    """Create a temporary project directory for testing"""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_dir = Path(tmpdir)

        # Create basic structure
        (project_dir / ".claude").mkdir(parents=True)
        (project_dir / "forge").mkdir(parents=True)
        (project_dir / "docs").mkdir(parents=True)

        yield project_dir


@pytest.fixture()
def sample_state() -> dict[str, Any]:
    """Sample state.json for testing"""
    return {
        "version": "1.0.0",
        "project": {
            "name": "test-project",
            "type": "web-app",
            "created_at": "2025-01-04T12:00:00Z",
            "last_updated": "2025-01-04T12:00:00Z",
            "forge_version": "1.0.0",
        },
        "architecture": {
            "backend": {"language": "python", "framework": "fastapi"},
            "database": {"type": "postgresql"},
        },
        "development": {
            "current_phase": "implementation",
            "phases_completed": ["planning"],
            "phases_remaining": ["testing", "deployment"],
            "features": {"completed": [], "in_progress": [], "planned": []},
        },
        "quality": {
            "tests": {
                "unit": {"total": 0, "passing": 0, "coverage": 0},
                "integration": {"total": 0, "passing": 0, "coverage": 0},
                "e2e": {"total": 0, "passing": 0, "coverage": 0},
            },
        },
        "checkpoints": [],
        "last_session": None,
    }


@pytest.fixture()
def sample_spec_answers() -> dict[str, Any]:
    """Sample spec answers for testing"""
    return {
        "project_name": "test-app",
        "project_type": "web-app",
        "description": "A test application",
        "backend_language": "python",
        "backend_framework": "fastapi",
        "database": "postgresql",
        "cache": "redis",
        "frontend_framework": "react",
        "ui_library": "tailwind",
        "deployment_target": "docker",
        "ci_cd": "github-actions",
        "authentication": "jwt",
        "payment": "stripe",
        "realtime": "websocket",
        "file_storage": "s3",
        "min_test_coverage": "85",
        "linting": "strict",
        "type_checking": "strict",
    }


@pytest.fixture()
def create_state_file(temp_project_dir, sample_state):
    """Create a state.json file in temp project"""

    def _create(state_data=None):
        state_path = temp_project_dir / ".claude" / "state.json"
        with open(state_path, "w") as f:
            json.dump(state_data or sample_state, f, indent=2)
        return state_path

    return _create
