# NXTG-Forge Documentation

Complete documentation for NXTG-Forge - the intelligent enhancement system for Claude Code.

## Quick Navigation

### Getting Started

- [Installation & Setup](../GETTING-STARTED.md) - 30-second quickstart guide
- [Real-World Examples](../EXAMPLES.md) - See it in action with actual scenarios
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions

### Architecture & Design

- [System Architecture](ARCHITECTURE.md) - How everything works together
- [UX Redesign Philosophy](UX-REDESIGN-2026-01-07.md) - From configuration tool to invisible intelligence
- [UX Implementation Details](UX-IMPLEMENTATION-2026-01-07.md) - Technical implementation of the redesign
- [API Reference](API.md) - Complete API documentation

### Operations

- [Deployment Guide](DEPLOYMENT.md) - Production deployment instructions
- [Gap Analysis](GAP-ANALYSIS.md) - Project improvement recommendations
- [Project Health](../README.md#project-health) - Current status and metrics

### Customization (Advanced)

- [Customization Guide](CUSTOMIZATION.md) - Advanced configuration options
- [State Recovery](STATE-RECOVERY.md) - Session persistence and recovery

### Internal Documentation

- [Runbook](.asif/RUNBOOK.md) - Operational procedures
- [UAT Guide](.asif/UAT-GUIDE.md) - User acceptance testing
- [FAQ](.asif/FAQ.md) - Frequently asked questions
- [Sysadmin Guide](.asif/SYSADMIN.md) - System administration

## Philosophy

NXTG-Forge follows a **zero-configuration** philosophy:

- **90% of users**: Never touch configuration
- **9% of users**: Edit auto-generated config for minor tweaks
- **1% of users**: Deep customization with custom agents/workflows

The best documentation is the one users don't need to read.

## Quick Reference

### Installation (3 commands)

```bash
git clone https://github.com/nxtg-ai/nxtg-forge.git
cd nxtg-forge
pip install -e .
```

### Project Setup (2 commands)

```bash
cd ~/my-project
forge init
```

### Use (1 command)

```bash
claude
```

That's it. Claude is now smarter.

## Documentation Principles

All NXTG-Forge documentation follows these principles:

1. **Show, Don't Tell** - Examples over explanations
2. **Experience-Focused** - What users get, not how it works
3. **Progressive Disclosure** - Simple first, advanced optional
4. **Real-World Scenarios** - Actual use cases, not toy examples
5. **Honest and Accurate** - No aspirational claims, only reality

## Getting Help

- **Quick Questions**: Check [GETTING-STARTED.md](../GETTING-STARTED.md)
- **Issues**: [GitHub Issues](https://github.com/nxtg-ai/nxtg-forge/issues)
- **Discussions**: [GitHub Discussions](https://github.com/nxtg-ai/nxtg-forge/discussions)
- **Email**: <axw@nxtg.ai>

## Contributing to Documentation

When updating documentation:

1. **Test everything** - Every command must actually work
2. **No hallucination** - Only document what exists
3. **User perspective** - Write for the person installing, not the person who built it
4. **Examples first** - Show before explaining
5. **Keep it current** - Update when code changes

## Document Status

All documentation is current as of 2026-01-07.

Last major update: UX Redesign (complete removal of setup wizard, zero-config implementation)

---

**Made with NXTG-Forge**
