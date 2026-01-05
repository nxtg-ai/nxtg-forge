# NXTG-Forge Complete Guide

**Version**: 1.0.0  
**Last Updated**: January 2026

---

## Table of Contents

1. [Introduction](#introduction)
2. [Quick Start](#quick-start)
3. [Core Concepts](#core-concepts)
4. [Command Reference](#command-reference)
5. [Workflows](#workflows)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Topics](#advanced-topics)

---

## Introduction

NXTG-Forge is a **self-deploying, state-aware AI development infrastructure** that transforms Claude Code into a complete autonomous development system.

### What Makes NXTG-Forge Different?

```
Traditional Development:
├── Write code manually
├── Configure tools manually
├── Track progress mentally
├── Recover from interruptions manually
└── Hope everything works

NXTG-Forge Development:
├── Specify what you want
├── AI builds entire system
├── State tracked automatically
├── Resume from any point instantly
└── Guaranteed quality through automation
```

### Key Features

✅ **Self-Deploying**: One command creates entire project infrastructure  
✅ **State-Aware**: Never lose context, resume from anywhere  
✅ **Agent-Orchestrated**: Specialized AI agents work together  
✅ **MCP Auto-Config**: Automatically detects and configures needed tools  
✅ **Quality-Enforced**: Automated testing, linting, security scanning  
✅ **Zero-Context Recovery**: Power outages can't stop you  

---

## Quick Start

### Installation

```bash
# Install NXTG-Forge globally
curl -fsSL https://nxtg.ai/install.sh | bash

# Or with wget
wget -qO- https://nxtg.ai/install.sh | bash
```

### Create New Project

```bash
# 1. Create project directory
mkdir my-awesome-app
cd my-awesome-app

# 2. Start Claude Code
claude

# 3. Initialize NXTG-Forge
/init nxtg-forge --new

# 4. Follow interactive prompts to build spec

# 5. Let AI build your entire project!
```

### Upgrade Existing Project

```bash
# 1. Navigate to your project
cd my-existing-project

# 2. Start Claude Code
claude

# 3. Upgrade to NXTG-Forge
/init nxtg-forge --upgrade

# 4. Review and approve upgrade plan

# 5. Get gap analysis and recommendations
```

---

## Core Concepts

### The State System

**Everything revolves around state.**

```
.claude/state.json
├── Project metadata
├── Architecture decisions
├── Development phase
├── Features (completed, in-progress, planned)
├── Agent assignments
├── MCP server configs
├── Quality metrics
├── Checkpoints
└── Last session (for recovery)
```

**Why This Matters:**

- **Zero-Context Continuation**: Claude can resume from any state
- **Power Outage Proof**: State saved every change
- **Team Sync**: Share state, everyone knows exactly what's happening
- **Time Travel**: Checkpoints let you go back to any point

### The Agent Team

Six specialized agents handle different aspects:

```
┌──────────────────────────────────────────┐
│           Lead Architect                 │
│  (Plans, coordinates, makes decisions)   │
└──────────┬───────────────────────────────┘
           │
    ┌──────┴──────┬──────┬──────┬──────┐
    │             │      │      │      │
┌───▼────┐  ┌────▼───┐ ┌▼─────┐ ┌▼────▼──┐
│Backend │  │  CLI   │ │Platf.│ │Integr. │
│Master  │  │Artisan │ │Build.│ │Special.│
└───┬────┘  └────────┘ └──────┘ └────┬───┘
    │                                 │
    └──────────────┬──────────────────┘
                   │
              ┌────▼─────┐
              │    QA    │
              │ Sentinel │
              └──────────┘
```

Each agent has:

- Specialized skills
- Clear responsibilities
- Ability to work autonomously
- Checkpoints at each step

### Skills System

Skills are **knowledge modules** loaded into Claude's context:

```
.claude/skills/
├── core/
│   ├── nxtg-forge.md         # How the system works
│   ├── architecture.md       # Your architecture patterns
│   ├── coding-standards.md   # Your code style
│   └── testing.md            # Your testing approach
├── domain/
│   └── your-domain.md        # Business logic rules
├── tech-stack/
│   └── framework-x.md        # Framework conventions
└── agents/
    └── agent-name.md         # Agent-specific skills
```

**Skills = Reusable Expertise**

Write once, benefit forever. Every new feature gets smarter because skills accumulate.

### MCP Auto-Detection

NXTG-Forge analyzes your project and automatically configures needed MCP servers:

```
Project Analysis
     ↓
Uses PostgreSQL? → Add postgres MCP server
     ↓
GitHub repo? → Add github MCP server
     ↓
Stripe in spec? → Add stripe MCP server
     ↓
Auto-configure everything
```

No manual MCP configuration needed!

### Checkpoints

State snapshots at critical points:

```
Checkpoint Timeline:
├─ cp-001: After architecture design
├─ cp-002: After user auth implementation
├─ cp-003: After payment integration
├─ cp-004: Before major refactoring
└─ cp-005: Production-ready state
```

**Use Cases:**

- Before risky changes
- After completing features
- Before deployments
- Milestone markers
- Recovery points

---

## Command Reference

### Core Commands

#### `/init nxtg-forge`

Initialize NXTG-Forge in project.

```bash
# New project (interactive)
/init nxtg-forge --new

# New project from spec
/init nxtg-forge --new --spec docs/PROJECT-SPEC.md

# Upgrade existing project
/init nxtg-forge --upgrade

# See what would be upgraded (dry run)
/init nxtg-forge --upgrade --dry-run
```

#### `/status`

Show complete project state.

```bash
# Full status
/status

# Detailed feature view
/status --detail features

# Detailed quality metrics
/status --detail quality

# JSON output
/status --json

# Export state
/status --export state-backup.json
```

#### `/checkpoint`

Create state checkpoint.

```bash
# Create checkpoint with description
/checkpoint "After implementing user authentication"

# Create checkpoint with auto-description
/checkpoint

# List all checkpoints
/checkpoint --list

# Show checkpoint details
/checkpoint --show cp-003
```

#### `/restore`

Restore from checkpoint.

```bash
# Restore latest checkpoint
/restore

# Restore specific checkpoint
/restore cp-003

# Restore with git reset
/restore cp-003 --reset-git

# Show diff before restoring
/restore cp-003 --diff
```

#### `/feature`

Add new feature.

```bash
# Add feature (interactive spec)
/feature "User Profile Management"

# Add high-priority feature
/feature "Payment Integration" --priority high

# Assign to specific agent
/feature "Admin CLI" --agent cli-artisan

# Add from existing spec file
/feature --spec features/profile-spec.md
```

#### `/gap-analysis`

Analyze improvement opportunities.

```bash
# Run gap analysis
/gap-analysis

# Output to specific file
/gap-analysis --output reports/gaps.md

# Show summary only
/gap-analysis --summary

# Generate action plan
/gap-analysis --with-plan
```

#### `/deploy`

Deploy application.

```bash
# Deploy to staging
/deploy staging

# Deploy to production
/deploy production

# Deploy with rollback on failure
/deploy production --auto-rollback

# Dry run (show what would happen)
/deploy production --dry-run
```

### Advanced Commands

#### `/agent-assign`

Manually assign work to agents.

```bash
# Assign feature to agent
/agent-assign feat-003 backend-master

# Show agent workload
/agent-assign --workload

# Rebalance work across agents
/agent-assign --rebalance
```

#### `/spec`

Specification operations.

```bash
# Generate spec interactively
/spec generate

# Validate existing spec
/spec validate docs/PROJECT-SPEC.md

# Update spec
/spec update

# Export spec to PDF
/spec export --format pdf
```

#### `/integrate`

Add integration.

```bash
# Add integration (auto-detect MCP server)
/integrate stripe

# Add with explicit config
/integrate custom-api --config integrations/custom.json

# List available integrations
/integrate --list

# Show integration status
/integrate --status stripe
```

---

## Workflows

### Workflow 1: Brand New Project

```
Day 1: Ideation & Planning
──────────────────────────
1. Create directory: mkdir my-project && cd my-project
2. Start Claude: claude
3. Initialize: /init nxtg-forge --new
4. Interactive spec building (15-30 min Q&A)
5. Approve generated spec
6. ☕ Coffee while AI generates entire infrastructure
7. Review generated files
8. First checkpoint created automatically

Day 1 Results:
✓ Complete project structure
✓ All configuration files
✓ Documentation scaffolding
✓ Agent team configured
✓ MCP servers connected
✓ CI/CD pipeline set up
✓ Testing infrastructure
✓ First checkpoint saved
```

```
Day 2-N: Feature Development
─────────────────────────────
For each feature:
  1. /feature "Feature Name"
  2. Review feature spec with AI
  3. Approve implementation plan
  4. AI implements across phases:
     - Design (Lead Architect)
     - Backend (Backend Master)
     - Frontend (if applicable)
     - CLI (CLI Artisan if needed)
     - Integration (Integration Specialist)
     - Testing (QA Sentinel)
  5. Review and test
  6. /checkpoint "Feature X complete"
  7. /deploy staging
```

```
Continuous Improvement
──────────────────────
Weekly/Monthly:
  1. /gap-analysis
  2. Review recommendations
  3. Address high-priority gaps
  4. /status to track health score
  5. Refactor as needed
```

### Workflow 2: Upgrade Existing Project

```
Phase 1: Analysis (1 hour)
──────────────────────────
1. cd my-existing-project
2. claude
3. /init nxtg-forge --upgrade --dry-run
4. Review analysis report:
   - Current state assessment
   - Proposed changes
   - Migration plan
   - Estimated impact
5. Approve or request modifications
```

```
Phase 2: Migration (2-4 hours)
───────────────────────────────
1. /init nxtg-forge --upgrade
2. AI executes migration:
   - Creates .claude/ infrastructure
   - Generates skills from existing code
   - Configures MCP servers
   - Sets up agents
   - Restructures if needed
   - Adds testing infrastructure
   - Creates documentation
3. Checkpoint after each major step
4. Review changes incrementally
```

```
Phase 3: Gap Closure (ongoing)
───────────────────────────────
1. /gap-analysis
2. Prioritize gaps:
   - Critical (security, tests)
   - High (code quality, docs)
   - Medium (optimization)
   - Low (nice-to-have)
3. Address systematically:
   /feature "Add comprehensive tests"
   /feature "Improve documentation"
   /feature "Optimize performance"
4. Track progress via /status
```

### Workflow 3: Recovery from Interruption

```
Scenario: Power Outage During Development
──────────────────────────────────────────

Before Outage:
- Working on "Payment Integration" feature
- Backend implementation 45% complete
- Last checkpoint: 30 minutes ago

After Outage (Zero-Context Recovery):
1. Open terminal
2. cd my-project
3. claude
4. /status (shows interrupted session)
5. Options presented automatically:
   a) Resume exact session: claude --resume session-xyz
   b) Restore last checkpoint: /restore
   c) Review what was in progress: /status --detail features
6. Choose option (usually a - resume)
7. Continue exactly where left off
   - AI knows what it was doing
   - All context preserved in state
   - No rework needed
```

---

## Best Practices

### State Management

```
DO:
✅ Create checkpoints before risky changes
✅ Use descriptive checkpoint names
✅ Commit state.json to git
✅ Review /status regularly
✅ Save checkpoints after each feature

DON'T:
❌ Manually edit state.json
❌ Skip checkpoints for "small" changes
❌ Ignore interrupted session warnings
❌ Delete checkpoint files
❌ Work without state tracking
```

### Agent Collaboration

```
DO:
✅ Let Lead Architect plan before implementation
✅ Trust agent specializations
✅ Use /agent-assign for complex orchestration
✅ Review handoff documents between agents

DON'T:
❌ Force wrong agent for a task
❌ Skip planning phase
❌ Micromanage agent work
❌ Override agent recommendations without reason
```

### Feature Development

```
Best Practice Feature Workflow:
1. Start with clear spec (/feature with good description)
2. Let AI create implementation plan
3. Review and approve plan
4. Let agents execute (checkpoint each phase)
5. Run tests continuously
6. Review before marking complete
7. Create final checkpoint
8. Deploy to staging
9. Manual testing
10. Deploy to production
```

### Quality Maintenance

```
Daily:
- Check /status health score
- Review test failures immediately
- Address security vulnerabilities

Weekly:
- Run /gap-analysis
- Review technical debt
- Plan refactoring sprints

Monthly:
- Comprehensive health check
- Update dependencies
- Performance optimization review
```

---

## Troubleshooting

### Common Issues

#### Issue: "Claude doesn't remember project context"

**Solution:**

```bash
# Check if state exists
cat .claude/state.json

# If missing, reinitialize
/init nxtg-forge --upgrade

# Load relevant skills
claude --load-skills .claude/skills/core/
```

#### Issue: "MCP server not connecting"

**Solution:**

```bash
# Check MCP status
/mcp

# Re-detect and configure
nxtg-forge mcp detect --configure

# Manual configuration
claude mcp add <server-name>

# Debug
claude --mcp-debug
```

#### Issue: "Can't resume after interruption"

**Solution:**

```bash
# Check recovery info
nxtg-forge recovery

# Try resume
claude --resume <session-id>

# If that fails, restore checkpoint
/restore

# Last resort: check state
/status --detail features
# Then manually continue work
```

#### Issue: "Tests failing after upgrade"

**Solution:**

```bash
# Restore to before upgrade
/restore <checkpoint-before-upgrade>

# Re-run upgrade with test preservation
/init nxtg-forge --upgrade --preserve-tests

# Or fix tests incrementally
/feature "Fix test suite"
```

### Debug Mode

Enable verbose logging:

```bash
# Start Claude with debug
claude --debug

# Or set environment variable
export CLAUDE_DEBUG=1
claude

# Check logs
tail -f ~/.claude/logs/debug.log
```

---

## Advanced Topics

### Custom Skills Creation

Create project-specific skills:

```markdown
# .claude/skills/custom/my-skill.md

**Purpose**: [What this skill provides]

**When to Use**: [Situations to apply this skill]

## Patterns

### Pattern 1
[Description and code example]

## Anti-Patterns
[What to avoid]

## Checklist
- [ ] Criterion 1
- [ ] Criterion 2
```

Then load it:

```bash
# In Claude Code
"Load skill: .claude/skills/custom/my-skill.md"
```

### Multi-Project Management

Manage multiple projects with NXTG-Forge:

```bash
# Project A
cd ~/projects/project-a
/status --export ~/forge-states/project-a-state.json

# Project B
cd ~/projects/project-b
/status --export ~/forge-states/project-b-state.json

# Compare states
nxtg-forge compare ~/forge-states/project-a-state.json ~/forge-states/project-b-state.json
```

### CI/CD Integration

Integrate NXTG-Forge with CI/CD:

```yaml
# .github/workflows/forge-ci.yml
name: NXTG-Forge CI

on: [push, pull_request]

jobs:
  forge-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install NXTG-Forge
        run: curl -fsSL https://nxtg.ai/install.sh | bash
      
      - name: Check Project Health
        run: |
          nxtg-forge health --detail
          HEALTH=$(nxtg-forge health --score)
          if [ $HEALTH -lt 75 ]; then
            echo "Health score too low: $HEALTH"
            exit 1
          fi
      
      - name: Validate State
        run: nxtg-forge status --json > state-report.json
      
      - name: Upload State Report
        uses: actions/upload-artifact@v3
        with:
          name: state-report
          path: state-report.json
```

### Team Collaboration

Share NXTG-Forge setup across team:

```bash
# Team lead sets up
/init nxtg-forge --new
git add .claude/ docs/
git commit -m "Add NXTG-Forge infrastructure"
git push

# Team members clone and use
git clone <repo>
cd <repo>
claude

# Everything just works!
# State, skills, agents all configured
```

### Remote Work with Claude Code Remote

Use NXTG-Forge with cloud execution:

```bash
# Start remote session
claude --remote

# Check remote session status
claude --list-remote

# Pull remote session locally
claude --teleport <session-id>

# State syncs automatically!
```

---

## FAQ

**Q: Does NXTG-Forge work with any programming language?**  
A: Yes! The system is language-agnostic. Skills and templates adapt to your stack.

**Q: Can I use this for existing large codebases?**  
A: Absolutely! Use `--upgrade` mode. It analyzes and integrates incrementally.

**Q: What if I don't like the generated code?**  
A: You have full control. Review at checkpoints, provide feedback, or manually adjust.

**Q: How much does NXTG-Forge cost?**  
A: NXTG-Forge itself is open-source. You pay only for Claude Code usage (Anthropic pricing).

**Q: Can multiple developers work simultaneously?**  
A: Yes! State management supports concurrent work. Use git branches + checkpoints.

**Q: What happens if Claude makes a mistake?**  
A: Checkpoints let you revert instantly. QA Sentinel catches most issues in testing phase.

**Q: Do I need to learn prompt engineering?**  
A: No! NXTG-Forge handles all prompt optimization automatically.

---

## Support & Resources

- **Documentation**: <https://nxtg.ai/docs>
- **Examples**: <https://github.com/nxtg-forge/docs/examples>
- **Community**: <https://discord.gg/nxtg-forge>
- **Issues**: <https://github.com/nxtg-forge/nxtg-forge/issues>

---

## Happy Forging! 🔨⚡
