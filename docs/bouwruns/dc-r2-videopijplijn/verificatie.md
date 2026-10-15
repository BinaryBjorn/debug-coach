---
type: verificatie
run: dc-r2-videopijplijn
ronde: 1
date: 2026-10-15
---

# Verificatie, keurronde 1

Geen testserver en geen webscherm: het resultaat is een opdrachtregelscript (contract §5). De keuring volgt daarom §5 en §9 van het contract: zelf de testvideo renderen, stilstaande beelden bekijken en het renderplan nalezen. De browserstappen (1440, 768 en 375 px) en de design-critic zijn hier niet van toepassing.

**Hoe getest.** Een eigen proefopname van 20 s, 1440×900, **120 fps** (`smptehdbars`), met merktekens op vaste plekken: een rood vierkant op het klikpunt van s01 (pixel 200,160), een groen vierkant op het zoomdoel van s02 (pixel 720,450) en een witte balk die met de tijd meeschuift (x = 72·t). Zo zie je in elk kader welk bronmoment er getoond wordt. Script en log zijn exacte kopieën van `tests/fixtures/video/demo/`. Gerenderd met `python3 videos/maak.py <map> --stem openai` **zonder** `OPENAI_API_KEY`. Daarna een tweede variant met randgevallen, en een map zonder opname.

## Scenario's

### S7a: van opname tot mp4 met vtt: **slaagt**

- `maak.py` maakte `uit/demo.mp4` en `uit/demo.vtt`. ffprobe: h264 1920×1080 30 fps, aac en mov_text, alle drie 8,000 s lang.
- Renderplan nagerekend volgens §7b:
  - s01: bron 1,0–2,5 s, handelingsduur 1,5 s, stapduur 3,0 s, bevriezen.
  - s02: bron 5,0–8,0 s, stapduur 3,0 s, niet bevriezen.
  - s03: bron 12,0–12,9 s, stapduur 2,0 s, bevriezen.
  - Totaal 8,0 s.
  - Kader: factor 1,008, 1452×906 op (234, 87). Dat klopt met min(0,84·1920/1440, 0,84·1080/900).
  - Zoomdoel s01: (400, 250), begrensd vanuit (200, 160). Zoomdoel s03: (1040, 650), begrensd vanuit (1600, 940), want die klik ligt buiten de opname.
- Vijf beelden volgens het contract:
  - `screenshots/S7a-1-begin.png` (0,1 s): kader op het verloop, afgeronde hoeken, 1×.
  - `screenshots/S7a-2-klik1.png` (1,0 s): 1,8× ingezoomd. De blauwe cirkel staat **precies op het rode klikdoel**.
  - `screenshots/S7a-3-tussenstuk.png` (4,5 s): s02 ingezoomd op het groene zoomdoel uit het script.
  - `screenshots/S7a-4-klik2.png` (6,0 s): de klik buiten de opname. De cirkel staat begrensd in de hoek rechtsonder, half over de achtergrond (beslissing 7, zoals §7b vraagt).
  - `screenshots/S7a-5-einde.png` (7,95 s): uitgezoomd tot bijna 1×.
- Kaders rond een klik: `S7a-klik1-voor.png` (0,8 s, halverwege het inzoomen), `S7a-2-klik1.png` en `S7a-klik1-na.png` (1,3 s, ingezoomd, cirkel nog zichtbaar). Rond klik 2: `S7a-klik2-na.png`. Overzicht van alle twaalf kaders: `screenshots/overzicht-S7.png`.
- Ondertitels: de `.vtt` en het spoor in de mp4 (uitgelezen met `ffmpeg -map 0:s -f webvtt`) hebben dezelfde drie cues: 0–3, 3–6 en 6–8 s, met de tekst uit het script.
- De echte opname van `videos/missie-5/` bestaat nog niet (niet-doel: het opnemen komt na de keten). Het `script.json` daar heeft dezelfde velden als de fixture.

### S7b: stem langer of korter dan de handeling: **slaagt**

- **Langer (s01: stem 3 s, handeling 1,5 s).** Op 1,3 s schuift de witte balk nog. In `S7b-s01-voor-bevriezen.png` (2,4 s) en `S7b-s01-bevroren.png` (2,9 s) staat hij op dezelfde plek: het laatste kader blijft staan tot het einde van de stap.
- **Weggeknipt.** In `S7b-s02-begin.png` (3,05 s) springt de balk naar bron ±5,0 s: het stuk van 2,5 tot 5,0 s is weg. In `S7a-4-klik2.png` (6,0 s) staat hij op bron 12,0 s (berekend x ≈ 640, gemeten ≈ 645): het stuk van 8,0 tot 12,0 s is weg.
- **Korter (s02: stem 2 s, handeling 3 s).** De handeling speelt volledig af en de stem wordt aangevuld met stilte. `silencedetect` vindt enkel stilte van 5,00 tot 6,00 s.

### S7c: geen sleutel: **slaagt**

- Met `--stem openai` en zonder `OPENAI_API_KEY` geeft `maak.py` één regel: `stem ontbreekt: OPENAI_API_KEY is niet gezet, de video krijgt de testtoon`. Daarna wordt de video toch volledig gemaakt.
- `videos/stem.py` bevat geen sleutel; de enige bron is `os.environ["OPENAI_API_KEY"]`. De echte aanroep naar OpenAI is niet getest, wat binnen het contract valt.

### Randgevallen (eigen variant)

Uitgebreid script met s01b (geen events, geen zoomdoel, `duur_s` 4,5) en s04 (twee kliks, waarvan één buiten de opname valt):

- Totaal 15,0 s = 3 + 4,5 + 3 + 2 + 2,5. De mp4, het geluid en de ondertitels duren elk 15,000 s.
- s01b toont het laatste kader van s01 (bron 2,5 s), op 1×, zonder cirkel. Dat volgt beslissing 3.
- Een map zonder `ruw/opname.mov` met `--plan-only` geeft gewoon het plan. Zonder `--plan-only` stopt het met `ffmpeg faalde: ... No such file or directory`: zichtbaar, niet stil.

## Harde checks

- `python3 "$BOUWRUN_CHECK" check docs/bouwruns/dc-r2-videopijplijn` → exit 0:
  ```
  V01    klaar
  V02    klaar
  V03    klaar
  V04    klaar
  V05    klaar
  V06    klaar
  V07    klaar
  V08    klaar
  => alles afgehandeld
  ```
- Basistest `python3 tests/feature.py BASIS` → exit 0, `Ran 3 tests ... OK`.
- Per feature, `python3 tests/feature.py V0N`, alle met exit 0 en `OK`:

  | Feature | Tests |
  |---|---|
  | V01 | 1 |
  | V02 | 2 |
  | V03 | 1 |
  | V04 | 1 |
  | V05 | 1 |
  | V06 | 1 |
  | V07 | 3 |
  | V08 | 1 |

- **Boekhouding.** In `features.json` staat V04 nog op `"status": "open", "passes": false`, terwijl de check groen is en de checker V04 als klaar toont. De bouwer heeft V04 nooit afgevinkt (`voortgang.md`, sessie 4: "V04 (staat nog open)"). Het gedrag zelf voldoet; zie S7b hierboven.

## Gevonden en door de bouwer gemist

Geen echte fouten gevonden die de checks misten.

Opmerkingen voor het pakket. Dit zijn geen fouten tegen het contract:

1. **Enkel de eerste klik per stap telt.** Een stap met twee kliks (in de variant: s04) krijgt zoom en cirkel enkel op de eerste klik. De rekenregels en V03 spreken van één cirkel per stap, dus dit volgt het contract. Toch belooft de contractkaart "inzoomen op elke klik". Neemt Claude later meerdere kliks per scriptstap op, dan blijft de tweede klik zonder cirkel.
2. **Klik buiten de opname.** De cirkel valt dan half op de achtergrond, in de hoek van het kader (`S7a-4-klik2.png`). Dat volgt de regel, maar in een echte video ziet het er vreemd uit. In een echte opname zou dit niet mogen voorkomen.
3. **Oude bestanden in `uit/` blijven staan.** De README zegt dat `uit/` "telkens opnieuw gemaakt" wordt, maar `maak.py` maakt de map enkel aan als ze ontbreekt. Een wav van een geschrapte stap blijft dus in `uit/stem/` staan. Dat heeft geen gevolg voor de video.
4. **Vloeiendheid niet bekeken.** Ik heb de zoombeweging enkel in losse kaders bekeken, niet als afgespeelde video. Of `zoompan` schokt bij het verschuiven tussen twee doelen (5,6 tot 6,0 s), moet Bjorn bij het nakijken zien.

## Design-critic

Niet geroepen: het contract heeft geen webscherm ("Designrichting: geen webscherm"). De huisstijlkleuren zijn wel nagekeken:

- De achtergrond loopt van `#0B1628` naar `#1A2D4A`.
- De cirkel is `#4A7CC9` op 40%.
- De hoekstraal is 24 px.

Ze staan als constanten in `videos/huisstijl.py` en zijn zichtbaar in `S7a-1-begin.png`.
