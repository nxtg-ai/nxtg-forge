"""NXTG-Forge - Self-Deploying AI Development Infrastructure.

A comprehensive system for building, deploying, and maintaining software projects
with Claude Code integration.
"""

__version__ = "1.0.0"
__author__ = "NXTG-Forge Contributors"

from .file_generator import FileGenerator
from .gap_analyzer import GapAnalyzer
from .mcp_detector import MCPDetector
from .spec_generator import SpecGenerator
from .state_manager import StateManager


__all__ = [
    "StateManager",
    "SpecGenerator",
    "FileGenerator",
    "MCPDetector",
    "GapAnalyzer",
]
