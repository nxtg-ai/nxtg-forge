# CANONICAL FORGE VISION - UNIFIED

**The Definitive Vision: Technical Architecture Meets Emotional Journey**

**Version:** 2.0 Unified Canonical
**Date:** 2026-01-08
**Status:** Single Source of Truth
**Authors:**

- Master Software Architect (Technical Architecture)
- Design Vanguard (UX & Emotional Journey)

**Supersedes:**

- `/docs/CANONICAL-FORGE-VISION.md` (Architect's technical vision)
- `/.asif/canonical-vision/CANONICAL-FORGE-VISION.md` (Designer's UX vision)

---

## Executive Summary

### The Transformation Story

NXTG-Forge 2.0 transforms exhausted developers into empowered creators through invisible intelligence:

```
Developer: Exhausted, context-switching between 5 projects, 2:47 AM
    ↓
Opens Claude Code → Sees: "✅ NXTG-FORGE-ENABLED"
    ↓
Types: /enable-forge
    ↓
Orchestrator: "What would you like to do?"
    1. Continue  2. Plan  3. Soundboard  4. Health
    ↓
Chooses Continue → Full context restored automatically
    ↓
Works in flow state while agents coordinate in background
    ↓
Quality gates run continuously, documentation updates automatically
    ↓
Types: "Ready to commit" → All checks pass → Perfect commit message generated
    ↓
Wakes up next morning → Complete session report with GitHub links
    ↓
Developer: Empowered, confident, in control
```

**Core Truth:** Powerful yet simple, elegant yet pragmatic, minimal yet complete.

### Technical Architecture

**Native Claude Code Integration:** Five markdown agents + eight Python services + five automation hooks

```
.claude/agents/                     ← Native Claude Code agents (markdown)
├── agent-forge-orchestrator.md    ← Menu & coordination
├── agent-forge-architect.md        ← Architecture design
├── agent-forge-backend.md          ← Implementation
├── agent-forge-qa.md               ← Testing & quality
└── agent-forge-integration.md      ← External services

forge/services/                     ← Python business logic (type-safe)
├── state_manager.py                ← Session & feature state
├── git_service.py                  ← Git operations & commits
├── quality_service.py              ← Quality metrics & gates
├── context_restoration.py          ← Continue mode context (NEW)
├── activity_reporter.py            ← Background status (NEW)
├── session_reporter.py             ← Morning reports (NEW)
├── quality_alerter.py              ← Interactive warnings (NEW)
└── recommendation_engine.py        ← Smart suggestions (NEW)

.claude/hooks/                      ← Automation backbone
├── pre-task.sh                     ← Precondition checks
├── post-task.sh                    ← Quality enforcement
├── on-error.sh                     ← Error recovery
├── on-file-change.sh               ← Continuous validation
└── state-sync.sh                   ← State persistence
```

**Hybrid Model:** Agents (markdown) provide natural coordination, services (Python) provide type-safe computation.

### Implementation Readiness

**Alignment Score:** 85% → 100% (after gap resolution)
**Confidence Level:** 95% (all technical challenges have solutions)
**Timeline:** 6-8 weeks total (2 weeks gap-filling + 4-6 weeks implementation)

**Status:** All gaps identified and resolved. Ready for implementation.

---

## Part 1: Philosophy & Principles

### Design Principles (Unified)

#### 1. Invisible Intelligence

**Architect:** "Native to Claude Code, not parallel to it"
**Designer:** "Zero cognitive load, complete transparency"
**Unified:** Automation should feel magical, not creepy. Present at recognition, invisible during flow.

#### 2. Elegant Abstraction

**Architect:** "Hide complexity while exposing power"
**Designer:** "Delightful automation that just works"
**Unified:** Complex orchestration hidden behind simple 4-option menu. Power without complexity.

#### 3. Complete Transparency

**Architect:** "Every action auditable, traceable, reversible"
**Designer:** "Trust through visibility"
**Unified:** Agent handoffs visible but subtle. Every automation logged. Checkpoints for rollback.

#### 4. Menu-Driven Simplicity

**Architect:** "1-4 choices maximum, zero cognitive load"
**Designer:** "Four perfect options that handle everything"
**Unified:** EXACTLY four menu options. No more, no less. Continue/Plan/Soundboard/Health.

#### 5. Git-Based Everything

**Architect:** "Version control as backbone of all operations"
**Designer:** "Morning-after confidence through complete audit trail"
**Unified:** Git commits are the source of truth. All state changes create git artifacts.

### The One Truth: The Canonical Menu

**This is the ONLY menu system. No variations allowed.**

```
What would you like to do?

┌────────────────────────────────────────────────────────────┐
│                                                            │
│  1. [Continue] Pick up where we left off                  │
│     Resume ongoing work with full context                 │
│                                                            │
│  2. [Plan] Review & plan new feature(s)                   │
│     Collaborative feature design and breakdown             │
│                                                            │
│  3. [Soundboard] Discuss current situation                │
│     Strategic advice and next steps                        │
│                                                            │
│  4. [Health] Deep dive into project health                │
│     Comprehensive analysis and recommendations             │
│                                                            │
│  Type 1-4 or just tell me what you need                   │
└────────────────────────────────────────────────────────────┘
```

**Rationale:**

- **4 options** (not 3, not 5): Optimal for zero cognitive load
- **Continue** covers 80% of use cases: resume previous work
- **Plan** covers feature design AND refactoring (architecture improvements)
- **Soundboard** for open exploration without execution commitment
- **Health** combines status + recommendations for complete visibility

**NO OTHER MENU FORMATS PERMITTED.** This is canonical.

---

## Part 2: The Emotional Journey

### The Six Acts

#### Act 1: The Exhaustion (Before Forge)

**State:** 2:47 AM, 5 projects, cognitive overload, imposter syndrome
**Emotions:** Fear, overwhelm, isolation, anxiety, inadequacy
**Quote:** "I'm drowning alone. I can't keep up. What if I break something?"

#### Act 2: The Recognition (Discovery)

**Trigger:** Opens Claude Code, sees "✅ NXTG-FORGE-ENABLED"
**Emotions:** Recognition, curiosity, hope
**Quote:** "Wait... there's help? Maybe I don't have to do this alone."

#### Act 3: The Activation (Empowerment Begins)

**Action:** Types `/enable-forge`, sees menu appear
**Emotions:** Relief, confidence, clarity, control
**Quote:** "Something is taking care of the details. I have backup now."

#### Act 4: The Working Session (Invisible Intelligence)

**Experience:** Chooses "Continue", full context restored, works in flow
**Emotions:** Focus, trust, flow, competence
**Quote:** "I can concentrate on solving problems. The system catches what I miss."

#### Act 5: The Commit (Automated Excellence)

**Action:** Types "Ready to commit", quality gates pass, perfect message generated
**Emotions:** Pride, confidence, relief, validation
**Quote:** "This is solid work. I built something good."

#### Act 6: The Morning After (Complete Confidence)

**Experience:** Wakes up, reads comprehensive report with GitHub links
**Emotions:** Confidence, readiness, empowerment
**Quote:** "I know exactly what happened. I trust this work. I'm powerful."

**The Transformation:** Exhaustion → Empowerment (6 acts, one journey)

---

## Part 3: Technical Architecture

### 3.1 Hybrid Agent System

**Core Principle:** Agents are native Claude Code markdown files. Complex logic delegated to Python services.

#### The Five Agents (Markdown)

**1. agent-forge-orchestrator.md** - The Conductor

- **Role:** High-level coordination, menu presentation, context switching
- **Capabilities:**
  - Present canonical 4-option menu
  - Load context from state.json for Continue mode
  - Coordinate specialist agents for Plan mode
  - Facilitate open discussion for Soundboard mode
  - Aggregate metrics for Health mode
- **Invokes:** All other agents + all services via `forge` CLI
- **Location:** `.claude/agents/agent-forge-orchestrator.md`

**2. agent-forge-architect.md** - The Designer

- **Role:** Architecture design, system planning, technical decisions
- **Invoked by:** Orchestrator during Plan mode
- **Capabilities:**
  - Domain modeling
  - API contract design
  - Technology stack recommendations
  - Architecture pattern selection
- **Returns:** Architecture specs as structured markdown
- **Location:** `.claude/agents/agent-forge-architect.md`

**3. agent-forge-backend.md** - The Builder

- **Role:** Implementation, coding, refactoring
- **Invoked by:** Orchestrator after architecture approved
- **Capabilities:**
  - Code generation following architecture
  - Refactoring existing code
  - Performance optimization
  - Error handling implementation
- **Returns:** Implemented code + documentation
- **Location:** `.claude/agents/agent-forge-backend.md`

**4. agent-forge-qa.md** - The Guardian

- **Role:** Testing, quality assurance, security validation
- **Invoked by:** Orchestrator after implementation OR on-demand
- **Capabilities:**
  - Test generation (unit, integration, E2E)
  - Security vulnerability detection
  - Performance testing
  - Quality metric validation
- **Returns:** Test suite + quality report
- **Location:** `.claude/agents/agent-forge-qa.md`

**5. agent-forge-integration.md** - The Connector

- **Role:** External service integration, API clients, MCP integration
- **Invoked by:** Orchestrator when external services needed
- **Capabilities:**
  - MCP server detection and configuration
  - API client generation
  - Third-party SDK integration
  - Service orchestration
- **Returns:** Integration code + configuration
- **Location:** `.claude/agents/agent-forge-integration.md`

#### Agent Visibility Specification

**Principle:** Transparent but not noisy

**Format:** When orchestrator invokes specialist agent:

```
🎯 [PHASE NAME] (agent: [AGENT-NAME])

[Agent output appears here]

✓ [PHASE NAME] complete
```

**Examples:**

```
🎯 Designing Architecture (agent: architect)
...architecture design output...
✓ Architecture design complete

🔨 Implementing Backend (agent: backend)
...implementation output...
✓ Backend implementation complete

🧪 Testing Implementation (agent: qa)
...test generation and execution...
✓ Testing complete
```

**Rationale:** Trust requires visibility. Developers see agent handoffs but presentation is subtle.

### 3.2 Service Layer (Python)

**Core Principle:** Type-safe, testable business logic. Services return Result types (no exceptions for control flow).

#### Existing Services

**1. StateManager** - `forge/services/state_manager.py`

- **Purpose:** Session and feature state persistence
- **Data:** `.claude/forge/state.json` (features, tasks, progress)
- **Methods:**
  - `get_current_state() -> ProjectState`
  - `update_feature_progress(feature_id, progress) -> Result[None, StateError]`
  - `save_session(session_data) -> Result[SessionId, StateError]`

**2. GitService** - `forge/services/git_service.py`

- **Purpose:** Git operations and commit message generation
- **Methods:**
  - `create_branch(name) -> Result[BranchName, GitError]`
  - `generate_commit_message(diff) -> Result[CommitMessage, GitError]`
  - `create_commit(message) -> Result[CommitHash, GitError]`
  - `create_pr(title, body) -> Result[PrUrl, GitError]`

**3. QualityService** - `forge/services/quality_service.py`

- **Purpose:** Quality metrics calculation and gate enforcement
- **Methods:**
  - `run_all_checks() -> QualityReport`
  - `calculate_health_score() -> HealthScore`
  - `check_coverage_threshold(min_coverage) -> Result[None, CoverageError]`

#### New Services (Gap Resolution)

**4. ContextRestorationService** - `forge/services/context_restoration.py` (NEW)

- **Purpose:** Restore full context for Continue mode
- **Why needed:** Designer specified "Continue" with smart recommendations. Architect didn't specify HOW.
- **Methods:**

  ```python
  def restore_context(self) -> ContinueContext:
      """Load last session context with smart recommendations."""
      # 1. Read state.json for last active feature/tasks
      # 2. Check current git branch and analyze diff from last commit
      # 3. Scan recently modified files (< 2 hours old)
      # 4. Calculate % complete based on task completion ratio
      # 5. Generate recommendations via code analyzer
      # 6. Detect code smells (hardcoded secrets, weak crypto, etc.)
      return ContinueContext(
          last_session_time=...,
          branch=...,
          progress_percent=...,
          outstanding_tasks=[...],
          recommendations=[...]
      )
  ```

**5. ActivityReporter** - `forge/services/activity_reporter.py` (NEW)

- **Purpose:** Report background activity to active Claude session
- **Why needed:** Designer specified real-time activity indicators. Architect specified hooks but not reporting mechanism.
- **Implementation:**

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

  # Hooks use this:
  # forge activity start "Running tests..."
  # pytest
  # forge activity complete "Tests passed" --duration=$SECONDS

  # Orchestrator polls this file and displays updates
  ```

**6. SessionReporter** - `forge/services/session_reporter.py` (NEW)

- **Purpose:** Generate comprehensive session reports (morning-after confidence)
- **Why needed:** Designer specified detailed overnight report. Architect specified session logs but not report generation.
- **Methods:**

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

**7. QualityAlerter** - `forge/services/quality_alerter.py` (NEW)

- **Purpose:** Surface quality issues interactively with remediation options
- **Why needed:** Designer specified interactive quality alerts. Architect specified quality checks but not interactive surfacing.
- **Methods:**

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

**8. RecommendationEngine** - `forge/services/recommendation_engine.py` (NEW)

- **Purpose:** Generate smart suggestions for Continue mode
- **Why needed:** Designer specified "💡 Smart Recommendations" with specific examples. Architect didn't specify generation mechanism.
- **Methods:**

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
      # This would call Claude with code snippets for deeper analysis
      ai_recommendations = self._ai_code_review(context.recent_files)
      recommendations.extend(ai_recommendations)

      # Prioritize and return top 3
      return sorted(recommendations, key=lambda r: r.priority, reverse=True)[:3]
  ```

### 3.3 Hook System (Automation Backbone)

**Core Principle:** Hooks provide continuous quality enforcement WITHOUT being gates. Non-interactive, provide guardrails not barriers.

**Hook Execution:** All hooks are bash scripts in `.claude/hooks/`. Claude Code executes them at defined lifecycle points.

#### Hook Specifications

**1. pre-task.sh** - Precondition Validation

```bash
#!/bin/bash
# Runs before agent starts task execution

# Check git status
if [[ -n $(git status --porcelain) ]]; then
    echo "⚠️  Working directory has uncommitted changes"
    echo "   Consider committing or stashing before starting new task"
fi

# Check environment
if ! forge check-env; then
    echo "❌ Environment check failed"
    exit 1
fi

# Save current state snapshot
forge state snapshot --tag=pre-task

exit 0  # Non-blocking warnings
```

**2. post-task.sh** - Quality Enforcement

```bash
#!/bin/bash
# Runs after agent completes task

# Report activity start
forge activity start "Running quality checks..."

# Format code
forge activity start "Formatting code..."
black . --quiet && ruff check . --fix
forge activity complete "Code formatted" --duration=$SECONDS

# Type check
forge activity start "Type checking..."
mypy . --quiet
forge activity complete "Type checking passed" --duration=$SECONDS

# Run tests
forge activity start "Running tests..."
pytest --quiet --tb=short
test_result=$?
forge activity complete "Tests completed" --duration=$SECONDS --success=$([ $test_result -eq 0 ] && echo "true" || echo "false")

# Calculate coverage
coverage_before=$(forge quality get-coverage)
coverage_after=$(coverage report --precision=0 | grep TOTAL | awk '{print $NF}' | sed 's/%//')

# Alert if coverage dropped
if [[ $coverage_after -lt $coverage_before ]]; then
    forge quality alert coverage-dropped \
        --before=$coverage_before \
        --after=$coverage_after
fi

# Update state
forge state update-metrics \
    --health-score=$(forge quality calculate-health) \
    --coverage=$coverage_after

exit 0  # Always succeed (enforcement, not gate)
```

**3. on-error.sh** - Error Recovery

```bash
#!/bin/bash
# Runs when agent encounters error

error_type=$1
error_message=$2

# Log error
forge state log-error --type=$error_type --message="$error_message"

# Create checkpoint for potential rollback
checkpoint_id=$(forge checkpoint create --auto --description="Before error recovery")

echo "🔖 Checkpoint created: $checkpoint_id"
echo "   Restore with: /restore $checkpoint_id"

# Suggest recovery actions
forge recommend-recovery --error-type=$error_type

exit 0
```

**4. on-file-change.sh** - Continuous Validation

```bash
#!/bin/bash
# Runs when files are modified (file watcher trigger)

changed_file=$1

# Quick validation only (no full test suite)
case $changed_file in
    *.py)
        ruff check $changed_file --quiet || echo "⚠️  Lint warning in $changed_file"
        ;;
    *.ts|*.tsx)
        eslint $changed_file --quiet || echo "⚠️  Lint warning in $changed_file"
        ;;
    *.md)
        # Update documentation index if docs changed
        if [[ $changed_file == docs/* ]]; then
            forge docs update-index
        fi
        ;;
esac

exit 0  # Never block
```

**5. state-sync.sh** - State Persistence

```bash
#!/bin/bash
# Runs periodically (every 5 minutes) OR on demand

# Save current session state
forge state save-session \
    --include-context \
    --include-metrics \
    --include-git-status

# Sync to remote backup if configured
if [[ -n $FORGE_BACKUP_URL ]]; then
    forge state sync-remote --quiet
fi

exit 0
```

#### Activity Monitoring (Phased Implementation)

**Phase 1: Synchronous (MVP)** - Simple, works everywhere

```bash
# After hook completes, show summary
✓ Quality checks complete (2.1s)
✓ Tests: 124 passed
✓ Coverage: 82% (+4%)
```

**Phase 2: Asynchronous (Enhancement)** - ANSI terminal required

```bash
# During hook execution, show live status in corner
┌─ Forge Activity ────────────────────────────────────────────┐
│ ✓ Code formatted (black)                       0.2s         │
│ ✓ Linting passed (ruff)                        0.4s         │
│ ✓ Type checking passed (mypy)                  0.8s         │
│ 🔍 Running tests...                                         │
└─────────────────────────────────────────────────────────────┘
```

**Technical Implementation (Phase 2):**

```python
# In forge/cli.py activity monitor command
def monitor_activity_display():
    """Non-blocking activity display using ANSI positioning."""
    import sys, select

    if not sys.stdout.isatty() or os.getenv('TERM') == 'dumb':
        return  # Fallback to Phase 1 (synchronous)

    while True:
        # Read activity status
        status = ActivityReporter().get_current_status()

        # Save cursor, move to bottom-right, draw box, restore cursor
        print("\033[s", end="")      # Save position
        print("\033[999;999H", end="") # Move to bottom-right
        print("\033[5A", end="")     # Move up 5 lines
        render_activity_box(status)
        print("\033[u", end="")      # Restore position
        sys.stdout.flush()

        time.sleep(0.5)  # Update every 500ms
```

**Fallback Strategy:** If ANSI not supported, gracefully degrade to Phase 1.

### 3.4 State Management

**Core Principle:** Git is source of truth. State files are caches/indexes for performance.

#### State Storage

**Project State:** `.claude/forge/state.json`

```json
{
  "project": {
    "name": "my-awesome-app",
    "tech_stack": ["python", "fastapi", "postgresql"],
    "health_score": 84,
    "coverage": 89
  },
  "features": [
    {
      "id": "feat-001",
      "name": "JWT Authentication",
      "status": "in_progress",
      "progress": 67,
      "branch": "feature/auth-system",
      "tasks": [
        {"id": "task-001", "description": "Database schema", "status": "complete"},
        {"id": "task-002", "description": "User model", "status": "complete"},
        {"id": "task-003", "description": "API endpoints", "status": "in_progress"},
        {"id": "task-004", "description": "Integration tests", "status": "pending"}
      ]
    }
  ],
  "last_session": {
    "id": "session_20260107_214530",
    "start_time": "2026-01-07T21:45:30Z",
    "end_time": null,
    "active": true
  }
}
```

**Session Logs:** `.claude/forge/sessions/<session_id>.json`

```json
{
  "id": "session_20260107_214530",
  "start_time": "2026-01-07T21:45:30Z",
  "end_time": "2026-01-08T03:15:22Z",
  "duration_seconds": 19792,
  "feature_id": "feat-001",
  "branch": "feature/auth-system",
  "commits": [
    {"hash": "a7b9c3d", "message": "feat(auth): implement JWT authentication", "time": "2026-01-07T22:30:00Z"},
    {"hash": "b2e4f1a", "message": "test(auth): add integration tests", "time": "2026-01-08T01:15:00Z"}
  ],
  "files_changed": 23,
  "lines_added": 847,
  "lines_removed": 93,
  "tests_added": 47,
  "coverage_before": 82,
  "coverage_after": 89,
  "health_before": 78,
  "health_after": 84,
  "pr_created": {
    "number": 127,
    "url": "https://github.com/company/api/pull/127",
    "status": "checks_passing"
  },
  "checkpoints": [
    {"id": "cp_2026-01-07_2245", "description": "JWT model complete", "commit": "a7b9c3d"},
    {"id": "cp_2026-01-08_0115", "description": "Tests passing", "commit": "b2e4f1a"}
  ]
}
```

**Checkpoint Metadata:** `.claude/forge/checkpoints/<checkpoint_id>.json`

```json
{
  "id": "cp_2026-01-07_2245",
  "created_at": "2026-01-07T22:45:00Z",
  "description": "JWT model complete - all tests passing",
  "git_commit": "a7b9c3d",
  "git_tag": "checkpoint/cp_2026-01-07_2245",
  "branch": "feature/auth-system",
  "state_snapshot": {
    "health_score": 81,
    "coverage": 85,
    "tests_passing": true
  }
}
```

#### State Operations

**Context Restoration (Continue Mode):**

```python
context = ContextRestorationService().restore_context()
# Returns:
# - Last session metadata
# - Current branch and uncommitted changes
# - Progress % based on task completion
# - Smart recommendations from code analysis
```

**Session Tracking:**

```python
# On /enable-forge
session_id = StateManager().start_session(feature_id="feat-001")

# Periodically during session (state-sync.sh hook)
StateManager().update_session(session_id, {
    "commits": git_service.get_recent_commits(),
    "metrics": quality_service.get_current_metrics()
})

# On session end (user exits or /disable-forge)
StateManager().end_session(session_id)
SessionReporter().generate_session_report(session_id)
```

**Checkpoint Creation:**

```python
# Manual checkpoint
checkpoint_id = CheckpointManager().create_checkpoint(
    description="JWT auth complete - all tests passing"
)
# Creates git tag + saves metadata

# Auto checkpoint (on-error.sh or significant milestone)
checkpoint_id = CheckpointManager().create_checkpoint(
    description="Before error recovery",
    auto=True
)
```

**Checkpoint Restoration:**

```python
# Safe restore (creates new branch)
CheckpointManager().restore_checkpoint(
    checkpoint_id="cp_2026-01-07_2245",
    strategy="new_branch"  # Or "stash_current" or "hard_reset"
)
```

---

## Part 4: Developer Experience

### 4.1 Status Detection & Display

**Principle:** Immediate recognition without requiring action.

#### Scenario 1: Forge Already Enabled

```bash
$ cd my-awesome-app
$ claude

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ✅ NXTG-FORGE-ENABLED                                        ║
║                                                              ║
║     Your AI development infrastructure is active             ║
║     and watching your back.                                  ║
║                                                              ║
║     Project: my-awesome-app                                  ║
║     Health Score: 84/100 (Good)                              ║
║     Active Agents: 5                                         ║
║     Monitoring: ON                                           ║
║                                                              ║
║     Commands:                                                ║
║       /enable-forge  - Start orchestrator                    ║
║       /status        - View detailed project state           ║
║       /help          - See all forge commands                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Claude>
```

#### Scenario 2: Forge Installed But Not Enabled

```bash
$ cd another-project
$ claude

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ✨ NXTG-FORGE-READY                                          ║
║                                                              ║
║     This project can have AI-powered infrastructure.         ║
║     Turn it on with: /enable-forge                           ║
║                                                              ║
║     It will:                                                 ║
║       • Set up intelligent project scaffolding               ║
║       • Enable continuous quality checks                     ║
║       • Activate autonomous documentation                    ║
║       • Deploy intelligent git workflows                     ║
║       • Monitor and optimize your project 24/7               ║
║                                                              ║
║     Ready? Type: /enable-forge                               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Claude>
```

#### Scenario 3: Forge Not Installed

```bash
$ cd brand-new-project
$ claude

Claude>  # Normal prompt, no banner
```

**Detection Logic:**

```python
# In .claude/hooks/on-session-start.sh
if [ -f .claude/FORGE-ENABLED ]; then
    forge status --banner --format=enabled
elif [ -f .claude/forge/state.json ]; then
    forge status --banner --format=ready
fi
# Else: silent (no banner)
```

**Implementation:** Hook executes in <500ms. Banner appears before first user prompt.

### 4.2 Activation Flow

**Command:** `/enable-forge`

**Experience:**

```bash
Claude> /enable-forge

╔══════════════════════════════════════════════════════════════╗
║  NXTG-FORGE ACTIVATION                                       ║
╚══════════════════════════════════════════════════════════════╝

🔍 Analyzing project structure...              ✓ Complete
🧬 Detecting technology stack...               ✓ Complete
📊 Assessing codebase health...                ✓ Complete
🔌 Discovering MCP servers...                  ✓ Complete
📚 Initializing knowledge base...              ✓ Complete
🎯 Configuring intelligent agents...           ✓ Complete
🔗 Setting up automation hooks...              ✓ Complete
📡 Enabling continuous monitoring...           ✓ Complete

╔══════════════════════════════════════════════════════════════╗
║  ✅ NXTG-FORGE IS NOW ACTIVE                                  ║
╚══════════════════════════════════════════════════════════════╝

Project: my-awesome-app
Health Score: 78/100 (Good - room for improvement)
Active Agents: 5
Monitoring: ON
Auto-documentation: ON
Quality Gates: ON

What would you like to do?

┌────────────────────────────────────────────────────────────┐
│                                                            │
│  1. [Continue] Pick up where we left off                  │
│     Resume ongoing work with full context                 │
│                                                            │
│  2. [Plan] Review & plan new feature(s)                   │
│     Collaborative feature design and breakdown             │
│                                                            │
│  3. [Soundboard] Discuss current situation                │
│     Strategic advice and next steps                        │
│                                                            │
│  4. [Health] Deep dive into project health                │
│     Comprehensive analysis and recommendations             │
│                                                            │
│  Type 1-4 or just tell me what you need                   │
└────────────────────────────────────────────────────────────┘
```

**Implementation:**

- Activation steps are sequential (not progress bar - CLI constraint acknowledged)
- Each step: simple checkmark on completion
- Total duration: 3-5 seconds typical
- Creates `.claude/FORGE-ENABLED` marker file
- Starts session tracking
- Loads orchestrator agent

### 4.3 Menu System

**The Canonical Menu** (detailed behavior)

#### Option 1: Continue - Context Restoration

**User Action:** Types `1` or "continue" or "pick up where we left off"

**Orchestrator Behavior:**

```bash
Claude> 1

╔══════════════════════════════════════════════════════════════╗
║  CONTINUING: JWT Authentication Feature                      ║
╚══════════════════════════════════════════════════════════════╝

📍 Context Restored
   Last session: 2 hours ago
   Branch: feature/auth-system
   Progress: 67% complete

🎯 Outstanding Tasks
   ✓ Database schema created
   ✓ User model implemented
   ✓ JWT service created
   ⏳ API endpoints (in progress)
   ⏸ Integration tests (pending)
   ⏸ Documentation (pending)

💡 Smart Recommendations
   • I noticed your JWT secret is hardcoded in config.py
     → I can move it to environment variables

   • Your password hashing uses SHA256
     → Should upgrade to bcrypt or argon2 for security

   • Tests are at 67% coverage
     → Should be 85% minimum for production readiness

What would you like me to work on?
```

**How it works:**

1. Orchestrator calls `ContextRestorationService().restore_context()`
2. Service reads state.json, analyzes git diff, scans recent files
3. Service calls `RecommendationEngine().analyze_and_recommend(context)`
4. Orchestrator formats and presents context + recommendations
5. Waits for user to specify what to work on
6. Delegates to appropriate specialist agent

**Conversation continues naturally:** User can say "finish the API endpoints" and orchestrator coordinates backend + qa agents.

#### Option 2: Plan - Feature Design

**User Action:** Types `2` or "plan" or "I want to add a new feature"

**Orchestrator Behavior:**

```bash
Claude> 2

╔══════════════════════════════════════════════════════════════╗
║  PLANNING MODE: Feature Design                               ║
╚══════════════════════════════════════════════════════════════╝

What feature would you like to plan?

[User describes feature]

Claude> I want to add email verification for new users

Great! Let's design this feature together.

🎯 Invoking agent-forge-architect for feature analysis...

[Architect agent analyzes requirements]

📋 Feature Breakdown: Email Verification

🏗️  Architecture Design (agent: architect)

Domain Model:
  • EmailVerification entity
    - user_id: UUID
    - token: str (secure random, 32 chars)
    - expires_at: datetime
    - verified_at: datetime | None

  • User entity updates
    - email_verified: bool
    - email_verification_sent_at: datetime | None

API Endpoints:
  • POST /api/auth/send-verification
    - Sends verification email with token
    - Rate limited: 1 per 5 minutes per user

  • POST /api/auth/verify-email
    - Validates token, marks user as verified
    - Token expires after 24 hours

External Dependencies:
  • Email service (SendGrid or AWS SES)
  • Background job queue (Celery or RQ) for async email

✓ Architecture design complete

📋 Implementation Tasks

1. Database Migration
   - Add email_verifications table
   - Add email_verified column to users
   Duration estimate: 30 minutes

2. Email Verification Service
   - Token generation with cryptographic randomness
   - Email template with verification link
   - Token validation with expiry check
   Duration estimate: 2 hours

3. API Endpoints
   - Send verification endpoint with rate limiting
   - Verify email endpoint with error handling
   Duration estimate: 1.5 hours

4. Integration Tests
   - Happy path: send → verify → user verified
   - Edge cases: expired token, invalid token, already verified
   Duration estimate: 1 hour

5. Documentation
   - API docs update
   - User guide for email verification
   Duration estimate: 30 minutes

Total Estimate: 5.5 hours

Ready to implement? I can:
  1. Start implementation now (full orchestration)
  2. Let you review and adjust the plan
  3. Create tickets/issues for manual implementation
  4. Save plan and implement later

What would you like to do?
```

**How it works:**

1. Orchestrator captures feature description from user
2. Invokes architect agent with feature requirements
3. Architect designs domain model, API contracts, dependencies
4. Orchestrator breaks design into concrete tasks with estimates
5. Presents plan to user for approval
6. On approval, orchestrates backend → qa → integration agents

#### Option 3: Soundboard - Strategic Discussion

**User Action:** Types `3` or "soundboard" or "I want to discuss"

**Orchestrator Behavior:**

```bash
Claude> 3

╔══════════════════════════════════════════════════════════════╗
║  SOUNDBOARD MODE: Strategic Discussion                       ║
╚══════════════════════════════════════════════════════════════╝

I'm here for open-ended discussion. No execution, just advice.

What's on your mind?

[User asks question]

Claude> Should I refactor this monolith into microservices?

🤔 Let's think through this carefully...

📊 Current State Analysis

Your codebase:
  • 47,000 lines of Python
  • Monolithic FastAPI application
  • 12 distinct functional domains identified
  • 89% test coverage (excellent)
  • Health score: 84/100 (good)

🎯 Microservices: When They Make Sense

Good reasons to split:
  ✓ Independent scaling needs (you have this: auth vs. data processing)
  ✓ Different deployment cadences (auth changes weekly, core is stable)
  ✓ Team organization (6+ engineers, different domains)

Not-so-good reasons:
  ✗ "Everyone else is doing it" (don't follow hype)
  ✗ "It's more modern" (monoliths can be excellent)
  ✗ "It will solve our problems" (microservices create new problems)

📈 Your Specific Situation

I analyzed your codebase. Here's what I see:

Strong candidates for extraction:
  1. Background job processor (different scaling, CPU-bound)
  2. Notification service (independent, high volume)
  3. Report generator (sporadic, memory-intensive)

Should STAY in monolith:
  • Core business logic (tightly coupled, that's OK!)
  • Authentication (shared by everything, keep it simple)
  • Admin panel (low traffic, benefits from simplicity)

💡 My Recommendation

Hybrid approach:
  1. Keep main monolith for core business logic
  2. Extract 3 independent services (listed above)
  3. Use shared libraries for common code
  4. Keep single database initially (no distributed transactions yet)

This gives you:
  ✓ Independent scaling where it matters
  ✓ Simpler deployment for extracted services
  ✓ Lower complexity than full microservices
  ✓ Easy rollback if extraction doesn't work out

📋 If you want to proceed:

Phase 1 (2 weeks):
  • Extract background job processor
  • Validate deployment pipeline
  • Monitor performance impact

Phase 2 (2 weeks):
  • Extract notification service
  • Implement service discovery

Phase 3 (2 weeks):
  • Extract report generator
  • Evaluate if further splitting makes sense

Want me to create a detailed plan? Or discuss specific concerns?
```

**How it works:**

1. Orchestrator analyzes project state (health, architecture, metrics)
2. Provides strategic advice based on analysis
3. NO CODE EXECUTION - purely advisory
4. Can deep-dive into specific topics on request
5. Can transition to Plan mode if user wants to implement suggestions

#### Option 4: Health - Comprehensive Analysis

**User Action:** Types `4` or "health" or "show me project health"

**Orchestrator Behavior:**

```bash
Claude> 4

╔══════════════════════════════════════════════════════════════╗
║  PROJECT HEALTH ANALYSIS: my-awesome-app                     ║
╚══════════════════════════════════════════════════════════════╝

📊 OVERALL HEALTH SCORE: 84/100 (Good)

─────────────────────────────────────────────────────────────

🧪 TESTING & QUALITY (Score: 89/100)

Test Coverage: 89% (target: 85%+)  ✓ Excellent
  • Unit tests: 847 tests, all passing
  • Integration tests: 124 tests, all passing
  • E2E tests: 18 tests, all passing

Code Quality: Grade A
  • Linting: 0 errors, 3 warnings
  • Type coverage: 94%
  • Complexity: Average 4.2 (target: <10)

⚠️  Areas needing attention:
  • auth/controllers.py: 0% test coverage (new file)
  • utils/validation.py: Complexity 15 (recommend refactor)

─────────────────────────────────────────────────────────────

🔒 SECURITY (Score: 82/100)

Dependencies: 47 total, 2 outdated
  ⚠️  fastapi 0.95.0 → 0.109.0 (security fix available)
  ⚠️  pydantic 1.10.4 → 2.5.3 (breaking changes)

Vulnerability Scan: 1 medium severity issue
  ⚠️  SQL injection risk in raw query (reports/generator.py:145)
      Recommendation: Use parameterized queries

Secrets: All secured ✓
  • No hardcoded secrets detected
  • .env file properly gitignored
  • Sensitive configs in environment variables

─────────────────────────────────────────────────────────────

📚 DOCUMENTATION (Score: 76/100)

API Documentation: 85% coverage
  • 34 endpoints documented
  • 6 endpoints missing examples

Code Documentation: 71% coverage
  ⚠️  23 public functions without docstrings
  ⚠️  12 classes without class-level docs

README: Complete ✓
  • Getting started guide
  • Architecture overview
  • Contributing guidelines

─────────────────────────────────────────────────────────────

🏗️  ARCHITECTURE (Score: 88/100)

Structure: Clean ✓
  • Clear separation of concerns
  • Dependency injection used consistently
  • Result types for error handling

Technical Debt: Moderate
  • 14 TODO comments in codebase
  • 3 deprecated functions still in use
  • 1 circular import detected (utils ↔ models)

Performance: Good
  • Average response time: 47ms
  • P95 latency: 180ms (target: <200ms)
  • No N+1 query issues detected

─────────────────────────────────────────────────────────────

🔗 GIT & DEPLOYMENT (Score: 90/100)

Commit Quality: Excellent ✓
  • 100% conventional commits
  • Average commit message length: 68 chars
  • All commits signed

Branching: Clean ✓
  • 3 active feature branches
  • 0 stale branches
  • PR review required for main

CI/CD: Passing ✓
  • All checks green on main
  • Average build time: 4m 32s
  • Deploy success rate: 98% (last 30 days)

─────────────────────────────────────────────────────────────

📈 RECOMMENDED ACTIONS (Priority Order)

1. 🔴 HIGH: Fix SQL injection vulnerability
   Action: forge security fix-sql-injection reports/generator.py:145
   Estimate: 15 minutes

2. 🟡 MEDIUM: Update fastapi to 0.109.0
   Action: forge deps update fastapi --major
   Estimate: 30 minutes (includes testing)

3. 🟡 MEDIUM: Add test coverage for auth/controllers.py
   Action: forge test generate auth/controllers.py
   Estimate: 1 hour

4. 🟢 LOW: Refactor high-complexity function
   Action: forge refactor utils/validation.py --target-complexity=8
   Estimate: 45 minutes

5. 🟢 LOW: Add missing docstrings
   Action: forge docs generate-docstrings --missing-only
   Estimate: 30 minutes

─────────────────────────────────────────────────────────────

Want me to work on any of these? I can:
  1. Fix high-priority issues now
  2. Create plan for all recommendations
  3. Show detailed analysis of specific area
  4. Generate report and save for later
```

**How it works:**

1. Orchestrator calls `QualityService().calculate_health_score()`
2. Service aggregates metrics from multiple sources:
   - Test results and coverage
   - Linting and type checking
   - Security scans
   - Documentation coverage
   - Git quality
   - Performance metrics
3. Orchestrator formats comprehensive report
4. Uses `RecommendationEngine()` to prioritize actions
5. Offers to implement recommendations immediately

### 4.4 Background Activity Monitoring

**Phase 1 Implementation:** Synchronous (works everywhere)

**When hooks complete:**

```bash
[User continues working]

┌─ Forge Activity ────────────────────────────────────────────┐
│ ✓ Quality checks complete                      2.1s         │
│   • Formatting: passed                                      │
│   • Linting: passed                                         │
│   • Type checking: passed                                   │
│   • Tests: 124 passed                                       │
│   • Coverage: 82% → 85% (+3%)                               │
└─────────────────────────────────────────────────────────────┘
```

**Phase 2 Implementation:** Asynchronous (ANSI terminals only)

**During hook execution:**

```bash
[User typing...]

# Activity box appears in bottom-right corner (non-blocking)
                                  ┌─ Forge Activity ─────────┐
                                  │ ✓ Formatted      0.2s    │
                                  │ ✓ Linted         0.4s    │
                                  │ ✓ Type checked   0.8s    │
                                  │ 🔍 Running tests...       │
                                  └──────────────────────────┘

[User can continue typing, box updates in real-time]
```

**Feature Detection:**

```python
def supports_async_display() -> bool:
    """Check if terminal supports ANSI escape codes."""
    return (
        sys.stdout.isatty() and
        os.getenv('TERM') != 'dumb' and
        os.getenv('NO_COLOR') is None
    )

# Graceful degradation
if supports_async_display():
    start_async_activity_monitor()
else:
    use_synchronous_reporting()
```

### 4.5 Git Automation & Observability

**Principle:** Every git operation is observable, auditable, and reversible.

#### Commit Workflow

**User says:** "Ready to commit" or "Let's commit this"

**Orchestrator coordinates:**

```bash
Claude> Ready to commit this

╔══════════════════════════════════════════════════════════════╗
║  PRE-COMMIT QUALITY GATES                                    ║
╚══════════════════════════════════════════════════════════════╝

Running comprehensive checks...

✓ Code formatting (black, prettier)          0.3s
✓ Linting (ruff, eslint)                     0.8s
✓ Type checking (mypy, tsc)                  1.2s
✓ Security scan (bandit, npm audit)          0.9s
✓ Unit tests (987 tests)                     4.1s
✓ Integration tests (43 tests)               2.7s
✓ Coverage check (89% - above 85% minimum)   0.2s

╔══════════════════════════════════════════════════════════════╗
║  ✅ ALL QUALITY GATES PASSED                                  ║
╚══════════════════════════════════════════════════════════════╝

📝 Analyzing changes...
   Modified: 8 files
   Added: 147 lines
   Removed: 23 lines
   Tests added: 24 tests

🤖 Generated commit message:

   feat(auth): implement JWT-based authentication system

   - Add User model with password hashing (bcrypt)
   - Implement JWT token generation and validation
   - Create login/logout API endpoints
   - Add auth middleware for protected routes
   - Move secrets to environment variables
   - Add comprehensive unit tests (89% coverage)

   Closes #42

   🤖 Generated with NXTG-Forge
   Co-Authored-By: Forge Orchestrator <forge@nxtg.ai>

Accept this commit? [Y/n/edit]
```

**User accepts:**

```bash
Y

✓ Commit created: a7b9c3d
✓ Running post-commit hooks...
  • Documentation auto-updated
  • Changelog entry added
  • API docs regenerated

📊 Project Health Update
   Health Score: 78 → 84 (+6)
   Coverage: 82% → 89% (+7%)
   Tests: 963 → 987 (+24)

🔖 Checkpoint automatically created: cp_2026-01-08_1430
   Restore anytime with: /restore cp_2026-01-08_1430

Next steps:
  • Push to remote: git push
  • Create PR: forge pr create
  • Continue working: tell me what's next
```

#### PR Creation Workflow

**User says:** "Create a pull request" or "Let's make a PR"

**Orchestrator coordinates:**

```bash
Claude> Create a pull request

🔍 Analyzing branch commits...
   Branch: feature/auth-system
   Base: main
   Commits: 7
   Files changed: 23 (+847, -93)

📝 Generating PR description...

╔══════════════════════════════════════════════════════════════╗
║  PULL REQUEST PREVIEW                                        ║
╚══════════════════════════════════════════════════════════════╝

Title: Implement JWT-based authentication system

Description:
───────────────────────────────────────────────────────────────

## Summary

This PR implements a complete JWT-based authentication system with:
- User model with secure password hashing (bcrypt)
- JWT token generation and validation
- Login/logout API endpoints
- Auth middleware for route protection
- Environment-based configuration (no hardcoded secrets)

## Changes

### Database
- Add users table with email, hashed_password, created_at
- Add password hashing with bcrypt (cost factor: 12)

### API Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - Login with JWT token
- `POST /api/auth/logout` - Logout (token invalidation)
- `POST /api/auth/refresh` - Token refresh

### Middleware
- JWT validation middleware for protected routes
- Role-based access control (RBAC) foundation

### Security
- Secrets moved to environment variables
- Password strength validation
- Rate limiting on auth endpoints (10 requests/minute)
- JWT expiry (15 minutes access, 7 days refresh)

## Testing

89% test coverage

- Unit tests: 24 new tests
  - Password hashing/validation
  - JWT generation/validation
  - Middleware authorization

- Integration tests: 12 new tests
  - Full registration flow
  - Login/logout flow
  - Token refresh flow
  - Protected route access

All tests passing ✓

## Documentation

- API documentation updated with new endpoints
- Authentication guide added to docs/
- Environment variable documentation updated

## Closes

Closes #42

───────────────────────────────────────────────────────────────

Create this PR? [Y/n/edit]
```

**User accepts:**

```bash
Y

✓ Pushing branch to remote...
✓ Creating pull request...

📝 PULL REQUEST CREATED
   #127: Implement JWT-based authentication system

   Status: ✅ All checks passing
   • CI/CD pipeline: ✓ Passed (4m 32s)
   • Security scan: ✓ No issues
   • Code review bot: ✓ Approved (high quality)
   • Test coverage: ✓ 89% (above 85% threshold)

   Ready for human review

   🔍 View PR: https://github.com/company/api/pull/127

PR created successfully!

What would you like to do next?
  1. Continue working on this branch
  2. Start a new feature
  3. Return to main menu
```

#### Commit Message Format (Canonical)

**Convention:** Conventional Commits with Forge attribution

**Format:**

```
<type>(<scope>): <brief summary>

- Bullet point changes (what was done)
- More details (why it was done)
- Technical notes (how it was done)

<Footer: issue links, breaking changes>

🤖 Generated with NXTG-Forge
Co-Authored-By: Forge Orchestrator <forge@nxtg.ai>
```

**Examples:**

```
feat(auth): implement JWT-based authentication system

- Add User model with password hashing (bcrypt)
- Implement JWT token generation and validation
- Create login/logout API endpoints
- Add auth middleware for protected routes
- Move secrets to environment variables

Closes #42

🤖 Generated with NXTG-Forge
Co-Authored-By: Forge Orchestrator <forge@nxtg.ai>
```

```
fix(api): resolve SQL injection vulnerability in report generator

Security fix for parameterized queries in reports/generator.py

- Replace string concatenation with parameterized queries
- Add input validation for report parameters
- Add security test cases

BREAKING CHANGE: Report API now requires parameter validation

Closes #156

🤖 Generated with NXTG-Forge
Co-Authored-By: Forge Orchestrator <forge@nxtg.ai>
```

**Generation Logic:**

```python
def generate_commit_message(diff: str) -> str:
    """Generate conventional commit message from diff."""

    # Analyze diff to determine:
    # 1. Type (feat/fix/docs/test/refactor/etc)
    # 2. Scope (affected module)
    # 3. Summary (what changed)
    # 4. Details (bullet points of changes)
    # 5. Issue links (extract from branch name or recent commits)

    analysis = analyze_diff_with_llm(diff)

    return format_conventional_commit(
        type=analysis.type,
        scope=analysis.scope,
        summary=analysis.summary,
        details=analysis.details,
        closes=analysis.issue_numbers,
        breaking=analysis.has_breaking_changes
    )
```

### 4.6 Morning Reports

**Principle:** Complete confidence through comprehensive audit trail.

#### Morning Report Trigger

**Scenario:** Developer opens project after overnight session

```bash
$ cd my-awesome-app
$ claude

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ✅ NXTG-FORGE-ENABLED                                        ║
║                                                              ║
║     Your AI development infrastructure is active             ║
║     and watching your back.                                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

📊 Overnight Session Completed
   Feature: JWT Authentication
   Commits: 7 | Tests: +47 | PR: #127
   Status: ✅ Ready for review

   View full report? Type /report or press Enter to continue

Claude>
```

**User types `/report`:**

```bash
Claude> /report

╔══════════════════════════════════════════════════════════════╗
║  OVERNIGHT ACTIVITY REPORT                                   ║
║  Session: 2026-01-07 22:30 - 03:15                           ║
╚══════════════════════════════════════════════════════════════╝

📊 SESSION SUMMARY
   Duration: 4h 45m
   Commits: 7
   Files changed: 23 files (+847, -93)
   Tests added: 47 tests
   Coverage: 82% → 89% (+7%)

─────────────────────────────────────────────────────────────

🔗 GIT ACTIVITY
   Branch: feature/auth-system

   Commits:
   • a7b9c3d feat(auth): implement JWT authentication system
     2026-01-07 22:45

   • b2e4f1a feat(auth): add password hashing with bcrypt
     2026-01-07 23:15

   • c3f6g2b feat(auth): implement JWT token generation
     2026-01-08 00:30

   • d4h7j3c test(auth): add unit tests for auth service
     2026-01-08 01:15

   • e5k8m4d feat(auth): add login/logout endpoints
     2026-01-08 02:00

   • f6n9p5e feat(auth): add auth middleware
     2026-01-08 02:45

   • g7q0r6f docs(auth): add authentication guide
     2026-01-08 03:10

   🔍 View commits:
      https://github.com/company/api/commits/feature/auth-system

─────────────────────────────────────────────────────────────

📝 PULL REQUEST CREATED
   #127: Implement JWT-based authentication system

   Status: ✅ All checks passing
   • CI/CD pipeline: ✓ Passed (4m 32s)
   • Security scan: ✓ No issues found
   • Code review bot: ✓ Approved (high quality)
   • Test coverage: ✓ 89% (above 85% threshold)

   Ready for human review

   🔍 View PR: https://github.com/company/api/pull/127

─────────────────────────────────────────────────────────────

📈 QUALITY IMPROVEMENTS

   Health Score: 78 → 84 (+6 points)

   Test Coverage:
     Before: 82% (963 tests)
     After:  89% (987 tests)
     Change: +7% (+24 tests)

   Code Quality:
     • Linting: 0 errors (unchanged)
     • Type coverage: 91% → 94% (+3%)
     • Security issues: 0 (unchanged)

   Documentation:
     • API docs: Updated with 4 new endpoints
     • Auth guide: Added (docs/authentication.md)
     • README: Updated with auth setup

─────────────────────────────────────────────────────────────

🔖 CHECKPOINTS CREATED

   Three automatic checkpoints saved for easy rollback:

   1. cp_2026-01-07_2245
      "JWT model complete - all tests passing"
      Restore: /restore cp_2026-01-07_2245

   2. cp_2026-01-08_0130
      "Auth service with tests complete"
      Restore: /restore cp_2026-01-08_0130

   3. cp_2026-01-08_0315
      "Feature complete - PR created"
      Restore: /restore cp_2026-01-08_0315

─────────────────────────────────────────────────────────────

💡 RECOMMENDED NEXT STEPS

   1. Review PR #127
      Verify implementation meets requirements
      Check test coverage and edge cases

   2. Merge when approved
      All quality gates passed, safe to merge

   3. Deploy to staging
      Run: make deploy-staging
      Verify auth flow in staging environment

   4. Plan next feature
      Options:
      • Email verification for new users
      • Two-factor authentication
      • OAuth integration (Google, GitHub)

─────────────────────────────────────────────────────────────

📂 AUDIT TRAIL

   Complete session log saved:
   .claude/forge/sessions/session_20260107_223000.json

   All commits signed and traceable:
   git log --show-signature feature/auth-system

─────────────────────────────────────────────────────────────

Everything completed successfully. What would you like to do next?

Type /enable-forge to continue with orchestrator menu
```

**Report Generation:**

```python
# Triggered automatically on session end
def on_session_end(session_id: str):
    SessionReporter().generate_session_report(session_id)
    # Report saved to .claude/forge/sessions/<session_id>_report.txt

# On next session start
def on_session_start():
    if SessionReporter().should_display_report_on_startup():
        print("📊 Overnight Session Completed")
        print("   [Brief summary: 3 lines]")
        print("   View full report? Type /report or press Enter")
```

---

## Part 5: Visual Specifications

**Reference Documents:**

- `.asif/canonical-vision/VISUAL-MOCKUPS.md` (11 detailed mockups)
- `.asif/canonical-vision/CANONICAL-DESIGN-LANGUAGE.md` (typography, colors, spacing)

### Design Language (Canonical)

#### Typography

- **Headers:** Bold, uppercase for major sections
- **Body:** Regular weight, sentence case
- **Code:** Monospace font
- **Emphasis:** Italic for subtle emphasis, bold for strong

#### Colors (Terminal ANSI)

- ✅ **Success/Complete:** Green (ANSI 32)
- ⚠️  **Warning:** Yellow (ANSI 33)
- ❌ **Error:** Red (ANSI 31)
- 🔍 **Info/Analysis:** Blue (ANSI 34)
- ⏳ **Progress/In-progress:** Cyan (ANSI 36)
- 💡 **Recommendation:** White (ANSI 37)

#### Spacing

- **Minimum line height:** 1.0 (terminal default)
- **Section padding:** 1 blank line between sections
- **Major section padding:** 2 blank lines OR separator line
- **Separator:** `─────────────────────────────────────────────────────────────`

#### Box Drawing Characters

- **Single line borders:** `┌─┐ └─┘ │` for menus, lists, activity indicators
- **Double line borders:** `╔═╗ ╚═╝ ║` for major sections, headers
- **Principle:** Double line for important demarcation, single line for content organization

#### Icons (Emoji)

Standard icon set (copy exactly):

- ✓ Complete / Success
- ⏳ In progress / Loading
- ⏸ Pending / Paused
- ❌ Error / Failed
- ⚠️  Warning / Alert
- 💡 Recommendation / Idea
- 📊 Metrics / Stats
- 🔗 Link / URL
- 🎯 Goal / Target / Phase
- 🔍 Analysis / Search
- 📝 Documentation / Notes
- 🔒 Security
- 🧪 Testing
- 🏗️  Architecture
- 🔨 Implementation
- 🤖 AI Generated

### Mockup References

**All UX flows specified in:** `.asif/canonical-vision/VISUAL-MOCKUPS.md`

**Mockups include:**

1. First Contact: Forge enabled banner
2. First Contact: Forge ready banner
3. Activation Flow: Step-by-step indicators
4. Continue Mode: Context restoration with recommendations
5. Background Activity: Real-time status (Phase 2)
6. Quality Gate Alert: Interactive remediation
7. Commit Workflow: Quality gates + message generation
8. PR Creation: Analysis + description generation
9. Morning Report: Comprehensive session summary
10. Agent Handoff: Transparent coordination
11. Checkpoint Restore: Safety options

**Technical Notes on Mockups:**

- All mockups are CLI-compatible (no GUI elements)
- Progress bars removed in favor of step-by-step checkmarks (CLI constraint)
- Activity monitoring has Phase 1 (synchronous) and Phase 2 (async ANSI) specs
- All text can be rendered in terminal with standard ANSI escape codes

---

## Part 6: Implementation Roadmap

### Timeline Overview

**Total Duration:** 6-8 weeks

- **Week 1-2:** Foundation (agent system + basic UX)
- **Week 3-4:** Automation (git workflow + quality gates)
- **Week 5-6:** Observability (sessions + reports + checkpoints)
- **Week 7-8:** Intelligence (multi-agent coordination + polish)

**Confidence Level:** 95% (all technical challenges have validated solutions)

### Phase 1: Foundation (Week 1-2)

**Goal:** Core infrastructure + basic menu system

**Deliverables:**

1. **Hybrid Agent Architecture**
   - [ ] Five markdown agents in `.claude/agents/`
   - [ ] Orchestrator presents canonical 4-option menu
   - [ ] Agent handoff visibility (transparent but subtle)
   - [ ] Service invocation via `forge` CLI commands

2. **Core Services**
   - [ ] StateManager (session & feature state)
   - [ ] ContextRestorationService (Continue mode)
   - [ ] Basic QualityService (health calculation)

3. **Status Indicator System**
   - [ ] Detection logic (FORGE-ENABLED vs READY)
   - [ ] Banner display on session start
   - [ ] Hook: `on-session-start.sh`

4. **Activation Flow**
   - [ ] `/enable-forge` command
   - [ ] Step-by-step activation indicators
   - [ ] Menu presentation after activation

**Success Criteria:**

- User sees "✅ NXTG-FORGE-ENABLED" on project open
- `/enable-forge` displays canonical menu
- Choosing option 1 (Continue) restores context
- Choosing option 4 (Health) shows project status

**Testing:**

- Unit tests for ContextRestorationService
- Integration test: full activation flow
- UX validation: menu comprehension (3-5 developers)

### Phase 2: Automation (Week 3-4)

**Goal:** Git workflow + quality gates + activity monitoring

**Deliverables:**

1. **Git Automation**
   - [ ] GitService (branch, commit, PR operations)
   - [ ] Commit message generation (conventional commits)
   - [ ] PR description generation
   - [ ] Integration with `gh` CLI

2. **Quality Gates**
   - [ ] QualityService (comprehensive checks)
   - [ ] QualityAlerter (interactive warnings)
   - [ ] Hooks: `pre-task.sh`, `post-task.sh`
   - [ ] Hook: `on-file-change.sh`

3. **Activity Monitoring (Phase 1)**
   - [ ] ActivityReporter (synchronous mode)
   - [ ] Activity status file mechanism
   - [ ] Display after hook completion

4. **Recommendation Engine**
   - [ ] Static analysis patterns (security, quality)
   - [ ] AI-powered code review integration
   - [ ] Priority scoring

**Success Criteria:**

- Orchestrator can create commits automatically with perfect messages
- Quality checks run after each task (non-blocking)
- User sees "✓ Tests passed (4.1s)" after operations
- Security issues surfaced interactively with remediation options

**Testing:**

- Unit tests for GitService, QualityService, RecommendationEngine
- Integration test: full commit workflow
- Integration test: PR creation workflow
- Security test: detect common vulnerabilities

### Phase 3: Observability (Week 5-6)

**Goal:** Session management + reports + checkpoints

**Deliverables:**

1. **Session Persistence**
   - [ ] Session tracking (start, update, end)
   - [ ] Session logs with full metadata
   - [ ] Hook: `state-sync.sh` (periodic saves)

2. **Report Generation**
   - [ ] SessionReporter service
   - [ ] Morning report format (designer's spec)
   - [ ] Git activity with GitHub links
   - [ ] Quality delta calculations
   - [ ] Next steps recommendations

3. **Checkpoint System**
   - [ ] Checkpoint creation (git tags + metadata)
   - [ ] Checkpoint listing
   - [ ] Checkpoint restoration with safety options
   - [ ] `/restore` command

4. **Error Recovery**
   - [ ] Hook: `on-error.sh`
   - [ ] Auto-checkpoint before recovery
   - [ ] Recovery recommendations

**Success Criteria:**

- User returns next day, sees comprehensive overnight report
- All git commits have clickable GitHub links in report
- `/restore cp_2026-01-08_1430` works with safety prompts
- Error recovery creates checkpoint automatically

**Testing:**

- Unit tests for SessionReporter, CheckpointManager
- Integration test: full session lifecycle
- Integration test: checkpoint creation and restoration
- Manual test: morning report usefulness (3-5 developers)

### Phase 4: Intelligence (Week 7-8)

**Goal:** Multi-agent coordination + complete UX polish

**Deliverables:**

1. **Agent Collaboration**
   - [ ] Orchestrator → Architect handoff
   - [ ] Architect → Backend handoff
   - [ ] Backend → QA handoff
   - [ ] Context passing between agents
   - [ ] Task decomposition with dependencies

2. **Plan Mode (Complete)**
   - [ ] Interactive requirements gathering
   - [ ] Architecture design workflow
   - [ ] Task breakdown with estimates
   - [ ] Implementation orchestration

3. **Soundboard Mode (Complete)**
   - [ ] Project analysis
   - [ ] Strategic recommendations
   - [ ] Architecture advice
   - [ ] Refactoring suggestions

4. **Activity Monitoring (Phase 2)**
   - [ ] Asynchronous display (ANSI terminals)
   - [ ] Terminal compatibility detection
   - [ ] Fallback to Phase 1 mode

5. **Polish**
   - [ ] Visual consistency pass
   - [ ] Spacing and alignment
   - [ ] Celebration moments
   - [ ] Accessibility considerations

**Success Criteria:**

- User chooses "2. Plan", gets full feature planning wizard
- Orchestrator successfully coordinates 3+ agents
- Feature implemented end-to-end with tests
- Background activity box appears (on compatible terminals)
- All UX flows match mockups exactly

**Testing:**

- Integration test: full Plan mode workflow
- Integration test: multi-agent coordination
- UX validation: complete flows (5-10 developers)
- Accessibility test: screen reader compatibility
- Performance test: activity monitoring overhead

### Phase 5: Documentation & Launch (Week 9-10)

**Goal:** Production-ready documentation + migration guides

**Deliverables:**

1. **Documentation**
   - [ ] User guide (getting started, workflows)
   - [ ] Architecture documentation
   - [ ] ADR documentation
   - [ ] API documentation (services)
   - [ ] UX design language guide

2. **Migration**
   - [ ] v3 → v4 migration guide
   - [ ] Automated migration tool
   - [ ] Migration validation

3. **Examples**
   - [ ] Sample projects with forge enabled
   - [ ] Video tutorials
   - [ ] Best practices guide

4. **Launch**
   - [ ] Beta release (select users)
   - [ ] Feedback collection
   - [ ] Bug fixes
   - [ ] Public release

**Success Criteria:**

- New user can get started in <10 minutes
- Existing v3 user can migrate in <30 minutes
- All documentation is accurate and complete
- Beta users report 90%+ satisfaction

---

## Part 7: Architectural Decision Records

### ADR-001: Native Agent Integration

**Status:** Accepted

**Context:** NXTG-Forge v3 has agents as Python code (`forge/agents/`) separate from Claude Code's native agent system (`.claude/agents/`). This creates redundancy and friction.

**Decision:** Agents will be native Claude Code markdown files in `.claude/agents/`. Complex logic delegated to Python services.

**Consequences:**

- ✅ Native to Claude Code (discoverable, customizable)
- ✅ Simpler architecture (less Python code)
- ✅ Easier for users to understand and modify
- ⚠️ Orchestration logic must be in prompts (less programmatic control)
- ⚠️ Service invocation via CLI commands (clear interface, some overhead)

**Alternatives Considered:**

- Pure Python orchestration (rejected: not native to Claude)
- Pure markdown with no services (rejected: too limited for complex logic)
- **Hybrid approach (CHOSEN):** Markdown agents + Python services

### ADR-002: Namespace Isolation

**Status:** Accepted

**Context:** Multiple Claude Code projects might have forge installed. Need to avoid conflicts.

**Decision:** All forge artifacts use `agent-forge-*` prefix. All forge data in `.claude/forge/` subdirectory.

**Consequences:**

- ✅ No naming conflicts with user's own agents
- ✅ Clear ownership (forge vs. user)
- ✅ Easy to identify forge components
- ⚠️ Longer names (acceptable trade-off)

### ADR-003: Activation Model

**Status:** Accepted

**Context:** Should forge be always-on or opt-in per session?

**Decision:** Forge is "installed" (agents present) but "opt-in activated" per session via `/enable-forge`.

**Rationale:**

- Developer may want Claude without orchestrator (manual control)
- Explicit activation gives sense of control
- Status indicator provides immediate recognition
- Easy to disable: just don't run `/enable-forge`

**Consequences:**

- ✅ Developer maintains control
- ✅ Clear distinction: forge present vs. forge active
- ✅ No surprise automation
- ⚠️ Extra step to activate (acceptable: 2 seconds)

### ADR-004: State Management Strategy

**Status:** Accepted

**Context:** How to persist state across sessions?

**Decision:** Git is source of truth. State files (`.claude/forge/state.json`) are caches/indexes for performance.

**Rationale:**

- Git already tracks all code changes
- State files enable fast context restoration
- If state file lost, can rebuild from git history
- Checkpoints are git tags (permanent, traceable)

**Consequences:**

- ✅ No proprietary formats
- ✅ State is auditable (git log)
- ✅ Easy backup (git push)
- ⚠️ Must keep state file in sync with git (solved: state-sync.sh hook)

### ADR-005: Hooks as Automation Backbone

**Status:** Accepted

**Context:** How to implement continuous quality enforcement?

**Decision:** Use Claude Code's native hook system (`.claude/hooks/`) for all automation.

**Types:**

- `pre-task.sh`: Precondition validation
- `post-task.sh`: Quality enforcement
- `on-error.sh`: Error recovery
- `on-file-change.sh`: Continuous validation
- `state-sync.sh`: State persistence

**Principle:** Hooks are **guardrails, not gates**. They provide warnings and enforce quality but never block progress.

**Consequences:**

- ✅ Native to Claude Code
- ✅ Language-agnostic (bash scripts)
- ✅ Non-interactive (run in background)
- ✅ Composable (can chain hooks)
- ⚠️ Limited error handling in bash (acceptable: hooks don't do complex logic)

### ADR-006: Hybrid Agent Model (NEW)

**Status:** Accepted

**Context:** Gap identified during alignment review. Two approaches to agent architecture:

- Architect's vision: Agents as native markdown files
- Designer's assumption: Python orchestration with prompt integration

**Decision:** Hybrid model combining best of both approaches.

**Architecture:**

```
Agents (Markdown) → High-level coordination, natural language
    ↓ (invoke via CLI)
Services (Python) → Complex logic, type-safe computation
```

**Example:**

```markdown
# In agent-forge-orchestrator.md

User chose "Continue" mode. Let me restore context:

[Bash command in backticks]
`context_json=$(forge context restore --format=json)`

Based on this context: {context_json}

Here's what we were working on...
```

**Rationale:**

- Markdown agents feel native to Claude Code
- Python services provide type safety and testability
- Clear separation: coordination (markdown) vs computation (Python)
- Easy to extend: add agents (markdown) or services (Python) independently

**Consequences:**

- ✅ Native Claude integration (markdown agents)
- ✅ Type-safe business logic (Python services)
- ✅ Clear interface (CLI commands)
- ✅ Easy to test (unit test services, integration test agents)
- ⚠️ Services must have CLI interface (adds some boilerplate)
- ⚠️ JSON serialization required for data passing (acceptable overhead)

**Implementation:**

```python
# forge/cli.py
@cli.command()
def context_restore():
    """Restore Continue mode context (JSON output)."""
    service = ContextRestorationService()
    context = service.restore_context()
    print(json.dumps(context.to_dict()))

# Agent invokes: forge context restore --format=json
# Agent receives: {"last_session_time": "...", "progress": 67, ...}
# Agent formats and presents to user
```

---

## Part 8: Success Metrics

### Developer Empowerment Metrics

**Primary Goal:** Transform exhausted developers into empowered creators

**Measurements:**

1. **Emotional Impact**
   - Time to first "wow" moment: <60 seconds (status indicator)
   - Self-reported confidence level: >8/10 after using forge
   - Self-reported stress level: Reduced by >30%
   - Would recommend to colleague: >90% yes

2. **Productivity Impact**
   - Context restoration time: <10 seconds (vs. 5-15 minutes manual)
   - Commit message quality: 100% conventional format
   - Test coverage: Average >85% (enforced by quality gates)
   - PR review time: Reduced by 40% (comprehensive descriptions)

3. **Quality Impact**
   - Code quality score: Average >80/100
   - Security vulnerabilities: Caught before commit (>95%)
   - Documentation coverage: >80% (auto-generated)
   - Build failures: Reduced by 60% (pre-commit gates)

4. **Adoption Metrics**
   - Setup time: <10 minutes (from install to first orchestrator use)
   - Daily active use: >60% of development time
   - Feature usage: All 4 menu options used within first week
   - Retention: >80% still using after 30 days

### Technical Excellence Metrics

**Goal:** Validate architectural decisions

1. **Performance**
   - Status indicator display: <500ms
   - Context restoration: <3 seconds
   - Quality checks: <10 seconds for typical project
   - Session report generation: <5 seconds

2. **Reliability**
   - Hook execution success rate: >99%
   - State consistency: 100% (state matches git)
   - Checkpoint restoration success: 100%
   - Error recovery success: >95%

3. **Maintainability**
   - Test coverage: >85% for all services
   - Documentation coverage: 100% for public APIs
   - Code complexity: Average <10 cyclomatic complexity
   - Type coverage: >90% (Python services)

### User Experience Metrics

**Goal:** Validate UX design decisions

1. **Clarity**
   - Menu comprehension: >95% understand all 4 options
   - Agent handoff visibility: >90% report trust increased
   - Activity monitoring: >80% find it helpful (not distracting)
   - Morning report usefulness: >85% read full report

2. **Efficiency**
   - Keystrokes to activate: 13 (`/enable-forge` + Enter)
   - Choices to start Continue mode: 1 (type `1` + Enter)
   - Time to first meaningful action: <20 seconds
   - Context switches: Reduced by >70% (forge handles details)

3. **Delight**
   - "Magical" automation feedback: >80% positive
   - Celebration moments noticed: >60%
   - Visual polish appreciated: >75%
   - Would miss if removed: >90% yes

---

## Part 9: Migration Path

### From v3 to v4 (Unified Vision)

**Philosophy:** Incremental migration, zero downtime, reversible at any point.

#### Step 1: Install v4 Alongside v3

```bash
# Backup current setup
cp -r .claude .claude.v3.backup
cp -r forge forge.v3.backup

# Install v4
pip install nxtg-forge==4.0.0

# Initialize v4 (does not affect v3)
forge init --version=4.0

# v3 and v4 now coexist
```

#### Step 2: Gradual Feature Migration

**Week 1: Test v4 status indicator**

```bash
# v4 status works immediately
cd your-project
claude
# See "✅ NXTG-FORGE-ENABLED" banner

# v3 still works
forge status  # v3 command
```

**Week 2: Test v4 orchestrator**

```bash
# Try v4 orchestrator
/enable-forge  # v4 command

# Can still use v3
forge feature "New feature"  # v3 command
```

**Week 3: Test v4 git automation**

```bash
# Use v4 commit workflow
[Work on feature]
"Ready to commit"  # v4 handles it

# Quality gates run automatically (v4)
```

**Week 4: Full v4 adoption**

```bash
# Remove v3 commands
forge migrate finalize

# v4 is now primary
```

#### Step 3: State Migration

**Automatic migration on first v4 activation:**

```python
def migrate_state_v3_to_v4():
    """Migrate v3 state to v4 format."""

    # Read v3 state
    v3_state = json.loads(Path(".forge/state.json").read_text())

    # Transform to v4 format
    v4_state = {
        "project": {
            "name": v3_state["project"]["name"],
            "tech_stack": detect_tech_stack(),  # Enhanced in v4
            "health_score": calculate_health_score(),  # New in v4
            "coverage": v3_state["quality"]["coverage"]
        },
        "features": [
            transform_feature_v3_to_v4(f)
            for f in v3_state["features"]
        ],
        "last_session": None  # Will be set on first v4 session
    }

    # Write v4 state
    Path(".claude/forge/state.json").write_text(json.dumps(v4_state))

    # Keep v3 state as backup
    Path(".claude/forge/state.v3.json").write_text(json.dumps(v3_state))
```

#### Step 4: Rollback (If Needed)

**V4 doesn't work? Rollback to v3 instantly:**

```bash
# Disable v4
forge disable

# Restore v3
cp -r .claude.v3.backup .claude
cp -r forge.v3.backup forge

# Uninstall v4
pip uninstall nxtg-forge
pip install nxtg-forge==3.0.0

# Back to v3, zero data loss
```

---

## Part 10: Risk Mitigation

### Identified Risks & Mitigations

#### Risk 1: Claude Code Hook Compatibility

**Risk:** Hooks may not work as expected in all Claude Code versions

**Mitigation:**

- Test on Claude Code versions: latest, latest-1, latest-2
- Document minimum required version
- Graceful degradation if hooks not supported
- Fallback to manual commands

**Contingency:** If hooks don't work, forge commands still work manually

#### Risk 2: Terminal Compatibility (Activity Monitoring)

**Risk:** ANSI escape codes may not work in all terminals

**Mitigation:**

- Implement Phase 1 (synchronous) first (works everywhere)
- Phase 2 (asynchronous ANSI) is optional enhancement
- Feature detection: `supports_async_display()`
- Clear documentation of terminal requirements

**Contingency:** Phase 1 provides 90% of value without ANSI

#### Risk 3: Git Workflow Interruptions

**Risk:** Automated commits might commit unwanted changes

**Mitigation:**

- Always show commit preview with diff summary
- Require explicit approval (`[Y/n/edit]`)
- Quality gates catch obvious mistakes
- Checkpoints enable easy rollback

**Contingency:** User can always `git reset` or `/restore checkpoint`

#### Risk 4: Agent Orchestration Complexity

**Risk:** Orchestrator prompt becomes too large (>1000 lines)

**Mitigation:**

- Modular prompt structure (include sub-prompts)
- Regular refactoring (keep orchestrator focused)
- Delegate complex logic to services (not prompt)
- Version control for prompts (track growth)

**Contingency:** Split orchestrator into specialized sub-orchestrators if needed

#### Risk 5: Performance Overhead

**Risk:** Quality checks slow down development

**Mitigation:**

- Hooks run asynchronously (non-blocking)
- Incremental checks on file change (not full suite)
- Full checks only on commit (when user expects wait)
- Configurable check levels (fast vs comprehensive)

**Contingency:** User can disable specific checks if too slow

---

## Part 11: Open Questions & Future Enhancements

### Resolved Questions

**Q1: What is the canonical menu?**
**A:** 4 options exactly: Continue, Plan, Soundboard, Health. No variations.

**Q2: How are agent handoffs shown to user?**
**A:** Transparent but subtle: `🎯 [Phase] (agent: name)` ... `✓ [Phase] complete`

**Q3: How does Continue mode restore context?**
**A:** ContextRestorationService reads state.json, analyzes git, scans recent files, generates recommendations via RecommendationEngine.

**Q4: How are background activities reported?**
**A:** Phase 1 (synchronous): show after completion. Phase 2 (async): ANSI box in corner (optional).

**Q5: When is morning report displayed?**
**A:** Brief summary on session start + full report via `/report` command.

### Future Enhancements (Post-Launch)

**Enhancement 1: AI-Powered Code Review**

- Orchestrator analyzes PR diffs and provides review comments
- Integration with GitHub code review API
- Suggests improvements before human review

**Enhancement 2: Cross-Project Learning**

- Forge learns from patterns across multiple projects
- Suggests architecture patterns used successfully elsewhere
- Identifies anti-patterns to avoid

**Enhancement 3: Team Collaboration**

- Forge sessions synchronized across team
- Shared checkpoint library
- Collaborative planning sessions

**Enhancement 4: Custom Agent Creation**

- User-defined specialist agents
- Agent marketplace
- Domain-specific agent templates

**Enhancement 5: Performance Profiling**

- Automatic performance regression detection
- Optimization recommendations
- Benchmark tracking over time

---

## Conclusion

### The Unified Vision

We have successfully merged two independent visions into a single canonical specification:

**From Architect:** Technical excellence, clean architecture, type safety, native integration

**From Designer:** Emotional journey, zero cognitive load, complete transparency, delightful automation

**Result:** A system that is both technically sound AND emotionally transformative.

### What Makes This Vision Canonical

1. **Single Source of Truth:** This document supersedes all previous vision documents
2. **Complete Specification:** Every component, service, flow, and UX detail specified
3. **Gap Resolution:** All 5 identified gaps filled (ContextRestoration, ActivityReporter, SessionReporter, QualityAlerter, RecommendationEngine)
4. **Alignment Confirmation:** 85% → 100% alignment achieved
5. **Implementation Ready:** 95% confidence, clear roadmap, validated technical approach

### Implementation Readiness

**Technical:** ✅ All challenges have solutions
**UX:** ✅ All flows specified with mockups
**Architecture:** ✅ Hybrid model validated
**Timeline:** ✅ 6-8 weeks realistic
**Risk:** ✅ All major risks mitigated

### The Transformation Promise

**Before Forge:**

- Exhausted developer, 2:47 AM, 5 projects, drowning in context switching
- Fear of breaking things, imposter syndrome, cognitive overload

**After Forge:**

- Empowered developer, confident, in control
- "I'm no longer alone. I have intelligent backup."
- "I can concentrate on solving problems. The system catches what I miss."
- "I know exactly what happened. I trust this work. I'm powerful."

**This is not about automation. This is about transformation.**

---

**Document Status:** UNIFIED CANONICAL VISION - APPROVED FOR IMPLEMENTATION

**Next Steps:**

1. Architecture team: Begin Phase 1 implementation
2. Design team: Finalize visual mockups for all flows
3. Product team: Prepare beta user recruitment
4. Documentation team: Start user guide based on this spec

**The code already works. The architecture is elegant. Now we make developers fall in love with using it.**

---

**End of Unified Canonical Vision**

Version: 2.0.0
Date: 2026-01-08
Authors: Master Software Architect + Design Vanguard
Status: CANONICAL - Single Source of Truth
