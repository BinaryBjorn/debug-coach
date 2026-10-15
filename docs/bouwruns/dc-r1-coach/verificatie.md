---
type: verificatie
run: dc-r1-coach
ronde: 2
datum: 2026-10-15
---

# Verificatie dc-r1-coach, keurronde 2

**Hoe gekeurd.** Het contract heeft geen scherm en er is geen testserver. Er is dus geen browser gebruikt, er zijn geen screenshots en de design-critic is niet geroepen. Ik heb gekeurd op:

- de code op deze tak: `git diff 327374b..HEAD`, en voor deze ronde vooral `5caf58a..HEAD` (de commits `3bac5b8` en `e04f418`);
- de harde checks;
- het opnieuw naspelen van `start` op de dummywerkmappen uit het testplan.

Net als in ronde 1 is het naspelen een droge run. De keurder mag enkel in de runmap schrijven, dus de schrijfacties zijn uitgerekend en niet echt uitgevoerd.

Sinds ronde 1 zijn enkel `plugin/skills/start/SKILL.md` en `plugin/skills/start/templates/ik/profiel.md` gewijzigd. De oordelen over de andere features komen uit ronde 1, en ik heb nagekeken dat hun bestanden niet veranderd zijn.

## Scenario's

### S1 Installatie + missie 1: **slaagt** (C01 blijft terecht geblokkeerd)

- **Profieltemplate (C02, terug uit ronde 1): hersteld.**
  - `templates/ik/profiel.md:7` zegt nu *"De coach leest dit elke keer"* en `:36` zegt *"hoe de AI voor jou schrijft"*.
  - Het pakket `dist/debug-coach-werkmap/ik/profiel.md` (opnieuw gebouwd om 19:01) heeft dezelfde tekst.
  - De enige productnamen die nog in de templates staan, zijn in `CLAUDE.md` en `AGENTS.md`: regel 1 en de tabel op regel 53. Daar leggen ze uit welke app welk bestand leest, en dat mag volgens A1.
- **`start` op `werkmap-claude-werk/` (enkel een gevuld profiel, geen `voortgang.md`): hersteld.**
  - Stap 0 (`SKILL.md:18-19`) ziet een los profiel nu als een bestaande werkmap.
  - Alleen de ontbrekende bestanden worden geschreven: `CLAUDE.md`, `AGENTS.md`, `voortgang.md`, `feedback.md`, `successen.md` en `projecten/README.md`.
  - Omdat Rol, Dossiers en Account op `gevuld` staan, bespreekt de coach enkel de trainingsschakelaar (`:22`). Er komen geen vragen opnieuw.
  - Het profiel wordt niet herschreven (`:63`, `:148`, `:164`).
  - Daarna staat missie 1 op `klaar`, de meter op 1/7, en komt de zin zonder code (de coachcode staat op `[TODO]`).
  - De afsluiting luidt *"Volgende missie: 2. Je eerste project."*
  - Klopt met "nooit overschrijven".
- **`start` op `werkmap-missie7/` (7/7, ladder op trede 2): hersteld.**
  - Er wordt niets overschreven, de meter staat op 7/7 en de link is `s=m1&k=ab12cd34`.
  - De afsluiting volgt nu `:213`: *"Alle zeven missies zijn klaar. Zeg: geef me een uitdaging, dan begin je aan de ladder."* De fout uit ronde 1 ("Volgende missie: je eerste project") is weg.
- **`start` op `werkmap-vreemd/` en `werkmap-leeg/`:** nog altijd een nieuwe start (geen `voortgang.md` en geen `ik/profiel.md`). Daarna verloopt alles zoals in ronde 1: `lijst.csv` en `notities.txt` blijven staan, en de vijf vragen, de coachcode, de schakelaar, de meter en de link `s=m1` komen er zoals het hoort.
- **C01:** het oude root-manifest `.claude-plugin/plugin.json` (v0.1.0) staat er nog. Zie de harde checks.

### S2 Een missie op echt werk: **slaagt**

- Er is niets veranderd sinds ronde 1. De oordelen over `werkmap-missie7/` (missie 2) blijven staan.
- **Nieuw na te spelen:** missie 3 op `werkmap-claude-werk/`. Dat kan nu wel, maar enkel na "start", want de fixture heeft zelf nog geen `voortgang.md`.
  - `missie/SKILL.md:16` stuurt eerst naar "start".
  - Na de herstelde `start` staat missie 1 op klaar. Dan stelt `missie` missie 3 voor (op "doe missie 3", of als tweede open missie na "sla over").
  - De route is `## Route Claude` plus `### Met een werkaccount` (`missie-03.md:29`, `:37`). Er komen geen vragen, want Platform en Account zijn ingevuld.
  - De afsluiting geeft de zin zonder code in plaats van een link. Klopt.

### S3 Vastlopen: **slaagt**

Niets veranderd. Elke missie heeft minstens drie foutpunten voor ChatGPT en twee voor Claude, en `missie` schrijft de hapering in de feedbackrij.

### S4 De ladder: **slaagt** (met opmerkingen)

Niets veranderd sinds ronde 1. Toen gaf ik twijfel. Bij herlezen hou ik het op slaagt, om twee redenen:

- De acceptatie van C07 zegt letterlijk *"weigert een zin of combinatie dossier+soort die al in het log staat"*. Dat is elke eerdere rij, en dat doet de skill.
- Op niveau 5 zijn er vier varianten. Met drie dossiers zijn er dus twaalf combinaties voor de skill om een nieuw dossier moet vragen. Het tekort dat ik in ronde 1 zag, bestaat enkel als je "soort" leest, en de skill zegt er zelf "(de variant uit `ladder.md`)" bij.

Wat overblijft, gaat als opmerking naar het pakket:

- `uitdaging/SKILL.md:47` gebruikt "soort" en "variant" door elkaar.
- `:89` *"Volgende trede: niveau <volgend niveau>"* kan na niveau 5 "niveau 6" opleveren. Een model met `:32` ernaast leest daar waarschijnlijk 5, maar de tekst zegt het niet.
- `:30` (de zin van een rij aanpassen) botst licht met `:59` (een rij toevoegen).

### S5 Verbeteren: **slaagt**

Niets veranderd. `docs/updates.md` en de README dekken Add a marketplace, Upgrade + Refresh en Check for updates. Geen enkele skill bevat een overschrijf- of wisinstructie voor de werkmap. Het overschrijfgat in `start` uit ronde 1 is nu dicht.

### S7 Videoscripts: **slaagt**

Niets veranderd. Er zijn zes geldige scripts en zes opnameopdrachten voor Claude met Computer Use, en de `.gitignore` klopt.

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
| C01 | **FAILED** (2 tests, 1 failure: `test_C01_catalogus_en_verhuis`, `tests/test_coach.py:178`, AssertionError: True is not false; `.claude-plugin/plugin.json` bestaat nog) |
| C02 | OK (3) |
| C03 | OK (1) |
| C04 | OK (3) |
| C05 tot C08 | OK (1 elk) |
| C09 | OK (2) |
| C10 | OK (2) |
| C11 | OK (2) |
| C12 | OK (1) |
| C13 | OK (1) |

- Er is geen beschermd bestand gewijzigd: `git diff --stat 327374b..HEAD -- tests/ docs/bouwruns/dc-r1-coach/bronnen docs/bouwruns/dc-r2-videopijplijn` is leeg.
- **C01 is nog altijd terecht geblokkeerd.** De hook weigert elk schrijfcommando met `.claude` in het pad, en dat geldt ook voor `.claude-plugin/`. De uitweg ligt buiten de run: `git rm .claude-plugin/plugin.json` en committen (roadblocks.md, V1). De bouwer kan hier binnen de run niets meer aan doen.
- **Nog altijd administratief:** C06 en C09 staan in `features.json` op `open` / `passes: false`, maar hun checks zijn groen en het checkscript meldt ze als `klaar`.

## Gevonden en door de bouwer gemist

Er zijn geen nieuwe fouten gevonden in de herstellingen van deze ronde. Uit ronde 1 staan deze punten nog open. Ze werden niet naar de bouwer teruggestuurd en gaan naar het pakket:

1. **`start` schrijft een README die niet klopt in een bestaande projectenmap.**
   - Reproduceren: zeg "start" op `werkmap-missie7/`. De map `projecten/` heeft drie projecten, maar geen `README.md`.
   - De coach schrijft dan het template met *"Nog geen projecten. In missie 2 maak je er een voor een van je dossiers."* (`templates/projecten/README.md:3`).
2. **Een klare missie opnieuw doen, verlaagt de meter.**
   - Reproduceren: zeg "doe missie 2" op `werkmap-missie7/`. De missie gaat op `bezig` (`missie/SKILL.md:36`).
   - Raakt de missie niet af, dan blijft de meter op 6/7 staan en is de oude datum 02/10 weg (`:70-71`).
3. **Missie 5 noemt te weinig audioformaten.** `missie-05.md:42` noemt WebM en MP4 (enkel audio) niet, terwijl C10 in de platformfeiten ze wel als ondersteund formaat noemt.

## Opmerkingen voor het pakket (geen fout tegen het contract)

- **Nieuw, `start` stap 0.3** (`SKILL.md:22`) op een vooraf gevuld profiel:
  - Missie 1 gaat op `klaar` zonder dat het profiel getoond wordt. "Klaar als" in `missie-01.md:40` vraagt *"Je hebt je profiel gezien in het gesprek"*. Een profiel dat de gebruiker zelf typte, telt redelijkerwijs als gezien, maar het staat er niet.
  - De feedbackrij uit "Missie 1 afsluiten" wordt in dit pad niet vermeld.
  - Bij platform `claude` moet de schakelaar `[TODO: nagaan, trainingsinstelling in Claude]` in de werkwijze zetten (`:144`). Die sectie staat op `gevuld`, en `:22` zegt dat je een gevulde sectie nooit opnieuw schrijft. Er gaat niets verloren, maar de twee regels spreken elkaar licht tegen.
- **`start` geeft bij elke herstart opnieuw de link `s=m1`**, ook op 7/7. Dat kan geen kwaad, want het is dezelfde stap.
- **Ladder (C07):** de tekst over soort en variant (`:47`), "niveau 6" na niveau 5 (`:89`), en aanpassen tegenover toevoegen (`:30` en `:59`). Zie S4.
- **Uit ronde 1, ongewijzigd:**
  - missie-06 *"terwijl jij kijkt"* tegenover C12, C19 en P3 (op macOS loopt het op de achtergrond).
  - K1: Cowork-taken draaien standaard in de cloud. Dat wordt nergens genoemd.
  - Niet in de bronnen gevonden: missie-02:29 en "Plugins > Refresh" in missie-07.
  - Planbeperkingen die de missies niet noemen: de ingebouwde browser, en de trainingsschakelaar bij een werkaccount.
  - missie-06: werkmap tegenover projectmap.
  - Wat er gebeurt bij "zeg: mijn coachcode is ...", staat nergens.
  - Fixtures: `werkmap-claude-werk/` mist `voortgang.md`, `successen.md` in de fixture is een tabel, en treden 1-2 en de eigen skill ontbreken.

## Design-critic

Niet van toepassing: het contract heeft geen scherm ("Designrichting: geen scherm").
