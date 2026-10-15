# Opname: Je werkmap klaarzetten

> **Opdracht voor Claude met Computer Use** op de Mac mini. Je bedient de ChatGPT-desktopapp en neemt enkel het ChatGPT-venster op. Daarna schrijf je `ruw/opname.mov` en `ruw/log.json`. Je bewerkt niets: de video wordt later gemaakt door de pijplijn (`videos/maak.py`, run 2).

**Slug:** `klaarzetten` · **Script:** `videos/klaarzetten/script.json` (9 stappen, samen 59 s gesproken tekst) · **App:** ChatGPT desktop (Work)

## Voor je begint

1. **Enkel het demo-account.** Log in ChatGPT in met het demo-account, nooit met een eigen account. Kijk de zijbalk na: staan er eigen projecten of recente gesprekken van iemand anders in, stop dan en meld het (zie proef P5).
2. **Enkel nepdata in beeld.** Elke naam, mail, map en elk document dat in beeld komt, is verzonnen. Maak de werkmap met `python3 scripts/bouw_werkmap.py` en kopieer `dist/debug-coach-werkmap/` naar de demomap; vul het profiel met een verzonnen persoon (bv. Sam Peeters, projectleider bij het verzonnen bedrijf Noorderlicht). Nooit echte namen, mails of klantgegevens.
3. **Uitgangstoestand voor deze video:** lege start: de coach en mijn-vaardigheden zijn nog niet geïnstalleerd; het werkmappakket staat uitgepakt als map debug-coach-werkmap (nepdata).
4. **Recht Schermopname** staat aan voor de ingebouwde Claude Code-app (`~/Library/Application Support/Claude/claude-code/<versie>/.../claude.app`), niet enkel voor Claude.app. Na een update van Claude mogelijk opnieuw.
5. **Dit is de enige video waarin de coach nog niet geïnstalleerd is.** Staat de catalogus `debug-marketing` er al, verwijder hem dan eerst (tandwiel > Settings > Plugins > tabblad Marketplace > prullenbak) en klik op Refresh. Een lokale catalogus verschijnt pas na een herstart van de app: open de werkmap één keer vóór de opname en herstart, zodat `mijn-werkmap` onder Personal staat.

## Werkwijze

1. **ChatGPT-venster vooraan**, niet schermvullend. Zet het venster vooraan met Computer Use. Houd elk zwevend Claude-paneel buiten het venster: niets mag over ChatGPT liggen.
2. **Venster meten.** Bepaal positie en grootte van het ChatGPT-venster in logische punten uit de CoreGraphics-vensterlijst (in P5: x 0, y 30, 805 × 720; `osascript` met System Events krijgt geen toegang). Noteer ook de schermmaat in logische punten en de schaal (pixels per punt: 2 op een Retina-scherm, 1 op een gewoon scherm).
3. **Opname starten** op de achtergrond, met `-R` op enkel het gebied van het venster:

   ```
   mkdir -p videos/klaarzetten/ruw
   python3 -c "import time;print(time.time())"
   screencapture -v -V 237 -R<x>,<y>,<breedte>,<hoogte> videos/klaarzetten/ruw/opname.mov &
   ```

   Het getal van de tweede regel is `opname.start_commando`. Wacht twee seconden voor de eerste handeling.
4. **Elke stap uit het script uitvoeren, in volgorde.** Elke handeling hoort bij precies één stap: noteer bij elk event de stap-id (`s01`, `s02`, ...). Vlak vóór elke klik noteer je het tijdstip met `python3 -c "import time;print(time.time())"` en de klikpositie in logische schermpunten (niet relatief aan het venster). Na een klik om te typen volgt een event `typ` met de getypte tekst. Het eerste event van `s01` is `start`, het laatste event van de laatste stap is `einde`.
5. **Tempo.** Werk rustig: na een klik minstens een halve seconde niets doen. Een stap duurt in de video minstens zo lang als zijn gesproken tekst; is de handeling korter, dan bevriest het beeld. Verstuur nooit iets buiten ChatGPT en laat ChatGPT nooit een mail versturen.
6. **Opname afronden.** Wacht tot `screencapture` stopt (na 237 s), of stop het met `kill -INT` op het proces als alles gedaan is.
7. **`start_video_gemeten` meten aan de eerste beeldwissel.** Zoek in de video het tijdstip v1 van de eerste beeldwissel na de eerste klik, bv. met

   ```
   ffmpeg -i videos/klaarzetten/ruw/opname.mov -vf "select='gt(scene,0.003)',showinfo" -f null - 2>&1 | grep pts_time
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
9. **Nakijken.** Haal per klik een controlebeeld uit de opname (`ffmpeg -ss <t − start_video_gemeten> -i videos/klaarzetten/ruw/opname.mov -frames:v 1 videos/klaarzetten/ruw/klik-<stap>.png`) en kijk na: het ChatGPT-venster staat in beeld, de cursor staat op de klikplek, er ligt geen ander venster voor, en er staat enkel nepdata in beeld. Klopt iets niet, neem de video opnieuw op.

`videos/*/ruw/` en `videos/*/uit/` staan in `.gitignore`: de opname en het log gaan nooit mee in git.

## Stappen

| Stap | Handeling | Wat je logt | Gesproken tekst |
|---|---|---|---|
| `s01` | Laat het venster stil staan op Home | `wacht` bij het begin, minstens de duur van de stap wachten, dan nog een `wacht` | Pak het werkmappakket uit in je OneDrive en zet die map op altijd op dit apparaat bewaren. Zo staan de bestanden echt op je computer. |
| `s02` | Klik bovenaan op Work | `klik` (tijdstip vlak vóór de klik, x en y) | Open ChatGPT en kies bovenaan Work. |
| `s03` | Open in Work de map debug-coach-werkmap en geef toestemming | twee keer `klik`, elk met tijdstip vlak vóór de klik | Open je werkmap: kies de map debug-coach-werkmap en geef Work toestemming om ze te lezen. |
| `s04` | Klik in de zijbalk op Plugins | `klik` (tijdstip vlak vóór de klik, x en y) | Ga in de zijbalk naar Plugins. |
| `s05` | Klik op Add en kies Add a marketplace | twee keer `klik`, elk met tijdstip vlak vóór de klik | Klik op Add en kies Add a marketplace. |
| `s06` | Klik in het veld Source, typ BinaryBjorn/debug-coach en klik op Add marketplace | `klik` in het veld, `typ` met de getypte tekst, `klik` op versturen of op de knop | Vul bij Source in: BinaryBjorn/debug-coach. Klik dan op Add marketplace. |
| `s07` | Klik op het tabblad Personal en op het plusje bij debug-coach | twee keer `klik`, elk met tijdstip vlak vóór de klik | Onder Personal staat nu debug-coach. Klik op het plusje om de coach te installeren. |
| `s08` | Klik op het plusje bij mijn-vaardigheden onder mijn-werkmap | `klik` (tijdstip vlak vóór de klik, x en y) | Installeer ook mijn-vaardigheden uit je werkmap. Daar komen later je eigen vaardigheden. Zie je ze niet, herstart dan de app. |
| `s09` | Open een nieuw gesprek in Work, typ: start, en verstuur | `klik` in het veld, `typ` met de getypte tekst, `klik` op versturen of op de knop | Open een nieuw gesprek in Work en zeg: start. De coach zet je werkmap klaar en leert jou kennen. |
