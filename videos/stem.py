"""Stem per stap: een testtoon (sinus, zonder internet) of OpenAI gpt-4o-mini-tts.

De sleutel komt enkel uit de omgevingsvariabele OPENAI_API_KEY; hij staat nooit in een bestand.
"""
import math
import os
import struct
import subprocess
import urllib.request
import wave

OPENAI_URL = "https://api.openai.com/v1/audio/speech"
OPENAI_MODEL = "gpt-4o-mini-tts"
OPENAI_STEM = "cedar"
RATE = 24000          # samples per seconde, mono (zoals de wav van OpenAI)
TOON_HZ = 440.0
TOON_VOLUME = 0.2
TOON_FADE = 0.02      # in- en uitfaden, in seconden, tegen klikjes


def testtoon(pad, duur):
    """Schrijf een sinus van exact `duur` seconden als 16-bit mono wav."""
    n = int(round(duur * RATE))
    fade = int(TOON_FADE * RATE)
    data = bytearray()
    for i in range(n):
        g = min(1.0, i / fade, (n - 1 - i) / fade) if fade else 1.0
        data += struct.pack("<h", int(32767 * TOON_VOLUME * max(g, 0.0) * math.sin(2 * math.pi * TOON_HZ * i / RATE)))
    with wave.open(str(pad), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(bytes(data))


def wav_duur(pad):
    """Duur via ffprobe: de wav van OpenAI kan een fictieve lengte in de header hebben."""
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(pad)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def openai_aanvraag(tekst, sleutel):
    """De aanvraag voor OpenAI text-to-speech, zonder ze te versturen."""
    return {
        "url": OPENAI_URL,
        "headers": {"Authorization": "Bearer %s" % sleutel, "Content-Type": "application/json"},
        "body": {"model": OPENAI_MODEL, "voice": OPENAI_STEM, "input": tekst, "response_format": "wav"},
    }


def openai_stem(tekst, pad, sleutel):
    """Verstuur de aanvraag en schrijf de wav naar `pad`."""
    import json
    a = openai_aanvraag(tekst, sleutel)
    req = urllib.request.Request(a["url"], data=json.dumps(a["body"]).encode(), headers=a["headers"], method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        pad.write_bytes(r.read())


def maak_stemmen(stappen, map_stem, provider):
    """Schrijf <id>.wav per stap. Geeft {id: duur} terug.

    Met provider 'openai' zonder OPENAI_API_KEY valt de pijplijn terug op de testtoon en meldt dat in één regel."""
    map_stem.mkdir(parents=True, exist_ok=True)
    sleutel = os.environ.get("OPENAI_API_KEY", "").strip()
    if provider == "openai" and not sleutel:
        print("stem ontbreekt: OPENAI_API_KEY is niet gezet, de video krijgt de testtoon")
        provider = "test"
    duren = {}
    for st in stappen:
        pad = map_stem / (st["id"] + ".wav")
        if provider == "openai":
            openai_stem(" ".join(st["tekst"].split()), pad, sleutel)
        else:
            testtoon(pad, st["duur_s"])
        duren[st["id"]] = wav_duur(pad)
    return duren
