---
type: verificatie
run: dc-r1-coach
ronde: 1
datum: 2026-10-15
---

# Verificatie dc-r1-coach, keurronde 1

**Hoe gekeurd.** Het contract heeft geen scherm en er is geen testserver: geen browser, geen screenshots, geen design-critic. Gekeurd op de code op deze tak (sinds `327374b`, de commit van het tekenen), de harde checks, en door elke skill letterlijk na te spelen op de dummywerkmappen van het testplan. Het naspelen was een droge run: een hook laat de keurder enkel in de runmap schrijven, dus de schrijfacties zijn uitgerekend en niet echt uitgevoerd in een kopie. De missies zijn gelezen tegen `bronnen/missies-brief.md`, `platformfeiten.md` en `proeven.md`. De belangrijkste feitelijke punten heb ik zelf in de bron nagekeken.

## Scenario's

### S1 Installatie + missie 1: **slaagt niet**

- **Nieuwe start op `werkmap-vreemd/` (Cowork, niet in OneDrive):** werkt. Welkom, OneDrive-tip, "bouw ernaast", tabel, projectbrein, vijf vragen één per bericht, het formulier enkel als extra (geen tool, dus niet aangeboden), coachcode `AB12CD34` wordt `ab12cd34`, de trainingsschakelaar eerlijk als `[TODO]` voor Claude, het profiel in de vier exacte regels, de meter 1/7, de link `s=m1&k=ab12cd34` en één volgende stap. `lijst.csv` en `notities.txt` blijven staan.
- **Opnieuw "start" op `werkmap-missie7/` (7/7, ladder op trede 2):** er wordt niets overschreven. Wel ontbrekende bestanden aangevuld (`CLAUDE.md`, `AGENTS.md`, `projecten/README.md`). Maar de afsluiting is fout. `plugin/skills/start/SKILL.md:209-212` kent maar twee gevallen (missie 1 klaar of niet). De coach zegt daardoor letterlijk *"Volgende missie: je eerste project"*, terwijl alle zeven missies klaar zijn en de gebruiker op de ladder zit. Daarnaast komt er een `projecten/README.md` met de tekst "Nog geen projecten", in een map met drie projecten. Het testplan vraagt precies dit na te spelen.
- **"start" op een werkmap met een gevuld profiel en zonder `voortgang.md`** (`werkmap-claude-werk/`): stap 0 (`SKILL.md:18`) ziet dat als een nieuwe start. Stap 2 stelt dan opnieuw alle vijf vragen en laat het profiel "vullen" en "opnieuw schrijven" (`SKILL.md:147`, `:163`). Het profiel lezen staat enkel in de tak voor een tweede keer (`:21`). Letterlijk gevolgd vervangt de coach een gevuld profiel door nieuwe antwoorden. Het contract zegt "nooit overschrijven" (S1, niet-doel 4).
- **Templates:** het profieltemplate zegt *"Claude leest dit elke keer"* (`templates/ik/profiel.md:7`) en `[TODO: hoe Claude voor jou schrijft ...]` (`:36`). Dat bestand gaat ook in het werkmappakket voor ChatGPT, dus de eerste werkmap die een ChatGPT-gebruiker opent, noemt de verkeerde app. A1 en de definition of done zeggen dat productnamen enkel in route en uitleg staan. Hier staat een uitleg die voor de helft van de gebruikers niet klopt.
- **C01:** het oude root-manifest `.claude-plugin/plugin.json` (versie 0.1.0, met "Start met /start") staat er nog. Zie de harde checks.

### S2 Een missie op echt werk: **slaagt** (met opmerkingen)

- **`werkmap-missie7/`, "volgende missie":** de meter 7/7 en de zin naar de ladder. Klopt.
- **`werkmap-missie7/`, "doe missie 2":** route ChatGPT, geen onnodige vragen (platform en account staan ingevuld), Klaar als gecontroleerd, één rij in successen en één in feedback, één keer een lagere stand voorgesteld (daarna `**Stand:** kort` in beide breinen), meter, link `s=m2&k=ab12cd34` en één volgende stap. Klopt met het contract.
- **Kanttekeningen (geen fout tegen het contract):**
  - Een missie die al `klaar` is opnieuw doen, zet ze op `bezig` en vervangt de oorspronkelijke datum. Wordt de herhaling niet afgemaakt, dan zakt de meter van 7/7 naar 6/7 (`missie/SKILL.md:36`, `:70-71`).
  - De rij in `successen.md` heeft de vorm van een opsomming (`:80`). In de fixture `werkmap-missie7` staat een tabel, dus het bestand krijgt twee vormen door elkaar. Het template legt geen vorm vast, en de fixture is beschermd.
- **Niet na te spelen:** missie 3 op `werkmap-claude-werk/` (claude, werk, code `[TODO]`), zoals het testplan vraagt. De fixture heeft enkel `ik/profiel.md`. De skill stopt dus terecht met *"Je werkmap staat nog niet klaar. Zeg: start ..."* (`missie/SKILL.md:16`). Uit de tekst gelezen klopt de route wel: Route Claude plus `### Met een werkaccount`, geen vragen, en de zin zonder code in plaats van een link. Dat is een gat in de fixture, geen fout van de bouwer.

### S3 Vastlopen: **slaagt**

- Elke missie heeft onder "Wat kan hier fout gaan" minstens drie items voor ChatGPT en twee voor Claude, in de juiste vorm. De skill `missie` verwijst ernaar en schrijft de hapering in de feedbackrij (`missie/SKILL.md:64`, `:90`).
- De oplossingen kloppen met de bronnen. Wat ontbreekt, staat onder Opmerkingen.

### S4 De ladder: **twijfel**

- **Poort:** werkt. Met missie 6 en 7 open komt er geen uitdaging en geen logrij, enkel de open missies.
- **Drie uitdagingen na elkaar op `werkmap-missie7/`:** trede 3, 4 en 5 op niveau 3, 4 en 5. Elke uitdaging noemt een dossier, geen zin of combinatie wordt herhaald, de links zijn `s=t3`, `t4` en `t5`, en er komt telkens één logrij bij. Een nieuwe uitdaging vragen voor de vorige gelukt is, geeft terecht een herinnering.
- **Twijfel over de dubbelregel:**
  - `uitdaging/SKILL.md:47` spreekt over "dossier en **soort** (de **variant** uit `ladder.md`)", maar `ladder.md:5` maakt van soort en variant twee verschillende dingen.
  - De gedeelde regel in `missie-formaat.md:58` verbiedt enkel hetzelfde dossier en dezelfde soort als de **vorige** rij. De skill verbiedt het voor **elke eerdere** rij.
  - Met "soort" gelezen: op niveau 5 is er maar één soort. Met drie dossiers moet de skill dan vanaf trede 8 bij elke trede om een nieuw dossier vragen, terwijl de ladder geen einde heeft.
  - De variant wordt nergens in het log bewaard, dus "variant" is niet te controleren.
- **Kleinere punten:**
  - `:89` *"Volgende trede: niveau <volgend niveau>"* geeft na niveau 5 letterlijk "niveau 6".
  - `:30` (rij aanpassen bij een andere uitdaging) botst met `:59` (een rij toevoegen).

### S5 Verbeteren: **slaagt**

- `docs/updates.md` en de README beschrijven Add a marketplace met `BinaryBjorn/debug-coach`, Upgrade en Refresh in ChatGPT, en Check for updates of Sync automatically in Claude. Ze zeggen allebei dat `mijn-vaardigheden` en de werkmap nooit geraakt worden.
- Geen enkele skill bevat een instructie om `ik/`, `projecten/`, `feedback.md`, `successen.md`, `voortgang.md` of `mijn-vaardigheden` te wissen of te overschrijven. Het overschrijfgat in `start` (zie S1) gaat niet over een update.
- De catalogus `.claude-plugin/marketplace.json` wijst met `./plugin` naar de plugin. `claude plugin validate ./plugin` en `claude plugin validate .` geven allebei "Validation passed".

### S7 Videoscripts: **slaagt**

- Zes `script.json` volgens het schema, met platform chatgpt.
- Elke `opname.md` is een opdracht voor Claude met Computer Use, met alles wat de acceptatie eist: enkel het demo-account en nepdata, het ChatGPT-venster vooraan, `screencapture -v -R` op enkel dat venster, een tijdstip vóór elke klik, `start_video_gemeten` gemeten aan de eerste beeldwissel, `ruw/log.json` in de vorm van het schema, een stap-id per handeling en een controlebeeld per klik.
- `.gitignore` sluit `videos/*/ruw/`, `videos/*/uit/` en `dist/` uit. De echte opname valt buiten de run.

## Harde checks

`python3 "$BOUWRUN_CHECK" check docs/bouwruns/dc-r1-coach` (exit 0):

```
C01    geblokkeerd
C02    klaar
C03    klaar
C04    klaar
C05    klaar
C06    klaar
C07    klaar
C08    klaar
C09    klaar
C10    klaar
C11    klaar
C12    klaar
C13    klaar
=> alles afgehandeld
```

Per feature `python3 tests/feature.py <ID>`:

| Check | Uitslag |
|---|---|
| BASIS | OK (3 tests) |
| C01 | **FAILED** (2 tests, 1 failure: `test_C01_catalogus_en_verhuis`, `tests/test_coach.py:178`, `.claude-plugin/plugin.json` bestaat nog) |
| C02 tot C13 | OK |

- Geen beschermd bestand gewijzigd: `git diff 327374b..HEAD` is leeg voor `tests/`, `bronnen/` en de map van dc-r2.
- **Afwijking in `features.json`:** C06 en C09 staan er nog op `open` / `passes: false`, maar hun checks zijn groen en het checkscript meldt ze als `klaar`. De bouwer heeft ze niet afgevinkt (zie zijn voortgang). Dat is administratief: inhoudelijk slagen ze.
- **C01 is terecht geblokkeerd.** De hook weigert elk schrijfcommando met `.claude` in het pad, en dat geldt ook voor `.claude-plugin/`. De uitweg staat in `roadblocks.md`: buiten de run `git rm .claude-plugin/plugin.json`. Daarna slaagt C01. Al de rest van C01 (`plugin/plugin.json` en `plugin/.claude-plugin/plugin.json` gelijk, de catalogus wijst naar `./plugin`, de oude mappen zijn verhuisd) heb ik nagekeken en klopt.

## Gevonden en door de bouwer gemist

1. **`start` op een werkmap waar alles klaar is, wijst missie 2 aan.** Reproduceren: speel `plugin/skills/start/SKILL.md` na op `tests/fixtures/werkmap-missie7/` en zeg "start". Stap 0 stuurt naar stap 3, en `SKILL.md:211` schrijft *"Volgende missie: je eerste project"* voor, terwijl de werkmap op 7/7 staat. Elke herstart geeft ook opnieuw de link `s=m1`.
2. **`start` vraagt een gevuld profiel opnieuw en schrijft het opnieuw.** Reproduceren: een werkmap met enkel een gevuld `ik/profiel.md` (zoals `werkmap-claude-werk/`), zeg "start". `SKILL.md:18` ziet dat als een nieuwe start, stap 2 stelt de vijf vragen opnieuw, en `:147` en `:163` schrijven het profiel opnieuw. Dat botst met "nooit overschrijven".
3. **`start` schrijft een README die niet klopt in een bestaande projectenmap.** Bestaat `projecten/` al met projecten maar zonder `README.md`, dan komt daar "Nog geen projecten. In missie 2 maak je er een" (`templates/projecten/README.md`). Reproduceren: "start" op `werkmap-missie7/`.
4. **Het profieltemplate noemt Claude, ook voor ChatGPT-gebruikers.** `plugin/skills/start/templates/ik/profiel.md:7` ("Claude leest dit elke keer") en `:36` ("hoe Claude voor jou schrijft"). Het staat ook in `dist/debug-coach-werkmap/ik/profiel.md`, het pakket dat bedoeld is voor ChatGPT.
5. **De dubbelregel van de ladder is dubbelzinnig en strenger dan het gedeelde formaat.** `uitdaging/SKILL.md:47` verwart soort en variant en kijkt naar elke eerdere rij in plaats van de vorige (`missie-formaat.md:58`). Op niveau 5 met drie dossiers moet de skill vanaf trede 8 telkens om een nieuw dossier vragen. Daarnaast geeft `:89` na niveau 5 "niveau 6".
6. **Missie 5 noemt te weinig audioformaten.** `missie-05.md:42` geeft "WAV, MP3, OGG, FLAC, AAC, M4A" als de ondersteunde formaten. C10 noemt ook WebM en MP4 (enkel audio). Een gebruiker met een MP4-opname leest dat zijn bestand niet kan.
7. **Een klare missie opnieuw doen, verlaagt de meter.** Reproduceren: `werkmap-missie7/`, zeg "doe missie 2". Ze gaat op `bezig` (`missie/SKILL.md:36`), de datum 02/10 wordt overschreven, en als de missie niet af raakt, staat de meter op 6/7.

## Opmerkingen voor het pakket (geen fout tegen het contract)

- **missie-06 belooft *"terwijl jij kijkt"* bij Computer Use.** C12, C19 en P3 zeggen dat dat op macOS op de achtergrond loopt en niet zichtbaar is. De bouwer volgde de brief letterlijk; de spanning zit in de bron. Een foutpunt "je ziet niets gebeuren (Mac)" ontbreekt.
- **Nergens staat dat Cowork-taken op Pro en Max sinds 06/10 standaard in de cloud draaien (K1).** Dat is de waarschijnlijkste reden waarom "Cowork je bestanden niet ziet" (missie-01:55, missie-03:59).
- **Niet in de bronnen gevonden:**
  - missie-02:29 ("Claude kent ook projecten"): geen feit gevonden.
  - missie-07 "Plugins > Refresh" om nieuwe skills te laden: C17 kent Refresh enkel voor de cataloguslijst.
- **Beperkingen die de missies niet noemen:**
  - De ingebouwde browser met inloggen (missie 4, ladder niveau 4) is volgens C13 Plus en Pro.
  - De trainingsschakelaar (C9) geldt voor Free, Plus en Pro; voor een werkaccount zegt missie 1 niets.
- **missie-06:** Route Claude maakt het bestand "in de werkmap", Klaar als eist "in de projectmap".
- **"Zeg: mijn coachcode is ..."** (README, `start:136`): geen skill beschrijft wat er dan gebeurt. Een model past de regel waarschijnlijk zelf aan, maar het staat nergens.
- **Fixtures** (beschermd, voor wie het testplan bijwerkt):
  - `werkmap-claude-werk/` mist `voortgang.md`, dus missie 3 op de Claude-werkroute is niet na te spelen.
  - `werkmap-missie7/successen.md` is een tabel. De skills schrijven opsommingsregels.
  - `werkmap-missie7/` mist successen voor treden 1 en 2 en de eigen skill uit missie 7.

## Design-critic

Niet van toepassing: het contract heeft geen scherm ("Designrichting: geen scherm").
