#!/bin/bash
# Bump version and sync across project

set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/bump-version.sh <major|minor|patch|VERSION>"
    echo "Examples:"
    echo "  ./scripts/bump-version.sh patch   # 1.0.0 -> 1.0.1"
    echo "  ./scripts/bump-version.sh minor   # 1.0.1 -> 1.1.0"
    echo "  ./scripts/bump-version.sh major   # 1.1.0 -> 2.0.0"
    echo "  ./scripts/bump-version.sh 1.2.3   # Set to 1.2.3"
    exit 1
fi

# Get current version
CURRENT=$(python3 -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])" 2>/dev/null || python3 -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])")
echo "Current version: $CURRENT"

# Calculate new version
if [[ "$1" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    NEW_VERSION="$1"
else
    IFS='.' read -r major minor patch <<< "$CURRENT"
    case "$1" in
        major) NEW_VERSION="$((major + 1)).0.0" ;;
        minor) NEW_VERSION="${major}.$((minor + 1)).0" ;;
        patch) NEW_VERSION="${major}.${minor}.$((patch + 1))" ;;
        *) echo "Invalid bump type: $1"; exit 1 ;;
    esac
fi

echo "New version: $NEW_VERSION"
echo

# Update pyproject.toml
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/^version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml
else
    # Linux
    sed -i "s/^version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml
fi
echo "✓ Updated pyproject.toml"

# Sync all other files
python3 scripts/sync-version.py

# Update CHANGELOG.md
TODAY=$(date +%Y-%m-%d)
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s/## \[Unreleased\]/## [Unreleased]\n\n## [$NEW_VERSION] - $TODAY/" CHANGELOG.md
else
    sed -i "s/## \[Unreleased\]/## [Unreleased]\n\n## [$NEW_VERSION] - $TODAY/" CHANGELOG.md
fi
echo "✓ Updated CHANGELOG.md"

echo
echo "✅ Version bumped from $CURRENT to $NEW_VERSION"
echo
echo "Next steps:"
echo "  1. Review changes: git diff"
echo "  2. Update CHANGELOG.md with release notes"
echo "  3. Commit: git commit -am 'chore: bump version to $NEW_VERSION'"
echo "  4. Tag: git tag -a v$NEW_VERSION -m 'Release v$NEW_VERSION'"
echo "  5. Push: git push && git push --tags"
