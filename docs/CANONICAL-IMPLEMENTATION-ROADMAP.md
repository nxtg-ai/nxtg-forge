# CANONICAL FORGE IMPLEMENTATION ROADMAP

**Practical step-by-step guide to implement NXTG-Forge 2.0**

**Status:** Implementation Plan
**Date:** 2026-01-08
**Estimated Timeline:** 4-6 weeks (3-4 focused development sprints)

---

## Prerequisites

**Before starting implementation:**

- [x] Canonical vision approved by Asif
- [x] Architecture decisions finalized (5 ADRs)
- [x] Current v3 codebase in stable state (B+ grade, 85/100)
- [ ] Team alignment on migration strategy
- [ ] Test project(s) identified for validation

---

## Implementation Phases

### Phase 1: Foundation (Week 1)

**Goal:** Create native agent templates and service refactoring

#### 1.1 Create Agent Prompt Templates

**Task:** Design markdown prompts for all 5 agents

**Deliverables:**

```
.claude/agents/
├── agent-forge-orchestrator.md  (300-400 lines)
├── agent-forge-architect.md     (200-300 lines)
├── agent-forge-backend.md       (200-300 lines)
├── agent-forge-qa.md            (200-300 lines)
└── agent-forge-integration.md   (200-300 lines)
```

**Orchestrator Template Structure:**

```markdown
# Agent: Forge Orchestrator

## Identity & Role
[Who you are, what you coordinate]

## Available Agents
[List of specialist agents with capabilities]

## Available Tools (forge CLI)
[State management, quality, git commands]

## Workflow Phases
1. Understand & Plan
2. Execute
3. Validate
4. Report

## Menu Interface
[Interactive menu presented to user]

## Quality Standards
[Non-negotiable quality requirements]

## Example Scenarios
[Detailed walkthroughs of common tasks]

## Error Handling
[How to handle failures gracefully]
```

**Acceptance Criteria:**

- [ ] All 5 agent prompts created
- [ ] Orchestrator menu interface defined
- [ ] Agent invocation patterns documented
- [ ] Quality standards explicit
- [ ] Tested with manual agent invocation

**Estimated Effort:** 3-4 days

#### 1.2 Refactor Python Services

**Task:** Reorganize Python code to support agent-driven architecture

**Current Structure:**

```
forge/agents/
├── orchestrator.py        ← DELETE
├── dispatcher.py          ← DELETE
├── selection/             ← DELETE
├── execution/             ← DELETE
├── domain/                ← MOVE to forge/domain/
└── services/              ← MOVE to forge/services/
```

**Target Structure:**

```
forge/
├── domain/                ← From agents/domain/
│   ├── agent.py
│   ├── task.py
│   └── message.py
├── services/              ← Consolidated services
│   ├── state_manager.py   (already refactored ✓)
│   ├── git_service.py     (NEW)
│   ├── quality_service.py (NEW)
│   ├── checkpoint_service.py (NEW)
│   ├── agent_loader.py    (from agents/services/)
│   ├── task_service.py    (from agents/services/)
│   └── mcp_detector.py    (refactored)
├── utils/
│   ├── result.py          (existing ✓)
│   ├── config.py          (existing ✓)
│   └── directory_manager.py (existing ✓)
└── cli.py                 (updated for new architecture)
```

**New Services to Create:**

**git_service.py:**

```python
"""Git operations for NXTG-Forge."""

from pathlib import Path
from forge.utils.result import Result, Ok, Err
from forge.domain.git import Branch, Commit, PullRequest

class GitService:
    """Handles all git operations."""

    def create_branch(self, feature_name: str) -> Result[Branch, GitError]:
        """Create feature branch."""
        # Implementation

    def commit(
        self,
        message: str,
        files: list[Path],
        conventional: bool = True
    ) -> Result[Commit, GitError]:
        """Create commit with conventional format."""
        # Implementation

    def create_pr(
        self,
        title: str,
        body: str,
        base: str = "main"
    ) -> Result[PullRequest, GitError]:
        """Create pull request."""
        # Implementation
```

**quality_service.py:**

```python
"""Quality check orchestration."""

from forge.utils.result import Result, Ok, Err
from forge.domain.quality import QualityReport

class QualityService:
    """Orchestrates quality checks."""

    def run_all_checks(self) -> Result[QualityReport, QualityError]:
        """Run tests, coverage, linting, security."""
        # Implementation

    def run_tests(self) -> Result[TestResult, QualityError]:
        """Run test suite."""
        # Implementation

    def check_coverage(self, threshold: float = 80.0) -> Result[Coverage, QualityError]:
        """Check code coverage."""
        # Implementation

    def lint_code(self) -> Result[LintResult, QualityError]:
        """Run linter."""
        # Implementation

    def security_scan(self) -> Result[SecurityReport, QualityError]:
        """Run security scanner."""
        # Implementation
```

**Acceptance Criteria:**

- [ ] All services moved/created
- [ ] Services use Result types throughout
- [ ] Domain models immutable and type-safe
- [ ] Services testable in isolation
- [ ] 80%+ test coverage for new services

**Estimated Effort:** 3-4 days

---

### Phase 2: CLI Integration (Week 2)

**Goal:** Update CLI to support agent-driven workflows

#### 2.1 Create forge CLI Commands

**New Commands:**

**forge state (subcommands):**

```bash
# State queries
forge state get                          # Get current state
forge state get-feature --id <id>        # Get specific feature
forge state get-task --id <id>           # Get specific task

# State updates
forge state create-feature --name <name> --description <desc>
forge state update-feature --id <id> --status <status>
forge state create-task --description <desc>
forge state update-task --id <id> --status <status>
forge state mark-complete --id <id>

# Session management
forge state create-session --id <id>
forge state update-session --task <task>
```

**forge quality:**

```bash
forge quality check                      # Run all quality checks
forge quality test                       # Run tests only
forge quality coverage                   # Coverage report
forge quality lint                       # Lint code
forge quality security                   # Security scan
```

**forge git:**

```bash
forge git create-branch --feature <name>
forge git commit --message <msg> [--files <files>] [--conventional]
forge git create-pr --title <title> [--body <body>] [--base <branch>]
```

**forge checkpoint:**

```bash
forge checkpoint create --description <desc>
forge checkpoint list
forge checkpoint restore --id <id>
```

**CLI Structure:**

```python
# forge/cli.py (refactored)

import click
from forge.services import (
    StateManager,
    GitService,
    QualityService,
    CheckpointService
)

@click.group()
def cli():
    """NXTG-Forge CLI."""
    pass

@cli.group()
def state():
    """State management commands."""
    pass

@state.command()
def get():
    """Get current state."""
    service = StateManager()
    result = service.get_state()
    # Handle result, print output

@cli.group()
def quality():
    """Quality check commands."""
    pass

@quality.command()
def check():
    """Run all quality checks."""
    service = QualityService()
    result = service.run_all_checks()
    # Handle result, print report

# ... more commands
```

**Acceptance Criteria:**

- [ ] All CLI commands implemented
- [ ] Commands use services (not direct implementation)
- [ ] Error handling via Result types
- [ ] Clear, helpful output messages
- [ ] Non-interactive (can be called from agents/hooks)
- [ ] Integration tests for all commands

**Estimated Effort:** 4-5 days

#### 2.2 Update Slash Commands

**Update existing commands to use agents:**

**.claude/commands/enable-forge.md:**

```markdown
---
description: "Activate the NXTG-Forge orchestrator"
---

# Enable NXTG-Forge

Activates the forge orchestrator for guided development.

## What This Does

Invokes the `agent-forge-orchestrator` agent, which presents
an interactive menu to guide your development workflow.

## Activation

Invoke agent: agent-forge-orchestrator

[Agent takes over with menu interface]
```

**.claude/commands/feature.md:**

```markdown
---
description: "Create new feature with orchestration"
---

# Feature Command

Quick feature creation via orchestrator.

## Usage

Arguments: $ARGUMENTS

Expected format: `/feature "Feature Name"`

## Delegation

This command delegates to the orchestrator:

Invoke agent: agent-forge-orchestrator

Context: User wants to create feature: "$ARGUMENTS"
Please proceed directly to feature planning.
```

**Acceptance Criteria:**

- [ ] Commands delegate to agents (not Python code)
- [ ] Clear, concise command descriptions
- [ ] Proper context passed to agents
- [ ] Commands tested manually

**Estimated Effort:** 1-2 days

---

### Phase 3: Migration Tool (Week 3)

**Goal:** Create automated migration from v3 → v2.0

#### 3.1 Build Migration Tool

**Command:** `forge upgrade v2`

**Migration Steps:**

1. **Backup current structure**

   ```bash
   cp -r .claude .claude.v1.backup
   ```

2. **Create v2.0 agent directory**

   ```bash
   mkdir -p .claude/agents
   ```

3. **Copy agent templates**

   ```bash
   # From forge package templates
   cp forge/templates/.claude/agents/* .claude/agents/
   ```

4. **Update commands**

   ```bash
   # Update enable-forge.md
   # Update feature.md
   # Keep others (already compatible)
   ```

5. **Validate state.json**

   ```bash
   # Ensure state.json schema compatible
   # No changes needed (format unchanged)
   ```

6. **Create FORGE-ENABLED marker**

   ```bash
   touch .claude/FORGE-ENABLED
   ```

7. **Update config.yml**

   ```bash
   # Add version: "2.0.0"
   # Add agents: [list of forge agents]
   ```

**Implementation:**

```python
# forge/commands/upgrade.py

from pathlib import Path
import shutil
from forge.utils.result import Result, Ok, Err

class UpgradeCommand:
    """Handle v3 → v2.0 migration."""

    def execute(self, target_version: str) -> Result[None, UpgradeError]:
        """Execute upgrade."""

        if target_version != "v2":
            return Err(UpgradeError("Only v2 upgrade supported"))

        # 1. Validate current state
        if not self._validate_current_installation():
            return Err(UpgradeError("Invalid current installation"))

        # 2. Backup
        backup_result = self._backup_current_structure()
        if backup_result.is_err():
            return backup_result

        # 3. Create v2 structure
        create_result = self._create_v2_structure()
        if create_result.is_err():
            # Rollback
            self._restore_from_backup()
            return create_result

        # 4. Migrate data
        migrate_result = self._migrate_data()
        if migrate_result.is_err():
            self._restore_from_backup()
            return migrate_result

        # 5. Validate migration
        validate_result = self._validate_migration()
        if validate_result.is_err():
            self._restore_from_backup()
            return validate_result

        return Ok(None)

    def _backup_current_structure(self) -> Result[None, UpgradeError]:
        """Backup .claude/ directory."""
        # Implementation

    def _create_v2_structure(self) -> Result[None, UpgradeError]:
        """Create v2.0 directory structure."""
        # Implementation

    def _migrate_data(self) -> Result[None, UpgradeError]:
        """Migrate state.json, config, etc."""
        # Implementation

    def _validate_migration(self) -> Result[None, UpgradeError]:
        """Ensure migration successful."""
        # Implementation

    def _restore_from_backup(self) -> None:
        """Rollback on error."""
        # Implementation
```

**Acceptance Criteria:**

- [ ] Migration tool implemented
- [ ] Automatic backup before migration
- [ ] Rollback on any error
- [ ] Validation of migrated structure
- [ ] Clear progress messages
- [ ] Tested on multiple real projects

**Estimated Effort:** 3-4 days

#### 3.2 Downgrade Support

**Command:** `forge downgrade v1`

**Purpose:** Allow rollback to v3 if issues found

**Implementation:**

```python
def downgrade_to_v1(self) -> Result[None, DowngradeError]:
    """Restore v1 from backup."""

    backup_path = Path(".claude.v1.backup")

    if not backup_path.exists():
        return Err(DowngradeError("No v1 backup found"))

    # Remove v2 structure
    shutil.rmtree(".claude/agents")
    # Restore from backup
    shutil.copytree(backup_path, ".claude", dirs_exist_ok=True)

    return Ok(None)
```

**Acceptance Criteria:**

- [ ] Downgrade tool implemented
- [ ] Restores from backup
- [ ] Tested on migrated projects

**Estimated Effort:** 1 day

---

### Phase 4: Testing & Validation (Week 4)

**Goal:** Comprehensive testing of v2.0 architecture

#### 4.1 Unit Tests

**Test Coverage Goals:**

- Domain models: 95%+
- Services: 85%+
- CLI commands: 80%+
- Overall: 85%+

**Critical Test Scenarios:**

**State Management:**

```python
def test_state_update_feature():
    """Test feature status update."""
    service = StateManager()
    result = service.update_feature(
        feature_id="feat-123",
        status="completed"
    )
    assert result.is_ok()
    # Verify state updated

def test_state_update_nonexistent_feature():
    """Test updating non-existent feature fails gracefully."""
    service = StateManager()
    result = service.update_feature(
        feature_id="nonexistent",
        status="completed"
    )
    assert result.is_err()
    assert isinstance(result.unwrap_err(), FeatureNotFoundError)
```

**Git Service:**

```python
def test_create_branch():
    """Test branch creation."""
    service = GitService()
    result = service.create_branch("payment-processing")
    assert result.is_ok()
    # Verify branch created

def test_conventional_commit():
    """Test conventional commit format."""
    service = GitService()
    result = service.commit(
        message="Add Stripe integration",
        files=[Path("payment/service.py")],
        conventional=True
    )
    assert result.is_ok()
    commit = result.unwrap()
    assert commit.message.startswith("feat:")
```

**Acceptance Criteria:**

- [ ] All critical paths tested
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] 85%+ overall coverage
- [ ] All tests passing

**Estimated Effort:** 4-5 days

#### 4.2 Integration Tests

**Test Agent Workflows:**

```python
def test_orchestrator_feature_workflow():
    """Test complete feature workflow via orchestrator."""

    # Setup
    init_project()

    # Simulate agent invocation
    result = invoke_agent(
        "agent-forge-orchestrator",
        context={"user_request": "Add user authentication"}
    )

    # Verify orchestrator response
    assert "feature" in result.lower()
    assert "authentication" in result.lower()

    # Verify state updated
    state = get_state()
    assert state.has_feature("user-authentication")

    # Verify files created
    assert Path("auth/models.py").exists()
    assert Path("tests/test_auth.py").exists()
```

**Test Quality Hooks:**

```python
def test_post_task_hook():
    """Test post-task hook execution."""

    # Create test file
    Path("test.py").write_text("def test(): pass")

    # Run post-task hook
    result = run_hook("post-task.sh")

    # Verify tests ran
    assert "tests passed" in result.output

    # Verify coverage checked
    assert "coverage" in result.output

    # Verify state updated
    state = get_state()
    assert state.quality.last_test_run is not None
```

**Acceptance Criteria:**

- [ ] Agent invocation workflows tested
- [ ] Hook automation tested
- [ ] State persistence verified
- [ ] Git workflow integration tested
- [ ] End-to-end scenarios passing

**Estimated Effort:** 3-4 days

#### 4.3 Real Project Validation

**Test on Real Projects:**

Select 2-3 test projects:

1. **Simple Python API** (Flask/FastAPI)
2. **Complex Microservice** (with database, cache, etc.)
3. **Existing NXTG-Forge v3 Project** (migration test)

**For each project:**

1. Run `forge init` or `forge upgrade v2`
2. Test `/enable-forge`
3. Create feature end-to-end
4. Verify quality checks
5. Verify git workflow
6. Check observability (logs, checkpoints)

**Success Criteria:**

- [ ] All test projects initialize successfully
- [ ] Features created without errors
- [ ] Quality enforced automatically
- [ ] Git workflow produces clean PRs
- [ ] Complete audit trail available

**Estimated Effort:** 3-4 days

---

### Phase 5: Documentation & Release (Week 5-6)

**Goal:** Complete documentation and prepare release

#### 5.1 Update Documentation

**Documents to Update:**

1. **README.md**
   - Quick start with v2.0
   - Installation steps
   - `/enable-forge` workflow
   - Example scenarios

2. **ARCHITECTURE.md**
   - Native agent integration
   - Service architecture
   - Data flow diagrams

3. **GETTING-STARTED.md**
   - Step-by-step tutorial
   - First feature walkthrough
   - Common workflows

4. **API-REFERENCE.md**
   - forge CLI commands
   - Agent invocation patterns
   - Service APIs

5. **MIGRATION-GUIDE.md**
   - v3 → v2.0 migration
   - Breaking changes (if any)
   - Rollback procedures

6. **ADRs (Architecture Decision Records)**
   - Document all 5 ADRs formally
   - Context, alternatives, rationale

**Acceptance Criteria:**

- [ ] All docs updated
- [ ] Examples tested and verified
- [ ] Screenshots/demos created
- [ ] API reference complete
- [ ] Migration guide validated

**Estimated Effort:** 5-6 days

#### 5.2 Create Release Package

**Release Checklist:**

- [ ] Version bumped to 2.0.0 (pyproject.toml)
- [ ] CHANGELOG.md updated
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Migration tool tested
- [ ] Example projects created
- [ ] PyPI package built
- [ ] GitHub release created

**Release Artifacts:**

1. **PyPI Package**

   ```bash
   python -m build
   twine upload dist/*
   ```

2. **GitHub Release**
   - Tag: v2.0.0
   - Release notes
   - Migration guide link
   - Breaking changes (if any)

3. **Example Projects**
   - Simple API with NXTG-Forge
   - Microservice with full automation
   - Migration example (v3 → v2.0)

**Acceptance Criteria:**

- [ ] Package published to PyPI
- [ ] GitHub release created
- [ ] Example projects published
- [ ] Announcement prepared

**Estimated Effort:** 2-3 days

#### 5.3 Rollout Strategy

**Phased Rollout:**

**Phase 1: Alpha (Week 5)**

- Internal testing only
- 2-3 real projects
- Bug fixes and refinements

**Phase 2: Beta (Week 6)**

- Limited external beta (opt-in)
- Collect feedback
- Documentation improvements

**Phase 3: General Availability (Week 7)**

- Public release
- PyPI publication
- Announcement

**Monitoring:**

- Track installations
- Monitor error reports
- Collect user feedback
- Address issues quickly

---

## Risk Mitigation

### Risk 1: Agent Prompt Complexity

**Risk:** Orchestrator prompt too complex to maintain

**Mitigation:**

- Start simple, add complexity incrementally
- Modular prompt structure (sections)
- Regular refactoring of prompts
- Version control for prompt changes

### Risk 2: Migration Failures

**Risk:** v3 → v2.0 migration breaks projects

**Mitigation:**

- Comprehensive testing on real projects
- Automatic backup before migration
- Easy rollback (`forge downgrade v1`)
- Clear error messages and recovery steps

### Risk 3: Performance Issues

**Risk:** Agent coordination overhead

**Mitigation:**

- Benchmark all operations
- Optimize hot paths
- Parallel execution where possible
- Caching for expensive operations

### Risk 4: Adoption Challenges

**Risk:** Users don't understand new architecture

**Mitigation:**

- Excellent documentation
- Video tutorials
- Example projects
- Active support during rollout

---

## Success Metrics

### Technical Metrics

**Before Release:**

- [ ] 85%+ test coverage
- [ ] 0 critical bugs
- [ ] < 100ms agent invocation overhead
- [ ] < 2s hook execution time
- [ ] Migration success rate: 100% on test projects

**Post-Release (30 days):**

- [ ] 90%+ successful installations
- [ ] < 5% rollback rate
- [ ] < 10 critical issues reported
- [ ] Average issue resolution: < 48 hours

### User Experience Metrics

**Qualitative:**

- [ ] "Easy to install" feedback
- [ ] "Intuitive to use" feedback
- [ ] "Quality improvements noticeable" feedback
- [ ] "Feel more productive" feedback

**Quantitative:**

- [ ] Time to first feature: < 5 minutes
- [ ] Features completed per session: 1-3
- [ ] Quality check failures: < 5%
- [ ] User satisfaction: 4.5/5+

---

## Timeline Summary

```
Week 1: Foundation
  ├── Agent prompts created
  └── Services refactored

Week 2: CLI Integration
  ├── forge CLI commands
  └── Slash commands updated

Week 3: Migration
  ├── Migration tool built
  └── Downgrade support added

Week 4: Testing
  ├── Unit tests (85%+ coverage)
  ├── Integration tests
  └── Real project validation

Week 5-6: Documentation & Release
  ├── All docs updated
  ├── Release package created
  └── Phased rollout

TOTAL: 4-6 weeks
```

---

## Next Steps (Immediate)

**After Vision Approval:**

1. **Create GitHub Project Board**
   - All tasks from this roadmap
   - Assigned to team members
   - Sprint planning

2. **Set Up Development Branch**

   ```bash
   git checkout -b feature/v2-canonical-architecture
   ```

3. **Create Phase 1 Tasks**
   - Issue for each agent prompt
   - Issue for each service refactoring
   - Assign and begin work

4. **Establish Testing Environment**
   - Select 2-3 test projects
   - Set up CI/CD for automated testing
   - Create benchmarking suite

5. **Weekly Progress Reviews**
   - Every Friday: review progress
   - Demo what's working
   - Adjust timeline as needed

---

## Team Roles (Suggested)

**Lead Architect (Asif)**

- Final approval on architectural decisions
- Agent prompt design review
- Migration strategy validation

**Backend Engineer**

- Python service refactoring
- CLI command implementation
- Testing infrastructure

**DevOps Engineer**

- Migration tool implementation
- CI/CD pipeline
- Release automation

**Technical Writer**

- Documentation updates
- Example project creation
- Tutorial videos

**QA Engineer**

- Test suite development
- Real project validation
- Bug triage and reporting

---

## Conclusion

**This roadmap transforms NXTG-Forge from parallel system to native Claude Code integration.**

**Key Deliverables:**

1. Five native Claude agents in `.claude/agents/`
2. Refactored Python services (state, git, quality)
3. Updated CLI with agent-friendly commands
4. Automated migration tool (v3 → v2.0)
5. Comprehensive testing and validation
6. Complete documentation update
7. PyPI release (v2.0.0)

**Expected Outcome:**

- Developer installs: `pip install nxtg-forge`
- Developer initializes: `forge init`
- Developer activates: `/enable-forge`
- Orchestrator guides through menu
- Complete automation via hooks
- Developer feels: **Powerful, not exhausted** ✅

---

**Document:** Implementation Roadmap
**Status:** Ready for Execution (pending approval)
**Date:** 2026-01-08
**Estimated Timeline:** 4-6 weeks
**Next Step:** Vision approval → Begin Phase 1
