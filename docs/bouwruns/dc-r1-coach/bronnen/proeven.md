# Proeven op het demo-account (Plus)

| Proef | Datum | Uitkomst | Gevolg |
|---|---|---|---|
| P1 coach op Plus | 15/10 | **Deels.** Het antwoord begon met KOMPAS (het projectbrein `AGENTS.md` werd gelezen), `profiel-voorbeeld.md` gelezen, `proef-resultaat.md` geschreven. Niet bevestigd: dat het via de geïnstalleerde plugin in Work liep (de hele proeflijst werd in één agent geplakt). | Herhalen: de plugin met de hand installeren, dan enkel "doe de proef" |
| P2 updates | 15/10 | Niet uitgevoerd (de agent kon de app niet bedienen; dit is een kijkproef voor Bjorn) | Herhalen met de hand |
| P3 ChatGPT neemt op | 15/10 | **Gezakt.** De schermopname werd meteen afgebroken; TextEdit bedienen liep vast; geen opname, geen log | Herhalen na het installeren van de plugin Computer Use en het geven van de toestemmingen Schermopname en Toegankelijkheid (feit C12) |
| P4 Outlook.com in Work | 15/10 | **Gezakt.** Fout van de browserverbinding bij het openen van Outlook | Eén keer herhalen in Work; blijft het falen, dan terugvalroute "mails bewaren of plakken" |

## Ronde 2 (15/10, opnieuw in één agent geplakt, gelopen in Codex op het demo-account)

| Proef | Uitkomst | Gevolg |
|---|---|---|
| P1, P2 | **Geblokkeerd door OpenAI zelf:** "Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons." Een agent van ChatGPT mag de ChatGPT-app niet bedienen. | P1 en P2 kan enkel een mens (of een agent buiten ChatGPT) doen |
| P3 | **Opnemen lukt** (`screencapture` buiten de zandbak: 25 s, 2704×1756, hoofdscherm 1352×878 punten, schaal 2). **Maar:** TextEdit stond niet zichtbaar in beeld (Computer Use werkt op macOS op de achtergrond; er is ook een tweede scherm), tijdstippen geschat, geen klikcoördinaten. | ChatGPT kan **zijn eigen app niet opnemen** en logt geen kliks: het videoplan B6 werkt zo niet voor video's van de ChatGPT-app |
| P4 | **Gelukt** in de ingebouwde browser: Outlook.com geopend, de gebruiker logde zelf in, zoekopdracht met datumfilter, tijdlijn gemaakt, niets verstuurd of verplaatst. Bijwerking: geopende mails krijgen de status gelezen. Ruis: meldingen van een geblokkeerde trackingdienst (HTTP 403), niet storend. | Missie 4 route ChatGPT = de ingebouwde browser; de missie zegt vooraf dat geopende mails op gelezen komen |

## Ronde 3 (15/10, Claude Computer Use bedient de ChatGPT-app op Bjorns laptop, demo-account Plus)

| Proef | Uitkomst | Gevolg |
|---|---|---|
| P1 | **Gelukt.** Na openen van de werkmap in Work en herstart stond onder Plugins > tabblad **Personal** de catalogus; installeren lukte; `@debug-coach-proef doe de proef` in Work gaf KOMPAS (AGENTS.md gelezen), map gelezen, bestand geschreven. De lijst toont de pluginnaam (`name`), niet `interface.displayName`. | Plugin `name` = wat de gebruiker ziet: `debug-coach`. Route ChatGPT bewezen op Plus |
| P2 | **Gelukt.** Plugins > Add: Create plugin · **Add a marketplace** · Upload plugin archive · Add custom MCP server · Record a skill | Updates kunnen via "Add a marketplace" lopen als die een publieke GitHub-repo aanvaardt (P2b) |
| P5 | **Deels.** Klikposities en tijden exact gelogd (1352×878 punten, schaal 2); klikbeelden tonen ChatGPT op de juiste plek. Geen video: Claude had geen recht Schermopname. Claude kwam soms vooraan tijdens het werk. Bijkomend: de zijbalk van de app op de laptop toont Bjorns eigen projecten en recente gesprekken, ook op het demo-account. | Echte opnames op een propere machine (de mini); P5 herhalen met het recht Schermopname en opname van enkel het ChatGPT-venster |

## Ronde 4 (15/10, Claude Computer Use, na het recht Schermopname)

| Proef | Uitkomst | Gevolg |
|---|---|---|
| P2b | **Gelukt.** Add a marketplace met `BinaryBjorn/debug-coach` (enkel het veld Source) aanvaard; onder Personal verscheen de catalogus `debug-marketing` met de plugin `debug-coach`. Verwijderen via tandwiel > Settings > Plugins > Marketplace > prullenbak; daarna Refresh. | Installeren en updaten van de coach via GitHub in beide apps (C17) |
| P5 | **Gelukt.** Opname van enkel het ChatGPT-venster, klikbeelden kloppen tot op 2 punten, geen ander venster ervoor. Volledige werkwijze en log: `proef-p5/VERSLAG.md` en `proef-p5/log.json`. | Werkwijze hieronder is de basis voor elke `opname.md` (R1 C11) |

### Werkwijze P5 (letterlijk, basis voor `opname.md`)

**Normatief is `tests/fixtures/gedeeld/log.schema.json`.** Het log in `proef-p5/log.json` is een oudere vorm (vrije tekst in `handeling`, extra velden); `opname.md` laat Claude schrijven in de vorm van het schema (`handeling` uit klik, typ, wacht, start, einde).

1. ChatGPT-venster vooraan, niet schermvullend; zwevende Claude-panelen buiten het venster houden.
2. Positie en grootte van het venster in logische punten bepalen (in P5 uit de CoreGraphics-vensterlijst: x 0, y 30, 805 × 720; `osascript` met System Events kreeg geen toegang).
3. Opname starten op de achtergrond: `screencapture -v -V <seconden> -R<x>,<y>,<breedte>,<hoogte> videos/<slug>/ruw/opname.mov` en het starttijdstip noteren met `python3 -c "import time;print(time.time())"` (`opname.start_commando`).
4. Vlak vóór elke klik het tijdstip noteren (zelfde commando) en de klikpositie in logische schermpunten; een event `typ` na de klik als er getypt wordt.
5. Na de opname `start_video_gemeten` meten: zoek in de video het tijdstip v1 van de eerste beeldwissel na de eerste klik; dan `start_video_gemeten = t_klik1 − v1` (afgerond op 0,01 s). In P5 lag dat 0,29 s na `start_commando`.
6. `videos/<slug>/ruw/log.json` schrijven in de vorm van `log.schema.json`; per klik een controlebeeld uit de opname halen (`ffmpeg -ss <t − start_video_gemeten> -i opname.mov -frames:v 1 ...`) en nakijken dat het ChatGPT-venster en de klikplek kloppen.
7. Recht Schermopname: ook voor de ingebouwde Claude Code-app (K8).
