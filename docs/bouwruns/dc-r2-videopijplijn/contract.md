---
type: bouwcontract
status: getekend
date: 2026-10-15
getekend: 2026-10-15 (Bjorn, chat: "teken, maar start meteen zonder de queue")
project: Debug-Marketing
tags: [bouwrun, contract, debug-coach, video]
---

> [!important] Run 2 van 3 in blok 1 van [Debug Coach](../../plans/spec-debug-coach-blok-1.md)
> Erft de doelkaart en beslissingen B5 en B6. Bouwt in `debug-coach`, op de tak van R1. Python 3.9 en ffmpeg 9 (mini), geen pakketten installeren.

## Contractkaart

> [!question] Teken of stuur bij
> **Wat er gebouwd wordt:** een pijplijn die een ruwe schermopname van de ChatGPT-app (gemaakt door Claude met Computer Use), het kliklog en het script van R1 omzet in een afgewerkte instructievideo in Tella-stijl: kader op een rustige achtergrond in de huisstijl, inzoomen op elke klik, klikcirkel, een stem per stap, ondertitels als spoor, stiltes weggeknipt.
> **Outputtype:** feature (een opdrachtregelscript).
> **Scenario's:** S7 (afwerking).
> **Niet in deze run:** het opnemen zelf (Claude op de mini, na de keten), de echte stem aanroepen (sleutel komt na de keten), de site.
> **Aannames met de meeste impact:** A1 enkel ffmpeg en standaard-Python (geen nieuwe pakketten); A2 het kliklog in de vorm van P5 (`log.schema.json`); A3 ondertitels als `.vtt` naast de video (de speler op de site toont die).
> **Designrichting:** geen webscherm; de stijl volgt de huisstijl van Debug Marketing (achtergrond `#0B1628` naar `#1A2D4A`, accent `#4A7CC9` voor de klikcirkel), uit `brand.json`.
> **Keten:** run 2 van 3, na R1, op de tak van R1 (`--bouw-op vorige`).
> **Budget:** 4 uur, 12 sessies.
> **Enkel jij kunt beantwoorden:** niets.

## 1. Doel

Bjorn neemt zelf niets op en bewerkt niets: een ruwe opname van ChatGPT wordt zonder handwerk een video die hij enkel goedkeurt.

## 2. Scenario's

- **S7a** Na een opname door Claude met Computer Use op de mini (`videos/missie-5/ruw/opname.mov` en `ruw/log.json`) draait `python3 videos/maak.py videos/missie-5` en er staat `videos/missie-5/uit/missie-5.mp4` met `missie-5.vtt` ernaast.
- **S7b** Een stap waarin de stem langer duurt dan de handeling: het beeld blijft staan op het laatste kader tot de zin uit is. Korter: de stilte wordt weggeknipt.
- **S7c** De echte stem is niet beschikbaar (geen sleutel): de pijplijn maakt een versie met de testtoon en zegt in één regel dat de stem ontbreekt; nooit een stille mislukking.

## 3. Niet-doelen

- Geen ingebrande tekst (de ffmpeg op de mini heeft geen `drawtext`/`libass`; nagekeken 15/10).
- Geen nieuwe Python-pakketten of npm-pakketten.
- Geen gezicht in beeld, geen muziek.

## 4. Aannames

| # | Aanname | Soort | Bron | Zekerheid | Impact | Hoe getest | Omkeerbaar |
|---|---|---|---|---|---|---|---|
| A1 | ffmpeg 9 op de mini heeft `zoompan`, `overlay`, `libx264`, `aac`, `mov_text`, `webvtt`; PNG's (achtergrond, masker, cirkel) maakt Python zelf met `zlib` en `struct` | technisch | nagekeken 15/10 | hoog | hoog | basistest rendert een testvideo | ja |
| A2 | Het kliklog volgt `tests/fixtures/gedeeld/log.schema.json` (`scherm`, `gebied`, `opname.start_video_gemeten`, events met epoch-tijd, stap-id en logische schermpunten) | technisch | proef P5 15/10 | hoog | hoog | P5 schreef dit formaat; fixture in dezelfde vorm | ja |
| A3 | De speler (Bunny of de site) toont het `.vtt`-spoor standaard aan | technisch | ontwerp | middel | laag | R3 zet `default` op het spoor | ja |
| A4 | De stem komt van OpenAI `gpt-4o-mini-tts`, stem `cedar`, via een module met de sleutel uit een omgevingsvariabele; in de run enkel de testtoon | technisch | keuze Bjorn 02/10 | hoog | middel | F07 met de testtoon; echte stem na de keten | ja |

### Inputkaart

| Gegeven | Bron | Hoe de run eraan komt | Echt voorbeeld gezien | Wie levert | Hoe vaak |
|---|---|---|---|---|---|
| Script | R1 `videos/<slug>/script.json` | tak van R1 | wordt gemaakt in R1, schema in `tests/fixtures/gedeeld/script.schema.json` | R1 | per video |
| Ruwe opname + kliklog | Claude Computer Use (P5, bewezen 15/10: 805×720 punten, schaal 2, 120 fps, klikposities ±2 punten, video start 0,29 s na het commando) | fixture in de vorm van `log.schema.json` met een testopname van `ffmpeg testsrc2` | ja (`proef-claude-2/`) | Claude op de mini, na de keten | per video |
| Huisstijl | `VisualGenerator/brands/debug-marketing/brand.json` | kopie in `bronnen/brand.json` (voorwerk V2) | ja | Claude | eenmalig |

## 5. Outputtype

**Feature:** een opdrachtregelscript. De keurder rendert de testvideo, haalt vijf stilstaande beelden uit (begin, klik 1 ingezoomd, tussenstuk, klik 2, einde) en beoordeelt die.

## 6. Technische vorm

| Onderdeel | Vorm | Waarom (in effect) | Afgewezen |
|---|---|---|---|
| Pijplijn | `videos/maak.py` (standaard-Python) die ffmpeg aanstuurt via een renderplan (`uit/plan.json`) | Elke stap is na te kijken en te testen zonder het beeld te bekijken | Een videobibliotheek: vraagt pakketten die de run niet mag installeren |
| Kader en achtergrond | PNG's door Python, overlay in ffmpeg, scherm op 84% met afgeronde hoeken | Tella-look zonder extra software | Ingebrande schaduw met filters die ontbreken |
| Inzoomen | `zoompan`-sleutelpunten per klik uit het log, 1,8× rond de klik, 0,4 s in en uit | Het oog volgt de klik zoals bij Tella | Vaste zoom: verliest overzicht |
| Stem | Per stap een audiobestand; provider `test` (sinus) of `openai` | Synchroon per stap, testbaar zonder internet | Eén lange stem: timing niet te sturen |
| Timing | Per stap: beeld bevriezen als de stem langer is, inkorten als de handeling langer is | Nooit praten over een leeg scherm of klikken zonder uitleg | Versnellen: oogt onrustig |
| Ondertitels | `.vtt` naast de video en als `mov_text`-spoor in de mp4 | Ingebrande tekst kan niet met deze ffmpeg | Ffmpeg vervangen: installeren mag niet in de run |

## 7. Features

Zie `features.json` (ID's V01 tot V08). Checks: `python3 tests/feature.py V0N` (het wrapperscript uit R1: faalt bij nul tests).

## 7b. Rekenregels (vast, uit `log.schema.json` `_regels`)

- **Handelingsduur** per stap = van het eerste tot het laatste event van die stap, plus 0,5 s. Een stap zonder events: 0 s.
- **Stapduur** = max(`duur_s` uit het script, handelingsduur). Is `duur_s` groter, dan bevriest het laatste kader van de stap tot het einde van de stap. Beeld tussen de stappen (na de handelingsduur van een stap en vóór het eerste event van de volgende) wordt weggeknipt.
- **Tijd**: videotijd = `t` − `opname.start_video_gemeten`.
- **Zoom**: een klik uit het log wint, daarna `zoomdoel` uit het script, anders geen zoom. Pixel in de opname = (x − `gebied.x`) × `schaal`, (y − `gebied.y`) × `schaal`, begrensd zodat het ingezoomde venster (opnamebreedte / 1,8 bij opnamehoogte / 1,8) binnen de opname blijft; x en y worden elk apart begrensd.
- **plan.json** = `{totaal, stappen: [...]}`.
- **Beeldsnelheid**: de opname mag 120 fps zijn; de uitvoer is 30 fps.
- **Testtoon**: per stap exact `duur_s` seconden.
- **Kader**: het scherm wordt geschaald zodat het in 84% van de breedte én 84% van de hoogte van 1920×1080 past (factor = min(0,84×1920/b, 0,84×1080/h)), beeldverhouding behouden, gecentreerd.
- **Klikcirkel**: in uitvoercoördinaten (1920×1080) van het ingezoomde kader op het kliktijdstip, begrensd tot het zichtbare scherm.
- **Huisstijlkleuren** staan als constanten in `videos/` (`#0B1628`, `#1A2D4A`, `#4A7CC9`), overgenomen uit `bronnen/brand.json`; de pijplijn leest geen bouwdocumenten tijdens het draaien.
- **Interface**: `python3 videos/maak.py <map> [--plan-only] [--stem test|openai]`; `videos/stem.py` met `openai_aanvraag(tekst, sleutel)` die een dict `{url, headers, body}` teruggeeft (body is een dict) zonder te versturen; `videos/README.md` noemt de omgevingsvariabele `OPENAI_API_KEY`.
- **Eén keer renderen per testmodule** (`setUpClass`, tijdelijke map) om binnen `check_timeout` te blijven.

## 8. Testplan en dummydata

Zie `testplan.md`. Dummydata: `tests/fixtures/video/` met een script van drie stappen, een testopname van 20 s (1440×900, gemaakt in de test met `ffmpeg testsrc2`, niet in git) en een kliklog met twee klikken. Randgevallen: een stap zonder klik, een stem langer dan de handeling, een log met een klik buiten het scherm (wordt begrensd), ontbrekende stem.

## 9. Definition of done

- Elke feature klaar of geblokkeerd met reden; basistest groen.
- Keurder: rendert de testvideo, bekijkt vijf stilstaande beelden en het renderplan; geen verzonnen tijdstippen.

## 10. Budget

4 uur, 12 sessies, 2 features per sessie, bouwer en keurder `opus`.

## 11. Designrichting

Huisstijl van Debug Marketing uit `brand.json`: achtergrondverloop `#0B1628` → `#1A2D4A`, klikcirkel `#4A7CC9` met 40% dekking, scherm met 24 px afgeronde hoeken. Lettertype is niet van toepassing (geen ingebrande tekst).

## 12. Keten

- **Plaats:** run 2 van 3. **Wacht op:** R1 (`--na dc-r1-coach`). **Bouwt op:** de tak van R1 (`--bouw-op vorige`). **Pakket:** na R3, één blokpakket.
- **Eindigt R1 met geblokkeerde features:** R2 bouwt toch en raakt R1-werk niet aan. De basistest van R2 is enkel de regressie van R1 (`BASIS`), niet de R1-features.
