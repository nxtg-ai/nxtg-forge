nxtg-forge/
├── .claude/
│   ├── settings.json              # Project-level Claude Code config
│   ├── state.json                 # CRITICAL: Current project state
│   ├── forge.config.json          # NXTG-Forge configuration
│   │
│   ├── commands/                  # Custom slash commands
│   │   ├── init.md               # /init - Initialize new project
│   │   ├── upgrade.md            # /upgrade - Upgrade existing project
│   │   ├── status.md             # /status - Show project state
│   │   ├── deploy.md             # /deploy - Deploy system
│   │   ├── checkpoint.md         # /checkpoint - Save state
│   │   ├── restore.md            # /restore - Restore from checkpoint
│   │   ├── spec.md               # /spec - Generate project spec
│   │   ├── feature.md            # /feature - Add new feature
│   │   ├── integrate.md          # /integrate - Add integration
│   │   ├── agent-assign.md       # /agent-assign - Assign to agent
│   │   └── gap-analysis.md       # /gap-analysis - Analyze gaps
│   │
│   ├── skills/                    # Skill library
│   │   ├── core/
│   │   │   ├── nxtg-forge.md     # Meta-skill about this system
│   │   │   ├── architecture.md
│   │   │   ├── coding-standards.md
│   │   │   └── testing.md
│   │   ├── domain/               # Generated per-project
│   │   ├── tech-stack/           # Generated based on stack
│   │   └── agents/               # Agent-specific skills
│   │       ├── lead-architect.md
│   │       ├── backend-master.md
│   │       ├── cli-artisan.md
│   │       ├── platform-builder.md
│   │       ├── integration-specialist.md
│   │       └── qa-sentinel.md
│   │
│   ├── hooks/                     # Lifecycle hooks
│   │   ├── pre-task.sh
│   │   ├── post-task.sh
│   │   ├── on-error.sh
│   │   ├── on-file-change.sh
│   │   └── state-sync.sh         # Auto-save state
│   │
│   ├── templates/                 # File generation templates
│   │   ├── backend/
│   │   │   ├── fastapi/
│   │   │   ├── django/
│   │   │   └── express/
│   │   ├── frontend/
│   │   │   ├── react/
│   │   │   ├── vue/
│   │   │   └── svelte/
│   │   ├── cli/
│   │   │   ├── python-click/
│   │   │   └── go-cobra/
│   │   └── infrastructure/
│   │       ├── docker/
│   │       ├── kubernetes/
│   │       └── terraform/
│   │
│   ├── checkpoints/              # State checkpoints
│   │   ├── checkpoint-001.json
│   │   ├── checkpoint-002.json
│   │   └── latest.json -> checkpoint-002.json
│   │
│   └── workflows/                # Automated workflows
│       ├── tdd-cycle.sh
│       ├── feature-pipeline.sh
│       ├── code-review.sh
│       └── deploy-pipeline.sh
│
├── .mcp/                         # MCP auto-configuration
│   ├── auto-detect.js           # Auto-detect needed MCP servers
│   ├── servers/                 # MCP server definitions
│   │   ├── github.json
│   │   ├── postgres.json
│   │   ├── stripe.json
│   │   └── custom/
│   └── config-generator.js      # Generate MCP config
│
├── forge/                        # Forge core system
│   ├── cli.py                   # Forge CLI tool
│   ├── state_manager.py         # State management
│   ├── spec_generator.py        # Interactive spec builder
│   ├── file_generator.py        # File generation engine
│   ├── mcp_detector.py          # MCP auto-detection
│   ├── gap_analyzer.py          # Gap analysis
│   └── agents/
│       ├── orchestrator.py      # Agent coordination
│       └── dispatcher.py        # Task distribution
│
├── docs/
│   ├── README.md                # Getting started
│   ├── FORGE-GUIDE.md           # Complete guide
│   ├── STATE-RECOVERY.md        # State recovery guide
│   └── CUSTOMIZATION.md         # Customization guide
│
├── scripts/
│   ├── install.sh               # Installation script
│   ├── upgrade.sh               # Upgrade script
│   └── bootstrap.sh             # Bootstrap new project
│
└── README.md
