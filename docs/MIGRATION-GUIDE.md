# NXTG-Forge v3 Migration Guide

**Version:** 3.0
**Date:** 2026-01-08
**Author:** nxtg.ai Master Software Architect
**Audience:** Developers using or contributing to NXTG-Forge

---

## Executive Summary

This guide helps you migrate from NXTG-Forge v2 (or earlier v3 pre-refactoring) to the refactored v3 with Result types, clean architecture, and explicit error handling.

**What Changed:**

- Exception-based → Result type-based error handling
- God classes → Clean architecture with SOLID principles
- Silent failures → Explicit error propagation
- Mixed patterns → Consistent conventions throughout

**Migration Effort:** Low to Medium

- **Simple API users:** 1-2 hours
- **Advanced users:** 4-6 hours
- **Contributors:** 8-12 hours

---

## Table of Contents

1. [Quick Start - Most Common Migrations](#quick-start)
2. [Understanding Result Types](#understanding-result-types)
3. [Error Handling Migration](#error-handling-migration)
4. [API Changes](#api-changes)
5. [CLI Changes](#cli-changes)
6. [Testing Changes](#testing-changes)
7. [Breaking Changes](#breaking-changes)
8. [Deprecations](#deprecations)
9. [Code Examples](#code-examples)
10. [Troubleshooting](#troubleshooting)

---

## Quick Start

### If you're just using the CLI

**No changes required!** The CLI remains backward compatible.

```bash
# All these still work
forge init
forge status
forge feature "Add authentication"
forge mcp
forge gap-analysis
```

### If you're importing NXTG-Forge as a library

**Update your imports and handle Result types:**

```python
# OLD (v2)
from forge.mcp_detector import MCPDetector

detector = MCPDetector()
recommendations = detector.detect()  # List or None

# NEW (v3)
from forge.mcp_detector import MCPDetector

detector = MCPDetector()
result = detector.detect()  # Result[list[MCPRecommendation], MCPDetectionError]

if result.is_error():
    print(f"Error: {result.error.message}")
    exit(1)

recommendations = result.value
```

### If you're contributing to NXTG-Forge

**Learn the new patterns:**

1. All operations return Result types
2. Use frozen dataclasses for errors
3. Static factory methods for common errors
4. Explicit error propagation
5. No exceptions for control flow

**Read the full guide below.**

---

## Understanding Result Types

### What is a Result Type?

A Result type represents an operation that can either succeed or fail, making error handling explicit and type-safe.

```python
from forge.result import Result, Ok, Err

# Success
success: Result[str, Error] = Ok("data")

# Failure
failure: Result[str, Error] = Err(SomeError("failed"))
```

### Why Result Types?

**Problems with Exceptions:**

```python
# Silent failures possible!
try:
    data = operation()
except:
    data = None  # What went wrong? Who knows!
```

**Solution with Results:**

```python
# Explicit error handling
result = operation()
if result.is_error():
    # Know exactly what went wrong
    print(f"Error: {result.error.message}")
    print(f"Context: {result.error.context}")
    return

# Safe to use value
data = result.value
```

### Basic Result API

```python
# Check result
if result.is_ok():
    value = result.value

if result.is_error():
    error = result.error

# Unwrap (raises on error)
value = result.unwrap()  # Only if you're sure it's Ok

# Unwrap with default
value = result.unwrap_or(default_value)

# Expect (custom error message)
value = result.expect("Expected operation to succeed")

# Transform values
mapped = result.map(lambda x: x.upper())

# Chain operations
chained = result.flat_map(lambda x: another_operation(x))
```

---

## Error Handling Migration

### Pattern 1: Simple Try/Except → Result

**Before (v2):**

```python
def load_config(self) -> dict[str, Any]:
    try:
        with open(self.config_file) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
```

**After (v3):**

```python
def load_config(self) -> Result[dict[str, Any], ConfigError]:
    if not self.config_file.exists():
        return Err(ConfigError.not_found(str(self.config_file)))

    try:
        with open(self.config_file) as f:
            data = json.load(f)
        return Ok(data)
    except json.JSONDecodeError as e:
        return Err(ConfigError.invalid_json(str(e)))
    except Exception as e:
        return Err(ConfigError(f"Failed to load config: {e}"))
```

**Calling Code Before:**

```python
config = loader.load_config()
if config:
    use(config)
```

**Calling Code After:**

```python
result = loader.load_config()
if result.is_error():
    print(f"Failed to load config: {result.error.message}")
    return

config = result.value
use(config)
```

### Pattern 2: Error Propagation

**Before (v2):**

```python
def high_level():
    try:
        data = low_level()
        return process(data)
    except Exception as e:
        log(e)
        return None
```

**After (v3):**

```python
def low_level() -> Result[Data, Error]:
    # ...
    return Ok(data) or Err(error)

def high_level() -> Result[Output, Error]:
    result = low_level()
    if result.is_error():
        return Err(result.error)  # Propagate

    data = result.value
    return Ok(process(data))
```

### Pattern 3: Multiple Operations

**Before (v2):**

```python
def complex_operation():
    try:
        step1 = operation1()
        step2 = operation2(step1)
        step3 = operation3(step2)
        return step3
    except Exception as e:
        log(e)
        return None
```

**After (v3):**

```python
def complex_operation() -> Result[Output, Error]:
    # Step 1
    result1 = operation1()
    if result1.is_error():
        return Err(result1.error)

    # Step 2
    result2 = operation2(result1.value)
    if result2.is_error():
        return Err(result2.error)

    # Step 3
    result3 = operation3(result2.value)
    if result3.is_error():
        return Err(result3.error)

    return Ok(result3.value)
```

**Or using flat_map:**

```python
def complex_operation() -> Result[Output, Error]:
    return (operation1()
            .flat_map(lambda r1: operation2(r1))
            .flat_map(lambda r2: operation3(r2)))
```

---

## API Changes

### Module: mcp_detector.py

**Breaking Changes:**

| Old API | New API | Migration |
|---------|---------|-----------|
| `detect() -> list` | `detect() -> Result[list[MCPRecommendation], MCPDetectionError]` | Check `is_error()` before using `.value` |
| `configure() -> None` | `configure() -> Result[None, MCPDetectionError]` | Handle errors explicitly |
| Dict recommendations | `MCPRecommendation` dataclass | Use `.name`, `.priority`, `.reason` |

**Migration Example:**

```python
# OLD
detector = MCPDetector()
recs = detector.detect()  # Could be None!
if recs:
    for rec in recs:
        print(rec["name"])

# NEW
detector = MCPDetector()
result = detector.detect()
if result.is_error():
    print(f"Detection failed: {result.error.message}")
    exit(1)

recs = result.value
for rec in recs:
    print(rec.name)  # Typed attribute
```

### Module: gap_analyzer.py

**Breaking Changes:**

| Old API | New API | Migration |
|---------|---------|-----------|
| `analyze() -> str` | `analyze() -> Result[str, GapAnalysisError]` | Check `is_error()` first |
| Exception on failure | Result type | Handle Result explicitly |

**Migration Example:**

```python
# OLD
analyzer = GapAnalyzer()
try:
    report = analyzer.analyze()
except Exception as e:
    print(f"Failed: {e}")
    exit(1)

# NEW
analyzer = GapAnalyzer()
result = analyzer.analyze()
if result.is_error():
    print(f"Analysis failed: {result.error.message}")
    if result.error.context:
        print(f"Context: {result.error.context}")
    exit(1)

report = result.value
```

### Module: state_manager.py

**DEPRECATED** - Use `state_manager_refactored.py`

**Migration:**

```python
# OLD
from forge.state_manager import StateManager

manager = StateManager()
state = manager.load()  # Could be empty dict

# NEW
from forge.state_manager_refactored import StateManager, ForgeState

manager = StateManager()
result = manager.load()
if result.is_error():
    # Handle error or create default state
    state = ForgeState.create_default()
else:
    state = result.value
```

### Module: agents/orchestrator.py

**DEPRECATED** - Use `agents/orchestrator_refactored.py`

**Major Changes:**

- God class (705 lines) → Clean architecture (160 lines)
- Mixed concerns → Separated services
- Hard-coded selection → Strategy pattern
- Mutable state → Immutable domain models

**Migration:**

```python
# OLD
from forge.agents.orchestrator import AgentOrchestrator

orch = AgentOrchestrator()
task = orch.create_task("Do something", "feature")
result = orch.execute_task(task)

# NEW
from forge.agents.orchestrator_refactored import AgentOrchestrator
from forge.agents.selection.strategy import KeywordStrategy

orch = AgentOrchestrator(strategy=KeywordStrategy())
task = orch.create_task("Do something", "feature")
result = orch.execute_task(task)

if result.is_error():
    print(f"Execution failed: {result.error}")
    exit(1)

task_result = result.value
```

---

## CLI Changes

### Backward Compatible

The CLI interface remains backward compatible. All commands work as before:

```bash
forge init
forge status
forge feature "Add authentication"
```

### Enhanced Error Messages

Error messages are now more informative:

**Before:**

```
Error occurred
```

**After:**

```
Error: MCP detection failed
Context: Node.js not found
```

### Exit Codes

Exit codes are now standardized:

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Invalid arguments |

---

## Testing Changes

### Testing Result-Returning Functions

**Before:**

```python
def test_operation():
    result = operation()
    assert result is not None
    assert result["key"] == "value"
```

**After:**

```python
def test_operation_success():
    result = operation()
    assert result.is_ok()
    assert result.value.key == "value"

def test_operation_failure():
    result = operation_with_bad_input()
    assert result.is_error()
    assert "expected error message" in result.error.message
```

### Mocking with Results

```python
from unittest.mock import Mock
from forge.result import Ok, Err, ConfigError

# Mock successful operation
mock_service = Mock()
mock_service.load_config.return_value = Ok({"key": "value"})

# Mock failed operation
mock_service.load_config.return_value = Err(ConfigError.not_found("/path"))

# Test code
result = mock_service.load_config()
assert result.is_ok()
```

---

## Breaking Changes

### Summary of All Breaking Changes

| Module | Change | Impact | Migration Effort |
|--------|--------|--------|------------------|
| **mcp_detector.py** | Returns Result types | HIGH | 1 hour |
| **gap_analyzer.py** | Returns Result types | MEDIUM | 30 min |
| **state_manager.py** | Deprecated | MEDIUM | 1 hour |
| **orchestrator.py** | Deprecated | HIGH | 2-4 hours |
| **All error handling** | Result types | HIGH | Varies |

### Detailed Breaking Changes

#### 1. MCP Detector

```python
# BREAKING: detect() return type changed
# OLD: list[dict] | None
# NEW: Result[list[MCPRecommendation], MCPDetectionError]

# Migration required in all calling code
```

#### 2. Gap Analyzer

```python
# BREAKING: analyze() return type changed
# OLD: str (raises on error)
# NEW: Result[str, GapAnalysisError]

# Migration required in all calling code
```

#### 3. State Manager

```python
# BREAKING: Module deprecated
# OLD: from forge.state_manager import StateManager
# NEW: from forge.state_manager_refactored import StateManager

# All methods now return Result types
```

#### 4. Agent Orchestrator

```python
# BREAKING: Complete rewrite
# OLD: 705-line god class
# NEW: Clean architecture with services

# Requires complete rewrite of integration code
```

---

## Deprecations

### Deprecated Modules (Still Work, Will Be Removed)

| Module | Status | Replacement | Removal |
|--------|--------|-------------|---------|
| `forge/agents/orchestrator.py` | Deprecated | `orchestrator_refactored.py` | v4.0 |
| `forge/state_manager.py` | Deprecated | `state_manager_refactored.py` | v4.0 |
| `forge/cli.py` | Deprecated | `cli_refactored.py` | v4.0 |

### Migration Timeline

- **v3.0** (Current): Deprecated modules still work, warnings logged
- **v3.5** (Q2 2026): Deprecation warnings escalated
- **v4.0** (Q4 2026): Deprecated modules removed

**Action Required:** Migrate to refactored modules before v4.0

---

## Code Examples

### Example 1: Complete MCP Detection Migration

**Before (v2):**

```python
from forge.mcp_detector import MCPDetector

detector = MCPDetector()
recommendations = detector.detect()

if not recommendations:
    print("No servers found")
    exit(0)

for rec in recommendations:
    print(f"{rec['name']}: {rec['priority']}")

detector.configure()
print("Configured!")
```

**After (v3):**

```python
from forge.mcp_detector import MCPDetector

detector = MCPDetector()

# Detect with error handling
result = detector.detect()
if result.is_error():
    print(f"Detection failed: {result.error.message}")
    if result.error.context:
        print(f"Details: {result.error.context}")
    exit(1)

recommendations = result.value
if not recommendations:
    print("No servers found")
    exit(0)

for rec in recommendations:
    print(f"{rec.name}: {rec.priority}")

# Configure with error handling
config_result = detector.configure()
if config_result.is_error():
    print(f"Configuration failed: {config_result.error.message}")
    exit(1)

print("Configured!")
```

### Example 2: Gap Analysis Migration

**Before (v2):**

```python
from forge.gap_analyzer import GapAnalyzer

analyzer = GapAnalyzer(project_root=".")
try:
    report = analyzer.analyze()
    with open("report.md", "w") as f:
        f.write(report)
except Exception as e:
    print(f"Analysis failed: {e}")
    exit(1)
```

**After (v3):**

```python
from forge.gap_analyzer import GapAnalyzer

analyzer = GapAnalyzer(project_root=".")

result = analyzer.analyze()
if result.is_error():
    print(f"Analysis failed: {result.error.message}")
    if result.error.context:
        print(f"Context: {result.error.context}")
    exit(1)

report = result.value
try:
    with open("report.md", "w") as f:
        f.write(report)
    print("Report saved!")
except IOError as e:
    print(f"Failed to save report: {e}")
    exit(1)
```

### Example 3: Custom Service with Result Types

**Creating a new service:**

```python
from dataclasses import dataclass
from forge.result import Result, Ok, Err

@dataclass(frozen=True)
class MyServiceError:
    """My service errors."""

    message: str
    context: str | None = None

    @staticmethod
    def operation_failed(reason: str) -> "MyServiceError":
        return MyServiceError("Operation failed", reason)

class MyService:
    """My service using Result types."""

    def perform_operation(self, input: str) -> Result[str, MyServiceError]:
        """Perform operation with explicit error handling.

        Args:
            input: Input string

        Returns:
            Result containing output or error
        """
        if not input:
            return Err(MyServiceError.operation_failed("Input cannot be empty"))

        try:
            output = self._process(input)
            return Ok(output)
        except ValueError as e:
            return Err(MyServiceError.operation_failed(str(e)))

    def _process(self, input: str) -> str:
        """Internal processing."""
        return input.upper()
```

---

## Troubleshooting

### Common Issues

#### Issue: "AttributeError: 'Result' object has no attribute 'key'"

**Cause:** Trying to access Result like a dict/object

**Solution:** Check `is_ok()` first and use `.value`

```python
# WRONG
result = operation()
print(result.some_field)  # Error!

# RIGHT
result = operation()
if result.is_ok():
    print(result.value.some_field)
```

#### Issue: "TypeError: 'Result' object is not iterable"

**Cause:** Trying to iterate over Result instead of value

**Solution:** Extract value first

```python
# WRONG
result = operation()
for item in result:  # Error!
    print(item)

# RIGHT
result = operation()
if result.is_ok():
    for item in result.value:
        print(item)
```

#### Issue: "Module not found: forge.state_manager_refactored"

**Cause:** Using old import path

**Solution:** Update import

```python
# OLD
from forge.state_manager import StateManager

# NEW
from forge.state_manager_refactored import StateManager
```

#### Issue: "Tests failing after migration"

**Cause:** Tests expect old API

**Solution:** Update tests to handle Result types

```python
# OLD TEST
def test_operation():
    result = operation()
    assert result is not None

# NEW TEST
def test_operation():
    result = operation()
    assert result.is_ok()
    assert result.value is not None
```

### Getting Help

**Documentation:**

- `docs/ERROR-HANDLING-AUDIT.md` - Error handling patterns
- `docs/PHASE-4-ERROR-HANDLING-COMPLETE.md` - Result type details
- `docs/CODE-CONSISTENCY-REVIEW.md` - Coding standards

**Examples:**

- See tests in `tests/unit/` for Result type usage
- Check refactored modules for patterns

**Support:**

- GitHub Issues: Report migration problems
- Discussions: Ask questions about migration

---

## Checklist: Migration Complete

Use this checklist to ensure complete migration:

### Code Changes

- [ ] All imports updated to new modules
- [ ] All function calls handle Result types
- [ ] Error handling uses `is_error()` checks
- [ ] Values extracted with `.value` after `is_ok()` check
- [ ] No deprecated modules used

### Testing

- [ ] All tests updated for Result types
- [ ] Both success and error paths tested
- [ ] Mocks return Result types
- [ ] Tests pass locally

### Documentation

- [ ] Code comments updated
- [ ] API documentation reflects Result types
- [ ] Examples show proper Result handling

### Deployment

- [ ] Integration tests pass
- [ ] Staging deployment successful
- [ ] Production deployment plan reviewed

---

## Summary

### Key Takeaways

1. **Result types are everywhere** - All operations that can fail return Result
2. **Always check `is_error()`** - Before accessing `.value`
3. **Errors are explicit** - No more silent failures
4. **Deprecated modules work** - But migrate before v4.0
5. **CLI is backward compatible** - No changes needed for basic CLI usage

### Migration Priority

**High Priority (Do First):**

1. Update `mcp_detector` usage
2. Update `gap_analyzer` usage
3. Migrate from deprecated `state_manager`

**Medium Priority (Next):**
4. Update test suite
5. Migrate custom services to Result types

**Low Priority (Later):**
6. Update internal tooling
7. Optimize error handling patterns

### Next Steps

1. Read this guide thoroughly
2. Update imports to refactored modules
3. Add Result type handling to calling code
4. Update tests
5. Test thoroughly
6. Deploy

---

**Version:** 1.0
**Last Updated:** 2026-01-08
**Status:** Complete and production-ready

**Questions?** Check the troubleshooting section or file an issue.
