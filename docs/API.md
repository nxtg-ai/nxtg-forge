# NXTG-Forge API Documentation

> Complete API reference for NXTG-Forge modules

## Python API

### StateManager

Manages project state, checkpoints, and recovery.

```python
from forge.state_manager import StateManager

# Initialize
manager = StateManager(project_root=".")

# Load/Save state
state = manager.load()
manager.save()

# Create checkpoint
checkpoint_id = manager.checkpoint("Description")

# Restore from checkpoint
manager.restore("cp-001")  # or None for latest

# Feature management
manager.update_feature("feat-001", {"progress": 50})
manager.move_feature("feat-001", "in_progress", "completed")

# Session tracking
manager.record_session("session-id", "agent-name", "task", "active")

# Recovery info
recovery_info = manager.get_recovery_info()
```

**Methods:**

#### `__init__(project_root: str = ".")`

Initialize state manager with project root directory.

#### `load() -> Dict[str, Any]`

Load current state from `.claude/state.json`. Creates initial state if file doesn't exist.

#### `save()`

Save current state to file. Auto-updates `last_updated` timestamp. Triggers `state-sync.sh` hook.

#### `create_initial_state() -> Dict[str, Any]`

Create initial state structure for new project.

#### `checkpoint(description: str) -> str`

Create state checkpoint with description. Returns checkpoint ID. Captures git commit hash if in repository.

#### `restore(checkpoint_id: Optional[str] = None)`

Restore from checkpoint. Uses latest if ID not specified. Optionally restores git state.

#### `update_feature(feature_id: str, updates: Dict[str, Any])`

Update feature with new data. Raises ValueError if feature not found.

#### `move_feature(feature_id: str, from_status: str, to_status: str)`

Move feature between statuses (planned/in_progress/completed).

#### `record_session(session_id: str, agent: str, task: str, status: str = "active")`

Record current session for recovery purposes.

#### `get_recovery_info() -> Optional[Dict[str, Any]]`

Get recovery information if session was interrupted. Returns None if no recovery needed.

---

### SpecGenerator

Interactive project specification builder.

```python
from forge.spec_generator import SpecGenerator

# Initialize
generator = SpecGenerator(project_root=".")

# Interactive mode
spec = generator.interactive_mode()

# From answers dict
answers = {
    "project_name": "myapp",
    "project_type": "web-app",
    "backend_language": "python",
    # ...
}
spec = generator.from_answers(answers)

# Validate spec
is_valid, errors = generator.validate_spec(spec_content)
```

**Methods:**

#### `__init__(project_root: str = ".")`

Initialize spec generator.

#### `interactive_mode() -> str`

Launch interactive Q&A to build specification. Returns generated spec markdown.

#### `from_answers(answers: Dict[str, Any]) -> str`

Generate spec from answers dictionary. Returns spec markdown.

#### `validate_spec(spec_content: str) -> Tuple[bool, List[str]]`

Validate spec completeness. Returns (is_valid, errors).

**Helper Methods:**

- `_get_framework_choices(language: str) -> List[str]`
- `_get_orm(answers: Dict[str, Any]) -> str`
- `_get_state_management(framework: str) -> str`
- `_get_build_tool(framework: str) -> str`
- `_get_orchestration(answers: Dict[str, Any]) -> str`
- `_get_naming_convention(answers: Dict[str, Any]) -> str`
- `_save_answers()`

---

### FileGenerator

Template-based file generation engine.

```python
from forge.file_generator import FileGenerator

# Initialize
generator = FileGenerator(project_root=".")

# Generate from spec
generated_files = generator.generate_from_spec(
    spec_content,
    template_set="full",  # or "minimal", "standard"
    dry_run=False
)

# Create directory structure
created_dirs = generator.create_directory_structure(config)

# Generate boilerplate
boilerplate = generator.generate_boilerplate(config)
```

**Methods:**

#### `__init__(project_root: str = ".")`

Initialize file generator with Jinja2 environment.

#### `generate_from_spec(spec_content: str, template_set: str = "full", dry_run: bool = False) -> List[str]`

Generate project files from specification. Returns list of generated file paths.

Parameters:

- `spec_content`: Markdown specification content
- `template_set`: "minimal", "standard", or "full"
- `dry_run`: If True, only lists files without creating them

#### `create_directory_structure(config: Dict[str, Any]) -> List[str]`

Create base directory structure. Returns list of created directories.

#### `generate_boilerplate(config: Dict[str, Any]) -> Dict[str, str]`

Generate basic boilerplate files (README, .gitignore, .env.example). Returns mapping of filename to path.

**Jinja2 Filters:**

- `snake_case`: Convert to snake_case
- `pascal_case`: Convert to PascalCase
- `camel_case`: Convert to camelCase
- `kebab_case`: Convert to kebab-case

---

### MCPDetector

MCP server auto-detection and configuration.

```python
from forge.mcp_detector import MCPDetector

# Initialize
detector = MCPDetector(project_root=".")

# Detect needed servers
recommendations = detector.detect()

# Configure servers
detector.configure()

# Display recommendations
detector.display_recommendations()
```

**Methods:**

#### `__init__(project_root: str = ".")`

Initialize MCP detector.

#### `detect() -> List[Dict[str, Any]]`

Run auto-detection. Returns list of recommended MCP servers.

Each recommendation contains:

```python
{
    "name": "github",
    "priority": "high",  # or "medium", "low"
    "reason": "Description of why needed",
    "config": { ... }  # MCP server configuration
}
```

#### `configure()`

Configure all detected MCP servers. Adds servers via Claude CLI.

#### `display_recommendations()`

Display recommendations in formatted table using rich.

---

### GapAnalyzer

Project analysis and improvement recommendations.

```python
from forge.gap_analyzer import GapAnalyzer

# Initialize with state
analyzer = GapAnalyzer(project_root=".", state=state_dict)

# Run analysis
report_markdown = analyzer.analyze()
```

**Methods:**

#### `__init__(project_root: str = ".", state: Optional[Dict[str, Any]] = None)`

Initialize gap analyzer with optional state.

#### `analyze() -> str`

Run comprehensive gap analysis. Returns markdown report.

Analysis includes:

- Testing coverage and quality
- Documentation completeness
- Security posture
- Code quality metrics
- Performance considerations
- Infrastructure setup

---

## CLI API

### forge Command

Main CLI entry point.

```bash
# Show help
forge --help
forge --version

# Status commands
forge status
forge status --json
forge status --detail features

# Checkpoint operations
forge checkpoint "Description"
forge restore
forge restore cp-001

# Spec operations
forge spec generate --interactive
forge spec generate --from-answers answers.json
forge spec validate spec-file.md

# MCP operations
forge mcp detect
forge mcp detect --configure
forge mcp list

# Analysis
forge gap-analysis
forge gap-analysis --output custom-path.md
forge health
forge health --detail

# Recovery
forge recovery

# File generation
forge generate --spec PROJECT-SPEC.md
forge generate --spec PROJECT-SPEC.md --dry-run
forge generate --spec PROJECT-SPEC.md --template-set minimal
```

---

## Slash Commands API

### /init

Initialize or upgrade project.

```
/init nxtg-forge --new
/init nxtg-forge --upgrade
/init nxtg-forge --spec existing-spec.md
```

### /status

Show project status.

```
/status
/status --detail features
/status --detail agents
/status --detail quality
/status --detail mcp
```

### /feature

Add new feature.

```
/feature "Feature Name"
```

### /checkpoint

Create checkpoint.

```
/checkpoint "Description"
```

### /restore

Restore from checkpoint.

```
/restore
/restore cp-001
```

### /gap-analysis

Run gap analysis.

```
/gap-analysis
```

---

## Template API

### Template Variables

Available in all `.j2` templates:

```jinja2
{{ project_name }}           - Project identifier
{{ project_type }}           - web-app, api, cli, platform
{{ description }}            - Project description
{{ backend_language }}       - python, node, go, rust, java
{{ backend_framework }}      - fastapi, django, express, etc.
{{ frontend_framework }}     - react, vue, svelte, angular
{{ database }}               - postgresql, mysql, mongodb
{{ cache }}                  - redis, memcached
{{ entity_name }}            - Domain entity name
{{ usecase_name }}           - Use case name
{{ component_name }}         - Component name
```

### Template Filters

```jinja2
{{ "hello_world" | pascal_case }}      {# HelloWorld #}
{{ "HelloWorld" | snake_case }}        {# hello_world #}
{{ "hello_world" | camel_case }}       {# helloWorld #}
{{ "HelloWorld" | kebab_case }}        {# hello-world #}
```

### Example Template

```jinja2
"""
{{ entity_name | pascal_case }} Entity

{{ description | default('Domain entity') }}
"""

from datetime import datetime
from pydantic import BaseModel

class {{ entity_name | pascal_case }}(BaseModel):
    """{{ entity_name | pascal_case }} domain model"""

    id: int
    name: str
    created_at: datetime

    def __repr__(self) -> str:
        return f"{{ entity_name | pascal_case }}(id={self.id})"
```

---

## State Schema API

### Project State

Complete state.json schema:

```typescript
interface State {
  version: string;
  project: {
    name: string;
    type: "web-app" | "api" | "cli" | "platform";
    created_at: string;  // ISO8601
    last_updated: string;  // ISO8601
    forge_version: string;
  };
  spec: {
    status: "pending" | "approved" | "outdated";
    file: string | null;
    hash: string | null;
    last_modified: string | null;
  };
  architecture: {
    pattern?: string;
    layers?: string[];
    backend?: {
      language: string;
      framework: string;
      version?: string;
    };
    frontend?: {
      framework: string;
      version?: string;
    };
    database?: {
      type: string;
      version?: string;
    };
    cache?: {
      type: string;
      version?: string;
    };
  };
  development: {
    current_phase: "setup" | "implementation" | "testing" | "deployment";
    phases_completed: string[];
    phases_remaining: string[];
    features: {
      completed: Feature[];
      in_progress: Feature[];
      planned: Feature[];
    };
  };
  agents: {
    active: string[];
    available: string[];
    history: AgentHistory[];
  };
  mcp_servers: {
    configured: MCPServer[];
    recommended: MCPRecommendation[];
  };
  quality: QualityMetrics;
  checkpoints: Checkpoint[];
  last_session: Session | null;
}
```

---

*Last Updated: 2025-01-04*
*Version: 1.0.0*
