"""Fresh synthetic journey, including installation into clean host folders."""
import json
from pathlib import Path
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workbench import core


def main():
    folder = ROOT / ".workbench" / ("demo-" + uuid.uuid4().hex[:8])
    project = folder / "project"
    example = ROOT / "examples/buy-side-dd"
    core.describe(project, example / "brief.md")
    core.model(project, example / "manifest.json")
    core.resolve(project)
    build = core.build(project)
    report = core.rehearse(project, example / "suite.json")
    assert report["passed"], report
    core.review(project, "reject", "SYNTHETIC reviewer", "SYNTHETIC refusal probe", True)
    try:
        core.release(project, folder / "releases")
    except core.WorkbenchError:
        pass
    else:
        raise AssertionError("Rejected candidate released")
    core.review(project, "approve", "SYNTHETIC reviewer", "SYNTHETIC exact candidate and route rehearsal inspected", True)
    released = core.release(project, folder / "releases")
    installed = []
    for host in ("codex", "claude-code"):
        receipt = core.install(released["release"], folder / host, host)
        skill = Path(receipt["installed"])
        validation = core.native("validate", skill / "manifest.json", runtime=skill / "scripts/runtime.pyz")
        assert validation["blueprint_hash"] == core.current(project)[1]["blueprint_hash"]
        installed.append(receipt)
    result = {"status": "passed", "synthetic": True, "cases": len(report["cases"]), "candidate": build,
              "refusal_blocks_release": True, "release": released, "installed": installed,
              "actual_host_model_execution": False, "limits": report["limitations"]}
    core.write(folder / "receipt.json", result)
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    main()
