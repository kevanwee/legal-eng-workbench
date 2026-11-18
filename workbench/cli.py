import argparse
import json
from pathlib import Path
from . import core


def main(argv=None):
    p = argparse.ArgumentParser(description="Describe -> model -> skills -> rehearse/review -> release -> invoke")
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("describe", help="Start with a legal-work brief")
    a.add_argument("project", type=Path); a.add_argument("--brief", required=True, type=Path)
    a = sub.add_parser("model", help="Get authoring instructions or validate/import a host-authored model")
    a.add_argument("project", type=Path); a.add_argument("--manifest", type=Path)
    a = sub.add_parser("resolve", help="Generate methods or reuse exact compatible skill folders")
    a.add_argument("project", type=Path); a.add_argument("--reuse", action="append", default=[], metavar="ID=FOLDER")
    for name in ("build", "status"):
        a = sub.add_parser(name); a.add_argument("project", type=Path)
    a = sub.add_parser("rehearse", help="Run explicitly synthetic fixtures through the native runner")
    a.add_argument("project", type=Path); a.add_argument("--suite", required=True, type=Path)
    a = sub.add_parser("review")
    a.add_argument("project", type=Path); a.add_argument("--decision", choices=["approve", "reject"], required=True)
    a.add_argument("--actor", required=True); a.add_argument("--evidence", required=True); a.add_argument("--synthetic", action="store_true")
    a = sub.add_parser("release")
    a.add_argument("project", type=Path); a.add_argument("--out", type=Path, required=True)
    a.add_argument("--channel", choices=["rehearsal", "reviewed"], default="rehearsal")
    a = sub.add_parser("install")
    a.add_argument("release", type=Path); a.add_argument("--target", type=Path, required=True)
    a.add_argument("--host", choices=["codex", "claude-code"], default="codex")
    a = sub.add_parser("invoke", help="Print the host invocation; does not call a model")
    a.add_argument("release", type=Path)
    a = sub.add_parser("runtime", help="Pass through to the pinned native compiler/runner")
    a.add_argument("args", nargs=argparse.REMAINDER)
    args = p.parse_args(argv)
    try:
        cmd = args.command
        if cmd == "describe": result = core.describe(args.project, args.brief)
        elif cmd == "model": result = core.model(args.project, args.manifest)
        elif cmd == "resolve":
            reuse = {}
            for item in args.reuse:
                if "=" not in item: raise core.WorkbenchError("Use --reuse ID=FOLDER")
                key, value = item.split("=", 1)
                if key in reuse or not value: raise core.WorkbenchError("Duplicate or empty reuse mapping")
                reuse[key] = value
            result = core.resolve(args.project, reuse)
        elif cmd == "build": result = core.build(args.project)
        elif cmd == "rehearse": result = core.rehearse(args.project, args.suite)
        elif cmd == "review": result = core.review(args.project, args.decision, args.actor, args.evidence, args.synthetic)
        elif cmd == "release": result = core.release(args.project, args.out, args.channel)
        elif cmd == "install": result = core.install(args.release, args.target, args.host)
        elif cmd == "invoke":
            info = core.verified_release(args.release)
            result = {"prompt": f"Use ${info['workflow']} to run the packaged workflow on the supplied inputs. Begin with scope, evidence and host capability checks.",
                      "channel": info["channel"], "model_invoked": False, "requires": "Install in the target host project and discover/reload the skill first."}
        elif cmd == "status":
            result = {"files": [n for n in ("brief.md", "manifest.json", "resolution.json", "candidate.json", "rehearsal.json", "review.json") if (args.project / n).exists()]}
            if (args.project / "candidate.json").exists(): result["candidate"] = core.current(args.project)[1]
        else: result = core.native(*args.args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if isinstance(result, dict) and result.get("passed") is False else 0
    except (core.WorkbenchError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 2
