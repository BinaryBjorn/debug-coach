"""Tests voor bouwrun dc-r1-coach (Debug Coach, run 1). Python 3.9, enkel standaardbibliotheek.
Elke testnaam bevat het feature-ID (C01..C13, BASIS); tests/feature.py selecteert daarop."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TESTS = ROOT / "tests"
GEDEELD = TESTS / "fixtures" / "gedeeld"
PLUGIN = ROOT / "plugin"
SKILLS = PLUGIN / "skills"
TEMPL = SKILLS / "start" / "templates"
MISSIES = PLUGIN / "missies"
VIDEOS = ROOT / "videos"
SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
VIDEO_SLUGS = ["welkom", "klaarzetten", "missie-3", "missie-5", "missie-7", "coach-uitzetten"]
MISSIE_VIDEO = {1: "geen", 2: "geen", 3: "missie-3", 4: "geen", 5: "missie-5", 6: "geen", 7: "missie-7"}
KOPPEN = ["## Doel", "## Resultaat", "## Route ChatGPT", "## Route Claude", "## Klaar als",
          "## Wat kan hier fout gaan", "## Begrippen"]
SLASH = re.compile(r"(?<![\w/.:`])/(start|missie|uitdaging|uitleg|coach|plugin|week)\b")
EM_DASH = "—"


def lees(p):
    return pathlib.Path(p).read_text(encoding="utf-8")


def link_cfg():
    return json.loads(lees(GEDEELD / "voortgangslink.json"))


def sectie(tekst, kop):
    """Inhoud onder een kop van niveau 2 tot de volgende kop van niveau 2."""
    m = re.search(r"^" + re.escape(kop) + r"[ \t]*$(.*?)(?=^## |\Z)", tekst, re.M | re.S)
    return m.group(1) if m else None


def subsectie(tekst, kop):
    m = re.search(r"^" + re.escape(kop) + r"[ \t]*$(.*?)(?=^##+ |\Z)", tekst, re.M | re.S)
    return m.group(1) if m else None


def frontmatter(tekst):
    m = re.match(r"^---\n(.*?)\n---\n", tekst, re.S)
    if not m:
        return None, []
    regels = [r for r in m.group(1).splitlines() if r.strip()]
    d = {}
    for r in regels:
        k, _, v = r.partition(":")
        d[k.strip()] = v.strip()
    return d, [r.partition(":")[0].strip() for r in regels]


def skill(naam):
    return lees(SKILLS / naam / "SKILL.md")


def missie(n):
    return lees(MISSIES / ("missie-%02d.md" % n))


def concrete_links(tekst):
    """Vervang de plaatshouders en geef alle voortgangslinks terug."""
    t = (tekst.replace("<coachcode>", "ab12cd34").replace("{coachcode}", "ab12cd34")
         .replace("<stap>", "m1").replace("m<N>", "m1").replace("m<n>", "m1")
         .replace("t<trede>", "t1").replace("t<N>", "t1"))
    return re.findall(r"https://debug\.marketing/coach/v\?[^\s)`>\]\"']*", t)


def link_geldig(url):
    cfg = link_cfg()
    basis, _, query = url.partition("?")
    if basis != cfg["basis"]:
        return False
    params = dict(p.partition("=")[::2] for p in query.split("&") if p)
    if set(params) != {"s", "k"}:
        return False
    return bool(re.match(cfg["regex_s"], params["s"]) and re.match(cfg["regex_k"], params["k"]))


# ---------- mini-validator voor script.schema.json (enkel wat het schema gebruikt) ----------
def valideer(obj, schema, pad="$"):
    fouten = []
    if "enum" in schema and obj not in schema["enum"]:
        fouten.append("%s: %r niet in %r" % (pad, obj, schema["enum"]))
    t = schema.get("type")
    typen = {"object": dict, "array": list, "string": str, "integer": int}
    if t == "number":
        if not isinstance(obj, (int, float)) or isinstance(obj, bool):
            return fouten + ["%s: geen getal" % pad]
        if "minimum" in schema and obj < schema["minimum"]:
            fouten.append("%s: < minimum" % pad)
        if "maximum" in schema and obj > schema["maximum"]:
            fouten.append("%s: > maximum" % pad)
    elif t in typen and not isinstance(obj, typen[t]):
        return fouten + ["%s: geen %s" % (pad, t)]
    if t == "string":
        if "pattern" in schema and not re.search(schema["pattern"], obj):
            fouten.append("%s: patroon" % pad)
        if len(obj) < schema.get("minLength", 0):
            fouten.append("%s: te kort" % pad)
    if t == "object":
        for k in schema.get("required", []):
            if k not in obj:
                fouten.append("%s: %s ontbreekt" % (pad, k))
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for k in obj:
                if k not in props:
                    fouten.append("%s: onbekende sleutel %s" % (pad, k))
        for k, v in obj.items():
            if k in props:
                fouten += valideer(v, props[k], pad + "." + k)
    if t == "array":
        if len(obj) < schema.get("minItems", 0):
            fouten.append("%s: te weinig items" % pad)
        if "maxItems" in schema and len(obj) > schema["maxItems"]:
            fouten.append("%s: te veel items" % pad)
        for i, it in enumerate(obj):
            fouten += valideer(it, schema.get("items", {}), "%s[%d]" % (pad, i))
    return fouten


class Basis(unittest.TestCase):
    def test_BASIS_lekcheck(self):
        # Vingerafdrukken (sha256, kleine letters) van namen die nooit in de openbare plugin mogen staan,
        # zodat de namen zelf niet in deze openbare repo staan.
        verboden_fp = {"05a642215a9ffabdf33cdcb5fb0e909fe8e51e662fb792d4f94d423982a32cb6", "428659af88676979d314d9684b4da6e8f40c8f262cad0da63cfeb9bc43eed082", "4a13e5a8415efbb88b976917559270de49eae1531604050ac5cb21168070e761", "7baa7f41869d29c14a2c4c548934bf8c9d159c7bcccfe859c0a4e5e442e233da"}
        adres = re.compile(r"@hotmail\.com", re.I)
        doelen = [PLUGIN, VIDEOS, ROOT / "README.md"]
        for d in doelen:
            if not d.exists():
                continue
            bestanden = [d] if d.is_file() else [p for p in d.rglob("*") if p.is_file()]
            for p in bestanden:
                try:
                    t = p.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                self.assertIsNone(adres.search(t), "lek in %s" % p.relative_to(ROOT))
                for w in re.findall(r"[a-z]+", t.lower()):
                    self.assertNotIn(hashlib.sha256(w.encode()).hexdigest(), verboden_fp, "lek in %s" % p.relative_to(ROOT))

    def test_BASIS_json_geldig(self):
        for d in (PLUGIN, VIDEOS):
            if d.exists():
                for p in d.rglob("*.json"):
                    json.loads(lees(p))

    def test_BASIS_hash_gedeeld(self):
        for regel in lees(TESTS / "gedeeld.sha256").splitlines():
            h, naam = regel.split()
            self.assertEqual(hashlib.sha256((GEDEELD / naam).read_bytes()).hexdigest(), h, naam)


class C01(unittest.TestCase):
    def test_C01_manifesten(self):
        a = json.loads(lees(PLUGIN / "plugin.json"))
        b = json.loads(lees(PLUGIN / ".claude-plugin" / "plugin.json"))
        self.assertEqual(a.get("$schema"), SCHEMA_URL)
        self.assertEqual(a["name"], "debug-coach")
        for k in ("name", "version", "description"):
            self.assertTrue(a.get(k))
            self.assertEqual(a[k], b.get(k), k)

    def test_C01_catalogus_en_verhuis(self):
        m = json.loads(lees(ROOT / ".claude-plugin" / "marketplace.json"))
        self.assertEqual(m["plugins"][0]["name"], "debug-coach")
        self.assertEqual(m["plugins"][0]["source"], "./plugin")
        self.assertFalse((ROOT / "skills").exists(), "skills/ staat nog in de root")
        self.assertFalse((ROOT / "missies").exists(), "missies/ staat nog in de root")
        self.assertFalse((ROOT / ".claude-plugin" / "plugin.json").exists())


class C02(unittest.TestCase):
    def test_C02_bestanden(self):
        for f in ("CLAUDE.md", "AGENTS.md", "ik/profiel.md", "voortgang.md", "feedback.md",
                  "successen.md", "projecten/README.md"):
            self.assertTrue((TEMPL / f).is_file(), f)

    def test_C02_brein_en_profiel(self):
        for f in ("CLAUDE.md", "AGENTS.md"):
            self.assertRegex(lees(TEMPL / f), r"\*\*Stand:\*\* (uitgebreid|kort|uit)")
        p = lees(TEMPL / "ik" / "profiel.md")
        for r in (r"^- \*\*Platform:\*\* \[TODO\]$", r"^- \*\*Account:\*\* \[TODO\]$",
                  r"^- \*\*Coachcode:\*\* \[TODO\]$", r"^- \*\*Tools:\*\* \[TODO\]"):
            self.assertRegex(p, re.compile(r, re.M))

    def test_C02_voortgang_feedback(self):
        v = lees(TEMPL / "voortgang.md")
        for n in range(1, 8):
            self.assertRegex(v, re.compile(r"^\| %d\. " % n, re.M))
        self.assertIn("## Ladder", v)
        self.assertIn("| Trede | Niveau | Datum | Uitdaging | Klaar |", v)
        f = lees(TEMPL / "feedback.md").lower()
        for k in ("missie", "datum", "onduidelijk", "vastgelopen", "wat de coach zag"):
            self.assertIn(k, f)


class C03(unittest.TestCase):
    def test_C03_stappen_en_regels(self):
        s = skill("start")
        low = s.lower()
        for w in ("inventaris", "werkmap", "missie 1", "meter", "formulier", "coachcode", "8 tekens",
                  "startplan", "improve the model for everyone", "platform"):
            self.assertIn(w, low, w)
        self.assertIn(link_cfg()["zonder_code"], s)
        self.assertTrue(any(link_geldig(u) for u in concrete_links(s)), "geen geldige voortgangslink m1")
        self.assertIsNone(SLASH.search(s), "slash-commando in start")


class C04(unittest.TestCase):
    def test_C04_formaat(self):
        for n in range(1, 8):
            t = missie(n)
            fm, volgorde = frontmatter(t)
            self.assertIsNotNone(fm, n)
            self.assertEqual(volgorde, ["missie", "titel", "video"], n)
            self.assertEqual(fm["missie"], str(n))
            self.assertTrue(fm["titel"])
            self.assertEqual(fm["video"], MISSIE_VIDEO[n], n)
            posities = [t.find("\n" + k + "\n") for k in KOPPEN]
            self.assertNotIn(-1, posities, "missie %d mist een kop" % n)
            self.assertEqual(posities, sorted(posities), "missie %d: koppen in verkeerde volgorde" % n)
            fout = sectie(t, "## Wat kan hier fout gaan")
            self.assertIn("### ChatGPT", fout)
            self.assertIn("### Claude", fout)

    def test_C04_taal(self):
        for n in range(1, 8):
            t = missie(n)
            self.assertNotIn(EM_DASH, t, n)
            self.assertIsNone(SLASH.search(t), n)

    def test_C04_herziene_missies(self):
        m4 = sectie(missie(4), "## Route ChatGPT").lower()
        self.assertTrue("outlook.com" in m4 or "plak" in m4)
        m5 = missie(5).lower()
        self.assertIn("audio", m5)
        self.assertIn("upload", m5)
        self.assertIn("mijn-vaardigheden", missie(7))
        self.assertIn("eigen-", missie(7))


class C05(unittest.TestCase):
    def test_C05_missie_skill(self):
        s = skill("missie")
        low = s.lower()
        for w in ("meter", "overslaan", "platform", "account", "[todo]", "klaar als", "successen.md",
                  "feedback.md", "stand"):
            self.assertIn(w, low, w)
        self.assertIn(link_cfg()["zonder_code"], s)
        self.assertTrue(any(link_geldig(u) and "s=m" in u for u in concrete_links(s)))
        self.assertIsNone(SLASH.search(s))


class C06(unittest.TestCase):
    def test_C06_foutpunten(self):
        item = re.compile(r"^- \*\*[^*]+:\*\* \S", re.M)
        for n in range(1, 8):
            fout = sectie(missie(n), "## Wat kan hier fout gaan")
            self.assertGreaterEqual(len(item.findall(subsectie(fout, "### ChatGPT") or "")), 3, n)
            self.assertGreaterEqual(len(item.findall(subsectie(fout, "### Claude") or "")), 2, n)


class C07(unittest.TestCase):
    def test_C07_ladder(self):
        l = lees(SKILLS / "uitdaging" / "ladder.md")
        for n in range(1, 6):
            self.assertRegex(l, re.compile(r"^## Niveau %d\b" % n, re.M))
        s = skill("uitdaging")
        low = s.lower()
        for w in ("missie 7", "niveau 5", "successen.md", "dossier", "## ladder"):
            self.assertIn(w, low, w)
        self.assertTrue(any(link_geldig(u) and "s=t" in u for u in concrete_links(s)))
        self.assertIn(link_cfg()["zonder_code"], s)


class C08(unittest.TestCase):
    def test_C08_standen_en_uitleg(self):
        c = skill("coach")
        for w in ("uitgebreid", "kort", "uit", "CLAUDE.md", "AGENTS.md", "**Stand:**"):
            self.assertIn(w, c)
        u = skill("uitleg")
        self.assertIn("Denk eraan als:", u)
        self.assertIn("150", u)
        for f in ("CLAUDE.md", "AGENTS.md"):
            self.assertIn("onomkeerba", lees(TEMPL / f).lower())


class C09(unittest.TestCase):
    def test_C09_links(self):
        alle = []
        for p in PLUGIN.rglob("*.md"):
            alle += concrete_links(lees(p))
        self.assertTrue(alle)
        for u in alle:
            self.assertTrue(link_geldig(u), u)
        for n in ("start", "missie", "uitdaging"):
            self.assertIn(link_cfg()["zonder_code"], skill(n))

    def test_C09_fixture_zelf(self):
        cfg = link_cfg()
        for u in cfg["geldig"]:
            self.assertTrue(link_geldig(u), u)
        for u in cfg["ongeldig"]:
            self.assertFalse(link_geldig(u), u)


class C10(unittest.TestCase):
    def test_C10_niet_overschrijven(self):
        self.assertIn("ontbreekt", skill("start").lower())
        doel = re.compile(r"(ik/|projecten/|feedback\.md|successen\.md|voortgang\.md|mijn-vaardigheden|eigen-)")
        actie = re.compile(r"(overschrijf|overschrijven|wis |wissen|verwijder)", re.I)
        for p in SKILLS.rglob("SKILL.md"):
            for zin in re.split(r"(?<=[.!?])\s+|\n", lees(p)):
                if doel.search(zin) and actie.search(zin):
                    self.assertRegex(zin.lower(), r"nooit|niet|vraag|eerst", "%s: %s" % (p.name, zin))

    def test_C10_update_doc(self):
        d = lees(ROOT / "docs" / "updates.md")
        for w in ("Add a marketplace", "BinaryBjorn/debug-coach", "Upgrade", "Refresh", "Check for updates", "mijn-vaardigheden"):
            self.assertIn(w, d, w)


class C11(unittest.TestCase):
    def test_C11_scripts(self):
        schema = json.loads(lees(GEDEELD / "script.schema.json"))
        for slug in VIDEO_SLUGS:
            s = json.loads(lees(VIDEOS / slug / "script.json"))
            self.assertEqual(valideer(s, schema), [], slug)
            self.assertEqual(s["slug"], slug)
            self.assertEqual(s["platform"], "chatgpt")

    def test_C11_opname_en_gitignore(self):
        for slug in VIDEO_SLUGS:
            o = lees(VIDEOS / slug / "opname.md")
            for w in ("Claude", "Computer Use", "screencapture -v", "-R", "start_video_gemeten", "ruw/opname.mov",
                      "ruw/log.json", "demo-account", "nepdata", "stap"):
                self.assertIn(w, o, "%s: %s" % (slug, w))
        g = lees(ROOT / ".gitignore")
        self.assertIn("videos/*/ruw/", g)
        self.assertIn("videos/*/uit/", g)


class C12(unittest.TestCase):
    def test_C12_pakket(self):
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "bouw_werkmap.py")], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stderr)
        w = ROOT / "dist" / "debug-coach-werkmap"
        for f in ("CLAUDE.md", "AGENTS.md", "ik/profiel.md", "voortgang.md", "feedback.md",
                  "successen.md", "projecten/README.md", ".coach/mijn-vaardigheden/plugin.json",
                  ".coach/mijn-vaardigheden/skills/README.md"):
            self.assertTrue((w / f).is_file(), f)
        self.assertFalse((w / ".coach" / "debug-coach").exists(), "de coach zelf komt via GitHub, niet in het pakket")
        mv = json.loads(lees(w / ".coach" / "mijn-vaardigheden" / "plugin.json"))
        self.assertEqual(mv["name"], "mijn-vaardigheden")
        m = json.loads(lees(w / ".agents" / "plugins" / "marketplace.json"))
        p = m["plugins"][0]
        self.assertEqual(p["name"], "mijn-vaardigheden")
        self.assertEqual(p["source"], {"source": "local", "path": "./.coach/mijn-vaardigheden"})
        self.assertEqual(p["policy"]["installation"], "AVAILABLE")
        z = ROOT / "dist" / "debug-coach-werkmap.zip"
        self.assertTrue(zipfile.is_zipfile(z))
        self.assertIn("dist/", lees(ROOT / ".gitignore"))


class C13(unittest.TestCase):
    def test_C13_readme(self):
        r = lees(ROOT / "README.md")
        low = r.lower()
        for w in ("work", "altijd op dit apparaat", "add a marketplace", "add marketplace", "binarybjorn/debug-coach",
                  "coachcode", "start", "upgrade", "check for updates", "mijn-vaardigheden"):
            self.assertIn(w, low, w)
        self.assertIsNone(SLASH.search(r))


if __name__ == "__main__":
    unittest.main()
