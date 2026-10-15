%% Bevroren bij het tekenen. %%

## Wat getest wordt

| Feature | Check | Wat de check bewijst | Wat hij níet bewijst (voor de keurder) |
|---|---|---|---|
| V01 | `python3 tests/feature.py V01` | Plan klopt met script en log, zoomdoel begrensd | Of de keuzes er goed uitzien |
| V02 | `python3 tests/feature.py V02` | Geldige PNG's, juiste maten en positie | Of het kader rustig oogt: keurder bekijkt een kader |
| V03 | `python3 tests/feature.py V03` | Zoomfactor en cirkelpositie op kliktijd | Of de beweging vloeiend oogt: keurder bekijkt drie kaders rond een klik |
| V04 | `python3 tests/feature.py V04` | Duur en bevriezen | Of het ritme natuurlijk voelt |
| V05 | `python3 tests/feature.py V05` | Cues en spoor | Leesbaarheid in de speler (R3) |
| V06 | `python3 tests/feature.py V06` | Formaat en codecs | Kwaliteit van het beeld |
| V07 | `python3 tests/feature.py V07` | Providers en terugval, sleutel nooit in code | De echte stem (na de keten) |
| V08 | `python3 tests/feature.py V08` | Handleiding dekt de keten | Leesbaarheid |

## Dummydata

`tests/fixtures/video/demo/`: `script.json` (drie stappen, s01-s03), `ruw/log.json` (scherm 1352×878 punten, opnamegebied 720×450 op x 0, y 30, schaal 2, `start_video_gemeten` 1000,0; twee klikken waarvan één buiten het opnamegebied; stap s02 zonder klik maar met zoomdoel), en een testopname die de test zelf maakt met `ffmpeg -f lavfi -i testsrc2=size=1440x900:rate=30 -t 20`. Uitvoer enkel in een tijdelijke map.

## Basistest

`python3 tests/feature.py BASIS`: de regressie van R1 (lekcheck, JSON, hash van de gedeelde formaten).
