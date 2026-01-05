"""
Unit tests for SpecGenerator
"""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from forge.spec_generator import SpecGenerator


class TestSpecGenerator:
    """Test SpecGenerator class"""

    def test_init(self, temp_project_dir):
        """Test initialization"""
        generator = SpecGenerator(temp_project_dir)

        assert generator.project_root == temp_project_dir
        assert generator.answers == {}

    def test_from_answers(self, temp_project_dir, sample_spec_answers):
        """Test generating spec from answers"""
        generator = SpecGenerator(temp_project_dir)
        spec = generator.from_answers(sample_spec_answers)

        assert "# test-app - Project Specification" in spec
        assert "fastapi" in spec.lower()
        assert "postgresql" in spec.lower()
        assert "react" in spec.lower()

    def test_spec_includes_all_sections(self, temp_project_dir, sample_spec_answers):
        """Test that spec includes all required sections"""
        generator = SpecGenerator(temp_project_dir)
        spec = generator.from_answers(sample_spec_answers)

        required_sections = [
            "## Overview",
            "## Architecture",
            "## Features",
            "## Quality Standards",
            "## Development Workflow",
            "## Documentation",
            "## Deployment",
        ]

        for section in required_sections:
            assert section in spec, f"Missing section: {section}"

    def test_validate_spec_valid(self, temp_project_dir, sample_spec_answers):
        """Test spec validation with valid spec"""
        generator = SpecGenerator(temp_project_dir)
        spec = generator.from_answers(sample_spec_answers)

        is_valid, errors = generator.validate_spec(spec)

        assert is_valid
        assert len(errors) == 0

    def test_validate_spec_invalid(self, temp_project_dir):
        """Test spec validation with invalid spec"""
        generator = SpecGenerator(temp_project_dir)
        incomplete_spec = "# Project\n\nSome content"

        is_valid, errors = generator.validate_spec(incomplete_spec)

        assert not is_valid
        assert len(errors) > 0

    def test_get_framework_choices_python(self, temp_project_dir):
        """Test framework choices for Python"""
        generator = SpecGenerator(temp_project_dir)
        choices = generator._get_framework_choices("python")

        assert "fastapi" in choices
        assert "django" in choices
        assert "flask" in choices

    def test_get_framework_choices_node(self, temp_project_dir):
        """Test framework choices for Node.js"""
        generator = SpecGenerator(temp_project_dir)
        choices = generator._get_framework_choices("node")

        assert "express" in choices
        assert "nestjs" in choices

    def test_get_orm_python_postgresql(self, temp_project_dir):
        """Test ORM selection for Python + PostgreSQL"""
        generator = SpecGenerator(temp_project_dir)
        answers = {"backend_language": "python", "database": "postgresql"}

        orm = generator._get_orm(answers)

        assert "SQLAlchemy" in orm
        assert "asyncpg" in orm

    def test_get_state_management_react(self, temp_project_dir):
        """Test state management for React"""
        generator = SpecGenerator(temp_project_dir)
        state_mgmt = generator._get_state_management("react")

        assert "Redux" in state_mgmt or "Zustand" in state_mgmt

    def test_get_build_tool_react(self, temp_project_dir):
        """Test build tool for React"""
        generator = SpecGenerator(temp_project_dir)
        build_tool = generator._get_build_tool("react")

        assert build_tool == "Vite"

    def test_get_naming_convention_python(self, temp_project_dir):
        """Test naming convention for Python"""
        generator = SpecGenerator(temp_project_dir)
        answers = {"backend_language": "python"}

        convention = generator._get_naming_convention(answers)

        assert convention == "snake_case"

    def test_save_answers(self, temp_project_dir, sample_spec_answers):
        """Test saving answers to temp file"""
        generator = SpecGenerator(temp_project_dir)
        generator.answers = sample_spec_answers
        generator._save_answers()

        answers_file = temp_project_dir / ".claude" / "tmp" / "spec-answers.json"
        assert answers_file.exists()

    def test_spec_includes_payment_section(self, temp_project_dir, sample_spec_answers):
        """Test that payment section is included when specified"""
        generator = SpecGenerator(temp_project_dir)
        spec = generator.from_answers(sample_spec_answers)

        assert "Payment Processing" in spec
        assert "stripe" in spec.lower()

    def test_spec_includes_realtime_section(self, temp_project_dir, sample_spec_answers):
        """Test that real-time section is included when specified"""
        generator = SpecGenerator(temp_project_dir)
        spec = generator.from_answers(sample_spec_answers)

        assert "Real-time Communication" in spec
        assert "websocket" in spec.lower()

    def test_spec_includes_file_storage_section(self, temp_project_dir, sample_spec_answers):
        """Test that file storage section is included when specified"""
        generator = SpecGenerator(temp_project_dir)
        spec = generator.from_answers(sample_spec_answers)

        assert "File Management" in spec
        assert "s3" in spec.lower()
