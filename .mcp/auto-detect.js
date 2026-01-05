#!/usr/bin/env node
/**
 * NXTG-Forge MCP Auto-Detection System
 *
 * Analyzes project and automatically configures needed MCP servers
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class MCPAutoDetector {
  constructor(projectRoot) {
    this.projectRoot = projectRoot;
    this.spec = null;
    this.packageJson = null;
    this.requirements = null;
    this.recommendations = [];
  }

  async detect() {
    console.log('🔍 Detecting required MCP servers...\n');

    await this.loadProjectFiles();

    // Detection strategies
    this.detectFromSpec();
    this.detectFromDependencies();
    this.detectFromFiles();
    this.detectFromGit();
    this.detectFromArchitecture();

    return this.recommendations;
  }

  loadProjectFiles() {
    // Load project spec
    const specPath = path.join(this.projectRoot, 'docs', 'PROJECT-SPEC.md');
    if (fs.existsSync(specPath)) {
      this.spec = fs.readFileSync(specPath, 'utf-8');
    }

    // Load package.json
    const pkgPath = path.join(this.projectRoot, 'package.json');
    if (fs.existsSync(pkgPath)) {
      this.packageJson = JSON.parse(fs.readFileSync(pkgPath, 'utf-8'));
    }

    // Load requirements.txt
    const reqPath = path.join(this.projectRoot, 'requirements.txt');
    if (fs.existsSync(reqPath)) {
      this.requirements = fs.readFileSync(reqPath, 'utf-8');
    }
  }

  detectFromSpec() {
    if (!this.spec) return;

    // GitHub integration
    if (this.spec.match(/github|pull request|ci\/cd/i)) {
      this.addRecommendation({
        name: 'github',
        priority: 'high',
        reason: 'Project spec mentions GitHub/PR workflow',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', '@modelcontextprotocol/server-github'],
          env: {
            GITHUB_TOKEN: '${GITHUB_TOKEN}'
          }
        }
      });
    }

    // Stripe integration
    if (this.spec.match(/payment|stripe|subscription/i)) {
      this.addRecommendation({
        name: 'stripe',
        priority: 'high',
        reason: 'Payment processing mentioned in spec',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', 'mcp-stripe'],
          env: {
            STRIPE_API_KEY: '${STRIPE_API_KEY}'
          }
        }
      });
    }

    // Database
    if (this.spec.match(/postgresql|postgres/i)) {
      this.addRecommendation({
        name: 'postgres',
        priority: 'high',
        reason: 'PostgreSQL database in architecture',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', '@modelcontextprotocol/server-postgres'],
          env: {
            DATABASE_URL: '${DATABASE_URL}'
          }
        }
      });
    }

    // Slack integration
    if (this.spec.match(/slack|notification|messaging/i)) {
      this.addRecommendation({
        name: 'slack',
        priority: 'medium',
        reason: 'Slack integration mentioned',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', '@modelcontextprotocol/server-slack'],
          env: {
            SLACK_BOT_TOKEN: '${SLACK_BOT_TOKEN}',
            SLACK_TEAM_ID: '${SLACK_TEAM_ID}'
          }
        }
      });
    }
  }

  detectFromDependencies() {
    // Node dependencies
    if (this.packageJson && this.packageJson.dependencies) {
      const deps = Object.keys(this.packageJson.dependencies);

      if (deps.includes('stripe')) {
        this.addRecommendation({
          name: 'stripe',
          priority: 'high',
          reason: 'Stripe package in dependencies'
        });
      }

      if (deps.includes('@octokit/rest') || deps.includes('octokit')) {
        this.addRecommendation({
          name: 'github',
          priority: 'high',
          reason: 'GitHub Octokit in dependencies'
        });
      }
    }

    // Python dependencies
    if (this.requirements) {
      if (this.requirements.includes('stripe')) {
        this.addRecommendation({
          name: 'stripe',
          priority: 'high',
          reason: 'Stripe in Python requirements'
        });
      }

      if (this.requirements.match(/psycopg|sqlalchemy/)) {
        this.addRecommendation({
          name: 'postgres',
          priority: 'high',
          reason: 'PostgreSQL drivers in requirements'
        });
      }
    }
  }

  detectFromFiles() {
    // Check for Docker usage
    if (fs.existsSync(path.join(this.projectRoot, 'Dockerfile')) ||
        fs.existsSync(path.join(this.projectRoot, 'docker-compose.yml'))) {
      this.addRecommendation({
        name: 'docker',
        priority: 'medium',
        reason: 'Docker files detected',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', 'mcp-docker']
        }
      });
    }

    // Check for Kubernetes
    if (fs.existsSync(path.join(this.projectRoot, 'k8s')) ||
        fs.existsSync(path.join(this.projectRoot, 'kubernetes'))) {
      this.addRecommendation({
        name: 'kubernetes',
        priority: 'medium',
        reason: 'Kubernetes configs detected',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', 'mcp-kubernetes']
        }
      });
    }
  }

  detectFromGit() {
    // Check if in git repo
    try {
      execSync('git rev-parse --git-dir', { cwd: this.projectRoot, stdio: 'ignore' });

      // Check remote
      const remote = execSync('git remote get-url origin', {
        cwd: this.projectRoot,
        encoding: 'utf-8'
      }).trim();

      if (remote.includes('github.com')) {
        this.addRecommendation({
          name: 'github',
          priority: 'high',
          reason: 'GitHub repository detected'
        });
      } else if (remote.includes('gitlab.com')) {
        this.addRecommendation({
          name: 'gitlab',
          priority: 'high',
          reason: 'GitLab repository detected',
          config: {
            type: 'stdio',
            command: 'npx',
            args: ['-y', 'mcp-gitlab'],
            env: {
              GITLAB_TOKEN: '${GITLAB_TOKEN}'
            }
          }
        });
      }
    } catch (e) {
      // Not a git repo or no remote
    }
  }

  detectFromArchitecture() {
    // Load state if exists
    const statePath = path.join(this.projectRoot, '.claude', 'state.json');
    if (!fs.existsSync(statePath)) return;

    const state = JSON.parse(fs.readFileSync(statePath, 'utf-8'));

    // Based on architecture patterns
    if (state.architecture?.database?.type === 'postgresql') {
      this.addRecommendation({
        name: 'postgres',
        priority: 'high',
        reason: 'PostgreSQL in architecture state'
      });
    }

    if (state.architecture?.cache?.type === 'redis') {
      this.addRecommendation({
        name: 'redis',
        priority: 'medium',
        reason: 'Redis in architecture state',
        config: {
          type: 'stdio',
          command: 'npx',
          args: ['-y', 'mcp-redis'],
          env: {
            REDIS_URL: '${REDIS_URL}'
          }
        }
      });
    }

    // Check for planned integrations
    if (state.development?.features?.planned) {
      state.development.features.planned.forEach(feature => {
        const name = feature.name.toLowerCase();

        if (name.includes('payment') || name.includes('stripe')) {
          this.addRecommendation({
            name: 'stripe',
            priority: 'medium',
            reason: `Planned feature: ${feature.name}`
          });
        }

        if (name.includes('email') || name.includes('sendgrid')) {
          this.addRecommendation({
            name: 'sendgrid',
            priority: 'medium',
            reason: `Planned feature: ${feature.name}`,
            config: {
              type: 'stdio',
              command: 'npx',
              args: ['-y', 'mcp-sendgrid'],
              env: {
                SENDGRID_API_KEY: '${SENDGRID_API_KEY}'
              }
            }
          });
        }
      });
    }
  }

  addRecommendation(rec) {
    // Deduplicate and merge configs
    const existing = this.recommendations.find(r => r.name === rec.name);
    if (existing) {
      existing.priority = this.higherPriority(existing.priority, rec.priority);
      existing.reason += `; ${rec.reason}`;
    } else {
      // Add default config if not provided
      if (!rec.config) {
        rec.config = this.getDefaultConfig(rec.name);
      }
      this.recommendations.push(rec);
    }
  }

  higherPriority(p1, p2) {
    const priorities = { high: 3, medium: 2, low: 1 };
    return priorities[p1] >= priorities[p2] ? p1 : p2;
  }

  getDefaultConfig(serverName) {
    const configs = {
      github: {
        type: 'stdio',
        command: 'npx',
        args: ['-y', '@modelcontextprotocol/server-github'],
        env: { GITHUB_TOKEN: '${GITHUB_TOKEN}' }
      },
      postgres: {
        type: 'stdio',
        command: 'npx',
        args: ['-y', '@modelcontextprotocol/server-postgres'],
        env: { DATABASE_URL: '${DATABASE_URL}' }
      },
      // ... other defaults
    };

    return configs[serverName] || {
      type: 'stdio',
      command: 'npx',
      args: ['-y', `mcp-${serverName}`]
    };
  }

  async configure() {
    console.log('🔧 Configuring MCP servers...\n');

    for (const rec of this.recommendations) {
      console.log(`Adding ${rec.name} (${rec.priority} priority)`);
      console.log(`  Reason: ${rec.reason}`);

      try {
        // Add MCP server via claude CLI
        const envVars = rec.config.env
          ? Object.entries(rec.config.env)
              .map(([k, v]) => `-e ${k}=${v}`)
              .join(' ')
          : '';

        const cmd = `claude mcp add-json ${rec.name} '${JSON.stringify(rec.config)}' --scope user ${envVars}`;

        execSync(cmd, { stdio: 'inherit', cwd: this.projectRoot });
        console.log(`  ✓ Configured\n`);
      } catch (error) {
        console.log(`  ✗ Failed: ${error.message}\n`);
      }
    }

    // Update state.json
    this.updateState();
  }

  updateState() {
    const statePath = path.join(this.projectRoot, '.claude', 'state.json');
    if (!fs.existsSync(statePath)) return;

    const state = JSON.parse(fs.readFileSync(statePath, 'utf-8'));

    if (!state.mcp_servers) {
      state.mcp_servers = { configured: [], recommended: [] };
    }

    // Mark as configured
    this.recommendations.forEach(rec => {
      state.mcp_servers.configured.push({
        name: rec.name,
        status: 'connected',
        auto_detected: true,
        reason: rec.reason,
        priority: rec.priority
      });
    });

    fs.writeFileSync(statePath, JSON.stringify(state, null, 2));
  }
}

// CLI Interface
if (require.main === module) {
  const detector = new MCPAutoDetector(process.cwd());

  detector.detect()
    .then(recommendations => {
      console.log('📋 MCP Server Recommendations:\n');
      recommendations
        .sort((a, b) => {
          const priorities = { high: 3, medium: 2, low: 1 };
          return priorities[b.priority] - priorities[a.priority];
        })
        .forEach(rec => {
          const icon = rec.priority === 'high' ? '🔴' : rec.priority === 'medium' ? '🟡' : '🟢';
          console.log(`${icon} ${rec.name} (${rec.priority})`);
          console.log(`   ${rec.reason}\n`);
        });

      // Ask to configure
      const readline = require('readline');
      const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });

      rl.question('\nConfigure these MCP servers now? (y/n): ', async (answer) => {
        if (answer.toLowerCase() === 'y') {
          await detector.configure();
          console.log('\n✅ MCP servers configured!');
          console.log('Run `/mcp` in Claude Code to verify connections.\n');
        }
        rl.close();
      });
    });
}

module.exports = MCPAutoDetector;
