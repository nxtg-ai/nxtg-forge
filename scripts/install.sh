#!/bin/bash
# NXTG-Forge Installation Script
# curl -fsSL https://raw.githubusercontent.com/nxtg-ai/nxtg-forge/main/install.sh | bash

set -e

FORGE_VERSION="1.0.0"
FORGE_REPO="https://github.com/nxtg-ai/nxtg-forge"
INSTALL_DIR="${HOME}/.nxtg-forge"
BIN_DIR="${HOME}/.local/bin"

echo "╔════════════════════════════════════════════════════════╗"
echo "║           NXTG-Forge Installer v${FORGE_VERSION}       ║"
echo "║     Self-Deploying AI Development Infrastructure       ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Check prerequisites
echo "🔍 Checking prerequisites..."

# Check Claude Code
if ! command -v claude &> /dev/null; then
    echo "❌ Claude Code CLI not found"
    echo ""
    echo "Please install Claude Code first:"
    echo "  npm install -g @anthropic-ai/claude-code"
    echo ""
    echo "Or visit: https://code.claude.ai"
    exit 1
fi
echo "  ✓ Claude Code CLI found"

# Check Node.js (for MCP servers)
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found (needed for MCP servers)"
    echo "  Install from: https://nodejs.org"
fi

# Check Python (for Forge tools)
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found"
    exit 1
fi
echo "  ✓ Python 3 found"

# Check Git
if ! command -v git &> /dev/null; then
    echo "❌ Git not found"
    exit 1
fi
echo "  ✓ Git found"

echo ""
echo "📦 Installing NXTG-Forge..."

# Create installation directory
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Clone or update forge repository
if [ -d "$INSTALL_DIR/.git" ]; then
    echo "  Updating existing installation..."
    cd "$INSTALL_DIR"
    git pull origin main
else
    echo "  Cloning NXTG-Forge..."
    git clone "$FORGE_REPO" "$INSTALL_DIR"
fi

# Install Python dependencies
echo ""
echo "🐍 Installing Python dependencies..."
cd "$INSTALL_DIR"
pip3 install -r requirements.txt --quiet

# Install Node dependencies (for MCP tools)
echo ""
echo "📦 Installing Node dependencies..."
npm install --prefix "$INSTALL_DIR" --quiet

# Create CLI symlinks
echo ""
echo "🔗 Creating CLI tools..."

cat > "$BIN_DIR/nxtg-forge" << 'EOF'
#!/bin/bash
# NXTG-Forge CLI wrapper
FORGE_HOME="${HOME}/.nxtg-forge"
exec python3 "$FORGE_HOME/forge/cli.py" "$@"
EOF

chmod +x "$BIN_DIR/nxtg-forge"

# Add to PATH if not already
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo ""
    echo "📝 Adding to PATH..."

    # Detect shell
    if [ -n "$BASH_VERSION" ]; then
        SHELL_RC="$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        SHELL_RC="$HOME/.zshrc"
    else
        SHELL_RC="$HOME/.profile"
    fi

    echo "" >> "$SHELL_RC"
    echo "# NXTG-Forge" >> "$SHELL_RC"
    echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$SHELL_RC"

    echo "  Added to $SHELL_RC"
    echo "  Run: source $SHELL_RC"
fi

# Install global Claude commands
echo ""
echo "🔧 Installing global Claude commands..."

GLOBAL_COMMANDS_DIR="${HOME}/.claude/commands"
mkdir -p "$GLOBAL_COMMANDS_DIR"

# Copy global commands
cp -r "$INSTALL_DIR/.claude/commands/"* "$GLOBAL_COMMANDS_DIR/"

echo "  ✓ Installed ${#INSTALL_DIR/.claude/commands/*} commands"

# Install MCP auto-detector as global
echo ""
echo "🔌 Setting up MCP auto-detection..."

cp "$INSTALL_DIR/.mcp/auto-detect.js" "$BIN_DIR/mcp-auto-detect"
chmod +x "$BIN_DIR/mcp-auto-detect"

# Configure Claude Code permissions
echo ""
echo "🔐 Configuring Claude Code permissions..."

# Create or update global Claude settings
CLAUDE_CONFIG="${HOME}/.claude.json"

if [ -f "$CLAUDE_CONFIG" ]; then
    echo "  Existing Claude config found"
else
    cat > "$CLAUDE_CONFIG" << 'EOF'
{
  "permissions": {
    "allow": [
      "Edit",
      "Read",
      "Grep",
      "LS",
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(python:*)",
      "Bash(pip:*)"
    ]
  }
}
EOF
    echo "  ✓ Created default Claude config"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🚀 Quick Start:"
echo ""
echo "  New Project:"
echo "    mkdir my-project && cd my-project"
echo "    /init nxtg-forge --new"
echo ""
echo "  Upgrade Existing:"
echo "    cd my-existing-project"
echo "    /init nxtg-forge --upgrade"
echo ""
echo "  CLI Tool:"
echo "    nxtg-forge --help"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📚 Documentation:"
echo "  https://github.com/your-org/nxtg-forge/wiki"
echo ""
echo "💡 Run 'source ~/.bashrc' (or your shell RC) to use CLI immediately"
echo ""
