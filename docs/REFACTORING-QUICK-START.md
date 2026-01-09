# Refactoring Quick Start Guide

This guide shows how to use the new architectural patterns introduced in Phase 1 of the refactoring.

---

## Using Result Types

### Basic Pattern

```python
from forge.result import Result, Ok, Err, FileError

def read_file(path: Path) -> Result[str, FileError]:
    """Function that can fail returns Result type"""
    if not path.exists():
        return Err(FileError.not_found(str(path)))

    try:
        content = path.read_text()
        return Ok(content)
    except PermissionError:
        return Err(FileError.permission_denied(str(path)))
```

### Handling Results

```python
# Check and unwrap
result = read_file(Path("config.yml"))
if result.is_ok():
    content = result.value
    print(f"File content: {content}")
else:
    error = result.error
    print(f"Error: {error.message}")

# Pattern matching (Python 3.10+)
match read_file(Path("config.yml")):
    case Ok(content):
        print(f"Content: {content}")
    case Err(FileError.NotFound(path)):
        print(f"File not found: {path}")
    case Err(FileError.PermissionDenied(path)):
        print(f"Permission denied: {path}")
```

### Chaining Operations

```python
result = (
    read_file(path)
    .map(lambda content: content.upper())  # Transform on success
    .flat_map(lambda content: parse_yaml(content))  # Chain another Result
)

if result.is_ok():
    print(f"Parsed: {result.value}")
```

---

## Using Dependency Injection

### Define Component with Dependencies

```python
from forge.container import DIContainer

class UserRepository:
    def __init__(self, database: Database):
        """Accept dependencies via constructor"""
        self.db = database

    def find_user(self, user_id: str) -> Result[User, DatabaseError]:
        # Use injected database
        return self.db.query("SELECT * FROM users WHERE id = ?", user_id)

class UserService:
    def __init__(self, repository: UserRepository):
        """Service depends on repository"""
        self.repo = repository

    def get_user(self, user_id: str) -> Result[User, ServiceError]:
        return self.repo.find_user(user_id)
```

### Setup Container

```python
def setup_container() -> DIContainer:
    """Wire up all dependencies"""
    container = DIContainer()

    # Register infrastructure (singletons)
    database = PostgresDatabase("connection_string")
    container.register_singleton(Database, database)

    # Register repositories (factories)
    container.register_factory(
        UserRepository,
        lambda c: UserRepository(c.resolve(Database))
    )

    # Register services
    container.register_factory(
        UserService,
        lambda c: UserService(c.resolve(UserRepository))
    )

    return container


# Use container
container = setup_container()
user_service = container.resolve(UserService)
user_result = user_service.get_user("123")
```

### Testing with Mocks

```python
from unittest.mock import Mock

def test_user_service():
    # Create mock repository
    mock_repo = Mock(UserRepository)
    mock_repo.find_user.return_value = Ok(User(id="123", name="Test"))

    # Inject mock
    service = UserService(mock_repo)

    # Test behavior
    result = service.get_user("123")

    assert result.is_ok()
    assert result.value.name == "Test"
    mock_repo.find_user.assert_called_once_with("123")
```

---

## Using DirectoryManager

### Basic Usage

```python
from forge.directory_manager import DirectoryManager
from pathlib import Path

# Create manager
dirs = DirectoryManager(Path.cwd())

# Ensure directory structure exists
result = dirs.ensure_structure()
if result.is_error():
    print(f"Failed to create directories: {result.error}")
    return

# Handle legacy migration
migration = dirs.migrate_legacy()
if migration.performed:
    print(f"Migrated: {migration.from_path} → {migration.to_path}")

# Access paths
config_file = dirs.config_file
state_file = dirs.state_file
memory_dir = dirs.memory_dir
```

### Validate Structure

```python
dirs = DirectoryManager(project_root)

validation_result = dirs.validate_structure()
match validation_result:
    case Ok(_):
        print("Directory structure is valid")
    case Err(error):
        print(f"Validation failed: {error.message}")
```

---

## Using Refactored Config

### Basic Usage

```python
from forge.config_refactored import create_forge_config
from pathlib import Path

# Create config manager (handles everything)
manager = create_forge_config(Path.cwd())

# Access configuration (lazy loaded)
config = manager.config

# Type-safe access
print(f"Forge version: {config.forge_version}")
print(f"Memory enabled: {config.get_memory_enabled()}")
print(f"Max parallel agents: {config.get_max_parallel_agents()}")

# Check features
if config.is_feature_enabled("tdd_workflow"):
    print("TDD workflow is enabled")

# Access project analysis
analysis = config.project_analysis
print(f"Languages: {analysis.languages}")
print(f"Frameworks: {analysis.frameworks}")
```

### Manual Component Usage

```python
from forge.directory_manager import DirectoryManager
from forge.config_refactored import (
    ConfigLoader,
    ProjectAnalyzer,
    ForgeConfigManager
)
from pathlib import Path

# Create components manually for testing
project_root = Path.cwd()

dirs = DirectoryManager(project_root)
dirs.ensure_structure()

loader = ConfigLoader(dirs.config_file)
analyzer = ProjectAnalyzer(dirs.project_root)

# Wire up manager
manager = ForgeConfigManager(
    directory_manager=dirs,
    config_loader=loader,
    project_analyzer=analyzer,
)

# Load config
config_result = manager.load_or_create()
match config_result:
    case Ok(config):
        print(f"Config loaded: {config.forge_version}")
    case Err(error):
        print(f"Failed to load config: {error.message}")
```

---

## Common Patterns

### Error Handling Chain

```python
def complex_operation(path: Path) -> Result[ProcessedData, OperationError]:
    """Chain multiple operations that can fail"""

    # Read file
    read_result = read_file(path)
    if read_result.is_error():
        return Err(OperationError.from_file_error(read_result.error))

    # Parse YAML
    parse_result = parse_yaml(read_result.value)
    if parse_result.is_error():
        return Err(OperationError.from_parse_error(parse_result.error))

    # Validate
    validate_result = validate_data(parse_result.value)
    if validate_result.is_error():
        return Err(OperationError.from_validation_error(validate_result.error))

    return Ok(validate_result.value)
```

### Service Layer Pattern

```python
class ConfigService:
    """Application service coordinating config operations"""

    def __init__(
        self,
        loader: ConfigLoader,
        validator: ConfigValidator,
        notifier: Notifier
    ):
        self.loader = loader
        self.validator = validator
        self.notifier = notifier

    def load_and_validate(self) -> Result[ValidatedConfig, ServiceError]:
        """Load, validate, and notify"""

        # Load
        load_result = self.loader.load()
        if load_result.is_error():
            return Err(ServiceError.LoadFailed(load_result.error))

        config = load_result.value

        # Validate
        validation_result = self.validator.validate(config)
        if validation_result.is_error():
            return Err(ServiceError.ValidationFailed(validation_result.error))

        # Notify
        self.notifier.notify("Config loaded successfully")

        return Ok(ValidatedConfig(config))
```

### Repository Pattern

```python
class StateRepository:
    """Handles state persistence"""

    def __init__(self, state_file: Path):
        self.state_file = state_file

    def load(self) -> Result[ProjectState, StateError]:
        """Load state from disk"""
        if not self.state_file.exists():
            return self._create_initial_state()

        try:
            with open(self.state_file) as f:
                data = json.load(f)
            return Ok(ProjectState.from_dict(data))
        except json.JSONDecodeError as e:
            return Err(StateError.invalid_state(str(e)))
        except Exception as e:
            return Err(StateError.load_failed(str(e)))

    def save(self, state: ProjectState) -> Result[None, StateError]:
        """Save state to disk"""
        try:
            with open(self.state_file, "w") as f:
                json.dump(state.to_dict(), f, indent=2)
            return Ok(None)
        except Exception as e:
            return Err(StateError.save_failed(str(e)))

    def _create_initial_state(self) -> Result[ProjectState, StateError]:
        """Create initial state with defaults"""
        state = ProjectState.create_initial()
        save_result = self.save(state)
        if save_result.is_error():
            return Err(save_result.error)
        return Ok(state)
```

---

## Migration Checklist

When refactoring existing code:

### 1. Extract Dependencies

- [ ] Identify all dependencies in constructor
- [ ] Move from creating to accepting
- [ ] Update type hints

**Before:**

```python
class MyClass:
    def __init__(self):
        self.config = ForgeConfig()  # Creates dependency
```

**After:**

```python
class MyClass:
    def __init__(self, config: ForgeConfigManager):
        self.config = config  # Accepts dependency
```

### 2. Convert to Result Types

- [ ] Identify functions that can fail
- [ ] Define error types
- [ ] Return Result instead of raising/returning None
- [ ] Update callers to handle Result

**Before:**

```python
def load() -> dict:
    try:
        return json.load(open(path))
    except:
        return {}  # Silent failure
```

**After:**

```python
def load() -> Result[Config, ConfigError]:
    if not path.exists():
        return Err(ConfigError.not_found(str(path)))

    try:
        data = json.load(open(path))
        return Ok(Config.from_dict(data))
    except json.JSONDecodeError as e:
        return Err(ConfigError.invalid_json(str(e)))
```

### 3. Split Large Classes

- [ ] Identify responsibilities
- [ ] Extract each into focused class
- [ ] Use composition in orchestrator
- [ ] Register in DI container

**Before (God class):**

```python
class GodClass:
    def load_config(self): ...
    def save_config(self): ...
    def analyze_project(self): ...
    def migrate_dirs(self): ...
    # 400+ more lines
```

**After (Focused classes):**

```python
class ConfigLoader:
    def load(self): ...
    def save(self): ...

class ProjectAnalyzer:
    def analyze(self): ...

class DirectoryManager:
    def migrate(self): ...
    def ensure_structure(self): ...

class ConfigManager:
    def __init__(self, loader, analyzer, dirs):
        # Orchestrates components
```

### 4. Add Tests

- [ ] Test each component independently
- [ ] Test with mocks
- [ ] Test error cases
- [ ] Aim for 85%+ coverage

```python
def test_config_loader():
    loader = ConfigLoader(test_path / "config.yml")

    result = loader.load()
    assert result.is_ok()
    assert result.value.protocol_version == "1.0"

def test_config_loader_missing_file():
    loader = ConfigLoader(Path("/nonexistent"))

    result = loader.load()
    assert result.is_error()
    assert isinstance(result.error, ConfigError.NotFound)
```

---

## Best Practices

### 1. Error Handling

- Always use Result types for operations that can fail
- Define specific error types for your domain
- Never swallow errors silently
- Provide context in error messages

### 2. Dependency Injection

- Accept dependencies via constructor
- Depend on interfaces, not implementations
- Use DI container for wiring
- Keep constructors simple (just assignment)

### 3. Immutability

- Use `@dataclass(frozen=True)` for data models
- Copy-on-write for state changes
- Avoid mutable class variables
- Return new instances instead of modifying

### 4. Single Responsibility

- Each class should have one reason to change
- Extract focused classes from God objects
- Compose complex behavior from simple components
- Keep classes under 300 lines

### 5. Testability

- Inject all dependencies
- Avoid constructors with side effects
- Use pure functions where possible
- Make I/O explicit and mockable

---

## Resources

- **Architectural Review:** [ARCHITECTURAL-REVIEW-2026-01-07.md](./ARCHITECTURAL-REVIEW-2026-01-07.md)
- **Refactoring Summary:** [REFACTORING-SUMMARY-2026-01-07.md](./REFACTORING-SUMMARY-2026-01-07.md)
- **Source Code:**
  - `forge/result.py` - Result type implementation
  - `forge/directory_manager.py` - Directory management
  - `forge/container.py` - DI container
  - `forge/config_refactored.py` - Refactored config example

---

**Last Updated:** 2026-01-07
**Status:** Complete
**Phase:** 1 of 5
