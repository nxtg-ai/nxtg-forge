# VISION ALIGNMENT ACTION LIST

**Concrete Changes Required for Unified Vision**

**Date:** 2026-01-08
**Owner:** Both teams (see assignments below)

---

## Critical Path: Agent Model Unification

### Priority 1: Agree on Hybrid Architecture

**Decision Needed:** Approve hybrid model (markdown agents + Python services)

**Design-Vanguard Actions:**

- [ ] Review hybrid model proposal in VISION-ALIGNMENT-REVIEW-ARCHITECT.md (Part III)
- [ ] Confirm orchestrator as markdown agent is acceptable
- [ ] Specify service invocation syntax preferences
- [ ] Update TECHNICAL-INTEGRATION.md with hybrid architecture

**Master Architect Actions:**

- [ ] Create hybrid architecture diagram
- [ ] Write ADR for hybrid agent model
- [ ] Specify service CLI interface (`forge service operation --args`)
- [ ] Update CANONICAL-FORGE-VISION.md agent section

**Target:** Agreement within 3 days

---

## Design-Vanguard Document Updates

### File: `.asif/canonical-vision/TECHNICAL-INTEGRATION.md`

**Add Section: "Hybrid Agent Architecture"**

```markdown
## Hybrid Agent Architecture

### Agent Layer (Markdown)
Agents are native Claude Code agents in .claude/agents/:
- agent-forge-orchestrator.md - High-level coordination
- agent-forge-architect.md - Architecture design
- agent-forge-backend.md - Implementation
- agent-forge-qa.md - Testing

### Service Layer (Python)
Complex logic implemented as Python services in forge/services/:
- orchestration_service.py - Task decomposition, dependency analysis
- state_manager.py - Session state management
- quality_service.py - Quality metrics, gate enforcement
- git_service.py - Git operations, commit generation

### Integration Pattern
Agents invoke services via CLI:
```bash
forge state update --feature-id=123 --status=complete
```

Services return JSON, agents interpret results.

```

**Add Section: "Activity Monitoring Phases"**
```markdown
## Background Activity Monitoring

### Phase 1: Synchronous Indicators (MVP)
Show results after operation completes:
```

✓ Quality checks complete (2.1s)
✓ Tests: 124 passed

```

Works everywhere. No terminal compatibility issues.

### Phase 2: Asynchronous Indicators (Enhancement)
Live updates during operation (ANSI escape codes):
```

┌─ Forge Activity ────────────────┐
│ 🔍 Running tests...             │
└─────────────────────────────────┘

```

Requires ANSI terminal support. Feature detection + fallback.
```

**Update Section: "Orchestrator Implementation"**

Change from:

```python
# forge/agents/orchestrator.py (Python class)
```

To:

```markdown
# .claude/agents/agent-forge-orchestrator.md (Markdown agent)

You are the NXTG-Forge Orchestrator...

When you need complex logic:
- Task decomposition: `forge orchestration analyze-task "description"`
- State updates: `forge state update-feature --id=X --status=Y`
- Quality checks: `forge quality check --all`
```

**Add Section: "Technical Feasibility Confirmation"**

```markdown
## Technical Feasibility

All UX mockups are implementable within Claude Code CLI:
✅ Status indicators - Hooks at session start
✅ Menu system - Formatted text output
✅ Git automation - Shell commands + gh CLI
✅ PR generation - GitHub CLI integration
✅ Morning reports - Data aggregation + templates
✅ Checkpoint system - Git tags + metadata
⚠️ Background activity - Phased approach (sync → async)

Validated by Master Architect on 2026-01-08.
```

---

## Master Architect Document Updates

### File: `docs/CANONICAL-FORGE-VISION.md`

**Replace Section: "Agent System Design"**

Remove:

```markdown
## Agent System Design

Agents live in .claude/agents/ as markdown files...
[Basic description]
```

Add:

```markdown
## Agent System Design

See Design-Vanguard's comprehensive UX vision:
- Visual mockups: .asif/canonical-vision/VISUAL-MOCKUPS.md
- Emotional journey: .asif/canonical-vision/CANONICAL-FORGE-VISION.md
- Technical integration: .asif/canonical-vision/TECHNICAL-INTEGRATION.md

### Hybrid Architecture

Agents (Markdown) + Services (Python) work together:

**Agent Layer:** `.claude/agents/agent-forge-*.md`
- High-level coordination
- User interaction
- Decision making
- Agent-to-agent communication

**Service Layer:** `forge/services/*.py`
- Complex algorithms
- State management
- Quality metrics
- Git operations

**Integration:** Agents invoke services via CLI, services return JSON.

For detailed architecture, see ADR-006-HYBRID-AGENT-MODEL.md
```

**Add Section: "UX Specifications"**

```markdown
## UX Specifications

The canonical UX is defined by Design-Vanguard's mockups.

### Visual Mockups (11 detailed scenarios)
See: .asif/canonical-vision/VISUAL-MOCKUPS.md

1. First Contact (Forge Enabled)
2. First Contact (Forge Not Enabled)
3. Activation Flow
4. Continue Mode (Context Restoration)
5. Background Activity (Subtle Indicators)
6. Quality Gate Alert (Warning)
7. Ready to Commit
8. Commit Complete
9. Morning Report (Overnight Session)
10. Planning Mode (Feature Wizard)
11. Soundboard Mode (Strategic Advisor)

### Implementation Requirement
All implementations must match these mockups exactly.
Use Design-Vanguard's box-drawing, icons, and formatting.
```

**Update Section: "Git Workflow Integration"**

Add attribution:

```markdown
## Git Workflow Integration

*(Specification by Design-Vanguard, validated by Master Architect)*

[Existing content...]
```

**Add ADR: "ADR-006: Hybrid Agent Model"**

Create new file: `docs/ADRs/ADR-006-HYBRID-AGENT-MODEL.md`

```markdown
# ADR-006: Hybrid Agent Model

## Status
PROPOSED (Pending Design-Vanguard Approval)

## Context
Two visions for agent architecture emerged:
1. Pure markdown agents (Master Architect)
2. Python orchestration with markdown skills (Design-Vanguard)

## Decision
Hybrid model combining both approaches:
- Agents are markdown files in .claude/agents/
- Complex logic delegated to Python services
- Agents invoke services via CLI
- Services return structured JSON

## Rationale
- Native Claude integration (markdown agents)
- Type-safe logic (Python services)
- Clear separation of concerns
- Easy to extend and customize

## Consequences
- Agents can be user-edited (markdown)
- Services can be unit tested (Python)
- CLI becomes integration layer
- Both teams' visions satisfied
```

---

## Naming Standardization

**Both Teams:** Adopt these conventions across all documents

### Agent Names

```
agent-forge-orchestrator.md
agent-forge-architect.md
agent-forge-backend.md
agent-forge-qa.md
agent-forge-integration.md
```

### Checkpoint IDs

```
cp_YYYY-MM-DD_HHMM

Examples:
cp_2026-01-08_1430
cp_2026-01-07_0315
```

### Session IDs

```
session_YYYYMMDD_HHMMSS

Examples:
session_20260108_143022
session_20260107_214530
```

### Service Commands

```
forge <service> <operation> --args

Examples:
forge state update-feature --id=123 --status=complete
forge quality check --all
forge git commit --auto
forge orchestration analyze-task "Add OAuth"
```

---

## Attribution Updates

### In Design-Vanguard Documents

**Add to:** `.asif/canonical-vision/README.md`

```markdown
## Collaboration

This vision was created in collaboration with:
- **Design-Vanguard:** UX design, emotional journey, visual mockups
- **Master Architect:** Technical validation, architecture review, feasibility analysis

Technical feasibility confirmed: 2026-01-08
See: /docs/VISION-ALIGNMENT-REVIEW-ARCHITECT.md
```

### In Master Architect Documents

**Add to:** `docs/CANONICAL-FORGE-VISION.md` (top)

```markdown
## Collaboration

This architecture was created in collaboration with:
- **Master Architect:** Technical architecture, system design, ADRs
- **Design-Vanguard:** UX vision, visual mockups, emotional journey

UX specifications by Design-Vanguard:
- Visual mockups: .asif/canonical-vision/VISUAL-MOCKUPS.md
- Emotional journey: .asif/canonical-vision/CANONICAL-FORGE-VISION.md

See unified vision: docs/VISION-ALIGNMENT-REVIEW-ARCHITECT.md
```

---

## Testing Requirements

### Phase 1 Testing (Both Teams)

**Test:** Status indicator appears

```bash
# Setup
cd test-project
forge init
touch .claude/FORGE-ENABLED

# Test
claude
# Expected: "✅ NXTG-FORGE-ENABLED" banner appears
```

**Test:** Menu displays after activation

```bash
# In Claude session
> /enable-forge

# Expected: 4-option menu appears
# 1. Continue
# 2. Plan
# 3. Soundboard
# 4. Health
```

**Test:** Commit message generation

```bash
# Make changes, stage them
git add .

# Test
forge git commit --auto

# Expected:
# - Conventional commit format
# - Descriptive summary
# - Bullet points for changes
# - Attribution footer
```

---

## Open Questions Requiring Decisions

### Q1: Service Invocation Syntax

**Options:**

- A) Bash in backticks: \`forge state update --args\`
- B) Special syntax: `{{forge.state.update(args)}}`
- C) Tool/function calling API

**Recommendation:** Option A (bash) - works with standard markdown
**Decision Needed By:** Design-Vanguard + Master Architect

---

### Q2: Terminal Compatibility Strategy

**Options:**

- A) Hard requirement (error if no ANSI support)
- B) Soft fallback (detect, use simple mode)
- C) User configuration (fancy/simple mode)

**Recommendation:** Option B (feature detect + fallback)
**Decision Needed By:** Design-Vanguard

---

### Q3: Session Auto-Save Frequency

**Options:**

- A) After each agent invocation (safe, overhead)
- B) End of session only (efficient, risky)
- C) Every N operations + end of session (hybrid)

**Recommendation:** Option C (auto-save every 5 operations + end)
**Decision Needed By:** Master Architect

---

## Timeline

### Week 1: Documentation Updates

- [ ] Both teams update documents (by day 3)
- [ ] Create unified specification (day 4-5)
- [ ] Review and approve (day 5)

### Week 2: Phase 1 Implementation

- [ ] Hybrid agent structure
- [ ] Status indicator system
- [ ] Basic menu
- [ ] Testing

### Week 3-4: Phase 2 (Automation)

- [ ] Git workflow
- [ ] Quality gates
- [ ] Activity indicators

### Week 5-6: Phase 3 (Observability)

- [ ] Session persistence
- [ ] Reports
- [ ] Checkpoints

---

## Success Criteria

### Documentation

- [ ] All conflicts resolved
- [ ] Single source of truth created
- [ ] Both teams credited appropriately
- [ ] ADRs written for key decisions

### Phase 1 Implementation

- [ ] User sees status indicator on project open
- [ ] `/enable-forge` displays 4-option menu
- [ ] Orchestrator agent can route to other agents
- [ ] Basic state management works

### Validation

- [ ] UX matches design mockups exactly
- [ ] Architecture matches technical specs exactly
- [ ] All tests pass
- [ ] User feedback incorporated

---

**Document Status:** READY FOR BOTH TEAMS
**Next Action:** Schedule sync meeting to approve hybrid model
**Target Date for Phase 1:** 2026-01-22 (2 weeks)
