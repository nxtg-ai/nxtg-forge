# Phase 2 Automation - Quick Start Guide

**5-Minute Guide to NXTG-Forge Phase 2 Features**

---

## What's New in Phase 2?

Phase 2 adds intelligent automation that works in the background:

1. **Smart Git Workflows** - Perfect commits and PRs automatically
2. **Continuous Quality Monitoring** - Track metrics, detect regressions
3. **Autonomous Workflows** - Multi-step feature implementation
4. **Quality Gates** - Automatic checks before commits
5. **Session Reports** - Morning-after confidence

---

## Quick Examples

### 1. Generate Perfect Commit Messages

```python
from forge.services.git_automation import GitAutomationService

service = GitAutomationService()

# Stage your changes first
# git add .

# Generate commit message
msg_result = service.generate_commit_message(
    feature_context="Add user authentication"
)

print(msg_result.value)
```

**Output:**

```
feat(auth): Add user authentication

- Implement JWT token generation
- Add password hashing with bcrypt
- Create login/logout endpoints

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

### 2. Monitor Quality Automatically

```python
from forge.services.quality_monitor import QualityMonitor

monitor = QualityMonitor()

# Track current metrics
metrics = monitor.track_metrics().value
print(f"Coverage: {metrics.test_coverage}%")
print(f"Health Score: {monitor.calculate_health_score().value}/100")

# Detect regressions
regressions = monitor.detect_regressions().value
for r in regressions:
    print(f"{r.severity.upper()}: {r.message}")
```

**Output:**

```
Coverage: 89.0%
Health Score: 84/100
HIGH: Test coverage dropped from 92.0% to 89.0%
```

### 3. Run Autonomous Workflows

```python
from forge.services.work_orchestrator import WorkOrchestrator, FeatureSpec

orchestrator = WorkOrchestrator()

feature = FeatureSpec(
    name="Email Verification",
    description="Add email verification for new users",
    requirements=[
        "Send verification email on registration",
        "Validate tokens with 24h expiry"
    ]
)

# Execute complete workflow (plan → build → test → review)
result = orchestrator.execute_feature_workflow(feature)

print(f"Status: {result.value.status}")
print(f"Checkpoints: {len(result.value.checkpoints_created)}")
```

---

## Hooks in Action

### What Happens When You Commit

```bash
git commit -m "feat: add auth"
```

**Behind the Scenes:**

1. **pre-commit hook runs:**

   ```
   ✓ Code formatting                          0.3s
   ✓ Linting (ruff)                           0.8s
   ✓ Type checking (mypy)                     1.2s
   ✓ Security scan (bandit)                   0.9s
   ✓ Unit tests (124 tests)                   4.1s
   ✓ Coverage check (89% - above 85%)         0.2s

   ✅ ALL QUALITY GATES PASSED
   ```

2. **Commit created**

3. **post-commit hook runs:**

   ```
   ✓ Commit created: a7b9c3d
   🔖 Checkpoint created: cp_2026-01-08_1430
   📈 Project Health: 78 → 84 (+6)
   ```

### What Happens When You Edit Files

```python
# You: Edit some Python files
```

**Behind the Scenes:**

1. **pre-tool-use hook:** Checks quality, warns if issues
2. **Your edit happens**
3. **post-tool-use hook:**

   ```
   ⚠️  Syntax warning in auth_service.py
   📈 Test coverage: 78% → 82% (+4%)

   ┌─ Forge Activity ─────────────────────┐
   │ ✓ Modified auth_service.py   0.1s    │
   │ ✓ Created test_auth.py       0.1s    │
   └──────────────────────────────────────┘
   ```

---

## Configuration

### Enable/Disable Hooks

Edit `.claude/config.json`:

```json
{
  "hooks": {
    "enabled": true,
    "pre_commit": true,
    "post_commit": true
  }
}
```

### Set Quality Thresholds

Edit `.claude/forge/config.json`:

```json
{
  "quality": {
    "min_coverage": 85,
    "max_complexity": 10,
    "block_on_security": true
  }
}
```

---

## Common Tasks

### Check Project Health

```python
from forge.services.quality_monitor import QualityMonitor

monitor = QualityMonitor()
score = monitor.calculate_health_score().value
print(f"Health: {score}/100")
```

### Create Feature Branch

```python
from forge.services.git_automation import GitAutomationService

service = GitAutomationService()
branch = service.create_feature_branch("User Profile Pages").value
print(f"Created: {branch}")
# Output: Created: feature/user-profile-pages
```

### Analyze Quality Trends

```python
from forge.services.quality_monitor import QualityMonitor

monitor = QualityMonitor()
trend = monitor.analyze_trends(days=7).value

print(f"Trend: {trend.overall_trend}")
print(f"Improving: {', '.join(trend.metrics_improving)}")
print(f"Declining: {', '.join(trend.metrics_declining)}")
```

### Create Pull Request

```python
from forge.services.git_automation import GitAutomationService

service = GitAutomationService()

pr = service.create_pull_request(
    title="Add user authentication",
    body="Implements JWT-based auth with bcrypt password hashing"
).value

print(f"PR #{pr.number}: {pr.url}")
```

---

## Troubleshooting

### "Quality gate failed"

Check which check failed:

```bash
make lint      # Check linting
make test      # Run tests
make typecheck # Type errors
```

Fix issues and commit will succeed.

### "Hook not running"

Check hook is enabled in `.claude/config.json`:

```json
{
  "hooks": {
    "enabled": true
  }
}
```

### "Metrics not tracking"

Ensure `.claude/forge/` directory exists:

```bash
mkdir -p .claude/forge
```

---

## Next Steps

**Read Full Documentation:**

- `docs/PHASE-2-AUTOMATION-COMPLETE.md` - Complete feature documentation
- `docs/CANONICAL-FORGE-VISION-UNIFIED.md` - Overall vision

**Run Tests:**

```bash
pytest tests/integration/test_phase2_automation.py -v
```

**Try Phase 3 Features:**

- Enhanced morning reports
- Session visualization
- Comprehensive audit trails

---

**Questions?** See `docs/PHASE-2-AUTOMATION-COMPLETE.md` for detailed documentation.
