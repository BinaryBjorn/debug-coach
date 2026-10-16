# Opname: De coach uitzetten

> **Opdracht voor Claude met Computer Use** op de Mac mini. Je bedient de ChatGPT-desktopapp en neemt enkel het ChatGPT-venster op. Daarna schrijf je `ruw/opname.mov` en `ruw/log.json`. Je bewerkt niets: de video wordt later gemaakt door de pijplijn (`videos/maak.py`, run 2).

**Slug:** `coach-uitzetten` · **Script:** `videos/coach-uitzetten/script.json` (6 stappen, samen 37 s gesproken tekst) · **App:** ChatGPT desktop (Work)

## Voor je begint

1. **Enkel het demo-account.** Log in ChatGPT in met het demo-account, nooit met een eigen account. Kijk de zijbalk na: staan er eigen projecten of recente gesprekken van iemand anders in, stop dan en meld het (zie proef P5).
2. **Enkel nepdata in beeld.** Elke naam, mail, map en elk document dat in beeld komt, is verzonnen. Maak de werkmap met `python3 scripts/bouw_werkmap.py` en kopieer `dist/debug-coach-werkmap/` naar de demomap; vul het profiel met een verzonnen persoon (bv. Sam Peeters, projectleider bij het verzonnen bedrijf Noorderlicht). Nooit echte namen, mails of klantgegevens.
3. **Uitgangstoestand voor deze video:** werkmap met nepdata, de coach staat op uitgebreid.
4. **Recht Schermopname** staat aan voor de ingebouwde Claude Code-app (`~/Library/Application Support/Claude/claude-code/<versie>/.../claude.app`), niet enkel voor Claude.app. Na een update van Claude mogelijk opnieuw.

## Werkwijze

1. **ChatGPT-venster vooraan**, niet schermvullend. Zet het venster vooraan met Computer Use. Houd elk zwevend Claude-paneel buiten het venster: niets mag over ChatGPT liggen.
2. **Venster meten.** Bepaal positie en grootte van het ChatGPT-venster in logische punten uit de CoreGraphics-vensterlijst (in P5: x 0, y 30, 805 × 720; `osascript` met System Events krijgt geen toegang). Noteer ook de schermmaat in logische punten en de schaal (pixels per punt: 2 op een Retina-scherm, 1 op een gewoon scherm).
3. **Opname starten** op de achtergrond, met `-R` op enkel het gebied van het venster:

   ```
   mkdir -p videos/coach-uitzetten/ruw
   python3 -c "import time;print(time.time())"
   screencapture -v -V 171 -R<x>,<y>,<breedte>,<hoogte> videos/coach-uitzetten/ruw/opname.mov &
   ```

   Het getal van de tweede regel is `opname.start_commando`. Wacht twee seconden voor de eerste handeling.
4. **Elke stap uit het script uitvoeren, in volgorde.** Elke handeling hoort bij precies één stap: noteer bij elk event de stap-id (`s01`, `s02`, ...). Vlak vóór elke klik noteer je het tijdstip met `python3 -c "import time;print(time.time())"` en de klikpositie in logische schermpunten (niet relatief aan het venster). Na een klik om te typen volgt een event `typ` met de getypte tekst. Het eerste event van `s01` is `start`, het laatste event van de laatste stap is `einde`.
5. **Tempo.** Werk rustig: na een klik minstens een halve seconde niets doen. Een stap duurt in de video minstens zo lang als zijn gesproken tekst; is de handeling korter, dan bevriest het beeld. Verstuur nooit iets buiten ChatGPT en laat ChatGPT nooit een mail versturen.
6. **Opname afronden.** Wacht tot `screencapture` stopt (na 171 s), of stop het met `kill -INT` op het proces als alles gedaan is.
7. **`start_video_gemeten` meten aan de eerste beeldwissel.** Zoek in de video het tijdstip v1 van de eerste beeldwissel na de eerste klik, bv. met

   ```
   ffmpeg -i videos/coach-uitzetten/ruw/opname.mov -vf "select='gt(scene,0.003)',showinfo" -f null - 2>&1 | grep pts_time
   ```

   Neem de eerste `pts_time` vanaf (t_klik1 − start_commando − 0,5). Dan is `start_video_gemeten = t_klik1 − v1`, afgerond op 0,01 s. In P5 lag dat 0,29 s na `start_commando`; wijkt het meer dan een seconde af, kijk dan opnieuw.
8. **`ruw/log.json` schrijven** in de vorm van `tests/fixtures/gedeeld/log.schema.json`:

   ```json
   {
     "scherm": {"breedte": 1352, "hoogte": 878, "schaal": 2},
     "gebied": {"x": 0, "y": 30, "breedte": 805, "hoogte": 720},
     "opname": {"start_commando": 0.0, "start_video_gemeten": 0.0},
     "events": [
       {"t": 0.0, "stap": "s01", "handeling": "start"},
       {"t": 0.0, "stap": "s01", "handeling": "klik", "x": 100, "y": 110},
       {"t": 0.0, "stap": "s01", "handeling": "typ", "tekst": "..."}
     ]
   }
   ```

   `handeling` is altijd één van `klik`, `typ`, `wacht`, `start`, `einde`. `x` en `y` enkel bij een klik, `tekst` enkel bij typ. Alle tijden in epoch-seconden. De waarden hierboven zijn voorbeelden: vul de echte in.
9. **Nakijken.** Haal per klik een controlebeeld uit de opname (`ffmpeg -ss <t − start_video_gemeten> -i videos/coach-uitzetten/ruw/opname.mov -frames:v 1 videos/coach-uitzetten/ruw/klik-<stap>.png`) en kijk na: het ChatGPT-venster staat in beeld, de cursor staat op de klikplek, er ligt geen ander venster voor, en er staat enkel nepdata in beeld. Klopt iets niet, neem de video opnieuw op.

`videos/*/ruw/` en `videos/*/uit/` staan in `.gitignore`: de opname en het log gaan nooit mee in git.

## Stappen

| Stap | Handeling | Wat je logt | Gesproken tekst |
|---|---|---|---|
| `s01` | Klik in het invoerveld, typ: hoe staat de coach? en verstuur | `klik` in het veld, `typ` met de getypte tekst, `klik` op versturen of op de knop | Hoeveel uitleg de coach geeft, kies je zelf. Vraag: hoe staat de coach? |
| `s02` | Wacht tot het antwoord er staat | `wacht` bij het begin, minstens de duur van de stap wachten, dan nog een `wacht` | Er zijn drie standen: uitgebreid, kort en uit. |
| `s03` | Typ: korter, en verstuur | `klik` in het veld, `typ` met de getypte tekst, `klik` op versturen of op de knop | Wil je minder uitleg, zeg dan: korter. Dan legt de coach enkel nieuwe begrippen uit, in één zin. |
| `s04` | Typ: zet de coach uit, en verstuur | `klik` in het veld, `typ` met de getypte tekst, `klik` op versturen of op de knop | Zeg: zet de coach uit. Dan doet hij het werk zonder uitleg, tenzij je erom vraagt. |
| `s05` | Wacht tot het antwoord er staat | `wacht` bij het begin, minstens de duur van de stap wachten, dan nog een `wacht` | Ook in de stand uit waarschuwt de coach altijd vóór iets wat je niet kan terugdraaien, zoals versturen of verwijderen. |
| `s06` | Typ: zet de coach terug aan, en verstuur | `klik` in het veld, `typ` met de getypte tekst, `klik` op versturen of op de knop | Wil je terug meer uitleg, zeg dan: zet de coach terug aan. |

## Beginsituatie

Missie 1 klaar, coach op stand uitgebreid. Enkel het demo-account en nepdata in beeld (persona Sam, Noorderlicht Techniek, verzonnen).
