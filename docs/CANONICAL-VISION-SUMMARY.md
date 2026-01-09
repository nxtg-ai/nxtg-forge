# CANONICAL FORGE VISION - Executive Summary

**One-Page Overview of NXTG-Forge 2.0 Architecture**

---

## The Core Problem

NXTG-Forge v3 exists **parallel** to Claude Code instead of being **native** to it:

- Agents are Python code in `forge/agents/` (NOT in `.claude/agents/`)
- Creates redundancy and missed integration opportunities
- Requires manual setup, lacks immediate visual feedback

## The Canonical Solution

**NXTG-Forge is native to Claude Code's agent system:**

```
.claude/
├── agents/                          ← ALL FORGE AGENTS HERE (native!)
│   ├── agent-forge-orchestrator.md  ← Coordinates everything
│   ├── agent-forge-architect.md     ← System design
│   ├── agent-forge-backend.md       ← Implementation
│   ├── agent-forge-qa.md            ← Testing & quality
│   └── agent-forge-integration.md   ← External services
├── commands/
│   └── enable-forge.md              ← Simple activation
├── hooks/                           ← Automation backbone
└── forge/
    ├── config.yml
    └── state.json
```

## The Experience

```
Developer opens project
    ↓
"✨ NXTG-FORGE-READY - Last session: Payment Processing 60% complete"
    ↓
Types: /enable-forge
    ↓
Menu appears:
  1. [Continue] Resume payment processing (60% complete)
  2. [New Feature] Plan and implement new feature
  3. [Soundboard] Discuss current state
    ↓
Complete automation through hooks
    ↓
Wakes up to: PR #127 created, 24 tests added, all checks passed ✓
    ↓
Reviews with confidence, merges, deploys
```

## Five Key Architectural Decisions

### 1. Orchestrator as Native Claude Agent (ADR-001)

**Decision:** Orchestrator lives in `.claude/agents/agent-forge-orchestrator.md`

- ❌ OLD: Python code in `forge/agents/orchestrator.py`
- ✅ NEW: Sophisticated markdown prompt in `.claude/agents/`

**Why:**

- Claude's agent system designed for this
- Native agent discovery and invocation
- Python services handle infrastructure (state, git, quality)
- Orchestrator coordinates via natural agent invocation

### 2. Agent Namespace Convention (ADR-002)

**All forge agents:** `agent-forge-*`

- `agent-forge-orchestrator.md` - The coordinator
- `agent-forge-architect.md` - Architecture & design
- `agent-forge-backend.md` - Implementation
- `agent-forge-qa.md` - Testing & quality
- `agent-forge-integration.md` - External services

**Why:** Clear namespace, prevents conflicts, easy discovery

### 3. Explicit Activation Model (ADR-003)

**Activation:** Via `/enable-forge` command (not automatic)

**Status indication:**

```
✨ NXTG-FORGE-READY
  Commands: /enable-forge, /status, /feature
```

**After activation:**

```
✅ NXTG-FORGE-ACTIVE
  Orchestrator: Ready | Session: 20260108_094530
```

**Why:** User control, clear mental model, discoverability

### 4. State Management via Services (ADR-004)

**Architecture:**

```
Agent (Markdown)
    ↓ invokes
forge CLI command
    ↓ uses
Python Service (state_manager.py)
    ↓ reads/writes
.claude/forge/state.json
```

**Why:** Markdown can't manipulate JSON reliably, Python services type-safe

### 5. Hooks as Automation Backbone (ADR-005)

**Hooks provide continuous automation:**

- `pre-task.sh` - Initialize session, check preconditions
- `post-task.sh` - Run tests, lint, security scan, update metrics
- `on-error.sh` - Log errors, suggest recovery
- `on-file-change.sh` - Auto-format, validate syntax
- `state-sync.sh` - Backup state, create checkpoints

**Why:** Automatic quality enforcement, complete observability

## What Changes in Migration

### What's Eliminated

- ❌ `forge/agents/orchestrator.py` (Python orchestrator)
- ❌ `forge/agents/dispatcher.py` (dispatcher logic)
- ❌ `forge/agents/selection/` (strategy classes)
- ❌ `forge/agents/execution/` (executor classes)

### What's Reorganized

- ✅ `forge/agents/domain/` → `forge/domain/` (domain models)
- ✅ `forge/agents/services/` → `forge/services/` (all services)

### What's Created

- ✅ `.claude/agents/agent-forge-orchestrator.md` (NEW)
- ✅ `.claude/agents/agent-forge-architect.md` (NEW)
- ✅ `.claude/agents/agent-forge-backend.md` (NEW)
- ✅ `.claude/agents/agent-forge-qa.md` (NEW)
- ✅ `.claude/agents/agent-forge-integration.md` (NEW)
- ✅ `.claude/commands/enable-forge.md` (NEW)

### What's Preserved

- ✅ All state.json data (no schema changes)
- ✅ All checkpoints (still valid)
- ✅ All hooks (unchanged)
- ✅ All commands (updated internally)
- ✅ Domain models (just moved)
- ✅ Services (just reorganized)

## Migration Path

```bash
# 1. Upgrade forge package
pip install --upgrade nxtg-forge  # v2.0

# 2. Run migration
cd ~/my-project
forge upgrade v2

# Output:
✓ Backed up .claude/ to .claude.v1.backup/
✓ Created 5 native agents in .claude/agents/
✓ Updated commands for v2.0
✓ Migrated state (no schema changes)
✓ Preserved all checkpoints

# 3. Test
claude
/enable-forge

# 4. Rollback if needed
forge downgrade v1
```

**Zero data loss. Complete backward compatibility.**

## Metrics

### Code Reduction

- Orchestration logic: 705 lines Python → ~300 lines markdown
- Total Python code: 2,500 lines (services only)
- Total markdown: ~8,000 lines (agents + commands + skills)
- **Overall: 52% reduction in complexity**

### DX Improvements

- Time to activate: < 2 seconds (`/enable-forge`)
- Commands to remember: 3 primary
- Manual quality checks: 0 (hooks automate)
- Setup steps: 2 (`forge init` + `/enable-forge`)

### Quality Guarantees

- Tests: Always run (hooks)
- Coverage: Always checked (>80% enforced)
- Linting: Always clean (0 issues)
- Security: Always scanned (0 critical/high)
- Commits: Always conventional format
- PRs: Always with detailed context

## Key Questions Answered

### Q: Should orchestrator live in `.claude/agents/agent-forge-orchestrator.md`?

**A: YES.** This aligns with "native to Claude Code" principle.

### Q: Should we eliminate `forge/agents/` entirely?

**A: Partially.**

- Eliminate orchestration logic (move to markdown)
- Keep domain models and services (Python infrastructure)

### Q: What's the minimal agent set?

**A: Five agents:**

1. Orchestrator (coordinator)
2. Architect (design)
3. Backend (implementation)
4. QA (testing)
5. Integration (external services)

### Q: How does status indication work?

**A: Marker file + startup check:**

- `.claude/FORGE-ENABLED` presence = installed
- Claude Code reads on startup
- Shows: "✨ NXTG-FORGE-READY"

### Q: How do hooks provide automation?

**A: Lifecycle integration:**

- Hooks run automatically at task lifecycle points
- Provide continuous quality enforcement
- No blocking (graceful degradation)
- Complete observability via logging

## Success Criteria

**We've succeeded when:**

1. **Installation:** `pip install nxtg-forge && forge init` (30 seconds)
2. **Detection:** Opening project shows "✨ NXTG-FORGE-READY" (instant)
3. **Activation:** `/enable-forge` shows menu (2 seconds)
4. **Automation:** Hooks enforce quality (continuous)
5. **Observability:** Complete audit trail (session logs)
6. **Confidence:** Developer feels powerful, not exhausted ✅

## Philosophy

**Powerful yet simple, elegant yet pragmatic, minimal yet complete.**

- **Powerful:** Complete features end-to-end
- **Simple:** One command activation
- **Elegant:** Native Claude Code integration
- **Pragmatic:** Ships production-ready code
- **Minimal:** 5 agents, 3 commands (primary)
- **Complete:** Quality, testing, git, observability

---

## Next Steps for Asif

**Review & Approve:**

1. ✅ Canonical architecture (agents in `.claude/agents/`)
2. ✅ Five-agent structure (orchestrator + 4 specialists)
3. ✅ Activation model (`/enable-forge` menu-driven)
4. ✅ Migration path (v3 → v2.0, backward compatible)

**Then Implement:**

1. Create agent markdown prompts
2. Refactor Python services
3. Build migration tool
4. Test on real projects
5. Update documentation

---

**Status:** Vision Document - Awaiting Approval
**Date:** 2026-01-08
**Full Document:** [CANONICAL-FORGE-VISION.md](./CANONICAL-FORGE-VISION.md)
