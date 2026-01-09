# CANONICAL FORGE ARCHITECTURE - Visual Diagrams

**Visual representation of NXTG-Forge 2.0 architecture**

---

## The Transformation: v3 → 2.0

### Current State (v3) - Split Brain Architecture ❌

```
┌─────────────────────────────────────────────────────────────┐
│                    User Project                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  forge/ (Python Package)                                    │
│  ├── agents/                    ← ORCHESTRATION LOGIC       │
│  │   ├── orchestrator.py (705 lines)  ← GOD CLASS          │
│  │   ├── dispatcher.py                                      │
│  │   ├── selection/              ← AGENT SELECTION          │
│  │   ├── execution/              ← EXECUTORS                │
│  │   ├── services/               ← INFRASTRUCTURE           │
│  │   └── domain/                 ← DOMAIN MODELS            │
│  │                                                           │
│  ├── cli.py (746 lines)          ← MASSIVE CLI              │
│  ├── state_manager.py                                       │
│  └── [other modules]                                        │
│                                                              │
│  .claude/ (Claude Code Native)                             │
│  ├── agents/                     ← EMPTY! ❌                │
│  ├── commands/                   ← Commands (good) ✓        │
│  │   ├── feature.md                                         │
│  │   ├── status.md                                          │
│  │   └── [10 more]                                          │
│  ├── hooks/                      ← Hooks (good) ✓           │
│  └── skills/agents/              ← Agent docs (markdown)    │
│      ├── lead-architect.md       ← SPLIT FROM LOGIC! ❌     │
│      └── [5 more agent docs]                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘

PROBLEM: Agents are Python code (forge/agents/) but definitions
         are markdown (.claude/skills/agents/). SPLIT BRAIN!
```

### Canonical State (2.0) - Native Integration ✅

```
┌─────────────────────────────────────────────────────────────┐
│                    User Project                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  .claude/ (Claude Code Native) ← EVERYTHING HERE!          │
│  ├── agents/                     ← ALL FORGE AGENTS ✓       │
│  │   ├── agent-forge-orchestrator.md  ← COORDINATOR         │
│  │   ├── agent-forge-architect.md     ← DESIGN              │
│  │   ├── agent-forge-backend.md       ← IMPLEMENTATION      │
│  │   ├── agent-forge-qa.md            ← TESTING             │
│  │   └── agent-forge-integration.md   ← EXTERNAL SERVICES   │
│  │                                                           │
│  ├── commands/                   ← Slash commands ✓         │
│  │   ├── enable-forge.md         ← SIMPLE ACTIVATION        │
│  │   ├── feature.md                                         │
│  │   └── [10 more]                                          │
│  │                                                           │
│  ├── hooks/                      ← Automation ✓             │
│  │   ├── pre-task.sh                                        │
│  │   ├── post-task.sh                                       │
│  │   └── [3 more]                                           │
│  │                                                           │
│  ├── forge/                      ← Project data             │
│  │   ├── config.yml                                         │
│  │   ├── state.json                                         │
│  │   ├── sessions/                                          │
│  │   └── checkpoints/                                       │
│  │                                                           │
│  └── FORGE-ENABLED               ← Marker file              │
│                                                              │
│  forge/ (Python Package) ← INFRASTRUCTURE ONLY              │
│  ├── domain/                     ← Domain models            │
│  ├── services/                   ← State, git, quality      │
│  │   ├── state_manager.py        ← State operations         │
│  │   ├── git_service.py          ← Git operations           │
│  │   ├── quality_service.py      ← Quality checks           │
│  │   └── [more services]                                    │
│  ├── utils/                      ← Utilities                │
│  │   ├── result.py               ← Result types             │
│  │   └── [more utils]                                       │
│  └── cli.py                      ← CLI entry point          │
│                                                              │
└─────────────────────────────────────────────────────────────┘

SOLUTION: Agents are native Claude Code agents (.claude/agents/)
          Python provides infrastructure services only.
```

---

## Agent Collaboration Architecture

### How Agents Coordinate (2.0)

```
                    ╔═══════════════════════════════╗
                    ║   User Types: /enable-forge   ║
                    ╚═══════════════════════════════╝
                                  ↓
         ┌────────────────────────────────────────────┐
         │  .claude/agents/agent-forge-orchestrator.md│
         │                                             │
         │  • Analyzes request                        │
         │  • Decomposes into tasks                   │
         │  • Selects appropriate agents              │
         │  • Coordinates execution                   │
         │  • Tracks progress via forge CLI           │
         │  • Ensures quality standards               │
         └────────────────────────────────────────────┘
                                  ↓
        ┌──────────────┬──────────┴───────────┬────────────┐
        ↓              ↓                      ↓            ↓
┌──────────────┐ ┌──────────────┐  ┌──────────────┐ ┌─────────────┐
│agent-forge-  │ │agent-forge-  │  │agent-forge-  │ │agent-forge- │
│architect.md  │ │backend.md    │  │qa.md         │ │integration  │
│              │ │              │  │              │ │.md          │
│• Design      │ │• Implement   │  │• Test        │ │• Integrate  │
│• Data models │ │• Code        │  │• Quality     │ │• External   │
│• API specs   │ │• Database    │  │• Security    │ │  APIs       │
└──────────────┘ └──────────────┘  └──────────────┘ └─────────────┘
        ↓              ↓                      ↓            ↓
        └──────────────┴──────────────────────┴────────────┘
                                  ↓
                    ╔═══════════════════════════════╗
                    ║    Python Infrastructure      ║
                    ╠═══════════════════════════════╣
                    ║ forge CLI                     ║
                    ║   ↓                           ║
                    ║ services/                     ║
                    ║   • state_manager.py          ║
                    ║   • git_service.py            ║
                    ║   • quality_service.py        ║
                    ║   ↓                           ║
                    ║ .claude/forge/state.json      ║
                    ╚═══════════════════════════════╝
                                  ↓
                    ╔═══════════════════════════════╗
                    ║         Hooks (Auto)          ║
                    ╠═══════════════════════════════╣
                    ║ post-task.sh                  ║
                    ║   • Run tests                 ║
                    ║   • Check coverage            ║
                    ║   • Lint code                 ║
                    ║   • Security scan             ║
                    ║   • Update metrics            ║
                    ╚═══════════════════════════════╝
                                  ↓
                    ╔═══════════════════════════════╗
                    ║      Git Workflow (Auto)      ║
                    ╠═══════════════════════════════╣
                    ║ • Create branch               ║
                    ║ • Commit with messages        ║
                    ║ • Create PR                   ║
                    ║ • Complete audit trail        ║
                    ╚═══════════════════════════════╝
```

---

## Data Flow Architecture

### State Management Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Agent (Markdown)                          │
│              agent-forge-orchestrator.md                     │
│                                                              │
│  Decision: Feature implementation complete                  │
│  Action: Update state to mark feature done                  │
└─────────────────────────────────────────────────────────────┘
                              ↓ Invokes
┌─────────────────────────────────────────────────────────────┐
│                     forge CLI Command                        │
│                                                              │
│  $ forge state update-feature \                             │
│      --id "feat-123" \                                      │
│      --status "completed"                                    │
│                                                              │
│  • Parses arguments                                         │
│  • Validates input                                          │
│  • Calls Python service                                     │
└─────────────────────────────────────────────────────────────┘
                              ↓ Uses
┌─────────────────────────────────────────────────────────────┐
│              Python Service (Type-Safe)                      │
│                forge/services/state_manager.py              │
│                                                              │
│  def update_feature(id: str, status: str) -> Result[...]:  │
│      # Validate feature exists                              │
│      # Update feature status                                │
│      # Save to state.json                                   │
│      # Create backup                                        │
│      # Return Result (success/error)                        │
└─────────────────────────────────────────────────────────────┘
                              ↓ Reads/Writes
┌─────────────────────────────────────────────────────────────┐
│                  State File (JSON)                           │
│              .claude/forge/state.json                       │
│                                                              │
│  {                                                          │
│    "features": [                                            │
│      {                                                      │
│        "id": "feat-123",                                    │
│        "name": "Payment Processing",                        │
│        "status": "completed",  ← Updated!                   │
│        "completed_at": "2026-01-08T14:30:22Z"              │
│      }                                                      │
│    ]                                                        │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
                              ↓ Triggers
┌─────────────────────────────────────────────────────────────┐
│                   Hooks (Automatic)                          │
│                .claude/hooks/state-sync.sh                  │
│                                                              │
│  • Backup state.json                                        │
│  • Create checkpoint                                        │
│  • Update metrics                                           │
│  • Calculate health score                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Hook Automation Flow

### The Continuous Quality Loop

```
┌──────────────────────────────────────────────────────────────┐
│                  Developer Works with Claude                  │
│                                                               │
│  User: "Add payment processing"                              │
│  Claude (orchestrator): [Coordinates implementation]         │
└──────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────┐
│                    File Changes Occur                         │
│                                                               │
│  • payment/models.py created                                 │
│  • payment/service.py created                                │
│  • tests/test_payment.py created                             │
└──────────────────────────────────────────────────────────────┘
                                ↓ Triggers
┌──────────────────────────────────────────────────────────────┐
│            .claude/hooks/on-file-change.sh                   │
│                                                               │
│  FOR EACH changed file:                                      │
│    IF .py file:                                              │
│      • Run black (auto-format)                               │
│      • Check syntax                                          │
│    IF .json/.yml file:                                       │
│      • Validate syntax                                       │
│    IF test file:                                             │
│      • Suggest running tests                                 │
└──────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────┐
│                    Task Completes                             │
│                                                               │
│  Orchestrator: Implementation phase complete                 │
└──────────────────────────────────────────────────────────────┘
                                ↓ Triggers
┌──────────────────────────────────────────────────────────────┐
│              .claude/hooks/post-task.sh                      │
│                                                               │
│  1. Run full test suite                                      │
│     $ pytest --quiet                                         │
│                                                               │
│  2. Check coverage                                           │
│     $ coverage report                                        │
│                                                               │
│  3. Lint all code                                            │
│     $ ruff check .                                           │
│                                                               │
│  4. Security scan                                            │
│     $ bandit -r .                                            │
│                                                               │
│  5. Update state.json                                        │
│     $ forge state update-quality \                           │
│         --tests "passing" \                                  │
│         --coverage "94%" \                                   │
│         --linting "0 issues"                                 │
│                                                               │
│  6. Report results                                           │
│     ✅ All quality checks passed!                            │
│     💡 Next: Create PR with forge git create-pr              │
└──────────────────────────────────────────────────────────────┘
                                ↓ If quality passes
┌──────────────────────────────────────────────────────────────┐
│                   Git Workflow                                │
│                                                               │
│  Orchestrator decides to create PR                           │
│    ↓                                                          │
│  $ forge git create-branch --feature "payment-processing"    │
│  $ forge git commit --message "feat: add Stripe integration" │
│  $ forge git create-pr --title "Payment Processing"          │
└──────────────────────────────────────────────────────────────┘
                                ↓ Triggers
┌──────────────────────────────────────────────────────────────┐
│            .claude/hooks/state-sync.sh                       │
│                                                               │
│  • Backup state.json                                         │
│  • Create checkpoint: "payment-processing-complete"          │
│  • Update project health score                               │
│  • Log session completion                                    │
└──────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────┐
│                  Developer Receives                           │
│                                                               │
│  ✅ Feature Complete: Payment Processing                     │
│                                                               │
│  • PR: #145 (ready for review)                              │
│  • Tests: 24 new tests, all passing                         │
│  • Coverage: 94%                                             │
│  • Quality: All checks passed ✓                             │
│  • Checkpoint: payment-processing-complete                   │
│                                                               │
│  Next: Review PR and merge                                   │
└──────────────────────────────────────────────────────────────┘
```

---

## Developer Experience Flow

### From Installation to Feature Delivery

```
╔══════════════════════════════════════════════════════════════╗
║                    PHASE 1: Installation                      ║
╚══════════════════════════════════════════════════════════════╝

Developer's Terminal:
  $ pip install nxtg-forge
  $ cd ~/my-project
  $ forge init

NXTG-Forge:
  ✓ Analyzing project (Python, FastAPI, PostgreSQL)
  ✓ Creating .claude/agents/ (5 agents)
  ✓ Creating .claude/commands/ (12 commands)
  ✓ Creating .claude/hooks/ (5 hooks)
  ✓ Creating .claude/forge/config.yml
  ✓ Creating .claude/forge/state.json

  ✅ NXTG-Forge initialized!

  Next: claude (then /enable-forge)

Time: 30 seconds
─────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════╗
║                    PHASE 2: First Use                         ║
╚══════════════════════════════════════════════════════════════╝

Developer Opens Project:
  $ claude

Claude Shows:
  ✨ NXTG-FORGE-READY

  Project: my-project (Python API)
  Health: 87/100 ✓

  Commands:
    /enable-forge  - Start orchestrator
    /status        - Project status
    /feature       - Quick feature

  What would you like to work on?

Developer Types:
  /enable-forge

Time: < 2 seconds
─────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════╗
║                 PHASE 3: Feature Request                      ║
╚══════════════════════════════════════════════════════════════╝

Orchestrator Menu:
  ╔═══════════════════════════════════════════════════════════╗
  ║            NXTG-Forge Orchestrator v2.0                   ║
  ╚═══════════════════════════════════════════════════════════╝

  What would you like to do?

    1. [Continue] Resume previous work
    2. [New Feature] Plan and implement new feature  ← Developer chooses
    3. [Soundboard] Discuss current state
    4. [Status] View project status

Developer Input:
  Choice: 2
  Feature: "Add payment processing with Stripe"

Orchestrator:
  [Asks 3 clarifying questions]
  [Presents implementation plan]
  [Gets approval]

Time: 2 minutes (interactive planning)
─────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════╗
║              PHASE 4: Automated Implementation                ║
╚══════════════════════════════════════════════════════════════╝

Orchestrator Coordinates:

  [Checkpoint: before-stripe-integration]

  Phase 1: Architecture (agent-forge-architect)
    ✓ Domain models designed
    ✓ API contracts specified
    ✓ Database schema defined

  Phase 2: Implementation (agent-forge-backend)
    ✓ Payment models created
    ✓ Stripe service implemented
    ✓ Webhook handlers added
    ✓ Database migrations generated

    [Hook: on-file-change.sh]
      ✓ Auto-formatted 8 Python files
      ✓ No syntax errors

  Phase 3: Testing (agent-forge-qa)
    ✓ 18 unit tests created
    ✓ 8 integration tests created
    ✓ 6 webhook tests created
    ✓ All tests passing

    [Hook: post-task.sh]
      ✓ Coverage: 94%
      ✓ Linting: 0 issues
      ✓ Security: 0 vulnerabilities

  Phase 4: Git Workflow
    ✓ Branch: feature/stripe-payment
    ✓ 8 commits with clear messages
    ✓ PR #145 created

  [Checkpoint: stripe-integration-complete]

Time: 2-3 hours (fully automated)
Developer Involvement: ZERO (they can do other work)
─────────────────────────────────────────────────────────────────

╔══════════════════════════════════════════════════════════════╗
║                  PHASE 5: Review & Deploy                     ║
╚══════════════════════════════════════════════════════════════╝

Next Morning - Developer Receives:

  ✅ Feature Complete: Stripe Payment Processing

  Summary:
    • PR: #145 (https://github.com/user/project/pull/145)
    • Files: 12 changed (+680, -15)
    • Tests: 32 new tests, all passing
    • Coverage: 94% (+3%)
    • Quality: All checks passed ✓

  What was built:
    1. Payment domain models
    2. Stripe integration service
    3. Webhook endpoint with verification
    4. API endpoints
    5. Database migrations
    6. Complete test suite
    7. Documentation

  Next steps:
    → Review PR #145
    → Test in staging
    → Merge and deploy

  Audit trail:
    • Session log: .claude/forge/sessions/20260108_143022.log
    • Checkpoint: stripe-integration-complete

Developer:
  • Reviews PR (15 minutes)
  • Tests in staging (10 minutes)
  • Approves and merges (1 minute)
  • Deploys to production (5 minutes)

Total Time: 31 minutes (vs. 8+ hours manual)

Feeling: POWERFUL, not exhausted ✅
```

---

## Component Interaction Matrix

### Who Calls What

```
┌────────────────────┬──────────┬──────────┬──────────┬──────────┐
│                    │ Agents   │ Commands │ Services │ Hooks    │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ User               │    —     │    ✓     │    —     │    —     │
│ (types /command)   │          │          │          │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Commands           │    ✓     │    —     │    —     │    —     │
│ (/enable-forge)    │ invoke   │          │          │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Agents             │    ✓     │    —     │    ✓     │    —     │
│ (orchestrator)     │ invoke   │          │ via CLI  │          │
│                    │ others   │          │          │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Agents             │    —     │    —     │    ✓     │    —     │
│ (specialists)      │          │          │ via CLI  │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Services           │    —     │    —     │    ✓     │    —     │
│ (state, git, etc)  │          │          │ call     │          │
│                    │          │          │ each     │          │
│                    │          │          │ other    │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Hooks              │    —     │    —     │    ✓     │    —     │
│ (post-task, etc)   │          │          │ via CLI  │          │
├────────────────────┼──────────┼──────────┼──────────┼──────────┤
│ Claude Code        │    ✓     │    ✓     │    —     │    ✓     │
│ (lifecycle)        │ loads    │ loads    │          │ executes │
└────────────────────┴──────────┴──────────┴──────────┴──────────┘

Key:
  ✓ = Direct interaction
  — = No direct interaction
```

---

## File Organization Comparison

### Side-by-Side: v3 vs. 2.0

```
┌─────────────────────────────────┬─────────────────────────────────┐
│         CURRENT (v3)            │      CANONICAL (2.0)            │
├─────────────────────────────────┼─────────────────────────────────┤
│ forge/                          │ .claude/                        │
│ ├── agents/ ❌                  │ ├── agents/ ✅                  │
│ │   ├── orchestrator.py (705)  │ │   ├── agent-forge-            │
│ │   ├── dispatcher.py           │ │   │   orchestrator.md (300)  │
│ │   ├── selection/              │ │   ├── agent-forge-architect.md│
│ │   ├── execution/              │ │   ├── agent-forge-backend.md │
│ │   ├── domain/                 │ │   ├── agent-forge-qa.md      │
│ │   └── services/               │ │   └── agent-forge-           │
│ │                               │ │       integration.md          │
│ ├── cli.py (746)                │ ├── commands/                   │
│ ├── state_manager.py            │ │   ├── enable-forge.md ✅     │
│ ├── gap_analyzer.py             │ │   ├── feature.md             │
│ ├── mcp_detector.py             │ │   └── [10 more]              │
│ └── [others]                    │ ├── hooks/                      │
│                                  │ │   ├── pre-task.sh            │
│ .claude/                        │ │   ├── post-task.sh           │
│ ├── agents/ ❌ EMPTY!           │ │   └── [3 more]               │
│ ├── commands/ ✅                │ └── forge/                      │
│ │   ├── feature.md              │     ├── config.yml             │
│ │   ├── status.md               │     ├── state.json             │
│ │   └── [10 more]               │     ├── sessions/              │
│ ├── hooks/ ✅                   │     └── checkpoints/           │
│ │   ├── pre-task.sh             │                                 │
│ │   └── [4 more]                │ forge/ (Python package)        │
│ ├── skills/agents/ ⚠️           │ ├── domain/                    │
│ │   ├── lead-architect.md       │ │   ├── agent.py               │
│ │   └── [5 more - SPLIT!]       │ │   ├── task.py                │
│ └── forge/                      │ │   └── message.py             │
│     ├── config.yml               │ ├── services/ ✅               │
│     └── state.json               │ │   ├── state_manager.py       │
│                                  │ │   ├── git_service.py         │
│ PROBLEMS:                        │ │   ├── quality_service.py     │
│ • Orchestrator is Python ❌     │ │   └── [more]                 │
│ • Agents not in .claude/agents/ │ ├── utils/                     │
│ • Split brain (code + docs)     │ │   ├── result.py              │
│ • 705-line orchestrator         │ │   └── [more]                 │
│ • Manual activation required    │ └── cli.py (200 lines)         │
│                                  │                                 │
│                                  │ BENEFITS:                       │
│                                  │ • Native Claude agents ✅      │
│                                  │ • Simple activation ✅         │
│                                  │ • Unified architecture ✅      │
│                                  │ • Clean separation ✅          │
│                                  │ • 52% less code ✅             │
└─────────────────────────────────┴─────────────────────────────────┘
```

---

## Summary: The Canonical Vision

### Core Architectural Principles

1. **Native Integration**: Agents in `.claude/agents/`, not parallel Python code
2. **Simple Activation**: One command (`/enable-forge`) → menu → automation
3. **Clear Separation**: Markdown for agents, Python for infrastructure
4. **Complete Automation**: Hooks enforce quality continuously
5. **Full Observability**: Every operation logged and auditable

### What Changes

- Orchestrator: Python → Markdown (native Claude agent)
- Agent logic: Hardcoded → Prompt-based (flexible, extensible)
- Activation: Manual setup → Simple command (`/enable-forge`)
- Architecture: Split brain → Unified (all agents in `.claude/agents/`)

### What's Preserved

- All state data (no schema changes)
- All checkpoints (still valid)
- All hooks (same functionality)
- Domain models (just reorganized)
- Services (cleaner structure)

### Developer Experience

```
Before:  Manual → Complex → Uncertain
After:   Simple → Automated → Confident

Time to value:     Hours → Minutes
Quality guarantee: Manual → Automatic
Observability:     Limited → Complete
Feeling:          Exhausted → Powerful ✅
```

---

**Document:** Architecture Diagrams
**Companion to:** CANONICAL-FORGE-VISION.md
**Date:** 2026-01-08
**Status:** Visual Reference
