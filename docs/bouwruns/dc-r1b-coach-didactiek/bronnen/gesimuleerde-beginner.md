# Gesimuleerde beginner Debug Coach (blok 1)

**Haalt een beginner het zonder hulp? Deels.** Sam raakt zonder vastlopen door missie 1 tot 7 en drie treden. Maar dat lukt vooral omdat de coach het werk zelf doet: Sam leert weinig zelf vragen, en missie 7 staat op klaar terwijl de skill nooit geüpload of getest is.

## Opzet

- **Route:** Claude (Claude Code zonder scherm, `--plugin-dir`, model sonnet, `acceptEdits`), persona Sam (accountmanager, Noorderlicht Techniek, persoonlijk Hotmail-account). De ChatGPT-route is niet uitgeprobeerd.
- **Werkmap:** gebouwd met `scripts/bouw_werkmap.py` in een kopie (`sim/dc-kopie/`), plus Sams dummybestanden in `mijn-bestanden/`: een CV, `offertes-q1.csv`, vijf mails over de beurs en een transcript.
- **Afscherming:** `--setting-sources project,local` en `--strict-mcp-config`, zodat Bjorns eigen CLAUDE.md, plugins en MCP's niet meelezen (nagekeken: de coach zag geen vault-instructies).
- **Kosten en tijd:** 44 berichten in één sessie, samen **$10,09** en **24 minuten** rekentijd. Daarbovenop: een mislukte eerste poging ($0,28) en de skilltest ($0,21). Missie 6 alleen kostte $2,15 en 260 seconden in de eerste beurt (zie de testbeperkingen hieronder).
- **Bronnen:** het volledige gesprek staat in `sim/transcript-volledig.md`, het log per beurt (nieuwe en gewijzigde bestanden, kosten) in `sim/log.md`.

## Per missie en per trede

| Stap | Gelukt | Berichten | Wat er in de werkmap kwam | Hapering |
|---|---|---|---|---|
| M1 De coach leert jou kennen | ja | 9 | `ik/profiel.md` gevuld (Platform `claude`, Account `persoonlijk (Hotmail)`, Coachcode `nl7k2p9q`, hoofdletters goed omgezet), `voortgang.md` 1/7, feedbackrij | Het werkmappakket bevat al alle templates, dus `start` neemt de weg "tweede keer": geen welkom, geen tabel van de werkmap, geen uitleg over projectbrein of context, en geen meter na het afsluiten. De eerste feedbackrij werd geschreven met `[TODO: vraag aan gebruiker]` en pas aangevuld na Sams antwoord. Trainingsschakelaar wel besproken ("Eerlijk gezegd weet ik niet zeker hoe die instelling in Claude heet"). |
| M2 Je eerste project | ja | 6 | `projecten/beurs-2027/` met README, 3 bronnen (gekopieerd uit `mijn-bestanden`), `overzicht-koen.md`; rij in successen | De coach koos de bronnen en schreef de README zelf. Toonde wel wat een goede vraag bevat, maar Sam nam gewoon het voorbeeld over. De uitleg over projecten in Claude (stap 5 van de route) ontbrak. Lagere stand voorgesteld: werkt, ook vastgelegd in de feedback. |
| M3 Bestanden en mail binnenhalen | ja | 5 | `bronnenlijst.md`, `samenvatting-offerte-kubus.md` | Bronnenlijst gemaakt vóór Sam iets koos. OneDrive kort vermeld en overgeslagen ("Dat werk is dus al gedaan"). Op Sams vraag hoe nieuwe Hotmail-mails binnenkomen: enkel "bewaar als bestand of plak", zonder te zeggen hoe je dat doet in Outlook.com. |
| M4 Tijdlijn uit je mails | ja | 4 | `tijdlijn-beurs-2027.md` (6 data, 5 open punten, bron per regel) | Grootste leerverlies. Sam koos geen onderwerp of periode: "Ik neem het dossier beurs 2027 ... Ik maak de tijdlijn nu." Op "hoe deed je dat?" sloot de coach eerst de missie af. Pas na een tweede vraag kwam de herbruikbare vraag. Sams feedback: "je deed alles al voor ik iets kon kiezen". |
| M5 Van gesprek naar verslag | ja | 3 | `verslag-10-10-2026.md`, `concept-mail-lien-koen.md` (concept, niet verstuurd) | Goed: Sam stelt zelf de vraag. Wel kleine fouten. De samenvatting zegt dat nog beslist moet worden wie het toestel regelt, terwijl de beslissing staat dat de werkplaats het doet. De mail zegt "ons overleg van vandaag" voor een overleg van vijf dagen geleden. Toestemming om op te nemen en de audio-twijfel uit de Claude-route niet vermeld (er lag al een transcript). |
| Coach op kort | ja | 1 | Enkel de regel `**Stand:**` in CLAUDE.md en AGENTS.md (rest byte voor byte gelijk) | Geen. Bevestiging en waarschuwingsregel volgens de skill. |
| M6 Excel en PowerPoint | ja | 4 | `projecten/offertes-q1/` met kopie van de csv, `analyse-offertes-q1.xlsx` met een kolom "% van totaal" | De coach koos zelf het bestand. Eerst geen xlsx (Python was geblokkeerd in de test). Daarna verwijderde hij de tussen-csv **zonder te waarschuwen**, tegen de vaste regel in. De feedbackrij vulde hij zelf in ("Wat precies een echt .xlsx-bestand is ...") zonder Sam de twee vragen te stellen. |
| M7 Je eigen vaardigheid | **nee, maar wel op klaar gezet** | 4 | `projecten/eigen-skills/eigen-offerte-opvolging/SKILL.md` + zip | De coach schreef de skill in één beurt, zonder het samen te doen. Sam: "ik vind die customize knop niet". Coach: "Normaal zit Customize bij je accountinstellingen (vaak via je naam of avatar ...)". Toch: "Missie 7 staat op klaar", terwijl "werkt in een nieuw gesprek" niet gehaald was. Ik testte de skill zelf in een nieuwe sessie (als losse plugin): die werkt. De uploadroute is niet getest. |
| T1 niveau 1 | ja | 3 | `projecten/nieuwsbrief-klanten/README.md` + `inhoud-idee.md` | Het "bronbestand" maakte de coach zelf uit Sams chatzin. |
| T2 niveau 2 | ja | 2 | `contentoverzicht-nieuwsbrief.xlsx` | "Combineren" werd één vaardigheid (enkel Excel), geen twee. |
| T3 niveau 3 | deels | 2 | SKILL.md uitgebreid, zip opnieuw gemaakt (overschreven zonder te vragen) | Klaar zonder opnieuw te uploaden of te testen. Dat je de skill opnieuw moet uploaden, werd niet gezegd. |
| Opnieuw "start" | ja | 1 | niets | Overschrijft niets, toont de meter en wijst naar de ladder. |

## Controle tegen het contract

| Check | Resultaat |
|---|---|
| Bestanden | profiel (met de vier Werkwijze-regels in de juiste vorm), voortgang, successen (7 rijen), feedback (7 rijen), ladderlog (3 rijen), projecten/: allemaal aanwezig |
| Voortgangslink | Tien keer correct: `https://debug.marketing/coach/v?s=m1..m7&k=nl7k2p9q` en `s=t1..t3`. Maar altijd tussen backticks, dus als code en niet klikbaar. |
| Geen overschreven bestanden | De bestanden van Sam (`mijn-bestanden/`) zijn onaangeroerd. Templates enkel aangevuld waar dat mocht. Uitzonderingen: een csv verwijderd (M6) en een zip overschreven (T3), allebei zonder te vragen. |
| Nederlands | ja, overal |
| Em dash (lang streepje) | 0 in wat de coach zei, 0 in de werkmap. Wel in de output van Sams eigen skill in de nieuwe sessie (niet de coach). |
| Slash-commando's | 0 |
| Coachstand wisselen | werkt, beide bestanden, enkel die ene regel |
| "Denk eraan als:" | Enkel 2 keer in 44 beurten, en allebei op vraag van Sam ("leg uit wat een skill is", "wat is een bronnenlijst"). In de stand uitgebreid gaf de coach uit zichzelf nooit een begrip uit `## Begrippen` in die vorm, op één losse variant na ("Denk aan 'lokaal' als:"). |

## Top 5 verbeterpunten

1. **De coach doet het werk in de plaats van de beginner** (M2, M3, M4, M6, M7, T3).
   - **Plek:** `plugin/skills/missie/SKILL.md` stap 3, en de routes in `plugin/missies/missie-0N.md`.
   - **Voorstel:** een harde regel in stap 3: "Maak niets in dezelfde beurt als het voorstel van de missie. Laat de gebruiker eerst het dossier, het bestand of het onderwerp kiezen en de vraag zelf stellen. Verbeter die vraag, en voer pas dan uit." Markeer in de missiebestanden per stap wie ze doet ("jij" of "de coach").
2. **"Klaar als" wordt niet echt gecontroleerd** (M7 op klaar zonder upload of test, T3 zonder heruploaden).
   - **Plek:** `plugin/skills/missie/SKILL.md` stap 4, `plugin/missies/missie-07.md`, `plugin/skills/uitdaging/SKILL.md` stap 4.
   - **Voorstel:** een item dat buiten de chat gebeurt ("werkt in een nieuw gesprek", "geüpload") telt pas als de gebruiker bevestigt dat hij het deed. Anders blijft de missie op `bezig`, zonder link. Zet het echte menupad naar Customize > Skills (uit `bronnen/platformfeiten.md`) stap voor stap in "Wat kan hier fout gaan", zodat de coach het niet moet raden. Voeg bij niveau 3 van de ladder toe: "opnieuw uploaden en testen".
3. **De feedbackrij met verzonnen of lege antwoorden** (M1 eerst `[TODO]`, M6 en M7 ingevuld zonder dat de vragen gesteld waren).
   - **Plek:** `plugin/skills/missie/SKILL.md` en `plugin/skills/start/SKILL.md`, stap "Eén rij in feedback.md".
   - **Voorstel:** "Schrijf de kolommen Onduidelijk en Vastgelopen enkel met het letterlijke antwoord van de gebruiker. Stel de twee vragen, en schrijf de rij pas in je volgende beurt. Vul nooit zelf in." Dit bestand gaat naar Bjorn, dus verzonnen rijen vervuilen de evaluatie.
4. **Een vers werkmappakket wordt behandeld als een tweede keer**, waardoor het welkom en de uitleg wegvallen (geen werkmaptabel, geen projectbrein, geen context, geen meter na M1).
   - **Plek:** `plugin/skills/start/SKILL.md` stap 0 en stap 3.
   - **Voorstel:** staan alle missies op `open` en het profiel op `status: leeg`, dan is het een nieuwe start: doe het welkom, de tabel en de uitleg over projectbrein en context, ook al bestaan de bestanden. Herhaal onderaan stap 2: "na missie 1 altijd de meter met de tabel".
5. **De stand uitgebreid legt bijna niets uit uit zichzelf** (2 keer "Denk eraan als", allebei op vraag).
   - **Plek:** `plugin/skills/missie/SKILL.md` stap 3.
   - **Voorstel:** "In uitgebreid leg je per missie minstens één begrip uit `## Begrippen` uit, op het moment dat het opduikt, letterlijk met **Denk eraan als:**. In kort: één zin per nieuw begrip, ook als de gebruiker er niet om vraagt."

**Kleiner, maar het noteren waard:**
- De link staat tussen backticks en is dus niet klikbaar. Schrijf in start, missie en uitdaging: "de link als gewone tekst, nooit als code".
- Waarschuwen vóór verwijderen of overschrijven vergeten (M6 csv, T3 zip), hoewel de skill coach het belooft.
- Technische woorden voor de gebruiker: "Ik zet je platform alvast op `claude`", bestandsnamen tussen backticks.
- Hoe je een mail als bestand bewaart vanuit Outlook.com staat nergens. Hoort in `missie-03.md`, maar enkel met een geverifieerd menupad.
- Ladder niveau 2 werd geen echte combinatie. `ladder.md` kan eisen dat de uitdaging twee missienummers noemt.

## Wat ik niet kon testen

- **De hele ChatGPT-route:** Work, `AGENTS.md` als projectbrein, de plugin `mijn-vaardigheden` en Plugins > Refresh, Data controls, Outlook.com in de ingebouwde browser (M4), audio uploaden (M5), Computer Use en de add-ins (M6).
- **Echte klikken in de Claude-app:** het formulier in Cowork (de widget bestaat niet in Claude Code), Customize > Skills > Upload, de marketplace-installatie en updates, OneDrive "altijd op dit apparaat bewaren".
- **De voortgangslink zelf:** of de site (R3) hem aanvaardt. Ik controleerde enkel de vorm.

**Wat de test zelf beïnvloedde:**
- In `claude -p` mocht de coach eerst de pluginbestanden niet lezen. Hij zei dan tegen de gebruiker: "Ik kan het missiebestand voor missie 1 nog niet lezen (geen toestemming)". Ik herstartte met `--add-dir`.
- Python was eerst geblokkeerd (M6, eerste poging), daarna toegelaten met `--allowedTools=Bash`. In Cowork is dat waarschijnlijk anders, maar het toont dat de coach een beperking eerst als technische uitleg aan de gebruiker geeft.
- `-p` geeft enkel het laatste tekstblok terug. De volledige berichten heb ik uit het sessielog gehaald.
- Sams bestanden stonden al in de werkmap. Dat maakte M2 tot M5 makkelijker dan voor een echte beginner, die zijn mails eerst zelf uit Hotmail moet halen.
