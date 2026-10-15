"""Tests voor bouwrun dc-r2-videopijplijn (Debug Coach, run 2). Python 3.9, standaardbibliotheek + ffmpeg/ffprobe.
Testnamen bevatten V01..V08; tests/feature.py (uit R1) selecteert daarop.

Interface die de bouwer maakt (vast in het contract):
  python3 videos/maak.py <map> [--plan-only] [--stem test|openai]
    <map>/script.json, <map>/ruw/opname.mov, <map>/ruw/log.json  ->  <map>/uit/
    uit/plan.json, uit/achtergrond.png, uit/masker.png, uit/cirkel.png, uit/stem/<id>.wav,
    uit/<slug>.vtt, uit/<slug>.mp4
  videos/stem.py: openai_aanvraag(tekst, sleutel) -> dict(url, headers, body) zonder te versturen.
"""
import importlib.util
import json
import os
import pathlib
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIX = ROOT / "tests" / "fixtures" / "video" / "demo"
MAAK = ROOT / "videos" / "maak.py"
ZOOM = 1.8
BREED, HOOG = 1920, 1080


def ffprobe(pad, *args):
    r = subprocess.run(["ffprobe", "-v", "error"] + list(args) + ["-of", "json", str(pad)],
                       capture_output=True, text=True, timeout=60)
    return json.loads(r.stdout or "{}")


def duur(pad):
    return float(ffprobe(pad, "-show_entries", "format=duration")["format"]["duration"])


def png_maat(pad):
    b = pathlib.Path(pad).read_bytes()
    assert b[:8] == b"\x89PNG\r\n\x1a\n", "geen PNG"
    assert b[12:16] == b"IHDR"
    return struct.unpack(">II", b[16:24])


def verwacht_plan():
    """Onafhankelijke berekening van de rekenregels (log.schema.json _regels) voor de fixture."""
    script = json.loads((FIX / "script.json").read_text())
    log = json.loads((FIX / "ruw" / "log.json").read_text())
    s = log["scherm"]["schaal"]
    g = log["gebied"]
    t0 = log["opname"]["start_video_gemeten"]
    bw, bh = g["breedte"] * s, g["hoogte"] * s
    vw, vh = bw / ZOOM, bh / ZOOM
    uit = []
    t_uit = 0.0
    for st in script["stappen"]:
        ev = [e for e in log["events"] if e["stap"] == st["id"]]
        hd = (max(e["t"] for e in ev) - min(e["t"] for e in ev) + 0.5) if ev else 0.0
        sd = max(st["duur_s"], hd)
        klik = [e for e in ev if e["handeling"] == "klik"]
        if klik:
            zx, zy = (klik[0]["x"] - g["x"]) * s, (klik[0]["y"] - g["y"]) * s
        elif "zoomdoel" in st:
            zx, zy = (st["zoomdoel"][0] - g["x"]) * s, (st["zoomdoel"][1] - g["y"]) * s
        else:
            zx = zy = None
        if zx is not None:
            zx = min(max(zx, vw / 2), bw - vw / 2)
            zy = min(max(zy, vh / 2), bh - vh / 2)
        uit.append({"id": st["id"], "handelingsduur": round(hd, 3), "stapduur": round(sd, 3),
                    "bevriezen": st["duur_s"] > hd, "zoomdoel": None if zx is None else [round(zx), round(zy)],
                    "uit_begin": round(t_uit, 3), "uit_einde": round(t_uit + sd, 3), "tekst": st["tekst"],
                    "bron_begin": round(min(e["t"] for e in ev) - t0, 3) if ev else None})
        t_uit += sd
    return uit, round(t_uit, 3), (bw, bh)


class _Render(unittest.TestCase):
    """Rendert één keer per testklasse in een tijdelijke map."""
    stem = "test"
    plan_only = False

    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp(prefix="dcvideo-"))
        cls.map = cls.tmp / "demo"
        shutil.copytree(FIX, cls.map)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=size=1440x900:rate=30",
                        "-t", "20", "-pix_fmt", "yuv420p", str(cls.map / "ruw" / "opname.mov")],
                       check=True, timeout=120)
        args = [sys.executable, str(MAAK), str(cls.map), "--stem", cls.stem]
        if cls.plan_only:
            args.append("--plan-only")
        env = dict(os.environ)
        env.pop("OPENAI_API_KEY", None)
        cls.res = subprocess.run(args, capture_output=True, text=True, timeout=500, env=env)
        cls.uit = cls.map / "uit"

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def plan(self):
        self.assertEqual(self.res.returncode, 0, self.res.stderr[-2000:])
        return json.loads((self.uit / "plan.json").read_text())


class V01(_Render):
    plan_only = True

    def test_V01_plan_volgens_rekenregels(self):
        p = self.plan()
        verwacht, totaal, _ = verwacht_plan()
        self.assertEqual([s["id"] for s in p["stappen"]], [v["id"] for v in verwacht])
        for s, v in zip(p["stappen"], verwacht):
            for k in ("handelingsduur", "stapduur", "uit_begin", "uit_einde"):
                self.assertAlmostEqual(float(s[k]), v[k], delta=0.05, msg="%s %s" % (v["id"], k))
            self.assertEqual(bool(s["bevriezen"]), v["bevriezen"], v["id"])
            if v["bron_begin"] is not None:
                self.assertAlmostEqual(float(s["bron_begin"]), v["bron_begin"], delta=0.05, msg="%s bron_begin (videotijd = t - start_video_gemeten)" % v["id"])
            if v["zoomdoel"] is None:
                self.assertIsNone(s["zoomdoel"])
            else:
                self.assertAlmostEqual(s["zoomdoel"][0], v["zoomdoel"][0], delta=2, msg=v["id"])
                self.assertAlmostEqual(s["zoomdoel"][1], v["zoomdoel"][1], delta=2, msg=v["id"])
        self.assertAlmostEqual(float(p["totaal"]), totaal, delta=0.05)


class V02(_Render):
    def test_V02_beelden(self):
        self.plan()
        self.assertEqual(png_maat(self.uit / "achtergrond.png"), (BREED, HOOG))
        _, _, (bw, bh) = verwacht_plan()
        f = min(0.84 * BREED / bw, 0.84 * HOOG / bh)
        mw, mh = png_maat(self.uit / "masker.png")
        self.assertAlmostEqual(mw, bw * f, delta=3)
        self.assertAlmostEqual(mh, bh * f, delta=3)
        cw, ch = png_maat(self.uit / "cirkel.png")
        self.assertEqual(cw, ch)

    def test_V02_huisstijl(self):
        bron = (ROOT / "videos").rglob("*.py")
        tekst = "\n".join(p.read_text() for p in bron).lower()
        for kleur in ("0b1628", "1a2d4a", "4a7cc9"):
            self.assertIn(kleur, tekst, kleur)


class V03(_Render):
    def test_V03_zoom_en_cirkel(self):
        p = self.plan()
        for s in p["stappen"]:
            if s["zoomdoel"] is not None:
                self.assertAlmostEqual(float(s["zoomfactor"]), ZOOM, delta=0.01, msg=s["id"])
        kliks = [s for s in p["stappen"] if s.get("cirkel")]
        self.assertEqual(len(kliks), 2, "twee kliks in de fixture")
        for s in kliks:
            x, y, t = s["cirkel"]
            self.assertTrue(0 <= x <= BREED and 0 <= y <= HOOG, s["id"])
            self.assertTrue(float(s["uit_begin"]) <= t <= float(s["uit_einde"]), s["id"])


class V04(_Render):
    def test_V04_duur(self):
        self.plan()
        _, totaal, _ = verwacht_plan()
        self.assertAlmostEqual(duur(self.uit / "demo.mp4"), totaal, delta=0.5)


class V05(_Render):
    def test_V05_ondertitels(self):
        self.plan()
        vtt = (self.uit / "demo.vtt").read_text()
        self.assertTrue(vtt.startswith("WEBVTT"))
        cues = re.findall(r"(\d\d:\d\d:\d\d\.\d{3}) --> (\d\d:\d\d:\d\d\.\d{3})\n(.+)", vtt)
        verwacht, _, _ = verwacht_plan()
        self.assertEqual(len(cues), len(verwacht))

        def sec(t):
            h, m, s = t.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
        for (a, b, tekst), v in zip(cues, verwacht):
            self.assertAlmostEqual(sec(a), v["uit_begin"], delta=0.1)
            self.assertAlmostEqual(sec(b), v["uit_einde"], delta=0.1)
            self.assertEqual(tekst.strip(), v["tekst"])
        st = ffprobe(self.uit / "demo.mp4", "-show_streams")["streams"]
        self.assertTrue(any(s.get("codec_name") == "mov_text" for s in st))


class V06(_Render):
    def test_V06_formaat(self):
        self.plan()
        st = ffprobe(self.uit / "demo.mp4", "-show_streams")["streams"]
        v = [s for s in st if s["codec_type"] == "video"][0]
        self.assertEqual(v["codec_name"], "h264")
        self.assertEqual((v["width"], v["height"]), (BREED, HOOG))
        self.assertIn(v["r_frame_rate"], ("30/1", "30000/1000"))
        self.assertTrue(any(s["codec_type"] == "audio" and s["codec_name"] == "aac" for s in st))


class V07(_Render):
    def test_V07_testtoon(self):
        self.plan()
        script = json.loads((FIX / "script.json").read_text())
        for st in script["stappen"]:
            self.assertAlmostEqual(duur(self.uit / "stem" / (st["id"] + ".wav")), st["duur_s"], delta=0.05)

    def test_V07_openai_aanvraag_en_terugval(self):
        spec = importlib.util.spec_from_file_location("stem", str(ROOT / "videos" / "stem.py"))
        stem = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(stem)
        a = stem.openai_aanvraag("Hallo.", "nep-sleutel")
        self.assertEqual(a["url"], "https://api.openai.com/v1/audio/speech")
        self.assertEqual(a["headers"]["Authorization"], "Bearer nep-sleutel")
        self.assertEqual(a["body"]["model"], "gpt-4o-mini-tts")
        self.assertEqual(a["body"]["voice"], "cedar")
        for p in (ROOT / "videos").rglob("*.py"):
            self.assertNotRegex(p.read_text(), r"sk-[A-Za-z0-9]{10,}", p.name)


class V07b(_Render):
    stem = "openai"

    def test_V07_zonder_sleutel_terugval(self):
        self.plan()
        uitvoer = (self.res.stdout + self.res.stderr).lower()
        self.assertIn("stem ontbreekt", uitvoer)
        self.assertTrue((self.uit / "demo.mp4").is_file())


class V08(unittest.TestCase):
    def test_V08_handleiding(self):
        r = (ROOT / "videos" / "README.md").read_text().lower()
        for w in ("script.json", "opname.md", "ruw/opname.mov", "ruw/log.json", "maak.py", "uit/", "openai_api_key"):
            self.assertIn(w, r, w)


if __name__ == "__main__":
    unittest.main()
