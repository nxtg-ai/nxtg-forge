"""NXTG-Forge Agent Orchestrator

Coordinates multiple specialized agents to complete complex development tasks.

NOTE: This is a simplified v1.0 implementation. Full orchestration will be
      implemented in v1.1 with advanced features like:
      - Multi-agent task decomposition
      - Parallel agent execution
      - Agent-to-agent communication
      - Dynamic agent selection based on context
      - Learning from past agent interactions
"""

import logging
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Optional


logger = logging.getLogger(__name__)


class AgentType(Enum):
    """Available agent types"""

    LEAD_ARCHITECT = "lead-architect"
    BACKEND_MASTER = "backend-master"
    CLI_ARTISAN = "cli-artisan"
    PLATFORM_BUILDER = "platform-builder"
    INTEGRATION_SPECIALIST = "integration-specialist"
    QA_SENTINEL = "qa-sentinel"


@dataclass
class Task:
    """Represents a development task"""

    id: str
    description: str
    type: str  # feature, bugfix, refactor, etc.
    priority: str  # high, medium, low
    assigned_agent: Optional[AgentType] = None
    status: str = "pending"  # pending, in_progress, completed, failed
    metadata: dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class AgentOrchestrator:
    """Orchestrates specialized AI agents to complete development tasks.

    v1.0: Basic agent routing and task tracking
    v1.1+: Advanced multi-agent coordination, parallel execution, learning
    """

    def __init__(self, project_root: Path = None):
        """Initialize the orchestrator.

        Args:
            project_root: Root directory of the project
        """
        self.project_root = project_root or Path.cwd()
        self.agents = self._load_available_agents()
        self.active_tasks: dict[str, Task] = {}

    def _load_available_agents(self) -> dict[AgentType, dict[str, Any]]:
        """Load available agent configurations.

        Returns:
            Dictionary mapping agent types to their configurations
        """
        # v1.0: Simple static configuration
        # v1.1: Load from .claude/skills/agents/ dynamically
        return {
            AgentType.LEAD_ARCHITECT: {
                "name": "Lead Architect",
                "expertise": ["architecture", "design", "patterns"],
                "skill_file": ".claude/skills/agents/lead-architect.md",
            },
            AgentType.BACKEND_MASTER: {
                "name": "Backend Master",
                "expertise": ["api", "database", "business-logic"],
                "skill_file": ".claude/skills/agents/backend-master.md",
            },
            AgentType.CLI_ARTISAN: {
                "name": "CLI Artisan",
                "expertise": ["cli", "commands", "ux"],
                "skill_file": ".claude/skills/agents/cli-artisan.md",
            },
            AgentType.PLATFORM_BUILDER: {
                "name": "Platform Builder",
                "expertise": ["infrastructure", "deployment", "cicd"],
                "skill_file": ".claude/skills/agents/platform-builder.md",
            },
            AgentType.INTEGRATION_SPECIALIST: {
                "name": "Integration Specialist",
                "expertise": ["apis", "mcp", "webhooks"],
                "skill_file": ".claude/skills/agents/integration-specialist.md",
            },
            AgentType.QA_SENTINEL: {
                "name": "QA Sentinel",
                "expertise": ["testing", "quality", "review"],
                "skill_file": ".claude/skills/agents/qa-sentinel.md",
            },
        }

    def assign_agent(self, task: Task) -> AgentType:
        """Assign the most appropriate agent to a task.

        v1.0: Simple keyword-based routing
        v1.1: ML-based agent selection based on task context and history

        Args:
            task: The task to assign

        Returns:
            The assigned agent type
        """
        # Simple keyword-based assignment
        description_lower = task.description.lower()
        task_type_lower = task.type.lower()

        # Architecture and design tasks
        if any(
            keyword in description_lower
            for keyword in ["architect", "design", "pattern", "structure"]
        ):
            return AgentType.LEAD_ARCHITECT

        # Backend implementation
        if any(
            keyword in description_lower
            for keyword in ["api", "endpoint", "database", "backend", "repository"]
        ):
            return AgentType.BACKEND_MASTER

        # CLI tasks
        if any(keyword in description_lower for keyword in ["cli", "command", "terminal"]):
            return AgentType.CLI_ARTISAN

        # Infrastructure and deployment
        if any(
            keyword in description_lower
            for keyword in ["deploy", "docker", "kubernetes", "cicd", "infrastructure"]
        ):
            return AgentType.PLATFORM_BUILDER

        # Integration tasks
        if any(
            keyword in description_lower
            for keyword in ["integration", "webhook", "mcp", "external"]
        ):
            return AgentType.INTEGRATION_SPECIALIST

        # Testing and QA
        if any(keyword in description_lower for keyword in ["test", "qa", "quality", "review"]):
            return AgentType.QA_SENTINEL

        # Default: use task type
        if task_type_lower == "feature":
            return AgentType.BACKEND_MASTER
        elif task_type_lower in ["bugfix", "refactor"]:
            return AgentType.QA_SENTINEL

        # Fallback
        logger.warning(
            f"Could not determine agent for task: {task.description}, using LEAD_ARCHITECT",
        )
        return AgentType.LEAD_ARCHITECT

    def create_task(
        self,
        description: str,
        task_type: str = "feature",
        priority: str = "medium",
        metadata: Optional[dict[str, Any]] = None,
    ) -> Task:
        """Create a new task and assign it to an agent.

        Args:
            description: Task description
            task_type: Type of task (feature, bugfix, refactor, etc.)
            priority: Task priority (high, medium, low)
            metadata: Additional task metadata

        Returns:
            Created task with assigned agent
        """
        import uuid

        task = Task(
            id=str(uuid.uuid4())[:8],
            description=description,
            type=task_type,
            priority=priority,
            metadata=metadata or {},
        )

        task.assigned_agent = self.assign_agent(task)
        self.active_tasks[task.id] = task

        logger.info(
            f"Created task {task.id}: '{description}' assigned to {task.assigned_agent.value}",
        )

        return task

    def get_agent_context(self, agent_type: AgentType) -> str:
        """Get the skill context for an agent.

        v1.0: Return path to skill file
        v1.1: Load and parse skill file, inject into context

        Args:
            agent_type: Type of agent

        Returns:
            Agent context/skill file path
        """
        agent_info = self.agents.get(agent_type)
        if not agent_info:
            return ""

        skill_file = self.project_root / agent_info["skill_file"]

        # v1.0: Just return the path
        # v1.1: Load file content and inject into Claude's context
        return str(skill_file)

    def list_tasks(self, status: Optional[str] = None) -> list[Task]:
        """List tasks, optionally filtered by status.

        Args:
            status: Filter by status (pending, in_progress, completed, failed)

        Returns:
            List of matching tasks
        """
        tasks = list(self.active_tasks.values())

        if status:
            tasks = [t for t in tasks if t.status == status]

        return sorted(tasks, key=lambda t: t.priority, reverse=True)

    def update_task_status(self, task_id: str, status: str) -> Optional[Task]:
        """Update task status.

        Args:
            task_id: Task ID
            status: New status

        Returns:
            Updated task or None if not found
        """
        task = self.active_tasks.get(task_id)
        if task:
            task.status = status
            logger.info(f"Task {task_id} status updated to: {status}")
        return task

    def get_recommended_agent(self, context: str) -> AgentType:
        """Recommend an agent based on context.

        v1.0: Simple keyword matching
        v1.1: Context-aware recommendation using embeddings

        Args:
            context: Current context or question

        Returns:
            Recommended agent type
        """
        # Create temporary task to use assignment logic
        temp_task = Task(id="temp", description=context, type="query", priority="medium")

        return self.assign_agent(temp_task)


# Convenience function for simple agent suggestion
def suggest_agent(description: str) -> str:
    """Suggest which agent should handle a given task.

    Args:
        description: Task or question description

    Returns:
        Suggested agent name
    """
    orchestrator = AgentOrchestrator()
    agent_type = orchestrator.get_recommended_agent(description)
    return orchestrator.agents[agent_type]["name"]
