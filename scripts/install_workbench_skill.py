"""Make the canonical authoring skill discoverable in this project."""
import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workbench.core import files

p = argparse.ArgumentParser()
p.add_argument("--host", choices=["codex", "claude-code"], default="codex")
a = p.parse_args()
source = ROOT / "skills/legal-eng-workbench"
target = ROOT / (".agents/skills" if a.host == "codex" else ".claude/skills") / source.name
if target.exists() and files(source) != files(target):
    raise SystemExit("Installed authoring skill differs; preserve it and review the change before reinstalling")
if not target.exists():
    shutil.copytree(source, target)
print(f"Installed {target}. Reload/discover project skills, then use $legal-eng-workbench.")
