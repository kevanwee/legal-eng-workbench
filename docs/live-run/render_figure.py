"""Render docs/assets/live-run.svg from the recorded live-run evidence in this folder.

Every quote, citation, classification and outcome in the figure is read from the
JSON files beside this script; nothing is typed in by hand.
"""
import json
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent
OUT = HERE.parent / "assets" / "live-run.svg"
findings = json.loads((HERE / "approval/findings.json").read_text(encoding="utf-8"))
status = {run: json.loads((HERE / run / "status-final.json").read_text(encoding="utf-8"))["result"] for run in ("approval", "rejection")}
source = (HERE / "inputs/contract-c.txt").read_text(encoding="utf-8").splitlines()
injection_line = next(i for i, line in enumerate(source, 1) if "Document instruction" in line)
assert any(f"line {injection_line}" in u and "not followed" in u for u in findings["unresolved"]), "host did not record the instruction"

PILL = {"express-consent": ("#fde7d9", "#9a3b12"), "express-exception": ("#dcefe4", "#1d6b43"),
        "assignment-only": ("#e6e9f2", "#3c4a6b"), "unresolved": ("#fbf0c9", "#7a5a00")}
W, row_h, top = 1200, 58, 150
rows = findings["findings"]
H = top + row_h * len(rows) + 250
s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" role="img" aria-label="Live run findings">',
     "<style>text{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;fill:#1d2733}"
     ".mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.dim{fill:#5d6b78}</style>",
     f'<rect width="{W}" height="{H}" rx="14" fill="#fbfaf7" stroke="#dcd8cf"/>',
     '<text x="40" y="52" style="font-size:13px;letter-spacing:.12em" class="dim">LIVE RUN · FRESH CODEX SESSION · GENERATED SKILL</text>',
     '<text x="40" y="92" style="font-size:28px;font-weight:600">$consent-triage on three contract extracts</text>',
     '<text x="40" y="122" style="font-size:15px" class="dim">Findings register written by the host model. Each quote below matches the cited source line exactly.</text>']
for i, f in enumerate(rows):
    y = top + i * row_h
    cite = f"{f['document'].replace('.txt', '')}:{f['line_start']}" + (f"–{f['line_end']}" if f["line_end"] != f["line_start"] else "")
    quote = f["quote"].replace("\n", " ")
    quote = quote if len(quote) <= 88 else quote[:85] + "…"
    bg, fg = PILL[f["classification"]]
    s += [f'<line x1="40" x2="{W-40}" y1="{y}" y2="{y}" stroke="#e7e3da"/>',
          f'<text x="40" y="{y+35}" class="mono" style="font-size:14px">{escape(cite)}</text>',
          f'<text x="230" y="{y+35}" style="font-size:15px">“{escape(quote)}”</text>',
          f'<rect x="{W-230}" y="{y+15}" width="190" height="28" rx="14" fill="{bg}"/>',
          f'<text x="{W-135}" y="{y+34}" text-anchor="middle" class="mono" style="font-size:13px;fill:{fg}">{f["classification"]}</text>']
y = top + row_h * len(rows)
inj = source[injection_line - 1]
s += [f'<line x1="40" x2="{W-40}" y1="{y}" y2="{y}" stroke="#e7e3da"/>',
      f'<rect x="40" y="{y+22}" width="{W-80}" height="62" rx="10" fill="#fff4f2" stroke="#f0c9c2"/>',
      f'<text x="60" y="{y+48}" class="mono" style="font-size:14px;fill:#9b2c1f">contract-c:{injection_line}</text>',
      f'<text x="230" y="{y+48}" style="font-size:15px">“{escape(inj)}”</text>',
      f'<text x="230" y="{y+70}" style="font-size:14px" class="dim">Embedded instruction recorded as evidence and not followed. Missing Schedule 4 kept unresolved.</text>']
y += 110
for j, run in enumerate(("approval", "rejection")):
    st = status[run]
    x = 40 + j * ((W - 100) // 2 + 20)
    w = (W - 100) // 2
    ok = st["business_success"]
    s += [f'<rect x="{x}" y="{y}" width="{w}" height="96" rx="10" fill="#ffffff" stroke="#dcd8cf"/>',
          f'<text x="{x+20}" y="{y+30}" style="font-size:13px;letter-spacing:.1em" class="dim">{run.upper()} RUN · SYNTHETIC PARTNER DECISION</text>',
          f'<text x="{x+20}" y="{y+62}" class="mono" style="font-size:17px">status={st["status"]}  outcome={st["outcomes"][0]["code"]}</text>',
          f'<text x="{x+20}" y="{y+84}" class="mono" style="font-size:14px;fill:{"#1d6b43" if ok else "#9b2c1f"}">business_success={str(ok).lower()}</text>']
s.append(f'<text x="40" y="{H-18}" style="font-size:12px" class="dim">Rendered by docs/live-run/render_figure.py from the recorded run evidence. Synthetic documents; not legal advice.</text>')
s.append("</svg>")
OUT.write_text("\n".join(s) + "\n", encoding="utf-8")
print(OUT)
