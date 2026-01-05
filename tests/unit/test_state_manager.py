"""
Unit tests for StateManager
"""

import json
import sys
from pathlib import Path


# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from forge.state_manager import StateManager


class TestStateManager:
    """Test StateManager class"""

    def test_init_creates_directories(self, temp_project_dir):
        """Test that initialization creates necessary directories"""
        manager = StateManager(temp_project_dir)

        assert manager.state_file.parent.exists()
        assert manager.checkpoints_dir.exists()

    def test_create_initial_state(self, temp_project_dir):
        """Test initial state creation"""
        manager = StateManager(temp_project_dir)
        state = manager.create_initial_state()

        assert state["version"] == "1.0.0"
        assert state["project"]["name"] == temp_project_dir.name
        assert "architecture" in state
        assert "development" in state
        assert "quality" in state

    def test_load_existing_state(self, temp_project_dir, create_state_file, sample_state):
        """Test loading existing state file"""
        create_state_file(sample_state)

        manager = StateManager(temp_project_dir)
        state = manager.load()

        assert state["project"]["name"] == "test-project"
        assert state["version"] == "1.0.0"

    def test_save_state(self, temp_project_dir):
        """Test saving state to file"""
        manager = StateManager(temp_project_dir)
        manager.state["project"]["name"] = "updated-project"
        manager.save()

        # Verify file was written
        assert manager.state_file.exists()

        # Verify content
        with open(manager.state_file) as f:
            saved_state = json.load(f)

        assert saved_state["project"]["name"] == "updated-project"
        assert "last_updated" in saved_state["project"]

    def test_checkpoint_creation(self, temp_project_dir, create_state_file, sample_state):
        """Test creating a checkpoint"""
        create_state_file(sample_state)
        manager = StateManager(temp_project_dir)

        checkpoint_id = manager.checkpoint("Test checkpoint")

        assert checkpoint_id.startswith("cp-")
        assert len(manager.state["checkpoints"]) == 1
        assert manager.state["checkpoints"][0]["description"] == "Test checkpoint"

        # Verify checkpoint file exists
        checkpoint_file = manager.checkpoints_dir / f"{checkpoint_id}.json"
        assert checkpoint_file.exists()

    def test_checkpoint_symlink(self, temp_project_dir, create_state_file, sample_state):
        """Test that latest symlink is created"""
        create_state_file(sample_state)
        manager = StateManager(temp_project_dir)

        checkpoint_id = manager.checkpoint("Latest checkpoint")
        latest_link = manager.checkpoints_dir / "latest.json"

        assert latest_link.exists()
        assert latest_link.is_symlink()

    def test_update_feature(self, temp_project_dir, create_state_file, sample_state):
        """Test updating a feature"""
        # Add a feature to test state
        sample_state["development"]["features"]["in_progress"] = [
            {"id": "feat-001", "name": "Test Feature", "status": "in_progress"},
        ]
        create_state_file(sample_state)

        manager = StateManager(temp_project_dir)
        manager.update_feature("feat-001", {"progress": 50})

        # Verify update
        features = manager.state["development"]["features"]["in_progress"]
        assert features[0]["progress"] == 50

    def test_move_feature(self, temp_project_dir, create_state_file, sample_state):
        """Test moving feature between statuses"""
        sample_state["development"]["features"]["in_progress"] = [
            {"id": "feat-001", "name": "Test Feature"},
        ]
        create_state_file(sample_state)

        manager = StateManager(temp_project_dir)
        manager.move_feature("feat-001", "in_progress", "completed")

        # Verify move
        assert len(manager.state["development"]["features"]["in_progress"]) == 0
        assert len(manager.state["development"]["features"]["completed"]) == 1
        assert manager.state["development"]["features"]["completed"][0]["id"] == "feat-001"

    def test_record_session(self, temp_project_dir, create_state_file, sample_state):
        """Test recording session info"""
        create_state_file(sample_state)
        manager = StateManager(temp_project_dir)

        manager.record_session("session-123", "backend-master", "Implement API", "active")

        assert manager.state["last_session"]["id"] == "session-123"
        assert manager.state["last_session"]["agent"] == "backend-master"
        assert manager.state["last_session"]["status"] == "active"

    def test_get_recovery_info_no_interruption(
        self,
        temp_project_dir,
        create_state_file,
        sample_state,
    ):
        """Test recovery info when no interruption"""
        create_state_file(sample_state)
        manager = StateManager(temp_project_dir)

        recovery_info = manager.get_recovery_info()
        assert recovery_info is None

    def test_get_recovery_info_with_interruption(
        self,
        temp_project_dir,
        create_state_file,
        sample_state,
    ):
        """Test recovery info with interrupted session"""
        sample_state["last_session"] = {
            "id": "session-123",
            "status": "interrupted",
            "agent": "backend-master",
            "task": "Test task",
        }
        sample_state["development"]["features"]["in_progress"] = [
            {"id": "feat-001", "name": "In Progress Feature"},
        ]
        create_state_file(sample_state)

        manager = StateManager(temp_project_dir)
        manager.checkpoint("Before interruption")

        recovery_info = manager.get_recovery_info()

        assert recovery_info is not None
        assert recovery_info["session"]["id"] == "session-123"
        assert recovery_info["checkpoint"] is not None
        assert len(recovery_info["in_progress_features"]) == 1
        assert len(recovery_info["recovery_commands"]) > 0
