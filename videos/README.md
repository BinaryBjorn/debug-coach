# Video's: van script tot afgewerkte instructievideo

Bjorn neemt zelf niets op en bewerkt niets. Claude neemt de ChatGPT-app op, de pijplijn maakt er een video van, Bjorn kijkt hem enkel na.

Elke video heeft een eigen map `videos/<slug>/` (bv. `videos/missie-5/`).

## De keten

1. **Script** (`videos/<slug>/script.json`, gemaakt in run 1). Per stap: id (`s01`, `s02`, ...), de gesproken tekst, `duur_s` en eventueel een `zoomdoel`. Vorm: `tests/fixtures/gedeeld/script.schema.json`.
2. **Opname door Claude met Computer Use op de Mac mini.** Claude volgt `videos/<slug>/opname.md`: demo-account en nepdata, enkel het ChatGPT-venster opnemen met `screencapture`, elke stap uit het script uitvoeren en elke handeling met tijdstip, stap-id en klikpositie noteren. Er komen twee bestanden uit:
   - `ruw/opname.mov`: de ruwe schermopname (120 fps mag);
   - `ruw/log.json`: het kliklog, in de vorm van `tests/fixtures/gedeeld/log.schema.json`.
3. **Video maken:**

   ```
   python3 videos/maak.py videos/<slug>
   ```

   Opties: `--plan-only` schrijft enkel `uit/plan.json` (om de timing na te kijken zonder te renderen); `--stem test` (standaard) zet een testtoon per stap, `--stem openai` de echte stem (zie hieronder).
4. **Nakijken.** Bekijk `uit/<slug>.mp4` van begin tot einde: zoomt het in op elke klik, staat de cirkel op de knop, valt de stem samen met de handeling, kloppen de ondertitels, staat er geen echte naam of gegeven in beeld? Klopt iets niet, pas dan het script aan of laat Claude opnieuw opnemen, en draai `maak.py` opnieuw. Een video met de testtoon is nooit de eindversie.
5. **Daarna.** De goedgekeurde `uit/<slug>.mp4` en `uit/<slug>.vtt` gaan naar de videospeler van de Debug Coach-site (Bunny of de site zelf, run 3), die de ondertitels standaard aanzet. De pijplijn zelf uploadt niets.

## Wat er in `uit/` staat

| Bestand | Wat |
|---|---|
| `uit/plan.json` | Het renderplan: per stap bron in de opname, stapduur, zoom, klikcirkel; bovenaan het totaal |
| `uit/achtergrond.png`, `uit/masker.png`, `uit/cirkel.png` | Achtergrond in de huisstijl, afgeronde hoeken van het kader, de klikcirkel |
| `uit/stem/<id>.wav` | De stem per stap (testtoon of OpenAI) |
| `uit/<slug>.vtt` | De ondertitels, één cue per stap |
| `uit/<slug>.mp4` | De video: 1920×1080, 30 fps, h264, aac-geluid, ondertitels als `mov_text`-spoor |

`uit/` wordt telkens opnieuw gemaakt; bewerk daar niets met de hand.

## De echte stem: `OPENAI_API_KEY`

De stem komt van OpenAI (`gpt-4o-mini-tts`, stem `cedar`). De sleutel staat nooit in een bestand; zet hem enkel in de omgeving van de terminal:

```
export OPENAI_API_KEY=sk-...
python3 videos/maak.py videos/<slug> --stem openai
```

Met de echte stem telt de gemeten duur van elke zin: is de zin langer dan de handeling, dan blijft het beeld staan tot de zin uit is. Zonder sleutel meldt de pijplijn in één regel `stem ontbreekt` en maakt ze de video met de testtoon; ze faalt nooit stil.

## Nodig

Python 3.9 (standaardbibliotheek) en ffmpeg met `zoompan`, `overlay`, `libx264`, `aac` en `mov_text`. Geen extra pakketten.
