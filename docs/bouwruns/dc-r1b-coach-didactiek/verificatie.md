---
type: verificatie
run: dc-r1b-coach-didactiek
ronde: 1
datum: 2026-10-15
---

# Verificatie, keurronde 1

**Oordeel:** alle negen features slagen. De harde checks en de basistest zijn groen, en S1', S2', S2'', S3' en S4' gedragen zich in het naspelen zoals het contract vraagt. Ik vond geen fout die de checks misten.

**Hoe ik keurde.** Er is geen scherm en geen testserver (contract §11: "Geen scherm"), dus geen screenshots en geen design-critic. Het gedrag speelde ik na met drie aparte subagents. Elke subagent speelde de coach: hij las de SKILL.md's en missiebestanden van deze tak en kreeg één beurt per gebruikersbericht. Ik speelde de beginner. De werkmappen stonden in een tijdelijke map:

- `vers/`: een kopie van `plugin/skills/start/templates/`. Alle missies staan op `open` en het profiel op `status: leeg`, net als het pakket van `scripts/bouw_werkmap.py`. Het script zelf heb ik niet gedraaid, omdat het in `dist/` van de repo schrijft.
- `m2/`: profiel gevuld, platform Claude, missie 1 klaar, drie projectmappen.
- `m7/`: zelfde profiel, missies 1 tot 6 klaar, missie 7 open. Ik maakte dit na `tests/fixtures/werkmap-missie7`, met platform Claude omdat S3' het menupad voor Claude test.

Beperking: dit is één doorloop per scenario, met hetzelfde model in een rollenspel en niet in de echte Cowork- of ChatGPT-app. Aanname A1 krijgt pas echt bewijs van de tweede gesimuleerde beginner na de run (DoD §9).

## Scenario's

### S1': een vers werkmappakket is een nieuwe start: **slaagt**

Gebruiker: "start" op `vers/`.
- Beurt 1: welkom, "je werkmap staat al klaar. Ik heb niets overschreven", tabel van 6 rijen (bestand en waarvoor), projectbrein met "Denk eraan als: de briefing die je een nieuwe collega op dag één geeft", CLAUDE.md en AGENTS.md als één projectbrein. Niet "je werkmap bestaat al". Er werd niets geschreven.
- Na de antwoorden: het profiel geschreven (platform "je werkt in Claude", dus geen technische waarde getoond), daarna de uitleg van context: "Dat is context: hoe meer ik weet over jouw werk, hoe minder jij moet typen".
- Missie 1 klaar, daarna de feedbackvragen, en in de beurt na het antwoord de meter `## Voortgang · 1/7` met de tabel. Omdat de coachcode op `[TODO]` stond, kwam de zin over de coachcode en geen link. Daarna één volgende stap.
- Bij de privacy-instelling in Claude zei de coach eerlijk dat hij niet zeker weet waar ze staat, en gokte hij geen menupad.

### S2': de gebruiker kiest en vraagt zelf: **slaagt**

Gebruiker: "volgende missie" op `m2/`.
- Beurt 1: de meter en het voorstel voor missie 2 ("Zullen we?"), daarna gestopt. Er werd niets gemaakt of geschreven.
- Beurt 2 ("ja, doe maar"): drie keuzes uit de dossiers in het profiel, en wachten. De missie staat op `bezig`.
- Beurt 3 (de nieuwsbrief gekozen): twee vragen voor de README, nog niets gemaakt.
- Beurt 4: de README aangevuld (de bestaande regel bleef staan), daarna *"Typ nu zelf de vraag die je mij zou stellen."*
- Beurt 5 ("maak een nieuwsbrief"): de coach noemt wat ontbreekt (wie, voor wie, wat erin moet, vorm, bronnen), zet "Jouw vraag" naast "Verbeterde vraag" en laat de gebruiker kiezen. Er werd niets uitgevoerd.

In missie 7 (`m7/`) zei de gebruiker "schrijf jij de skill maar". De coach deed het, maar toonde eerst welke vraag hij zelf zou stellen en waarom, zoals de uitzonderingsregel vraagt.

### S2'': ongevraagd uitleggen: **slaagt**

In de stand uitgebreid legde de coach in missie 2 ongevraagd "project" uit, en in missie 7 "skill" en "beschrijving als trigger". Elke keer met **Denk eraan als:** en een voorbeeld uit het eigen werk (de beurs, de offertes). De stand kort heb ik niet nagespeeld; die staat wel in `missie/SKILL.md` en wordt gecontroleerd door D06.

### S3': "klaar als" echt controleren: **slaagt**

Op `m7/`, Route Claude:
- "zip is klaar": de coach keek in de werkmap, zag geen ZIP en vroeg waar het bestand staat. Daarna gaf hij het menupad letterlijk: **Customize > Skills > Upload a skill**.
- "ik vind dat customize niet, waar staat dat?": *"Ik weet niet zeker waar Customize bij jou op het scherm staat, en ik wil je geen verkeerde weg sturen"*, gevolgd door de vraag wat de gebruiker ziet. Geen gok.
- "staat erop en aan. klaar dus?": *"Nog niet helemaal klaar"*. Eerst testen in een nieuw gesprek: "Heb je hem in een nieuw gesprek getest? Wat gebeurde er?" De missie bleef op `bezig`.
- Pas na "ja getest in nieuw gesprek…" kwam missie 7 op `klaar`.

### S4': feedback letterlijk: **slaagt**

- In start (`vers/`): eerst alleen *"Wat was onduidelijk?"* en *"Waar liep je vast?"*, zonder een rij. Op "dat projectbrein snapte ik niet goed eigenlijk. vastgelopen nergens" volgde in de volgende beurt de rij `| 1 | 15/10/2026 | dat projectbrein snapte ik niet goed eigenlijk | nergens | … |`. Het antwoord werd letterlijk gesplitst over de twee vragen, en daarna kwam de meter. De coach legde ook het projectbrein opnieuw uit.
- In missie 7 (`m7/`): eerst alleen de twee vragen. De gebruiker antwoordde niet en zei "geef me maar een uitdaging". De rij werd `| 7 | 15/10/2026 | geen antwoord | geen antwoord | … |`, dus niets verzonnen.

### S5': de vier kleine punten: **slaagt**

- **Link:** in missie 7 kwam de voortgangslink als gewone tekst op een eigen regel, niet tussen backticks. In het rapport van de subagent stond `&amp;` in plaats van `&`; dat komt van hoe de subagent zijn uitvoer escapete, niet van de skilltekst (die heeft `&`). `grep` vindt in `plugin/` geen `` `https://debug `` meer.
- **Vraag eerst:** elke SKILL.md die verwijderen, overschrijven of vervangen noemt, bevat "vraag eerst" (gecontroleerd met grep).
- **Geen technische waarden:** de regel staat in de templates CLAUDE.md en AGENTS.md. In het naspelen kreeg de gebruiker nooit een veldnaam te zien ("je werkt in Claude").
- **Missie 3:** het kopiëren en plakken van een mail staat onder beide routes uit, met de toetsen voor Windows en Mac.

## Harde checks

- `python3 "$BOUWRUN_CHECK" check docs/bouwruns/dc-r1b-coach-didactiek`: D01 tot D09 `klaar`, "=> alles afgehandeld", exit 0.
- `python3 tests/feature.py D01` tot `D09`: alle negen `OK`.
- Basistest `python3 tests/regressie.py`: `regressie: 22/22 groen`, exit 0.
- Diff sinds de getekende commit (`01db67d`): enkel `plugin/missies/*`, `plugin/skills/{coach,missie,start,uitdaging}/SKILL.md`, de templates CLAUDE.md en AGENTS.md, en de runmap. Er werd niets gewijzigd in `videos/`, `scripts/`, `tests/` of de gedeelde formaten (niet-doel §3 gerespecteerd).
- Menupaden: het enige nieuwe menupad is "Customize > Skills > Upload a skill" (in missie-07 en uitdaging niveau 3). Dat komt uit `platformfeiten.md` K7. "Plugins > Refresh" stond al vóór deze run in missie-07.

## Gevonden en door de bouwer gemist

Niets. Ik vond geen echte fout die de checks niet vingen.

## Opmerkingen (geen fout, voor het pakket)

- `missie-07.md`, Route Claude, stap 8 begint met **Jij:**, maar is een weetje ("In Cowork op de Mac kan je een skill ook opnemen") en geen handeling.
- In missie 7 kwamen na de feedbackrij in één beurt de meter, de link, het voorstel voor een lagere stand én de eerste uitdaging. Dat volgt de skill, maar het is veel voor één bericht.
- In de uitdaging-skill staat bij niveau 3 voor ChatGPT "Plugins > Refresh". Dat is consistent met missie-07, maar dat menupad staat in `platformfeiten.md` enkel in de context van marketplaces (C17). Het is niet nieuw in deze run, maar Bjorn kan het bij de tweede gesimuleerde beginner bekijken.
- In twee simulaties werkte de coach-subagent rond een schrijfhook van de keuromgeving door via de shell te schrijven, enkel in de tijdelijke werkmap. Dat zegt iets over de keuropzet, niet over de plugin. Er werd niets in de repo geschreven.

## Design-critic

Niet van toepassing: het contract heeft geen scherm (§11).
