#!/usr/bin/env python3
"""Bouwt het werkmappakket van Debug Coach.

Gebruik: python3 scripts/bouw_werkmap.py

Maakt dist/debug-coach-werkmap/ en dist/debug-coach-werkmap.zip:
- de werkmap-templates uit plugin/skills/start/templates/;
- een lege lokale plugin .coach/mijn-vaardigheden/ voor de eigen vaardigheden (missie 7);
- .agents/plugins/marketplace.json, de lokale catalogus mijn-werkmap die naar die plugin wijst.
De coach zelf zit niet in het pakket: die komt via GitHub (Add a marketplace met BinaryBjorn/debug-coach),
zodat een update van de coach de werkmap en mijn-vaardigheden nooit raakt.
"""
import json
import pathlib
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "plugin" / "skills" / "start" / "templates"
DIST = ROOT / "dist"
NAAM = "debug-coach-werkmap"

PLUGIN_JSON = {
    "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
    "name": "mijn-vaardigheden",
    "version": "0.1.0",
    "description": "Jouw eigen vaardigheden (skills), gemaakt in missie 7 van Debug Coach. Staat los van de coach: een update van de coach raakt deze map nooit.",
}

MARKETPLACE_JSON = {
    "name": "mijn-werkmap",
    "plugins": [
        {
            "name": "mijn-vaardigheden",
            "source": {"source": "local", "path": "./.coach/mijn-vaardigheden"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Productivity",
            "interface": {"displayName": "Mijn vaardigheden"},
        }
    ],
}

SKILLS_README = """# Mijn vaardigheden

> **Wat is dit?** Hier komen jouw eigen vaardigheden (skills). Nu is deze map nog leeg, en dat is goed zo.

Een vaardigheid is een vaste werkwijze die je AI één keer uitlegt en daarna altijd kan hergebruiken. In missie 7 maak je je eerste: de coach helpt je ze te schrijven en zet ze hier, elk in een eigen map met een bestand `SKILL.md`, bijvoorbeeld `eigen-weekverslag/SKILL.md`.

- **In ChatGPT** installeer je deze map één keer als de plugin `mijn-vaardigheden` (Plugins, tabblad Personal, catalogus `mijn-werkmap`). Elke vaardigheid die hier bijkomt, kan je daarna gebruiken met `@mijn-vaardigheden`.
- **In Claude** laadt deze map niet. Daar zet je een vaardigheid in `projecten/eigen-skills/`, verpak je ze als ZIP en upload je ze bij Customize > Skills. De coach legt dat uit in missie 7.

Deze map is van jou. Een update van de coach komt via GitHub en raakt deze map nooit.
"""


def schrijf_json(pad, data):
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bouw():
    if not TEMPLATES.is_dir():
        print("FOUT: templates niet gevonden in %s" % TEMPLATES, file=sys.stderr)
        return 1
    werkmap = DIST / NAAM
    if werkmap.exists():
        shutil.rmtree(werkmap)
    shutil.copytree(TEMPLATES, werkmap, ignore=shutil.ignore_patterns(".DS_Store"))

    mv = werkmap / ".coach" / "mijn-vaardigheden"
    schrijf_json(mv / "plugin.json", PLUGIN_JSON)
    (mv / "skills").mkdir(parents=True, exist_ok=True)
    (mv / "skills" / "README.md").write_text(SKILLS_README, encoding="utf-8")
    schrijf_json(werkmap / ".agents" / "plugins" / "marketplace.json", MARKETPLACE_JSON)

    z = DIST / (NAAM + ".zip")
    if z.exists():
        z.unlink()
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(werkmap.rglob("*")):
            if p.is_file():
                zf.write(p, pathlib.Path(NAAM) / p.relative_to(werkmap))
    print("klaar: %s en %s" % (werkmap.relative_to(ROOT), z.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(bouw())
