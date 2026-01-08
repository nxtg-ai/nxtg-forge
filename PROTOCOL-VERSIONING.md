# Protocol Versioning Strategy

## Overview

NXTG-Forge uses **two distinct version numbers**:

1. **Package Version** (`FORGE_VERSION`) - Semantic versioning for the Python package
2. **Protocol Version** (`PROTOCOL_VERSION`) - API contract versioning for Claude Code integration

This document defines when and how each version changes.

---

## Package Version (FORGE_VERSION)

**Source of Truth**: `pyproject.toml` → `version` field

**Format**: `X.Y.Z` (Semantic Versioning 2.0.0)

**Example**: `1.2.3`

### Semantic Versioning Rules

Given version `MAJOR.MINOR.PATCH`:

- **PATCH** (`1.0.0` → `1.0.1`): Bug fixes, documentation updates, internal refactoring
- **MINOR** (`1.0.1` → `1.1.0`): New features, backwards-compatible changes
- **MAJOR** (`1.1.0` → `2.0.0`): Breaking changes to public API

### Examples

| Change | Old Version | New Version | Type |
|--------|-------------|-------------|------|
| Fix typo in error message | 1.0.0 | 1.0.1 | PATCH |
| Add new CLI command | 1.0.1 | 1.1.0 | MINOR |
| Remove deprecated function | 1.1.0 | 2.0.0 | MAJOR |
| Add optional parameter | 1.2.0 | 1.3.0 | MINOR |
| Change config file structure | 1.3.0 | 2.0.0 | MAJOR |

---

## Protocol Version (PROTOCOL_VERSION)

**Source of Truth**: `forge/config.py` → `ForgeConfig.PROTOCOL_VERSION`

**Format**: `X.Y` (Major.Minor only)

**Example**: `1.0`

### Protocol Version Rules

The protocol version defines the **contract between Claude Code and NXTG-Forge**.

**Only changes when:**
- `.claude/forge/config.yml` structure changes in a breaking way
- `handle_request()` API signature changes
- State file schema changes incompatibly
- Integration API contract breaks

**Does NOT change when:**
- Package version changes for bug fixes
- New features are added to existing APIs
- Internal implementation changes
- Documentation updates

### Version Matrix

| Scenario | Package Version Change | Protocol Version Change |
|----------|------------------------|-------------------------|
| Fix bug in file generator | 1.0.0 → 1.0.1 (PATCH) | 1.0 → 1.0 (unchanged) |
| Add new CLI command | 1.0.1 → 1.1.0 (MINOR) | 1.0 → 1.0 (unchanged) |
| Add optional config field | 1.1.0 → 1.2.0 (MINOR) | 1.0 → 1.0 (unchanged) |
| Add new feature that requires config change (backwards compatible) | 1.2.0 → 1.3.0 (MINOR) | 1.0 → 1.1 (MINOR) |
| Change config structure (breaking) | 1.3.0 → 2.0.0 (MAJOR) | 1.1 → 2.0 (MAJOR) |
| Remove deprecated integration API | 2.0.0 → 3.0.0 (MAJOR) | 2.0 → 3.0 (MAJOR) |

### Protocol Compatibility

**Rule**: Claude Code checks protocol version before using forge.

```python
from forge.config import ForgeConfig

config = ForgeConfig()
protocol_version = config.PROTOCOL_VERSION

if protocol_version.startswith("1."):
    # Use v1 protocol
    use_v1_protocol()
elif protocol_version.startswith("2."):
    # Use v2 protocol
    use_v2_protocol()
else:
    # Unknown protocol, fallback
    use_standard_behavior()
```

**Backwards Compatibility Promise**:
- Minor protocol bumps (1.0 → 1.1) are backwards compatible
- Major protocol bumps (1.x → 2.0) may break compatibility
- Claude Code must support at least 2 major protocol versions

---

## Version Synchronization

### Single Source of Truth

**Package Version**:
```
pyproject.toml (canonical)
    ↓ (importlib.metadata)
forge/__init__.py (__version__)
    ↓ (import from forge)
forge/cli.py (FORGE_VERSION)
forge/integration.py (_FORGE_VERSION)
forge/config.py (FORGE_VERSION property)
    ↓ (scripts/sync-version.py)
package.json
scripts/install.sh
.claude/state.json.template
```

**Protocol Version**:
```
forge/config.py (PROTOCOL_VERSION class variable)
    ↓ (manual update only when protocol changes)
```

### Automated Synchronization

**Tool**: `scripts/sync-version.py`

**Usage**:
```bash
# Sync all files to current pyproject.toml version
python scripts/sync-version.py

# Check if versions are synchronized (CI/CD)
python scripts/sync-version.py --check
```

**What it syncs**:
- package.json → version field
- scripts/install.sh → FORGE_VERSION variable
- .claude/state.json.template → version and forge_version fields

### Version Bumping

**Tool**: `scripts/bump-version.sh`

**Usage**:
```bash
# Bump patch version (1.0.0 → 1.0.1)
./scripts/bump-version.sh patch

# Bump minor version (1.0.1 → 1.1.0)
./scripts/bump-version.sh minor

# Bump major version (1.1.0 → 2.0.0)
./scripts/bump-version.sh major

# Set specific version
./scripts/bump-version.sh 1.2.3
```

**What it does**:
1. Updates `pyproject.toml` version
2. Runs `scripts/sync-version.py` to sync all files
3. Updates `CHANGELOG.md` with new version header
4. Prints next steps (commit, tag, push)

---

## Release Workflow

### Standard Release (Patch/Minor)

```bash
# 1. Bump version (package only)
./scripts/bump-version.sh minor  # or patch

# 2. Update CHANGELOG.md with release notes
# [Manual edit]

# 3. Commit and tag
git commit -am "chore: release v1.1.0"
git tag -a v1.1.0 -m "Release v1.1.0"

# 4. Push
git push && git push --tags

# Protocol version: unchanged (still 1.0)
```

### Protocol-Breaking Release (Major)

```bash
# 1. Manually update protocol version in forge/config.py
# Change: PROTOCOL_VERSION = "1.0" → PROTOCOL_VERSION = "2.0"

# 2. Bump package version (major)
./scripts/bump-version.sh major  # 1.x.x → 2.0.0

# 3. Update CHANGELOG.md with BREAKING CHANGES
# [Manual edit - document protocol changes]

# 4. Update integration docs
# [Update .claude/forge/AUTO-SETUP.md with protocol v2 details]

# 5. Commit and tag
git commit -am "chore: release v2.0.0 (BREAKING: protocol v2)"
git tag -a v2.0.0 -m "Release v2.0.0 - Protocol v2"

# 6. Push
git push && git push --tags
```

---

## Verification

### Pre-commit Hook

The version sync check runs automatically on commit:

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: version-sync-check
      name: Check version synchronization
      entry: python scripts/sync-version.py --check
      language: python
      pass_filenames: false
```

### CI/CD Check

```yaml
# .github/workflows/ci.yml
- name: Verify version synchronization
  run: |
    python scripts/sync-version.py --check
```

### Manual Verification

```bash
# Check all versions match
python -c "
import forge
from forge.config import ForgeConfig
from forge.cli import FORGE_VERSION
from forge.integration import get_forge_version

versions = [forge.__version__, FORGE_VERSION, get_forge_version()]
config = ForgeConfig()
versions.append(config.FORGE_VERSION)

if len(set(versions)) == 1:
    print(f'✅ All versions: {versions[0]}')
else:
    print(f'❌ Mismatch: {versions}')
"
```

---

## FAQ

### Q: When do I bump the protocol version?

**A**: Only when you change something that breaks the integration contract:
- Config file structure changes (breaking)
- Integration API changes (breaking)
- State file schema changes (incompatible)

If you're not sure, **don't bump it**. Most releases don't need protocol version bumps.

### Q: Can I have protocol v1.1 with package v2.0.0?

**A**: Yes! Package version can change many times without protocol version changing.

Example timeline:
- v1.0.0 (protocol 1.0) - Initial release
- v1.1.0 (protocol 1.0) - New features, same protocol
- v1.2.0 (protocol 1.0) - More features, same protocol
- v2.0.0 (protocol 1.0) - Breaking Python API change, protocol unchanged
- v2.1.0 (protocol 1.1) - Config file gets new optional fields
- v3.0.0 (protocol 2.0) - Major protocol overhaul

### Q: What if I forget to sync versions?

**A**: The pre-commit hook will catch it and prevent the commit. If you bypass hooks, CI/CD will catch it and fail the build.

### Q: Can I manually edit versions in files?

**A**: **NO**. Only edit `pyproject.toml` version, then run `scripts/sync-version.py`. All other files are auto-generated.

Exception: `PROTOCOL_VERSION` in `forge/config.py` must be manually updated when protocol changes.

---

## Version History

### Protocol Version History

| Protocol | Package Versions | Changes |
|----------|------------------|---------|
| 1.0 | 1.0.0 - current | Initial protocol from AUTO-SETUP.md |

### Compatibility Matrix

| Claude Code Version | Protocol Support | Forge Versions |
|---------------------|------------------|----------------|
| 2024.x | 1.x | 1.0.0+ |

---

**Last Updated**: 2026-01-07
**Status**: Active
**Authority**: This document defines the canonical versioning strategy for NXTG-Forge.
