#!/usr/bin/env python3
"""Synchronize version across all project files"""

import json
import re
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

PROJECT_ROOT = Path(__file__).parent.parent


def get_canonical_version() -> str:
    """Read version from pyproject.toml"""
    with open(PROJECT_ROOT / "pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]


def sync_package_json(version: str, check_only: bool = False) -> bool:
    """Update package.json"""
    file = PROJECT_ROOT / "package.json"
    data = json.loads(file.read_text())

    if check_only:
        if data["version"] != version:
            print(f"❌ package.json has {data['version']}, expected {version}")
            return False
        return True

    data["version"] = version
    file.write_text(json.dumps(data, indent=2) + "\n")
    print(f"✓ Updated package.json to {version}")
    return True


def sync_install_script(version: str, check_only: bool = False) -> bool:
    """Update scripts/install.sh"""
    file = PROJECT_ROOT / "scripts" / "install.sh"
    content = file.read_text()

    match = re.search(r'FORGE_VERSION="([^"]+)"', content)
    if match:
        current = match.group(1)
        if check_only:
            if current != version:
                print(f"❌ scripts/install.sh has {current}, expected {version}")
                return False
            return True

        updated = re.sub(
            r'FORGE_VERSION="[^"]+"',
            f'FORGE_VERSION="{version}"',
            content
        )
        file.write_text(updated)
        print(f"✓ Updated scripts/install.sh to {version}")
    return True


def sync_state_template(version: str, check_only: bool = False) -> bool:
    """Update .claude/state.json.template"""
    file = PROJECT_ROOT / ".claude" / "state.json.template"
    data = json.loads(file.read_text())

    if check_only:
        issues = []
        if data.get("version") != version:
            issues.append(f"state.json.template version field: {data.get('version')}")
        if data.get("project", {}).get("forge_version") != version:
            issues.append(f"state.json.template forge_version: {data.get('project', {}).get('forge_version')}")
        if issues:
            print(f"❌ .claude/state.json.template mismatches:")
            for issue in issues:
                print(f"   - {issue}")
            return False
        return True

    data["version"] = version
    if "project" not in data:
        data["project"] = {}
    data["project"]["forge_version"] = version
    file.write_text(json.dumps(data, indent=2) + "\n")
    print(f"✓ Updated .claude/state.json.template to {version}")
    return True


def main():
    check_only = "--check" in sys.argv

    version = get_canonical_version()

    if not check_only:
        print(f"Canonical version from pyproject.toml: {version}")
        print()

    results = [
        sync_package_json(version, check_only),
        sync_install_script(version, check_only),
        sync_state_template(version, check_only),
    ]

    if check_only:
        if all(results):
            print(f"✅ All files synchronized with version {version}")
            sys.exit(0)
        else:
            print(f"\n❌ Version synchronization check FAILED")
            print(f"Run: python scripts/sync-version.py")
            sys.exit(1)
    else:
        print()
        print(f"✅ All files synchronized to version {version}")


if __name__ == "__main__":
    main()
