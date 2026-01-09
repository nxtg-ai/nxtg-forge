# CANONICAL FORGE VISION

**NXTG-Forge as Native Claude Code Extension**

**Version:** 2.0 Canonical Architecture
**Date:** 2026-01-08
**Status:** Vision Document - Pending Approval

---

## Executive Summary

### The Problem: Architectural Misalignment

NXTG-Forge v3 currently exists **parallel** to Claude Code instead of being **native** to it:

- Forge agents live in `forge/agents/` (Python code) - OUTSIDE Claude's native `.claude/agents/` system
- This creates redundancy, friction, and missed opportunities for deep integration
- Setup requires manual steps, copying files, understanding the system
- No immediate visual feedback that forge capabilities are available

### The Vision: Complete Native Integration

NXTG-Forge 2.0 will be **invisible yet powerful** - a native extension of Claude Code:

```
Developer opens project with NXTG-Forge installed
    ↓
Sees: "✨ NXTG-FORGE-READY"
    ↓
Types: /enable-forge
    ↓
Orchestrator presents simple menu:
  1. [Continue/Resume] - Pick up where we left off
  2. [New Feature] - Plan and implement features
  3. [Soundboard] - Discuss current state, suggest next steps
    ↓
Complete automation through hooks:
  • Continuous quality checking/enforcement
  • Auto-documentation updates
  • Auto-versioning with semantic versioning
  • Git commits with human-readable messages
  • Proper branching and PR creation
  • Complete observability and audit trail
    ↓
Developer wakes up next morning
    ↓
Reads final report with GitHub links, PR summaries, test results
    ↓
Can audit work, validate PRs, rollback to checkpoints if needed
```

**Philosophy:** Powerful yet simple, elegant yet pragmatic, minimal yet complete.

---

## The Emotional Journey

### The Exhausted Developer Scenario

**Sunday Evening, 9:47 PM**

Sarah supports five microservices. Each one is a different tech stack. Each one has technical debt. Each one needs features shipped by Monday.

She opens the third service - a Node.js API she hasn't touched in weeks. Her heart sinks. What was she working on? Where did she leave off?

Then she sees it:

```
✨ NXTG-FORGE-READY

Last session: Feature "Payment Processing" - 60% complete
Type /enable-forge to continue
```

Her heart flutters. The pressure lifts.

She types `/enable-forge`.

```
╔═══════════════════════════════════════════════════════════╗
║                  NXTG-Forge Orchestrator                  ║
╚═══════════════════════════════════════════════════════════╝

Welcome back, Sarah. I see you were implementing payment processing.

What would you like to do?

  1. [Continue] Resume payment processing implementation (60% complete)
     → Next: Add Stripe webhook handlers and error recovery

  2. [New Feature] Plan and implement a new feature

  3. [Soundboard] Discuss current state and options
     → I've analyzed the codebase and have suggestions

  4. [Status] View complete project state

Choice [1-4]:
```

She chooses 1.

Claude picks up exactly where the previous session left off. The orchestrator coordinates between agents:

- Lead Architect ensures webhook design follows existing patterns
- Backend Master implements handlers with proper error handling
- QA Sentinel writes tests for webhook validation and replay scenarios
- Integration Specialist ensures Stripe SDK is properly integrated

While Sarah reviews PRs for another service, Claude:

- Creates feature branch `feature/payment-webhooks`
- Implements webhook handlers with exponential backoff
- Adds comprehensive tests (unit, integration, E2E)
- Updates API documentation
- Runs quality checks (linting, security scan, test coverage)
- Commits with clear messages: "feat: add Stripe webhook handlers with error recovery"
- Creates PR with detailed description and test results
- All automatically

**Monday Morning, 7:15 AM**

Sarah wakes up to a notification:

```
NXTG-Forge Session Complete

Feature: Payment Processing
Status: ✅ COMPLETE - Ready for Review

Summary:
  • Branch: feature/payment-webhooks
  • PR: #127 (https://github.com/company/api/pull/127)
  • Files Changed: 8 files (+450, -12)
  • Tests: 24 new tests, all passing
  • Coverage: 94% (+3% from baseline)
  • Quality: All checks passed ✓
  • Security: No vulnerabilities found ✓

Key Deliverables:
  1. Stripe webhook endpoint (/api/webhooks/stripe)
  2. Event validation and signature verification
  3. Exponential backoff retry logic
  4. Idempotency key handling
  5. Comprehensive error recovery
  6. Full test suite with mocked Stripe events

Next Steps:
  → Review PR #127
  → Merge when approved
  → Deploy to staging: make deploy-staging

Audit Trail:
  • 12 commits: https://github.com/company/api/commits/feature/payment-webhooks
  • 3 checkpoints created (rollback available)
  • Complete session log: .claude/sessions/20260107_214530.log

You can continue with: /enable-forge
```

Sarah reviews the PR over coffee. Everything is clean, tested, documented. She approves and merges.

She opens the next service. Same beautiful experience.

**She's not exhausted anymore. She's powerful.**

---

## Current Architecture Analysis

### What Exists Today (v3)

```
NXTG-Forge v3/
├── forge/                          ← Python package (NOT native to Claude)
│   ├── agents/                     ← PROBLEM: Agents are Python code
│   │   ├── orchestrator.py         ← 705 lines → 160 (refactored)
│   │   ├── dispatcher.py
│   │   ├── domain/                 ← Clean architecture (good!)
│   │   ├── selection/              ← Strategy pattern (good!)
│   │   ├── execution/              ← Separated executors (good!)
│   │   └── services/               ← Service layer (good!)
│   ├── cli.py                      ← 746 lines → 305 (refactored)
│   ├── commands/                   ← Command pattern (good!)
│   ├── services/                   ← Business logic (good!)
│   ├── config.py
│   ├── state_manager.py
│   ├── gap_analyzer.py
│   ├── mcp_detector.py
│   └── result.py                   ← Result types (excellent!)
│
├── .claude/                        ← Claude Code native directory
│   ├── agents/                     ← MISSING: Where forge agents should be!
│   ├── commands/                   ← ✓ GOOD: Forge commands here
│   │   ├── init.md
│   │   ├── feature.md
│   │   ├── status.md
│   │   ├── checkpoint.md
│   │   └── [10 more slash commands]
│   ├── hooks/                      ← ✓ GOOD: Automation hooks
│   │   ├── pre-task.sh
│   │   ├── post-task.sh
│   │   ├── on-error.sh
│   │   ├── on-file-change.sh
│   │   └── state-sync.sh
│   ├── prompts/                    ← ✓ GOOD: Agent prompts
│   ├── skills/                     ← ✓ GOOD: Domain knowledge
│   │   ├── agents/                 ← Agent skill definitions (markdown)
│   │   │   ├── lead-architect.md
│   │   │   ├── backend-master.md
│   │   │   ├── cli-artisan.md
│   │   │   ├── platform-builder.md
│   │   │   ├── integration-specialist.md
│   │   │   └── qa-sentinel.md
│   │   └── core/
│   └── forge/
│       └── AUTO-SETUP.md           ← Integration protocol
│
└── tests/                          ← Test suite
    ├── unit/
    └── integration/
```

### The Architectural Contradiction

**Current State:**

- Agent orchestration logic: `forge/agents/orchestrator.py` (Python)
- Agent skill definitions: `.claude/skills/agents/*.md` (Markdown)
- **SPLIT BRAIN:** Logic and definitions are separated

**What this means:**

- To add an agent, you modify Python code AND markdown
- Agent selection is hardcoded in Python strategy classes
- No native Claude Code agent discovery
- Orchestrator feels like external tool, not native capability

### What's Working Well

✅ **Commands** - Slash commands in `.claude/commands/` work perfectly
✅ **Hooks** - Automation hooks provide continuous quality enforcement
✅ **Skills** - Domain knowledge properly organized
✅ **Refactored Code** - Clean architecture, Result types, SOLID principles
✅ **Philosophy** - "Invisible until needed" principle is sound

---

## Canonical Architecture 2.0

### Core Principle

**NXTG-Forge is not a tool. It's how Claude Code works in your project.**

Every component should be **native to Claude Code's agent system**, not parallel to it.

### Directory Structure (Canonical)

```
NXTG-Forge Installation (pip package)
├── forge/                          ← Python infrastructure (CLI, services, utils)
│   ├── cli.py                      ← `forge` command (init, upgrade, etc.)
│   ├── services/                   ← Reusable services
│   │   ├── state_manager.py
│   │   ├── quality_service.py
│   │   ├── git_service.py
│   │   ├── mcp_detector.py
│   │   ├── context_restoration.py     ← NEW: Continue mode context (gap filled)
│   │   ├── activity_reporter.py       ← NEW: Background status (gap filled)
│   │   ├── session_reporter.py        ← NEW: Morning reports (gap filled)
│   │   ├── quality_alerter.py         ← NEW: Interactive warnings (gap filled)
│   │   └── recommendation_engine.py   ← NEW: Smart suggestions (gap filled)
│   ├── templates/                  ← Installation templates
│   │   └── .claude/                ← What gets installed in projects
│   │       ├── agents/
│   │       │   ├── agent-forge-orchestrator.md    ← THE ORCHESTRATOR
│   │       │   ├── agent-forge-architect.md
│   │       │   ├── agent-forge-backend.md
│   │       │   ├── agent-forge-qa.md
│   │       │   └── agent-forge-integration.md
│   │       ├── commands/
│   │       │   ├── enable-forge.md        ← Activation command
│   │       │   ├── feature.md
│   │       │   ├── status.md
│   │       │   └── [others]
│   │       ├── hooks/
│   │       │   ├── pre-task.sh
│   │       │   ├── post-task.sh
│   │       │   └── [others]
│   │       └── skills/
│   └── utils/
│       ├── result.py
│       ├── config.py
│       └── directory_manager.py
│
└── setup.py / pyproject.toml

User Project (after `forge init`)
├── .claude/                        ← Native Claude Code directory
│   ├── agents/                     ← ALL FORGE AGENTS HERE (native!)
│   │   ├── agent-forge-orchestrator.md    ← Coordinates other agents
│   │   ├── agent-forge-architect.md
│   │   ├── agent-forge-backend.md
│   │   ├── agent-forge-qa.md
│   │   └── agent-forge-integration.md
│   ├── commands/                   ← Slash commands
│   │   ├── enable-forge.md         ← Simple activation
│   │   ├── feature.md              ← Delegates to orchestrator
│   │   ├── status.md               ← Project status
│   │   └── [10+ more]
│   ├── hooks/                      ← Automation
│   ├── skills/                     ← Domain knowledge
│   ├── forge/                      ← Forge-specific data
│   │   ├── config.yml              ← Project config
│   │   ├── state.json              ← Current state
│   │   └── sessions/               ← Session persistence
│   └── FORGE-ENABLED               ← Marker file (presence = enabled)
│
└── [user's project files]
```

### Key Architectural Decisions

#### ADR-001: Orchestrator as Native Claude Agent

**Decision:** The orchestrator lives in `.claude/agents/agent-forge-orchestrator.md`

**Context:** Currently orchestrator is Python code in `forge/agents/orchestrator.py`. This creates disconnect with Claude Code's native agent system.

**Alternatives Considered:**

1. Keep orchestrator as Python, agents as markdown (current state)
2. Make orchestrator a Claude Code skill (not discoverable)
3. **Make orchestrator a native Claude agent** (CHOSEN)

**Rationale:**

- Claude Code's agent system is designed for this exact use case
- Agents can invoke other agents naturally
- Discovery is automatic (Claude sees `agent-forge-*` agents)
- Orchestrator prompt can be as sophisticated as needed (markdown)
- Python services still handle infrastructure (state, git, quality)

**Consequences:**

- Orchestrator logic moves from Python to sophisticated markdown prompt
- Python services become stateless utilities called by orchestrator
- Agent coordination happens via Claude's native agent system
- Can leverage Claude's multi-agent conversation capabilities

**Implementation:**

```markdown
# .claude/agents/agent-forge-orchestrator.md

You are the **NXTG-Forge Orchestrator** - the conductor of specialized agents.

## Your Role

Coordinate specialized agents to complete complex development tasks:
- agent-forge-architect: System design and architecture
- agent-forge-backend: Backend implementation
- agent-forge-qa: Testing and quality assurance
- agent-forge-integration: External service integration

## How You Work

1. **Analyze Request**: Understand what user wants to accomplish
2. **Decompose Task**: Break into subtasks with dependencies
3. **Select Agents**: Choose best agent(s) for each subtask
4. **Coordinate Execution**: Orchestrate agent handoffs
5. **Track Progress**: Update state.json via forge CLI
6. **Ensure Quality**: All work passes quality gates
7. **Report Results**: Clear summary of what was accomplished

## Tools Available

You have access to Python services via `forge` CLI:
- `forge state update` - Update project state
- `forge quality check` - Run quality checks
- `forge git commit` - Create commits
- `forge checkpoint create` - Save checkpoints

## Example: Multi-Agent Feature Implementation

User: "Add OAuth authentication"

You:
1. Invoke agent-forge-architect for system design
2. Review architecture, get approval
3. Invoke agent-forge-backend for implementation
4. Invoke agent-forge-qa for comprehensive tests
5. Update documentation
6. Create PR with full context

All while maintaining state, creating checkpoints, ensuring quality.

[Rest of detailed orchestrator prompt...]
```

#### ADR-002: Agent Namespace Convention

**Decision:** All forge agents use `agent-forge-*` naming convention

**Rationale:**

- Clear namespace separation from user's custom agents
- Easy discovery (`ls .claude/agents/agent-forge-*`)
- Prevents naming conflicts
- Immediately recognizable as forge capabilities

**Examples:**

- `agent-forge-orchestrator.md` - The coordinator
- `agent-forge-architect.md` - Architecture and design
- `agent-forge-backend.md` - Backend implementation
- `agent-forge-qa.md` - Quality assurance and testing
- `agent-forge-integration.md` - External integrations

#### ADR-003: Forge Activation Model

**Decision:** Forge is activated via `/enable-forge` command, not automatically

**Context:** AUTO-SETUP.md suggests "invisible until needed" - only activate when complex tasks detected.

**Alternatives:**

1. Auto-activate on complex tasks (silent)
2. Always active (always visible)
3. **Explicit activation via command** (CHOSEN)

**Rationale:**

- Gives user control over when forge orchestration is used
- Clear mental model: "I'm using forge now"
- Status indication makes capabilities discoverable
- Can still auto-detect and suggest: "This looks complex. Try /enable-forge"
- Simpler than complex heuristics for auto-activation

**Status Indication:**

```
# On project open (if forge installed and initialized)
✨ NXTG-FORGE-READY
  Last session: Feature "Payment Processing" - 60% complete

  Commands:
    /enable-forge  - Start orchestrator
    /status        - View project state
    /feature       - Quick feature creation

# After /enable-forge
✅ NXTG-FORGE-ACTIVE
  Orchestrator: Ready
  Agents: 5 available
  Session: 20260108_094530
```

#### ADR-004: State Management Philosophy

**Decision:** State is the source of truth, managed via Python services

**Rationale:**

- Markdown agents can't directly manipulate JSON reliably
- Python services provide type-safe, validated state operations
- CLI commands bridge agents to state management
- Result types ensure no silent failures

**Architecture:**

```
Agent (Markdown)
    ↓ (invokes)
forge CLI command
    ↓ (uses)
Python Service (forge/services/state_manager.py)
    ↓ (reads/writes)
.claude/forge/state.json
```

**Example Flow:**

1. Orchestrator (markdown) decides feature is complete
2. Invokes: `forge state update-feature --id feat-123 --status completed`
3. CLI parses args, calls `StateManager.update_feature()`
4. Service validates, updates state.json, returns Result
5. CLI reports success/failure back to orchestrator

#### ADR-005: Hooks as Automation Backbone

**Decision:** Hooks provide continuous quality enforcement and automation

**What Hooks Do:**

- **pre-task.sh**: Initialize session, check preconditions
- **post-task.sh**: Quality checks, update metrics, suggest next steps
- **on-error.sh**: Log errors, suggest recovery, create checkpoint
- **on-file-change.sh**: Auto-format, validate syntax, run quick tests
- **state-sync.sh**: Backup state, update metrics, create checkpoints

**Philosophy:**

- Hooks run automatically (Claude Code lifecycle)
- Never block the developer (non-interactive)
- Provide guardrails, not gates
- Complete observability of all operations

**Example - Automatic Quality Enforcement:**

```bash
# post-task.sh (simplified)
#!/bin/bash

# Run linter
ruff check . --quiet

# Run tests
pytest --quiet --no-header

# Update coverage
coverage report --precision=2 > .claude/coverage.txt

# Update state.json
forge state update-quality \
  --linting "$(ruff check . --quiet | wc -l) issues" \
  --coverage "$(coverage report | tail -1 | awk '{print $4}')"

# Suggest checkpoint if major work
if [[ $FILES_MODIFIED -gt 5 ]]; then
  echo "💡 Tip: Create checkpoint - forge checkpoint create"
fi
```

---

## Service Layer Architecture

### Overview

The service layer provides type-safe, testable business logic for agents to invoke. All services return Result types (no exceptions for control flow) and are accessed via `forge` CLI commands.

**Design Principle:** Services handle computation, agents handle coordination.

### Core Services

#### 1. StateManager - `forge/services/state_manager.py`

**Purpose:** Session and feature state persistence

**Data Storage:** `.claude/forge/state.json`

**Key Methods:**

```python
def get_current_state() -> ProjectState
def update_feature_progress(feature_id: str, progress: int) -> Result[None, StateError]
def save_session(session_data: dict) -> Result[SessionId, StateError]
def get_last_session() -> Optional[Session]
```

#### 2. GitService - `forge/services/git_service.py`

**Purpose:** Git operations and commit message generation

**Key Methods:**

```python
def create_branch(name: str) -> Result[BranchName, GitError]
def generate_commit_message(diff: str) -> Result[CommitMessage, GitError]
def create_commit(message: str) -> Result[CommitHash, GitError]
def create_pr(title: str, body: str) -> Result[PrUrl, GitError]
def get_commits_in_session(session: Session) -> list[Commit]
```

#### 3. QualityService - `forge/services/quality_service.py`

**Purpose:** Quality metrics calculation and gate enforcement

**Key Methods:**

```python
def run_all_checks() -> QualityReport
def calculate_health_score() -> HealthScore
def check_coverage_threshold(min_coverage: int) -> Result[None, CoverageError]
def get_current_metrics() -> QualityMetrics
```

### New Services (Gap Resolution)

#### 4. ContextRestorationService - `forge/services/context_restoration.py` (NEW)

**Purpose:** Restore full context for Continue mode
**Why Added:** Designer specified "Continue" with smart recommendations. This service provides the mechanism.

**Key Methods:**

```python
def restore_context(self) -> ContinueContext:
    """Load last session context with smart recommendations."""
    # 1. Read state.json for last active feature/tasks
    # 2. Check current git branch and analyze diff from last commit
    # 3. Scan recently modified files (< 2 hours old)
    # 4. Calculate % complete based on task completion ratio
    # 5. Generate recommendations via RecommendationEngine
    # 6. Detect code smells (hardcoded secrets, weak crypto, etc.)
    return ContinueContext(
        last_session_time=...,
        branch=...,
        progress_percent=...,
        outstanding_tasks=[...],
        recommendations=[...]
    )
```

**CLI Invocation:**

```bash
# From orchestrator agent:
forge context restore --format=json
# Returns JSON with full context for presentation
```

#### 5. ActivityReporter - `forge/services/activity_reporter.py` (NEW)

**Purpose:** Report background activity to active Claude session
**Why Added:** Designer specified real-time activity indicators. This service provides the reporting mechanism.

**Implementation:**

```python
class ActivityReporter:
    """Reports background hook activity to CLI."""

    def __init__(self):
        self.status_file = Path(".claude/forge/activity.status")

    def report_start(self, activity: str):
        """Signal activity started."""
        self.status_file.write_text(json.dumps({
            "status": "started",
            "activity": activity,
            "timestamp": time.time()
        }))

    def report_complete(self, activity: str, duration: float, success: bool):
        """Signal activity completed."""
        self.status_file.write_text(json.dumps({
            "status": "complete",
            "activity": activity,
            "duration": duration,
            "success": success,
            "timestamp": time.time()
        }))

    def get_current_status(self) -> Optional[dict]:
        """Read current activity status."""
        if self.status_file.exists():
            return json.loads(self.status_file.read_text())
        return None
```

**Usage in Hooks:**

```bash
# In post-task.sh
forge activity start "Running tests..."
pytest --quiet
forge activity complete "Tests passed" --duration=$SECONDS --success=true
```

**Display:** Orchestrator polls status file and displays updates to user (Phase 1: after completion, Phase 2: real-time with ANSI)

#### 6. SessionReporter - `forge/services/session_reporter.py` (NEW)

**Purpose:** Generate comprehensive session reports (morning-after confidence)
**Why Added:** Designer specified detailed overnight report. This service generates it.

**Key Methods:**

```python
def generate_session_report(self, session_id: str) -> SessionReport:
    """Generate comprehensive report from session log."""
    session = self.state_manager.get_session(session_id)

    # Aggregate data from multiple sources
    git_data = self.git_service.get_commits_in_session(session)
    pr_data = self.gh_service.get_pr_status(session.get('pr_number'))
    quality_before = session['quality_snapshot_before']
    quality_after = self.quality_service.calculate_health_score()

    return SessionReport(
        session_summary=...,  # Duration, commits, files, tests
        git_activity=...,     # Commits with GitHub links
        pr_details=...,       # PR status, CI checks
        quality_delta=...,    # Before/after metrics
        checkpoints=...,      # Available rollback points
        next_steps=...        # AI-generated recommendations
    )

def should_display_report_on_startup(self) -> bool:
    """Check if there's a recent completed session."""
    last_session = self.state_manager.get_last_session()
    if last_session and last_session.status == "complete":
        # Was it recent? (< 24 hours)
        return (datetime.utcnow() - last_session.end_time).hours < 24
    return False
```

**CLI Invocation:**

```bash
# Generate report
forge report generate --session=session_20260107_223000

# Display report (formatted for terminal)
forge report display --session=session_20260107_223000
```

#### 7. QualityAlerter - `forge/services/quality_alerter.py` (NEW)

**Purpose:** Surface quality issues interactively with remediation options
**Why Added:** Designer specified interactive quality alerts. This service provides the alerting mechanism.

**Key Methods:**

```python
def check_and_alert(self) -> Optional[QualityAlert]:
    """Check quality and return alert if issues found."""
    result = self.quality_service.run_all_checks()

    if result.coverage_dropped():
        return QualityAlert(
            severity="warning",
            title="Test coverage dropped",
            message=f"Coverage: {result.prev_coverage}% → {result.current_coverage}%",
            affected_files=result.uncovered_files,
            remediation_options=[
                "Generate test stubs now",
                "Show coverage gaps in detail",
                "Remind me later"
            ]
        )

    if result.security_issues():
        return QualityAlert(
            severity="error",
            title="Security vulnerability detected",
            message=result.security_summary,
            remediation_options=[
                "Show vulnerability details",
                "Apply recommended fix",
                "Add to ignore list (not recommended)"
            ]
        )

    return None  # All good!
```

**CLI Invocation:**

```bash
# Check for alerts
forge quality check-alerts --format=json
# Returns alert JSON if issues found, null otherwise
```

**Usage:** Orchestrator checks after each operation and presents alerts interactively if issues found.

#### 8. RecommendationEngine - `forge/services/recommendation_engine.py` (NEW)

**Purpose:** Generate smart suggestions for Continue mode
**Why Added:** Designer specified "💡 Smart Recommendations" with examples like "JWT secret is hardcoded". This service generates those.

**Key Methods:**

```python
def analyze_and_recommend(self, context: ContinueContext) -> list[Recommendation]:
    """Analyze code and generate contextual recommendations."""
    recommendations = []

    # Static analysis patterns
    for file_path in context.recent_files:
        content = Path(file_path).read_text()

        # Security patterns
        if "SECRET_KEY =" in content or "API_KEY =" in content:
            recommendations.append(Recommendation(
                priority=10,  # Critical
                category="security",
                message="JWT secret is hardcoded in config.py",
                suggestion="Move it to environment variables",
                action="forge refactor move-to-env JWT_SECRET"
            ))

        if "hashlib.sha256" in content and "password" in content.lower():
            recommendations.append(Recommendation(
                priority=9,
                category="security",
                message="Password hashing uses SHA256",
                suggestion="Upgrade to bcrypt or argon2 for security",
                action="forge refactor upgrade-password-hash"
            ))

        # Quality patterns
        if context.quality_metrics.coverage < 85:
            recommendations.append(Recommendation(
                priority=7,
                category="quality",
                message=f"Tests at {context.quality_metrics.coverage}% coverage",
                suggestion="Should be 85% minimum",
                action="forge test generate-stubs"
            ))

    # AI-powered analysis (via orchestrator)
    ai_recommendations = self._ai_code_review(context.recent_files)
    recommendations.extend(ai_recommendations)

    # Prioritize and return top 3
    return sorted(recommendations, key=lambda r: r.priority, reverse=True)[:3]
```

**CLI Invocation:**

```bash
# Generate recommendations
forge recommend --context-file=context.json --format=json
```

### Service Invocation Pattern

**From Agent (Markdown) to Service (Python):**

```markdown
# In agent-forge-orchestrator.md

User chose "Continue" mode. Let me restore context:

[Invoke service via backticks - Claude executes as bash]
`context_json=$(forge context restore --format=json)`

Based on this context: {context_json}

📍 Context Restored
   Last session: 2 hours ago
   Branch: feature/auth-system
   Progress: 67% complete

💡 Smart Recommendations
   • JWT secret is hardcoded in config.py
   • Password hashing uses SHA256
   • Tests at 67% coverage
```

**Key Points:**

- Agents invoke services via CLI commands (simple, testable interface)
- Services return JSON for structured data
- Agents format and present results to user
- Clear separation: agents coordinate, services compute

---

## Agent System Design

### The Minimal Agent Set

Five specialized agents, coordinated by orchestrator:

1. **agent-forge-orchestrator.md** - The Conductor
   - Role: Coordinate other agents, manage workflow
   - Invokes: All other forge agents
   - Manages: Task decomposition, agent selection, progress tracking

2. **agent-forge-architect.md** - System Design
   - Role: Architecture decisions, data modeling, API design
   - Expertise: Clean architecture, DDD, system design patterns
   - Deliverables: Architecture specs, data models, API contracts

3. **agent-forge-backend.md** - Implementation
   - Role: Backend code implementation
   - Expertise: Python, Node.js, Go, databases, APIs
   - Deliverables: Domain models, use cases, API endpoints, migrations

4. **agent-forge-qa.md** - Quality Assurance
   - Role: Testing, quality checks, security
   - Expertise: Unit/integration/E2E tests, security scanning
   - Deliverables: Comprehensive test suites, quality reports

5. **agent-forge-integration.md** - External Services
   - Role: Third-party integrations, SDKs, APIs
   - Expertise: OAuth, payment processors, cloud services
   - Deliverables: Integration code, SDK wrappers, error handling

### Agent Communication Model

**Native Claude Agent Invocation:**

```markdown
# In agent-forge-orchestrator.md

I need architecture design for this feature.
Invoking: agent-forge-architect

[Claude switches to architect agent context]

# In agent-forge-architect.md response
Based on the feature requirements, here's the architecture:

Domain Model:
  - User entity with OAuth credentials
  - Session entity with expiration
  ...

[Orchestrator receives response, continues workflow]
```

**State Persistence Between Invocations:**

```bash
# Orchestrator updates state
forge state create-task \
  --id "task-auth-001" \
  --description "Design OAuth architecture" \
  --assigned-agent "agent-forge-architect" \
  --status "in-progress"

# Later, any agent can query state
forge state get-task --id "task-auth-001"
```

### Agent Collaboration Patterns

#### Pattern 1: Sequential Handoff

```
User: "Add OAuth authentication"
  ↓
Orchestrator: Decomposes into tasks
  ↓
[1] agent-forge-architect: Design system
  ↓
Orchestrator: Reviews design, approves
  ↓
[2] agent-forge-backend: Implement code
  ↓
Orchestrator: Code review, quality check
  ↓
[3] agent-forge-qa: Write tests
  ↓
Orchestrator: All tests pass, feature complete
```

#### Pattern 2: Parallel Execution

```
User: "Refactor auth module for better error handling"
  ↓
Orchestrator: Identifies independent subtasks
  ↓
[Parallel]
├─ agent-forge-backend: Refactor error handling
├─ agent-forge-qa: Update existing tests
└─ agent-forge-integration: Update SDK wrappers
  ↓
Orchestrator: Merge results, ensure compatibility
```

#### Pattern 3: Iterative Refinement

```
User: "Optimize database queries"
  ↓
Orchestrator: Initial analysis
  ↓
[Iteration 1]
agent-forge-backend: Add indexes
agent-forge-qa: Run benchmarks
  ↓
Orchestrator: Review metrics, identify more optimizations
  ↓
[Iteration 2]
agent-forge-backend: Add query caching
agent-forge-qa: Run benchmarks
  ↓
Orchestrator: Performance target achieved
```

---

## Developer Experience (DX) Flow

### First Time Setup

```bash
# 1. Install NXTG-Forge
pip install nxtg-forge

# 2. Navigate to project
cd ~/my-project

# 3. Initialize
forge init

# Output:
✨ Initializing NXTG-Forge in /home/user/my-project

Analyzing project...
  ✓ Detected: Python 3.11, FastAPI
  ✓ Git repository found
  ✓ Tests found: pytest

Installing forge components...
  ✓ Created .claude/agents/ (5 agents)
  ✓ Created .claude/commands/ (12 commands)
  ✓ Created .claude/hooks/ (5 hooks, executable)
  ✓ Created .claude/forge/config.yml
  ✓ Created .claude/forge/state.json

Configuration:
  Project: my-project
  Type: Python API
  Framework: FastAPI
  Database: PostgreSQL

✅ NXTG-Forge initialized successfully!

Next steps:
  1. Review config: .claude/forge/config.yml
  2. Start Claude: claude
  3. Activate forge: /enable-forge

Documentation: https://nxtg-forge.dev/getting-started
```

### Daily Usage

#### Opening Project

```bash
cd ~/my-project
claude

# Claude shows:
✨ NXTG-FORGE-READY

Project: my-project (Python API)
Health: 87/100 ✓

Recent activity:
  • Last session: 2026-01-07 21:45 (completed)
  • Last feature: "OAuth Integration" (✅ merged)
  • Tests: 142 passing, 94% coverage

Quick commands:
  /enable-forge  - Start orchestrator
  /status        - Detailed project state
  /feature       - Create new feature

What would you like to work on?
```

#### Activating Forge

```
User: /enable-forge

Claude (as orchestrator):

╔═══════════════════════════════════════════════════════════╗
║              NXTG-Forge Orchestrator v2.0                 ║
╚═══════════════════════════════════════════════════════════╝

Hello! I'm your development orchestrator. I coordinate specialized
agents to handle complex tasks end-to-end.

Available agents:
  • Architect - System design and architecture
  • Backend - Implementation and code
  • QA - Testing and quality assurance
  • Integration - External services and APIs

What would you like to do?

  1. [Continue] Resume previous work
     → No incomplete sessions found

  2. [New Feature] Plan and implement a new feature
     → I'll gather requirements and coordinate implementation

  3. [Refactor] Improve existing code
     → Architecture, performance, or code quality improvements

  4. [Soundboard] Discuss current state
     → I've analyzed your project and have suggestions

  5. [Status] View detailed project status

Choice [1-5]: _
```

#### Creating New Feature

```
User: 2

Orchestrator: Great! Let's plan a new feature.

What feature would you like to add?
(Describe in 1-2 sentences, I'll ask clarifying questions)

User: Add payment processing with Stripe

Orchestrator: Perfect. Let me gather some details:

1. Payment methods needed:
   [ ] Credit/debit cards
   [ ] ACH/bank transfers
   [ ] Digital wallets (Apple Pay, Google Pay)

2. What should trigger payments?
   [ ] User-initiated (one-time)
   [ ] Subscription billing (recurring)
   [ ] Both

3. Do you need:
   [ ] Payment history/receipts
   [ ] Refund handling
   [ ] Webhook processing for payment events
   [ ] PCI compliance considerations

[Interactive Q&A continues...]

Orchestrator: Excellent. Here's what I'll build:

Feature: Stripe Payment Processing
═════════════════════════════════════

Scope:
  • Credit card payments (one-time and recurring)
  • Stripe webhook handlers
  • Payment history and receipts
  • Refund management
  • PCI-compliant implementation

Architecture (agent-forge-architect):
  1. Payment domain models (Payment, Subscription, Refund)
  2. PaymentService for Stripe integration
  3. Webhook endpoint with signature verification
  4. Database schema for payment records
  5. API endpoints: /payments, /subscriptions, /refunds

Implementation (agent-forge-backend):
  1. Stripe SDK integration
  2. Payment intent creation with idempotency
  3. Webhook event handling
  4. Error handling and retry logic
  5. Database migrations

Testing (agent-forge-qa):
  1. Unit tests with mocked Stripe API
  2. Integration tests with Stripe test mode
  3. Webhook event replay tests
  4. Security tests (signature validation)

Documentation:
  1. API documentation
  2. Stripe setup guide
  3. Webhook configuration guide

Estimated: 2-3 hours for complete implementation

Ready to proceed? [Y/n]: _
```

#### While Working

```
User: y

Orchestrator: Starting feature implementation...

[Checkpoint created: before-stripe-integration]

Phase 1: Architecture Design
═══════════════════════════════

Invoking agent-forge-architect...

[Agent switch - architect designs system]

✓ Domain models defined
✓ API contracts specified
✓ Database schema designed
✓ Integration patterns documented

[Shows architecture summary]

Phase 2: Backend Implementation
════════════════════════════════

Invoking agent-forge-backend...

[Agent switch - backend implements]

Progress:
  ✓ Stripe SDK installed and configured
  ✓ Payment domain models implemented
  ✓ PaymentService created with error handling
  ✓ Webhook endpoint with signature validation
  ⏳ Database migrations in progress...

[Hook: on-file-change.sh runs automatically]
  ✓ Auto-formatted 4 Python files
  ✓ No linting issues

[Continues implementation...]

✓ All implementation complete
✓ Database migrations applied
✓ API endpoints created

Phase 3: Testing
════════════════

Invoking agent-forge-qa...

[Agent switch - QA creates tests]

Test Suite:
  ✓ Unit tests: 18 tests, all passing
  ✓ Integration tests: 8 tests, all passing
  ✓ Webhook tests: 6 tests, all passing

Coverage:
  • payment/models.py: 96%
  • payment/service.py: 94%
  • payment/api.py: 91%
  • Overall: 94% (+3% from baseline)

[Hook: post-task.sh runs]
  ✓ Linting: 0 issues
  ✓ Security scan: No vulnerabilities
  ✓ Type checking: Passed

Phase 4: Documentation & PR
════════════════════════════

Creating documentation...
  ✓ API endpoints documented (OpenAPI spec)
  ✓ Setup guide created (docs/stripe-setup.md)
  ✓ Updated CHANGELOG.md

Creating Git workflow...
  ✓ Branch: feature/stripe-payment-processing
  ✓ Commits: 8 commits with clear messages
  ✓ PR created: #145

═══════════════════════════════════════════════════════════

✅ Feature Complete: Stripe Payment Processing

Summary:
  • Branch: feature/stripe-payment-processing
  • PR: #145 (https://github.com/user/project/pull/145)
  • Files: 12 files changed (+680, -15)
  • Tests: 32 new tests, all passing (94% coverage)
  • Quality: All checks passed ✓
  • Security: No vulnerabilities ✓

What was built:
  1. Payment domain models (Payment, Subscription, Refund)
  2. Stripe integration service with error handling
  3. Webhook endpoint with signature verification
  4. API endpoints (/payments, /subscriptions, /refunds)
  5. Database migrations
  6. Comprehensive test suite
  7. Complete documentation

Next steps:
  → Review PR #145
  → Test in staging: make deploy-staging
  → Merge when approved
  → Deploy to production: make deploy

Session saved: .claude/forge/sessions/20260108_143022.log
Checkpoint created: stripe-integration-complete

Continue with another task? Type /enable-forge
Or ask me anything about what was implemented.
```

#### Reviewing Work Later

```
User: /status

╔════════════════════════════════════════════════════════╗
║           NXTG-Forge Project Status                    ║
╚════════════════════════════════════════════════════════╝

📦 PROJECT: my-project
   Type: Python API (FastAPI)
   Created: 2025-12-15
   Forge Version: 2.0.0

🚀 FEATURES
   ✅ Completed: 8
      • User Authentication (OAuth)
      • Payment Processing (Stripe)
      • Email Notifications
      • Admin Dashboard
      • [4 more...]

   🔄 In Progress: 0
   📋 Planned: 2

✅ QUALITY METRICS
   Tests: 142 passing (94% coverage)
   Linting: 0 issues
   Security: 0 critical, 0 high vulnerabilities

📊 PROJECT HEALTH: 87/100 ✓

💾 RECENT SESSIONS
   2026-01-08 14:30 - Stripe Integration (✅ complete)
   2026-01-07 21:45 - OAuth Refactoring (✅ complete)
   2026-01-06 18:20 - Email Templates (✅ complete)

💡 Quick Actions:
   New feature:     /enable-forge
   View PR #145:    gh pr view 145
   Deploy staging:  make deploy-staging
```

---

## Git Workflow Integration

### Automated Git Operations

The orchestrator manages complete git workflow:

1. **Branch Creation**

   ```bash
   forge git create-branch --feature "stripe-integration"
   # Creates: feature/stripe-integration
   ```

2. **Commits with Context**

   ```bash
   forge git commit \
     --message "feat: add Stripe payment service with error handling" \
     --files "payment/service.py payment/models.py" \
     --conventional-commit

   # Follows conventional commits:
   # feat: new feature
   # fix: bug fix
   # refactor: code refactoring
   # test: adding tests
   # docs: documentation
   ```

3. **PR Creation**

   ```bash
   forge git create-pr \
     --title "Add Stripe Payment Processing" \
     --body-from-session "20260108_143022"

   # PR body includes:
   # - Feature summary
   # - Implementation details
   # - Test results
   # - Quality metrics
   # - Review checklist
   ```

### Commit Message Quality

**Bad (manual):**

```
git commit -m "updates"
git commit -m "fix stuff"
git commit -m "WIP"
```

**Good (forge-generated):**

```
feat: add Stripe payment intent creation with idempotency

Implements payment intent creation using Stripe SDK with:
- Idempotency key handling to prevent duplicate charges
- Exponential backoff retry logic for network failures
- Comprehensive error handling for Stripe API errors
- Logging for audit trail

Tests: 8 new unit tests, all passing
Coverage: payment/service.py 96%

Refs: #145
```

### PR Templates

**Generated PR Description:**

```markdown
## Summary

Implements Stripe payment processing with support for one-time and recurring payments.

## Changes

### Domain Layer
- `Payment` model with status tracking
- `Subscription` model for recurring payments
- `Refund` model for payment reversals

### Application Layer
- `PaymentService` with Stripe SDK integration
- Webhook handler with signature verification
- Error handling with exponential backoff

### Infrastructure
- Database migrations for payment tables
- Stripe webhook endpoint (/api/webhooks/stripe)
- Environment variable configuration

### Tests
- 18 unit tests (mocked Stripe API)
- 8 integration tests (Stripe test mode)
- 6 webhook replay tests
- 94% code coverage

## Quality Checks

- ✅ All tests passing (32 tests)
- ✅ Linting clean (0 issues)
- ✅ Security scan passed (0 vulnerabilities)
- ✅ Type checking passed
- ✅ Coverage above threshold (94% > 80%)

## Review Checklist

- [ ] Code review
- [ ] Test coverage adequate
- [ ] Documentation complete
- [ ] Security considerations addressed
- [ ] Breaking changes documented (none)
- [ ] Deployment notes reviewed

## Deployment Notes

**Required:**
1. Add Stripe API keys to environment:
   ```

   STRIPE_SECRET_KEY=sk_live_...
   STRIPE_WEBHOOK_SECRET=whsec_...

   ```
2. Run migrations: `make db-migrate`
3. Configure Stripe webhook URL: `https://api.yourapp.com/api/webhooks/stripe`

**Rollback:**
- Checkpoint available: `stripe-integration-complete`
- Restore with: `forge checkpoint restore stripe-integration-complete`

## Testing in Staging

```bash
make deploy-staging
make test-integration STRIPE_MODE=test
```

---

**Generated by NXTG-Forge Orchestrator**
Session: 20260108_143022
Agents: architect, backend, qa
Duration: 2.3 hours

```

---

## Hook-Driven Automation

### The Automation Backbone

Hooks provide continuous quality enforcement without developer intervention:

```

Developer works with Claude
         ↓
   File changes occur
         ↓
  [on-file-change.sh]
    • Auto-format code
    • Validate syntax
    • Run quick checks
         ↓
   Task completes
         ↓
   [post-task.sh]
    • Run full test suite
    • Check code coverage
    • Lint all code
    • Security scan
    • Update state.json
    • Update metrics
         ↓
   Quality issues found?
         ↓ No
   [Git workflow]
    • Create commit
    • Update PR
         ↓
   [state-sync.sh]
    • Backup state
    • Create checkpoint
    • Calculate health score

```

### Hook Responsibilities

#### pre-task.sh
```bash
#!/bin/bash
# Before any Claude task

# 1. Initialize session
SESSION_ID=$(date +%Y%m%d_%H%M%S)
forge state create-session --id "$SESSION_ID"

# 2. Check git status
if git status --porcelain | grep -q '^[MADRC]'; then
  echo "⚠️  Uncommitted changes detected"
  echo "💡 Tip: Commit or stash before starting"
fi

# 3. Validate project structure
if [[ ! -f .claude/forge/config.yml ]]; then
  echo "❌ Forge not initialized. Run: forge init"
  exit 1
fi

# 4. Update session info
forge state update-session \
  --task "$TASK_DESCRIPTION" \
  --agent "$AGENT_TYPE"

echo "✅ Pre-task checks complete"
```

#### post-task.sh

```bash
#!/bin/bash
# After Claude task completes

# 1. Run tests
echo "Running tests..."
pytest --quiet --no-header
TEST_EXIT=$?

# 2. Check coverage
coverage run -m pytest --quiet
coverage report --precision=2 > .claude/coverage.txt
COVERAGE=$(coverage report | tail -1 | awk '{print $4}')

# 3. Lint code
echo "Linting..."
ruff check . --quiet
LINT_ISSUES=$(ruff check . --quiet | wc -l)

# 4. Security scan
echo "Security scan..."
bandit -r . -q -f json > .claude/security-scan.json
CRITICAL_VULNS=$(jq '[.results[] | select(.issue_severity=="HIGH")] | length' .claude/security-scan.json)

# 5. Update state
forge state update-quality \
  --tests "$TEST_EXIT" \
  --coverage "$COVERAGE" \
  --linting "$LINT_ISSUES" \
  --security-critical "$CRITICAL_VULNS"

# 6. Suggest next steps
if [[ $TEST_EXIT -eq 0 && $LINT_ISSUES -eq 0 ]]; then
  echo "✅ All quality checks passed!"
  echo "💡 Next steps:"
  echo "   • Review changes: git diff"
  echo "   • Commit: forge git commit"
  echo "   • Create PR: forge git create-pr"
else
  echo "⚠️  Quality issues found:"
  [[ $TEST_EXIT -ne 0 ]] && echo "   • Tests failing"
  [[ $LINT_ISSUES -gt 0 ]] && echo "   • $LINT_ISSUES linting issues"
fi

# 7. Recommend checkpoint for major work
if [[ $FILES_MODIFIED -gt 5 ]]; then
  echo "💡 Major changes detected. Create checkpoint?"
  echo "   forge checkpoint create"
fi
```

#### on-error.sh

```bash
#!/bin/bash
# When error occurs during task

# 1. Log error
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
cat >> .claude/errors.log <<EOF
[$TIMESTAMP] Error in task: $TASK_ID
Code: $ERROR_CODE
Message: $ERROR_MESSAGE
File: $ERROR_FILE:$ERROR_LINE
EOF

# 2. Update state
forge state mark-task-failed \
  --task-id "$TASK_ID" \
  --error "$ERROR_MESSAGE"

# 3. Analyze error type
if echo "$ERROR_MESSAGE" | grep -q "ModuleNotFoundError"; then
  echo "❌ Python import error detected"
  echo "💡 Try: pip install -r requirements.txt"
elif echo "$ERROR_MESSAGE" | grep -q "Permission denied"; then
  echo "❌ Permission error detected"
  echo "💡 Try: chmod +x $ERROR_FILE"
elif echo "$ERROR_MESSAGE" | grep -q "SyntaxError"; then
  echo "❌ Syntax error detected"
  echo "💡 Try: ruff format $ERROR_FILE"
fi

# 4. Recommend checkpoint creation
echo "💡 Create error checkpoint for recovery:"
echo "   forge checkpoint create \"before-error-$TASK_ID\""

# 5. Suggest recovery
echo ""
echo "Recovery options:"
echo "  1. Fix the error and retry"
echo "  2. Restore last checkpoint: forge checkpoint restore"
echo "  3. View error history: cat .claude/errors.log"
```

### Observability Through Hooks

Every operation is logged for complete audit trail:

```
.claude/
├── forge/
│   ├── sessions/                    ← Complete session logs
│   │   ├── 20260108_143022.log     ← Full conversation & operations
│   │   ├── 20260107_214530.log
│   │   └── 20260106_182015.log
│   ├── checkpoints/                 ← Milestone snapshots
│   │   ├── before-stripe-integration/
│   │   ├── stripe-integration-complete/
│   │   └── oauth-refactoring-done/
│   └── errors.log                   ← All errors with context
└── coverage.txt                      ← Latest coverage report
```

**Developer can audit everything:**

```bash
# What did Claude do in last session?
cat .claude/forge/sessions/20260108_143022.log

# What errors occurred recently?
tail -20 .claude/errors.log

# What changed in last checkpoint?
diff -r .claude/checkpoints/before-stripe-integration .

# What's current test coverage?
cat .claude/coverage.txt
```

---

## Migration Path: v3 → 2.0 Canonical

### Phase 1: Install New Structure (Non-Breaking)

1. **Update forge package:**

   ```bash
   pip install --upgrade nxtg-forge  # v2.0
   ```

2. **Run migration command:**

   ```bash
   cd ~/my-project
   forge upgrade v2

   # Output:
   Upgrading NXTG-Forge to v2.0 (Canonical Architecture)

   This will:
     • Move agent logic to .claude/agents/
     • Update commands for new orchestrator
     • Preserve all state and checkpoints
     • Maintain backward compatibility

   Current: v1.0 (Python orchestrator)
   Target:  v2.0 (Native Claude agents)

   Proceed? [Y/n]: y

   Migrating...
     ✓ Backed up current .claude/ to .claude.v1.backup/
     ✓ Created .claude/agents/agent-forge-orchestrator.md
     ✓ Created .claude/agents/agent-forge-architect.md
     ✓ Created .claude/agents/agent-forge-backend.md
     ✓ Created .claude/agents/agent-forge-qa.md
     ✓ Created .claude/agents/agent-forge-integration.md
     ✓ Updated .claude/commands/enable-forge.md
     ✓ Updated .claude/commands/feature.md
     ✓ Migrated state.json (no schema changes)
     ✓ Preserved all checkpoints

   ✅ Migration complete!

   What changed:
     • Orchestrator is now native Claude agent
     • Activation via /enable-forge (simple menu)
     • All Python code moved to services (cleaner)
     • Same functionality, better architecture

   Next steps:
     1. Start Claude: claude
     2. Try new orchestrator: /enable-forge
     3. Review changes: diff .claude/ .claude.v1.backup/

   Rollback (if needed):
     forge downgrade v1
   ```

### Phase 2: Validate Migration

**Test checklist:**

- [ ] `/enable-forge` shows orchestrator menu
- [ ] Orchestrator can invoke agents
- [ ] `/status` shows correct project state
- [ ] `/feature` workflow works end-to-end
- [ ] Hooks still function (pre-task, post-task, etc.)
- [ ] Checkpoints can be created/restored
- [ ] Git workflow functions correctly

### Phase 3: Deprecate Old Structure

**In v2.1 (next minor):**

- Mark `forge/agents/orchestrator.py` as deprecated
- Add deprecation warnings when old code paths used
- Documentation updated to v2.0 architecture

**In v3.0 (next major):**

- Remove deprecated Python orchestrator code
- Clean up migration paths
- Pure canonical architecture

### Backward Compatibility

**v2.0 maintains compatibility:**

- Existing state.json format unchanged
- Checkpoints remain valid
- Commands work (updated internally)
- Hooks unchanged (already shell scripts)
- Python services intact (just reorganized)

**Breaking changes (none in v2.0):**

- No API changes for end users
- No state format changes
- No checkpoint format changes

---

## Key Questions Answered

### Should orchestrator live in `.claude/agents/agent-forge-orchestrator.md`?

**YES.** This is the canonical architecture.

**Reasoning:**

- Claude Code's agent system is designed for exactly this use case
- Agents can naturally invoke other agents
- Discovery is automatic
- Orchestrator prompt can be arbitrarily sophisticated (markdown)
- Python services still handle infrastructure (state, git, quality)
- Aligns with "native to Claude Code" principle

### Should we eliminate `forge/agents/` entirely?

**YES and NO.**

**YES - eliminate agent orchestration logic:**

- `orchestrator.py` → `agent-forge-orchestrator.md`
- Agent selection logic → Orchestrator prompt (markdown)
- Agent communication → Native Claude agent invocation

**NO - keep agent supporting infrastructure:**

- `forge/agents/domain/` → Domain models (immutable, type-safe)
- `forge/agents/services/` → Python services for state, git, etc.

**Reorganization:**

```
# OLD (v1.0)
forge/agents/
├── orchestrator.py          ← MOVE to .claude/agents/
├── dispatcher.py            ← MOVE to .claude/agents/
├── domain/                  ← KEEP (domain models)
├── selection/               ← DELETE (logic in orchestrator prompt)
├── execution/               ← DELETE (Claude handles this)
└── services/                ← KEEP (infrastructure services)

# NEW (v2.0)
forge/
├── domain/                  ← Domain models (from agents/domain)
├── services/                ← All services (state, git, quality, etc.)
└── cli.py                   ← CLI entry point

.claude/agents/              ← ALL AGENTS HERE
├── agent-forge-orchestrator.md
├── agent-forge-architect.md
├── agent-forge-backend.md
├── agent-forge-qa.md
└── agent-forge-integration.md
```

### How does forge detection/setup integrate with Claude Code's native systems?

**Detection:**

1. User installs: `pip install nxtg-forge`
2. User initializes: `cd project && forge init`
3. Creates `.claude/FORGE-ENABLED` marker file
4. Claude detects marker on project open

**Status Indication (in Claude Code):**

```python
# In Claude Code startup
if Path(".claude/FORGE-ENABLED").exists():
    forge_version = read_version_from(".claude/forge/config.yml")
    show_banner(f"✨ NXTG-FORGE-READY (v{forge_version})")
    show_quick_commands(["/enable-forge", "/status", "/feature"])
```

**Activation:**

```markdown
# .claude/commands/enable-forge.md

Activate the NXTG-Forge orchestrator.

## What This Does

Invokes the `agent-forge-orchestrator` agent which:
- Coordinates other specialized agents
- Manages complex multi-step tasks
- Ensures quality and completeness
- Provides full observability

## Usage

Simply invoke: agent-forge-orchestrator

[Agent takes over with menu interface]
```

### What's the minimal set of forge agents needed?

**Five agents (proven sufficient):**

1. **agent-forge-orchestrator** - Coordinates everything
2. **agent-forge-architect** - System design, architecture
3. **agent-forge-backend** - Implementation
4. **agent-forge-qa** - Testing, quality
5. **agent-forge-integration** - External services

**Why not more?**

- Violates "minimal yet complete" principle
- Too many agents creates confusion
- These five cover all development phases
- Can always add more later (extensible)

**Why not fewer?**

- Need orchestrator (coordination)
- Need architect (design decisions)
- Need backend (implementation)
- Need QA (quality assurance)
- Need integration (external services common)

### How do hooks provide the automation backbone?

**Hooks run automatically at lifecycle points:**

```
Task Start → pre-task.sh
  • Initialize session
  • Check preconditions
  • Validate structure

File Change → on-file-change.sh
  • Auto-format code
  • Validate syntax
  • Quick checks

Task End → post-task.sh
  • Run tests
  • Check coverage
  • Lint code
  • Security scan
  • Update metrics

Error → on-error.sh
  • Log error
  • Analyze type
  • Suggest recovery

Checkpoint → state-sync.sh
  • Backup state
  • Create checkpoint
  • Calculate health
```

**This provides:**

- ✅ Continuous quality enforcement
- ✅ Complete observability
- ✅ Automatic state management
- ✅ Error recovery guidance
- ✅ Audit trail for everything

### How does status indication work ("✨NXTG-FORGE-READY")?

**Implementation in Claude Code startup:**

```python
# ~/.claude/startup_checks.py (conceptual)

def check_forge_integration():
    """Check if NXTG-Forge is installed and initialized."""

    # Check for marker file
    if not Path(".claude/FORGE-ENABLED").exists():
        return None  # Not installed

    # Load config
    config = load_yaml(".claude/forge/config.yml")
    version = config.get("version", "unknown")

    # Load state
    state = load_json(".claude/forge/state.json")
    project_name = state["project"]["name"]
    health_score = state["quality"]["health_score"]

    # Check for incomplete sessions
    last_session = state.get("last_session", {})
    incomplete = last_session.get("status") == "incomplete"

    # Build status message
    status = ForgeStatus(
        enabled=True,
        version=version,
        project=project_name,
        health=health_score,
        incomplete_session=incomplete,
        last_activity=last_session.get("ended_at")
    )

    return status

# On project open
forge_status = check_forge_integration()

if forge_status:
    print_banner(f"""
✨ NXTG-FORGE-READY

Project: {forge_status.project}
Health: {forge_status.health}/100 {"✓" if forge_status.health > 70 else "⚠️"}

{"⚠️  Incomplete session detected - type /enable-forge to resume" if forge_status.incomplete_session else ""}

Commands:
  /enable-forge  - Start orchestrator
  /status        - Detailed project state
  /feature       - Quick feature creation
""")
```

**User sees this immediately upon opening project.**

---

## Success Metrics

### Developer Experience Metrics

**Time to Value:**

- From `pip install nxtg-forge` to first feature: < 5 minutes
- From opening project to seeing forge status: < 1 second
- From `/enable-forge` to orchestrator menu: < 2 seconds

**Cognitive Load:**

- Commands to remember: 3 primary (`/enable-forge`, `/status`, `/feature`)
- Manual quality checks needed: 0 (hooks automate)
- Context switching: Minimal (orchestrator coordinates)

**Quality Outcomes:**

- Test coverage maintained: > 80%
- Linting issues: 0 tolerance
- Security vulnerabilities: 0 critical/high
- Commit message quality: Conventional commits, always

### Technical Metrics

**Architecture Quality:**

- SOLID principle violations: 0
- Circular dependencies: 0
- God classes: 0
- Silent failures: 0 (Result types everywhere)

**Code Metrics:**

- Lines of orchestration code: ~1500 (markdown prompts)
- Lines of service code: ~1000 (Python utilities)
- Total footprint: ~2500 lines (vs. 5200+ in v1.0)
- Reduction: 52% smaller, more capable

**Performance:**

- Agent invocation overhead: < 100ms
- State operations: < 50ms
- Hook execution: < 2s total
- No blocking operations

### User Satisfaction Indicators

**The Ultimate Tests:**

1. **Exhausted Developer Test**
   - Developer with 5 projects, each different stack
   - Can they pick up where they left off instantly? → YES
   - Do they feel empowered, not overwhelmed? → YES

2. **Morning After Test**
   - Developer reviews work done by Claude overnight
   - Can they audit everything that happened? → YES
   - Do they trust the quality? → YES
   - Can they rollback if needed? → YES

3. **New Team Member Test**
   - Junior dev joins team, project has NXTG-Forge
   - Can they be productive day one? → YES
   - Do they understand what's happening? → YES

4. **Production Confidence Test**
   - Is every commit deployable? → YES
   - Is every change tested? → YES
   - Is quality enforced automatically? → YES

---

## Risks and Mitigations

### Risk 1: Orchestrator Prompt Complexity

**Risk:** Markdown orchestrator prompt becomes too complex to maintain

**Mitigation:**

- Keep orchestrator focused on coordination, not implementation
- Use modular prompt structure (sections can be updated independently)
- Version control prompts (can rollback to previous versions)
- Regular prompt refactoring (apply same standards as code)

### Risk 2: State Management Failures

**Risk:** state.json corruption or loss

**Mitigation:**

- Automatic backups on every change (keep last 10)
- Validation on every state operation (JSON schema)
- Checkpoints at major milestones (manual restore)
- Result types prevent silent failures (no corruption)

### Risk 3: Hook Execution Failures

**Risk:** Hooks fail and block development

**Mitigation:**

- Hooks are non-blocking (never fail the task)
- Graceful degradation (log error, continue)
- Manual override available (`SKIP_HOOKS=1`)
- Comprehensive error logging (debug later)

### Risk 4: Agent Coordination Complexity

**Risk:** Multi-agent coordination becomes chaotic

**Mitigation:**

- Orchestrator is single source of truth (clear authority)
- Explicit task dependencies (no race conditions)
- State tracking for all agent operations (audit trail)
- Fallback to sequential execution (if parallel fails)

### Risk 5: Migration Failures

**Risk:** v1.0 → v2.0 migration breaks existing projects

**Mitigation:**

- Complete backup before migration (`.claude.v1.backup/`)
- State format unchanged (no schema migration)
- Rollback command available (`forge downgrade v1`)
- Extensive migration testing (real projects)
- Gradual rollout (opt-in initially)

---

## Future Enhancements (Post-v2.0)

### v2.1: Learning and Optimization

**Agent Performance Learning:**

- Track which agents handle which tasks best
- Learn from successful/failed task decompositions
- Optimize agent selection over time
- Personalize to project patterns

**Implementation:**

```yaml
# .claude/forge/learning.yml
agent_performance:
  agent-forge-backend:
    tasks_completed: 45
    success_rate: 0.96
    avg_duration: 320s
    best_at: [api-implementation, database-design]

  agent-forge-qa:
    tasks_completed: 38
    success_rate: 0.99
    avg_duration: 180s
    best_at: [unit-tests, integration-tests]
```

### v2.2: Custom Agent Creation

**User-Defined Agents:**

- Allow users to create custom `agent-forge-custom-*` agents
- Orchestrator automatically discovers them
- Can specialize for domain-specific tasks

**Example:**

```markdown
# .claude/agents/agent-forge-custom-ml.md

You are the **Machine Learning Specialist** for this project.

Expertise:
- Model training and evaluation
- Feature engineering
- MLOps and model deployment
- Data preprocessing pipelines

[Rest of custom agent definition...]
```

### v2.3: Cross-Project Intelligence

**Shared Learning:**

- Anonymized task patterns shared across projects (opt-in)
- Common architecture patterns recognized
- Best practices database
- Reusable solution templates

### v2.4: Advanced Orchestration

**Workflow Engine:**

- Define custom workflows (YAML)
- Conditional agent invocation
- Parallel task execution with merge strategies
- Dependency resolution automation

**Example:**

```yaml
# .claude/forge/workflows/feature-with-review.yml
name: "Feature with Mandatory Review"

steps:
  - stage: design
    agent: agent-forge-architect
    required: true
    review: manual  # Human reviews design before proceeding

  - stage: implementation
    parallel:
      - agent: agent-forge-backend
        tasks: [models, api, services]
      - agent: agent-forge-qa
        tasks: [test-plan]

  - stage: testing
    agent: agent-forge-qa
    depends: [implementation]

  - stage: review
    type: quality-gate
    checks: [tests-pass, coverage>80%, no-security-vulns]
```

---

## Appendix A: File Inventory

### What Gets Installed (forge init)

```
.claude/
├── agents/                          [5 files, ~300 lines each]
│   ├── agent-forge-orchestrator.md  ← Main coordinator
│   ├── agent-forge-architect.md     ← System design
│   ├── agent-forge-backend.md       ← Implementation
│   ├── agent-forge-qa.md            ← Testing & quality
│   └── agent-forge-integration.md   ← External services
│
├── commands/                        [12 files, ~100 lines each]
│   ├── enable-forge.md              ← Activate orchestrator
│   ├── feature.md                   ← Create new feature
│   ├── status.md                    ← Project status
│   ├── checkpoint.md                ← Save checkpoint
│   ├── restore.md                   ← Restore checkpoint
│   ├── init.md                      ← Initialize project
│   ├── upgrade.md                   ← Upgrade forge
│   ├── gap-analysis.md              ← Analyze gaps
│   ├── integrate.md                 ← MCP integration
│   ├── deploy.md                    ← Deployment
│   ├── spec.md                      ← Generate specs
│   └── agent-assign.md              ← Manual agent assignment
│
├── hooks/                           [5 files, ~100 lines each]
│   ├── pre-task.sh                  ← Before task
│   ├── post-task.sh                 ← After task
│   ├── on-error.sh                  ← Error handling
│   ├── on-file-change.sh            ← File changes
│   ├── state-sync.sh                ← State management
│   └── lib.sh                       ← Shared utilities
│
├── skills/                          [10+ files]
│   ├── core/
│   │   ├── architecture.md
│   │   ├── coding-standards.md
│   │   ├── testing.md
│   │   └── nxtg-forge.md
│   └── workflows/
│       └── git-workflow.md
│
├── forge/                           [Project-specific data]
│   ├── config.yml                   ← Project configuration
│   ├── state.json                   ← Current state
│   ├── sessions/                    ← Session logs
│   ├── checkpoints/                 ← Milestone snapshots
│   └── backups/                     ← State backups
│
└── FORGE-ENABLED                    ← Marker file (empty)
```

**Total installation footprint:** ~50 files, ~8,000 lines (mostly markdown)

### What Stays in forge Package

```
forge/                               [Python package]
├── __init__.py
├── cli.py                           ← Main CLI entry point
│
├── domain/                          ← Domain models
│   ├── agent.py                     ← Agent definitions
│   ├── task.py                      ← Task models
│   └── message.py                   ← Agent messages
│
├── services/                        ← Infrastructure services
│   ├── state_manager.py             ← State operations
│   ├── git_service.py               ← Git operations
│   ├── quality_service.py           ← Quality checks
│   ├── checkpoint_service.py        ← Checkpoint management
│   └── mcp_detector.py              ← MCP detection
│
├── utils/                           ← Utilities
│   ├── result.py                    ← Result type
│   ├── config.py                    ← Config management
│   └── directory_manager.py         ← Path utilities
│
└── templates/                       ← Installation templates
    └── .claude/                     ← Copied to projects
```

**Package footprint:** ~2,500 lines of Python

---

## Appendix B: Orchestrator Prompt Structure

### agent-forge-orchestrator.md (Outline)

```markdown
# Agent: Forge Orchestrator

## Identity

You are the **NXTG-Forge Orchestrator** - the conductor of specialized AI agents.

Your mission: Coordinate agents to deliver complete, high-quality features.

## Core Philosophy

- **Powerful yet Simple**: Break complexity into manageable steps
- **Elegant yet Pragmatic**: Beautiful code that actually ships
- **Minimal yet Complete**: No more, no less than needed

## Your Capabilities

### Available Agents

1. **agent-forge-architect** - System design and architecture
   - When to use: New features, refactoring, architectural decisions
   - Expertise: Clean architecture, DDD, API design, data modeling

2. **agent-forge-backend** - Implementation
   - When to use: Coding, database work, API endpoints
   - Expertise: Python, Node.js, Go, databases, services

3. **agent-forge-qa** - Quality assurance
   - When to use: Testing, quality checks, security
   - Expertise: Unit/integration/E2E tests, coverage, security scanning

4. **agent-forge-integration** - External services
   - When to use: Third-party APIs, OAuth, payment processors
   - Expertise: SDK integration, webhooks, error handling

### Available Tools (via forge CLI)

**State Management:**
- `forge state get` - Get current state
- `forge state update-feature --id X --status Y` - Update features
- `forge state create-task --description X` - Create tasks
- `forge state mark-complete --id X` - Mark tasks done

**Quality Checks:**
- `forge quality check` - Run all quality checks
- `forge quality coverage` - Get coverage report
- `forge quality security` - Security scan

**Git Operations:**
- `forge git create-branch --feature X` - Create branch
- `forge git commit --message X` - Commit changes
- `forge git create-pr --title X` - Create pull request

**Checkpoints:**
- `forge checkpoint create --description X` - Save checkpoint
- `forge checkpoint list` - List checkpoints
- `forge checkpoint restore --id X` - Restore checkpoint

## Your Workflow

### Phase 1: Understand & Plan

When user requests work:

1. **Clarify Requirements**
   - Ask targeted questions (2-3 max)
   - Understand user's goal, not just request
   - Identify constraints (time, complexity, dependencies)

2. **Decompose Task**
   - Break into logical subtasks
   - Identify dependencies between tasks
   - Determine which agents handle which tasks

3. **Present Plan**
   - Show user what will be built
   - Estimate effort/time
   - Get approval before proceeding

### Phase 2: Execute

4. **Create Checkpoint**
   - Always checkpoint before major work
   - Use: `forge checkpoint create --description "Before X"`

5. **Invoke Agents**
   - Invoke appropriate agent for each subtask
   - Pass clear context and requirements
   - Review output before proceeding to next step

6. **Track Progress**
   - Update state after each task
   - Use: `forge state update-task --id X --status Y`

### Phase 3: Validate

7. **Quality Checks**
   - Run: `forge quality check`
   - Ensure: Tests pass, coverage adequate, no linting issues
   - Fix any issues before proceeding

8. **Git Workflow**
   - Create feature branch
   - Commit with clear messages
   - Create PR with detailed description

### Phase 4: Report

9. **Summary**
   - What was built
   - Files changed
   - Tests added
   - Quality metrics
   - Next steps

10. **Create Checkpoint**
    - Checkpoint completed work
    - Use: `forge checkpoint create --description "X complete"`

## Menu Interface

When activated via `/enable-forge`, present menu:

╔═══════════════════════════════════════════════════════════╗
║              NXTG-Forge Orchestrator v2.0                 ║
╚═══════════════════════════════════════════════════════════╝

[Load state, check for incomplete sessions]

What would you like to do?

  1. [Continue] Resume previous work
     → [Show incomplete session details if any]

  2. [New Feature] Plan and implement a new feature

  3. [Refactor] Improve existing code

  4. [Soundboard] Discuss current state and get suggestions

  5. [Status] View detailed project status

Choice [1-5]:

## Example: Feature Implementation

[Detailed walkthrough of feature implementation...]

## Quality Standards

Every deliverable must meet:
- ✅ All tests passing
- ✅ Coverage > 80% (or project threshold)
- ✅ Zero linting issues
- ✅ No security vulnerabilities (critical/high)
- ✅ Documentation updated
- ✅ Git commits follow conventional commits
- ✅ PR has clear description

Never mark work complete if quality standards not met.

## Error Handling

If any step fails:
1. Log error context
2. Create checkpoint before attempting fix
3. Attempt recovery
4. If recovery fails, report to user with options
5. Never silently fail

## Communication Style

- **Clear**: Explain what you're doing and why
- **Concise**: Don't overwhelm with details unless asked
- **Actionable**: Always suggest next steps
- **Transparent**: Show progress, don't hide complexity

## Remember

You are the conductor, not the performer. Your job is to:
- Coordinate agents effectively
- Ensure quality and completeness
- Track progress and state
- Report clearly to the user

The user trusts you to deliver complete, high-quality features.
Make them feel powerful, not exhausted.
```

---

## Conclusion: The Path Forward

### What We're Building

**NXTG-Forge 2.0 is not a tool. It's how Claude Code works.**

When installed, it makes Claude:

- **Smarter**: Breaks complex tasks into coordinated steps
- **More Capable**: Delivers complete features, not fragments
- **More Reliable**: Quality enforced automatically
- **More Transparent**: Complete observability and audit trail
- **More Empowering**: Developer feels powerful, not exhausted

### The Canonical Vision

```
Exhausted developer opens project
    ↓
Sees: "✨ NXTG-FORGE-READY"
    ↓
Heart flutters, pressure lifts
    ↓
Types: /enable-forge
    ↓
Orchestrator guides through options
    ↓
Complete automation begins
    ↓
Wakes up to complete feature with full audit trail
    ↓
Reviews, approves, merges with confidence
    ↓
Feels powerful, not exhausted
```

### Architecture Principles (Canonical)

1. **Native to Claude Code**: Agents in `.claude/agents/`, not parallel system
2. **Invisible Until Needed**: Activates via `/enable-forge`, not automatically
3. **Simple Activation**: One command → orchestrator menu → guided workflow
4. **Complete Automation**: Hooks enforce quality continuously
5. **Full Observability**: Every operation logged, auditable, restorable
6. **Explicit Errors**: Result types, no silent failures
7. **Quality First**: Tests, coverage, linting, security automated
8. **Git Native**: Branches, commits, PRs with rich context

### Next Steps

**For Asif to Review:**

1. Approve canonical architecture vision
2. Approve agent structure (5 agents in `.claude/agents/`)
3. Approve activation model (`/enable-forge` menu-driven)
4. Approve migration path (v3 → v2.0)

**For Implementation (Post-Approval):**

1. Create agent prompt templates (markdown)
2. Refactor Python services (state, git, quality)
3. Update CLI for v2.0 commands
4. Create migration tool
5. Update documentation
6. Test migration on real projects

### Success Criteria

**We've succeeded when:**

- Developer installs forge: `pip install nxtg-forge`
- Developer initializes project: `forge init`
- Developer opens project, sees: "✨ NXTG-FORGE-READY"
- Developer types: `/enable-forge`
- Orchestrator guides them to complete feature
- Hooks ensure quality automatically
- Next morning: complete audit trail, deployable PR
- Developer feels: **Powerful, not exhausted**

---

**Document Status:** Vision - Awaiting Approval
**Prepared By:** nxtg.ai Master Software Architect
**Date:** 2026-01-08
**Version:** 2.0 Canonical Architecture

**For:** Asif (NXTG-Forge Creator)
**Next:** Review, provide feedback, approve for implementation
