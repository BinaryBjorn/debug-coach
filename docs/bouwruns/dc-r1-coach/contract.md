---
type: bouwcontract
status: getekend
date: 2026-10-15
getekend: 2026-10-15 (Bjorn, chat: "teken, maar start meteen zonder de queue")
project: Debug-Marketing
tags: [bouwrun, contract, debug-coach]
---

> [!important] Run 1 van 3 in blok 1 van [Debug Coach](../../plans/spec-debug-coach-blok-1.md)
> Erft de doelkaart, de scenario's en de beslissingen B1 tot B13 van de bloknota. Bouwt in de repo `debug-coach`. Python 3.9 (mini), geen pakketten installeren.

## Contractkaart

> [!question] Teken of stuur bij
> **Wat er gebouwd wordt:** de coach als één plugin (map `plugin/`) die in ChatGPT (Work, desktop) en in Claude (Cowork) draait: skills `start`, `missie`, `uitdaging`, `uitleg`, `coach`, zeven missies met een ChatGPT- en een Claude-route, de werkmap-templates, een script dat het werkmappakket bouwt, de voortgangslink, feedback en successen, plus zes videoscripts met hun opnameopdracht.
> **Outputtype:** feature (een plugin met skills en een bouwscript).
> **Scenario's:** S1, S2, S3, S4, S5, S7 (scriptdeel) van de bloknota.
> **Niet in deze run:** de site (R3), de afwerkingspijplijn (R2), echte opnames, externe diensten.
> **Aannames met de meeste impact:** A1 dezelfde skilltekst werkt in beide apps (P1 bewezen op Plus); A2 updates via de GitHub-catalogus (P2b bewezen); A3 missie 4 via de ingebouwde browser (P4 bewezen); A6 Work leest `AGENTS.md` (P1 bewezen).
> **Designrichting:** geen scherm.
> **Keten:** run 1 van 3, vanaf `main`, wacht op niets.
> **Budget:** 5 uur, 16 sessies.
> **Enkel jij kunt beantwoorden:** niets.

## 1. Doel

Zie de [bloknota](../../plans/spec-debug-coach-blok-1.md). Deze run levert alles wat de gebruiker in de AI-app zelf ziet en doet.

## 2. Scenario's

- **S1** Installatie + missie 1: de gebruiker opent het **werkmappakket** (gemaakt door `scripts/bouw_werkmap.py`) in ChatGPT Work of Cowork, installeert de coach via **Add a marketplace** met `BinaryBjorn/debug-coach` (in beide apps, bewezen in P2b voor ChatGPT), in ChatGPT ook de lege plugin `mijn-vaardigheden` uit de werkmap, en zegt "start". `start` vult ontbrekende werkmapbestanden aan (nooit overschrijven), doet missie 1 in de chat (het formulier enkel als extra in Cowork), vraagt de **coachcode** van de startplanpagina en zet die in het profiel, bespreekt de trainingsschakelaar (ChatGPT, feit C9), geeft de voortgangslink en toont de meter.
- **S2** Een missie op echt werk: `missie` toont de meter, stelt de volgende open missie voor (overslaan mag), kiest de route uit `Platform` en `Account` in het profiel en vraagt enkel als die `[TODO]` zijn, begeleidt in de gekozen coachstand, controleert "Klaar als", schrijft één rij in `successen.md` en één in `feedback.md`, stelt één keer een lagere stand voor, geeft de voortgangslink.
- **S3** Vastlopen: elke missie heeft "Wat kan hier fout gaan" per platform; de coach schrijft de hapering in de feedbackrij.
- **S4** De ladder: `uitdaging` werkt pas na missie 7 (anders verwijst ze naar de open missies), kiest het volgende niveau volgens `ladder.md` en het ladder-log, bouwt op `successen.md` en de dossiers, geeft nooit een uitdaging die al in het log staat, schrijft een rij in het log en geeft de voortgangslink `t<trede>`.
- **S5** Verbeteren: een nieuwe versie komt via de catalogus op GitHub (ChatGPT: Upgrade, Claude: Check for updates) en vervangt enkel de coach; de werkmap (`ik/`, `projecten/`, `feedback.md`, `successen.md`, `voortgang.md`) en `mijn-vaardigheden` staan los ervan en worden nooit geraakt.
- **S7** Videoscripts: zes scripts volgens `script.schema.json`, met per script een `opname.md`: een opdracht voor **Claude met Computer Use** die op de mini de ChatGPT-app bedient en enkel dat venster opneemt (bewezen in P5).

## 3. Niet-doelen

- Geen site, geen database, geen mail (R3). Geen videobewerking (R2), geen echte opname.
- Geen MCP-server of koppeling naar buiten; de plugin is enkel skills.
- Geen slash-commando's in tekst voor de gebruiker ("zeg: volgende missie").
- `skills/start/` van fase 1 wordt herschreven, niet weggegooid: inventaris, nooit overschrijven, statussen leeg/ontwerp/gevuld en "verzin niets" blijven.
- De bouwer repareert niets buiten zijn features.

## 4. Aannames

| # | Aanname | Soort | Bron | Zekerheid | Impact | Hoe getest | Omkeerbaar |
|---|---|---|---|---|---|---|---|
| A1 | Eén skilltekst werkt in ChatGPT Work en in Claude als productnamen enkel in route-blokken en uitleg aan de gebruiker staan | technisch | proef 15/10 (Pro, Work en Claude Code) | hoog | hoog | P1 op Plus; gesimuleerde beginner na de keten; keurder leest | ja |
| A2 | Updates via de GitHub-catalogus: ChatGPT aanvaardt `BinaryBjorn/debug-coach` in het Claude-formaat (P2b); na de verhuis naar `plugin/` moet dat blijven werken | technisch | P2b 15/10 | hoog | hoog | na de keten: de catalogus opnieuw toevoegen op het demo-account en installeren | ja |
| A3 | Missie 4 via de ingebouwde browser op Outlook.com (C18, bewezen in P4); terugvalroute "mails bewaren of plakken" blijft in de missie | technisch | P4 15/10 | hoog | hoog | P4 | ja |
| A4 | Audio-upload werkt op Plus (C10) | technisch | release notes 06/10 | hoog | middel | testopname op het demo-account | ja |
| A5 | De voortgangslink volgt `tests/fixtures/gedeeld/voortgangslink.json` (sha256 `74baa8de…b2`), dezelfde als in R3 | technisch | ontwerp 15/10 | hoog | hoog | C09 hier, T06 in R3, hashtest in beide | ja |
| A6 | Work leest `AGENTS.md` in de werkmap (C16, bewezen in P1 op Plus) | technisch | P1 15/10 | hoog | hoog | P1 | ja |

### Inputkaart

| Gegeven | Bron | Hoe de run eraan komt | Echt voorbeeld gezien | Wie levert | Hoe vaak |
|---|---|---|---|---|---|
| Huidige plugin | `debug-coach` main | de kloon | ja | repo | eenmalig |
| Coachstijl | `ProjectCoach-Final` | `bronnen/projectcoach/` (coaching-style + vier beginnerbestanden) | ja | Claude (klaar) | eenmalig |
| Leervragen | mails 07/10 | `bronnen/leervragen.md` (zonder naam of adres) | ja | Claude (klaar) | eenmalig |
| Platformfeiten | onderzoek 15/10 | `bronnen/platformfeiten.md` (bron per feit, marketplace-vorm letterlijk) | ja | Claude (klaar, C16-C18 na P1/P2/P4) | eenmalig |
| Inhoud per missie | grill 07/10 en 15/10 | `bronnen/missies-brief.md` | ja | Claude (klaar) | eenmalig |
| Gedeelde formaten | grill 15/10 | `tests/fixtures/gedeeld/` (voortgangslink, missie-formaat met profiel- en ladderregels, script- en logschema) | ja | Claude (klaar) | eenmalig |
| Uitkomst P1 tot P5 | demo-account | `bronnen/proeven.md` (drie rondes) | ja | Bjorn + Claude | eenmalig |

## 5. Outputtype

**Feature:** een plugin met skills en een bouwscript. De keurder speelt elke skill na in de dummywerkmappen (Claude-route) en leest de ChatGPT-route tegen `bronnen/platformfeiten.md`. De ChatGPT-route zelf is in de run niet uit te proberen: dat doet de gesimuleerde beginner niet, P1 wel, en dat staat zo in het pakket.

## 6. Technische vorm

| Onderdeel | Vorm | Waarom (in effect) | Afgewezen |
|---|---|---|---|
| Repo-indeling | De plugin in `plugin/` (met `plugin.json` en `.claude-plugin/plugin.json`); `.claude-plugin/marketplace.json` in de root met `source: "./plugin"`; `docs/`, `tests/`, `scripts/` buiten de plugin | Bouwdocumenten en tests gaan nooit mee naar de gebruiker | Plugin in de root: alles gaat mee, ook de runmap |
| Skills | `plugin/skills/{start,missie,uitdaging,uitleg,coach}/SKILL.md` | Dezelfde coach in beide apps | Twee plugins |
| Missies | `plugin/missies/missie-0N.md` volgens `tests/fixtures/gedeeld/missie-formaat.md` | De site (R3) leest dezelfde bron | Missies in de skilltekst |
| Taal van de skills | Skilltekst voor het model in het Nederlands (de huidige `start` is Engels en wordt herschreven); woorden die de tests zoeken: "ontbreekt", "inventaris", "meter", "overslaan" | Eén taal in de plugin, zelfde als de gebruiker | Engels voor het model: de tests en de keurder lezen Nederlands |
| Werkmap | Templates in `plugin/skills/start/templates/` (CLAUDE.md, AGENTS.md, ik/profiel.md, voortgang.md met `## Ladder`, feedback.md, successen.md, projecten/README.md) | Beide apps lezen hun eigen projectbrein | Enkel CLAUDE.md |
| Werkmappakket | `scripts/bouw_werkmap.py` maakt `dist/debug-coach-werkmap/` (de templates, een lege lokale plugin `.coach/mijn-vaardigheden/`, `.agents/plugins/marketplace.json` die daarnaar wijst) en `dist/debug-coach-werkmap.zip`; de coach zelf komt via GitHub | De coach krijgt updates via de catalogus; eigen vaardigheden (missie 7) staan apart en een update raakt ze nooit | De coach als kopie in de werkmap: updaten zou betekenen dat de gebruiker mappen vervangt |
| Voortgang | Link per stap, coachcode uit het profiel, vorm uit de gedeelde fixture. In skilltekst staat de link altijd als `https://debug.marketing/coach/v?s=<stap>&k=<coachcode>`, of met `m<N>` of `t<trede>` als stap; geen andere plaatshouders (de test vult enkel deze in) | Werkt zonder koppeling | MCP-koppeling |
| Ladder | `plugin/skills/uitdaging/ladder.md` met vijf niveaus uit de brief | Persoonlijk, zonder einde | Vaste lijst |
| Videoscripts | `videos/<slug>/script.json` + `opname.md` (opdracht voor Claude Computer Use op de mini: ChatGPT-venster vooraan, `screencapture -v -R` op enkel dat venster, tijdstip vóór elke klik, `start_video_gemeten` meten); ruw in `videos/<slug>/ruw/`, uitvoer in `uit/`, beide in `.gitignore` | ChatGPT mag zijn eigen app niet bedienen (C19); Claude wel, met exacte klikposities (P5) | ChatGPT Computer Use: geblokkeerd door OpenAI |
| Checks | `python3 tests/feature.py <ID>`: draait de tests met dat ID in de naam en faalt als er nul liepen | Een lege testverzameling kan nooit groen geven | `unittest -k` rechtstreeks: geeft exit 0 bij nul tests (nagekeken 15/10) |

## 7. Features

Zie `features.json` (ID's C01 tot C13). Tests in `tests/` (beschermd), geschreven vóór het tekenen, falen nu.

## 8. Testplan en dummydata

Zie `testplan.md`.

## 9. Definition of done

- Elke feature klaar volgens het checkscript, of geblokkeerd met reden.
- Basistest groen (regressie: lekcheck, geldige JSON, hash van de gedeelde fixtures), geen beschermd bestand gewijzigd.
- Keurder: elke skill nagespeeld in de dummywerkmappen; elke missie gelezen als beginner (Nederlands, je-vorm, geen em dash, geen slash-commando, productnamen enkel in route en uitleg).
- Na de keten: de gesimuleerde beginner (buiten de run) doorloopt missie 1 tot 7 en drie treden; verslagen in het blokpakket.

## 10. Budget

5 uur, 16 sessies, 2 features per sessie, bouwer en keurder `opus`. In `run.json`.

## 11. Designrichting

Geen scherm.

## 12. Keten

- **Blok:** [Debug Coach blok 1](../../plans/spec-debug-coach-blok-1.md). **Plaats:** run 1 van 3. **Wacht op:** niets. **Bouwt op:** `main` van `debug-coach`. **Start:** nu als de poort het toelaat, anders de wachtrij. **Pakket:** na R3 één blokpakket.
- **Eindigt R1 met geblokkeerde features:** R2 start toch (op de tak van R1) en raakt ze niet aan; ze komen in het blokpakket.
