"""Tests voor dc-r1b-coach-didactiek (D01..D09). Python 3.9, standaardbibliotheek."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugin"
SKILLS = PLUGIN / "skills"
TEMPL = SKILLS / "start" / "templates"
MISSIES = PLUGIN / "missies"


def lees(p):
    return pathlib.Path(p).read_text(encoding="utf-8")


def skill(n):
    return lees(SKILLS / n / "SKILL.md")


def sectie(t, kop):
    m = re.search(r"^" + re.escape(kop) + r"[ \t]*$(.*?)(?=^## |\Z)", t, re.M | re.S)
    return m.group(1) if m else ""


def missie(n):
    return lees(MISSIES / ("missie-%02d.md" % n))


class D01(unittest.TestCase):
    def test_D01_nieuwe_start(self):
        s = skill("start").lower()
        for w in ("status: leeg", "open", "nieuwe start", "welkom", "projectbrein", "context", "meter"):
            self.assertIn(w, s, w)
        self.assertRegex(s, r"alle missies[^.\n]*open")


class D02(unittest.TestCase):
    def test_D02_zelf_vragen(self):
        m = skill("missie")
        self.assertIn("Maak niets in dezelfde beurt als het voorstel van de missie", m)
        low = m.lower()
        for w in ("kiest", "zelf de vraag", "verbeter", "voor wie", "vorm", "bronnen", "pas daarna"):
            self.assertIn(w, low, w)
        self.assertIn("niets in dezelfde beurt", skill("uitdaging").lower())


class D03(unittest.TestCase):
    def test_D03_jij_of_coach(self):
        stap = re.compile(r"^\d+\.\s", re.M)
        goed = re.compile(r"^\d+\.\s\*\*(Jij|De coach):\*\*")
        for n in range(1, 8):
            t = missie(n)
            for kop in ("## Route ChatGPT", "## Route Claude"):
                sec = sectie(t, kop)
                regels = [r for r in sec.splitlines() if stap.match(r)]
                self.assertTrue(regels, "missie %d %s: geen stappen" % (n, kop))
                for r in regels:
                    self.assertRegex(r, goed, "missie %d %s: %s" % (n, kop, r[:60]))
                self.assertTrue(any("**Jij:**" in r for r in regels), "missie %d %s: geen Jij-stap" % (n, kop))


class D04(unittest.TestCase):
    def test_D04_klaar_als(self):
        m = skill("missie").lower()
        self.assertIn("buiten de chat", m)
        self.assertIn("bevestig", m)
        self.assertRegex(m, r"(gok|raad)[^.\n]*nooit|nooit[^.\n]*(gok|raad)")
        m7 = missie(7)
        self.assertIn("Customize > Skills > Upload a skill", m7)
        self.assertIn("nieuw gesprek", m7.lower())
        u = skill("uitdaging").lower()
        self.assertRegex(u, r"niveau 3[\s\S]{0,400}opnieuw (uploaden|upload)")


class D05(unittest.TestCase):
    def test_D05_feedback(self):
        for n in ("missie", "start"):
            s = skill(n)
            self.assertIn("Wat was onduidelijk?", s, n)
            self.assertIn("Waar liep je vast?", s, n)
            low = s.lower()
            self.assertIn("letterlijk", low, n)
            self.assertIn("volgende beurt", low, n)
            self.assertRegex(low, r"nooit[^.\n]*verzin|verzin[^.\n]*nooit", n)


class D06(unittest.TestCase):
    def test_D06_uitleg(self):
        m = skill("missie")
        low = m.lower()
        self.assertIn("## Begrippen", m)
        self.assertIn("Denk eraan als:", m)
        self.assertIn("ongevraagd", low)
        self.assertRegex(low, r"stand uitgebreid|uitgebreid")
        self.assertRegex(low, r"stand kort|kort[^.\n]*één zin")


class D07(unittest.TestCase):
    def test_D07_link_gewone_tekst(self):
        for p in PLUGIN.rglob("*.md"):
            self.assertNotRegex(lees(p), r"`https://debug\.marketing/coach/v[^`]*`", str(p.relative_to(ROOT)))
        for n in ("start", "missie", "uitdaging"):
            self.assertIn("als gewone tekst", skill(n).lower(), n)


class D08(unittest.TestCase):
    def test_D08_eerst_vragen(self):
        actie = re.compile(r"verwijder|overschrijf|overschrijven|vervang", re.I)
        for p in SKILLS.rglob("SKILL.md"):
            t = lees(p)
            if actie.search(t):
                self.assertIn("vraag eerst", t.lower(), p.parent.name)
        for f in ("CLAUDE.md", "AGENTS.md"):
            self.assertIn("technische waarden", lees(TEMPL / f).lower(), f)


class D09(unittest.TestCase):
    def test_D09_mail_plakken(self):
        t = missie(3)
        for kop in ("## Route ChatGPT", "## Route Claude"):
            sec = sectie(t, kop).lower()
            self.assertIn("kopieer", sec, kop)
            self.assertIn("plak", sec, kop)


if __name__ == "__main__":
    unittest.main()
