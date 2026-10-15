---
type: validatie
status: wacht-op-bjorn
date: 2026-10-15
tags: [bouwrun, validatie]
---

> [!tip] In één zin
> Bijna alles staat er: 12 van de 13 onderdelen zijn gebouwd en gekeurd, maar onderdeel C01 (het opruimen van het oude pluginbestand in de root) is niet gehaald, want de run mocht dat bestand niet wissen. De run stopte daarom na 2 keurrondes. Eén commando van jou op de tak `bouwrun/dc-r1-coach` lost het op.

## 1. Wat er gebouwd is
Er is geen scherm in deze run, dus er zijn geen screenshots. Dit kun je nu:
- **S1, installeren en missie 1:** een werkmappakket bouwen (`scripts/bouw_werkmap.py`), de coach installeren via `BinaryBjorn/debug-coach` in ChatGPT en Claude, en "start" zeggen. `start` vult alleen aan wat ontbreekt, vraagt de coachcode, bespreekt de trainingsschakelaar en toont de meter. Bestaande bestanden worden niet overschreven.
- **S2, een missie op echt werk:** `missie` stelt de volgende open missie voor (overslaan mag), kiest de route per app, schrijft één rij in successen en één in feedback, en geeft de voortgangslink. De zeven missies staan er.
- **S3, vastlopen:** elke missie noemt minstens drie foutpunten voor ChatGPT en twee voor Claude.
- **S4, de ladder:** `uitdaging` werkt pas na missie 7, kiest het volgende niveau (na niveau 5 blijft het 5) en geeft nooit twee keer dezelfde uitdaging.
- **S5, verbeteren:** `docs/updates.md` en de README leggen uit hoe een update de coach vervangt en je werkmap en `mijn-vaardigheden` met rust laat.
- **S7, videoscripts:** zes scripts, elk met een opnameopdracht voor Claude met Computer Use. Er is nog niets opgenomen.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 2. Wat de keurder vond
Na 2 rondes slaagt elk scenario (S1, S2, S3, S4, S5, S7), met C01 als uitzondering. De keurder speelde `start` en `missie` droog na op de dummywerkmappen (hij mocht niet echt schrijven) en liet de checks draaien: alles groen behalve C01.

Wat de keurder vond dat de bouwer miste, en wat in ronde 1 al hersteld is (C02 en C03):
- Het profielsjabloon noemde een app bij naam; nu staat er "de coach" en "de AI" (hersteld).
- `start` kon een bestaande werkmap met alleen een profiel overschrijven of opnieuw uitvragen, en noemde bij 7 van 7 missies nog "je eerste project" als volgende stap (hersteld).

Drie fouten uit ronde 1 zijn niet hersteld, zie blok 6. Kleine opmerkingen zonder fout tegen het contract: in `uitdaging` staan "soort" en "variant" door elkaar, en de tekst kan na niveau 5 "niveau 6" suggereren. Missie 6 zegt "terwijl jij kijkt", maar op macOS loopt dat op de achtergrond. Cowork-taken draaien standaard in de cloud en dat staat nergens.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 3. Keuzes die Barri in jouw plaats maakte
20 keuzes, allemaal omkeerbaar (`beslissingen.md`). Wat je merkt:
- De plugin heet versie 0.2.0 en de beschrijving noemt geen app en geen slash-commando (1).
- Alle teksten gelden voor beide apps. `AGENTS.md` is `CLAUDE.md` met een andere eerste regel (3, 15).
- Je beantwoordt de vijf startvragen in de chat. In Cowork wordt het formulier alleen als extra aangeboden (5).
- Waar niet bekend is hoe Claude de trainingsinstelling toont, zegt de coach dat eerlijk en zet hij een `[TODO]` in het profiel (6).
- De uitlegvorm (één zin, "Denk eraan als", maximaal 150 woorden) geldt in elke stand, en de waarschuwing vóór versturen, verwijderen of overschrijven blijft ook bij "uit" (14, 15).
- Een ladderuitdaging staat in het log als "niet klaar" zodra ze gegeven is. Een open uitdaging blokkeert een nieuwe (13).
- De lege `mijn-vaardigheden`-map krijgt een korte uitleg in je-vorm (16).
- In de videoscripts figureren Sam Peeters en het bedrijf Noorderlicht als verzonnen demopersonen. Stappen buiten ChatGPT worden gesproken over een stilstaand beeld (17, 18).
- `start` behandelt een werkmap met alleen een profiel als bestaande werkmap (20).

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 4. Vragen met de standaard die toegepast werd
Eén vraag (`vragen.md`, V1): mag de beveiligingsregel van de run `.claude-plugin/` doorlaten en alleen `.claude/` beschermen? Toegepast: C01 blijft geblokkeerd en de regel is niet omzeild. Bij "ja" is het één commando.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 5. Aannames die nog niet live getoetst zijn
`aannames.md` is leeg: de bouwer voegde geen nieuwe toe. Uit het contract:
- **A1** (één tekst in beide apps) is bewezen in P1 op Plus. De gesimuleerde beginner na de keten (missie 1 tot 7 en drie treden) is nog niet gedaan. De ChatGPT-route is binnen de run niet uit te proberen, de keurder las ze tegen `bronnen/platformfeiten.md`.
- **A2** (updates via de catalogus) is bewezen vóór de verhuis naar `plugin/`. Na de verhuis, en met het oude root-bestand er nog bij, is het niet opnieuw getest.
- **A4** (audio-upload op Plus): nog geen testopname.
- **A5** (voortgangslink): hier groen, de test in R3 volgt.
- **A3** en **A6** zijn bewezen in P4 en P1.

## 6. Niet gehaald
- **C01, repo-indeling en twee manifesten:** 1 van 2 tests groen. De test `test_C01_catalogus_en_verhuis` faalt omdat het oude `.claude-plugin/plugin.json` (v0.1.0) nog in de root staat. De run-beveiliging weigert elk schrijf- of wiscommando met `.claude` in het pad, ook `.claude-plugin`. De bouwer heeft dat niet omzeild. De rest van C01 klopt (nieuwe manifesten in `plugin/`, catalogus met `source: ./plugin`). **Uitweg:** `git rm .claude-plugin/plugin.json` op de tak `bouwrun/dc-r1-coach`, committen, dan `python3 tests/feature.py C01`.
- **Drie fouten die de keurder vond en die niet hersteld zijn:**
  1. `start` schrijft de tekst "Nog geen projecten" in een bestaande `projecten/`-map zonder README.
  2. Een klare missie opnieuw doen zet ze op "bezig" en wist de datum, waardoor de meter kan zakken.
  3. Missie 5 noemt WebM en MP4 (alleen audio) niet als ondersteund formaat.
- **Administratief:** in `features.json` staan C06 en C09 nog op "open", terwijl hun checks groen zijn en het checkscript ze "klaar" meldt.
- **Buiten deze run, nog te doen:** de gesimuleerde beginner, de echte videoopnames en de test dat Work `mijn-vaardigheden` oppikt.

## 7. De run in cijfers
- **Duur:** 0,54 uur (wandklok), tegenover 5 uur budget.
- **Sessies:** 8 van de 16 bouwsessies, 2 keurrondes, 1 brandtest.
- **Verbruik (schatting in API-dollars, geen factuur):** $13,65 in totaal: bouwer $8,06, keurder $5,42, brandtest $0,17.
- **Berichten aan jou tijdens de run:** 0.
- **Weigeringen door de beveiliging:** 36 (6 bouwer, 30 keurder). De keurder deed er 26 in minder dan een minuut, telkens een schrijfpoging buiten de runmap.
