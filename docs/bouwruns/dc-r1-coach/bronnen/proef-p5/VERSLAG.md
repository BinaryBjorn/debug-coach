# Verslag proef-claude-2 (15 okt 2026)

ChatGPT-desktopapp (bundle `com.openai.codex`, demo-account). Computer Use voor de app, shell voor bestanden.

## P2b. Een catalogus vanaf GitHub

**Resultaat: aanvaard.** Plugin `debug-coach` verscheen. Verwijderen lukte.

Verloop:
1. Plugins › Add › **Add a marketplace** opent het dialoogvenster "Add plugin marketplace", met drie velden: Source, Git ref (placeholder `main`) en Sparse paths (placeholder `plugins/codex`). Alleen Source ingevuld: `BinaryBjorn/debug-coach`. Daarna **Add marketplace**.
2. Er kwam geen foutmelding. Het dialoogvenster sloot en de app sprong naar het tabblad *Public*. Ik heb geen bevestigingstoast gezien (wel mogelijk dat ik hem gemist heb).
3. Onder *Personal* staat nu een nieuwe sectie **`debug-marketing`** met plugin **`debug-coach`** (git-icoon, `+` om te installeren, niet geïnstalleerd). Screenshot: `p2b-resultaat.png`.
   - Let op: de catalogus heet `debug-marketing`, niet `debug-coach`. De naam komt dus uit de marketplace-manifest in de repo, niet uit de reponaam.
   - In `~/.codex/config.toml` verscheen:
     ```
     [marketplaces.debug-marketing]
     source_type = "git"
     source = "https://github.com/BinaryBjorn/debug-coach.git"
     ```
   - Log: request `marketplace/add` om 17:38:21.
4. **Verwijderen:** de catalogus heeft op de Plugins-pagina zelf geen menu (geen `…` bij de kop `debug-marketing`). De optie staat onder het tandwiel (**Manage**) › Settings › Plugins › tabblad **Marketplace (1)**. Daar staat `debug-marketing` met "1 plugin", een **Upgrade**-knop en een prullenbak. De prullenbak opent de vraag *"Remove 'debug-marketing'?"* met de uitleg dat de plugins niet meer verschijnen tot je de catalogus opnieuw toevoegt. Na **Remove** verscheen de toast "debug-marketing marketplace removed". Het blok verdween uit `config.toml`.
5. **Bijzonderheid:** terug op de Plugins-pagina (tijdens P5, s03) stond `debug-marketing › debug-coach` er nog, nu met een mapicoon in plaats van het git-icoon. Na een klik op **Refresh** was hij weg. Zie `p2b-na-verwijderen-refresh.png`. De lijst is dus een cache die pas bij Refresh bijwerkt.

Voor de flow betekent dit: een gebruiker moet het tandwiel kennen om een catalogus te verwijderen, en na verwijderen moet hij op Refresh drukken, anders lijkt het niet gelukt.

## P5. Opname van enkel het ChatGPT-venster

**Resultaat (poging 2): gelukt.** De opname bevat enkel het ChatGPT-venster. Op elk klikbeeld staat ChatGPT, de cursor staat op de juiste plek en er ligt geen ander venster voor.

### Poging 1: mislukt door ontbrekend schermopname-recht
Elke `screencapture` faalde met exit 1 ("could not create image from rect"), met én zonder `-R`. Het recht aanzetten voor Claude.app hielp niet. Claude start mijn shell via `/Applications/Claude.app/Contents/Helpers/disclaimer`, en dat hulpprogramma geeft de verantwoordelijkheid door aan de ingebouwde Claude Code-app: `~/Library/Application Support/Claude/claude-code/<versie>/<hash>/claude.app`. macOS kijkt alleen naar die app. Pas nadat Bjorn ook díe aan Schermopname toevoegde en Claude herstartte, werkte het.
**Voor Debug Coach:** het vinkje bij "Claude" volstaat niet. Bij een update van Claude Code (nieuwe versiemap) moet het mogelijk opnieuw.

### Poging 2
1. **Venster.** `osascript … System Events` faalt hier ("osascript is not allowed assistive access"). Ik heb positie en grootte daarom niet geschat, maar uit de CoreGraphics-vensterlijst gehaald: **x 0, y 30, 805 × 720** (logische punten).
   - Scherm: 1352×878 logisch, schaal 2. Een tweede scherm (3840×1080) staat erboven.
   - Ik had het venster eerder al smaller gesleept (het was 1352×848). Een **zwevend Claude-paneel** (laag 3, x 812–1332, y 50–770) lag over de rechterkant van ChatGPT. Het is onzichtbaar in mijn screenshots, en sommige van mijn eerste klikken in P2b kwamen daardoor in Claude terecht. Met x ≤ 805 valt dat paneel buiten het opnamegebied.
   - Na de herstart lag het grote Claude-venster vóór ChatGPT. Mijn eerste Computer Use-actie zette ChatGPT vooraan; Chrome, Teams, Telegram, Barri, Outlook en TextEdit werden daarbij verborgen.
   - Voor een schone start heb ik de concepttekst "Hallo coach" van poging 1 leeggemaakt en ChatGPT op Home gezet.
2. **Opname.** `screencapture -v -V 35 -R0,30,805,720 proef-claude-2/opname.mov` (met -R, dus zonder fallback). Tijdstip van het commando: 1792079252.987. Resultaat: 35,0 s, 1610×1440 px (805×720 × schaal 2), 120 fps, 25,8 MB.
3. **Klikstappen**, met het tijdstip vlak vóór elke klik (Python `time.time()`):

   | stap | handeling | t | x, y (logisch) | video-offset |
   |---|---|---|---|---|
   | s01 | klik New chat | 1792079255.031 | 122.2, 140.9 | 1.751 s |
   | s02 | klik invoerveld, typ "Hallo coach" (niet verstuurd) | 1792079259.222 | 571.5, 402.1 | 5.942 s |
   | s03 | klik Plugins (linkerbalk) | 1792079263.537 | 25.6, 275.9 | 10.257 s |

4. **Videoklok ≠ commandotijd.** Eerst haalde ik de beelden op `t − starttijdstip commando`. Die toonden al de toestand *na* de klik ("Hallo coach" stond er al, de Plugins-pagina was al open). Daarom heb ik in de video gezocht waar het beeld verandert: op 1,75 s, 5,95 s en 10,25 s. Vergeleken met de drie tijdstempels geeft dat telkens dezelfde vertraging: de video start **0,29 s (±0,01) na het commando**, op ongeveer 1792079253.28. Dat staat in `log.json` als `opname.start_video_gemeten`. Dat veld komt bovenop de gevraagde vorm; zonder dat veld kan een script niet van kliktijd naar videoframe rekenen.
   **Gevolg voor de pipeline:** het moment waarop `screencapture` start is niet het eerste frame. Meet de start (bv. met een eerste klik als ijkpunt, of via een beeldwissel), anders zitten alle frames ±0,3 s te laat.
5. **Beelden per klik** (`ffmpeg -ss <t − video-start>`), met elk een controlebeeld 1 s later (`-na`):
   - `klik-s01.png`: ChatGPT staat erop, de cursor staat op "New chat" (video ≈ 120,140 logisch), er ligt geen ander venster voor. Op `-na` is "New chat" gemarkeerd en het invoerveld leeg.
   - `klik-s02.png`: ChatGPT, de I-cursor staat in het lege invoerveld (≈ 572,402), geen ander venster. Op `-na` staat er "Hallo coach" en is de verstuurknop actief, maar niet verstuurd.
   - `klik-s03.png`: ChatGPT, de cursor staat op het Plugins-icoon (≈ 24,276) en de pagina is nog Home. Op `-na` staat de Plugins-pagina open. Geen ander venster.
   - De cursorposities in de video vallen binnen 2 punten samen met de gelogde coördinaten.

## Bestanden
- `p2b-resultaat.png`: Personal-tab met `debug-marketing › debug-coach`
- `p2b-na-verwijderen-refresh.png`: na Remove en Refresh, catalogus weg
- `opname.mov`: 35 s, enkel het ChatGPT-venster
- `log.json`: scherm, gebied, opname, drie events
- `klik-s01.png`, `klik-s02.png`, `klik-s03.png` (+ `-na`-controlebeelden)

## Neveneffecten
- ChatGPT-venster verkleind naar 805×720 (was 1352×848).
- Zoekveld op de Plugins-pagina leeggemaakt (er stond nog "Hallo coach" van een vorige proef).
- Er staat een nieuwe chat met concepttekst "Hallo coach" (niet verstuurd), uit poging 2.
- Catalogus `debug-marketing` toegevoegd en weer verwijderd. `config.toml` is terug zoals vóór de proef.
