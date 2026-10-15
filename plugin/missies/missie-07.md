---
missie: 7
titel: Je eigen vaardigheid
video: missie-7
---

## Doel

Een vaste werkwijze die de AI onthoudt en die je zelf terugvindt. Wat je vaak vraagt, hoef je daarna niet meer uit te leggen.

## Resultaat

Je eigen skill `eigen-<naam>` (bv. `eigen-weekverslag`: een weekverslag in jouw stijl), die werkt in een nieuw gesprek.

Een update van de coach raakt je eigen skills nooit: de coach komt via GitHub, je eigen vaardigheden staan apart.

## Route ChatGPT

1. **Jij:** Zeg: volgende missie. Kies iets wat je elke week opnieuw vraagt.
2. **De coach:** toont je wat er in een skill moet: wanneer de skill gebruikt wordt, wat ze doet, in welke vorm.
3. **Jij:** Schrijf de skill samen met de coach in de lokale plugin `mijn-vaardigheden` uit je werkmap: `.coach/mijn-vaardigheden/skills/eigen-<naam>/SKILL.md`.
4. **Jij:** Herstart de app, of kies **Plugins > Refresh**.
5. **Jij:** Test in een nieuw gesprek: met `@mijn-vaardigheden`, of door het gewoon te vragen. Zeg de coach daarna wat er gebeurde.
6. **De coach:** zet je skill in `successen.md`.

## Route Claude

1. **Jij:** Zeg: volgende missie. Kies iets wat je elke week opnieuw vraagt.
2. **De coach:** legt uit dat de coach in Claude uit GitHub komt, niet uit je werkmap. Een skill in de map `.coach/` laadt daar dus niet.
3. **Jij:** Schrijf de skill samen met de coach in `projecten/eigen-skills/eigen-<naam>/SKILL.md`.
4. **Jij:** Verpak de map `eigen-<naam>` als ZIP. De mapnaam is de naam van de skill.
5. **Jij:** Upload de ZIP in **Customize > Skills > Upload a skill** en zet de skill aan.
6. **Jij:** Test in een nieuw gesprek: vraag iets waarvoor de skill bedoeld is. Zeg de coach daarna dat je uploadde en testte, en wat er gebeurde.
7. **De coach:** zet je skill in `successen.md`.
8. **Jij:** In Cowork op de Mac kan je een skill ook opnemen (op Pro, Max en Team).

## Klaar als

- Je skill `eigen-<naam>` bestaat.
- Ze werkt in een nieuw gesprek.
- Ze staat in `successen.md`.

## Wat kan hier fout gaan

### ChatGPT

- **Je skill verschijnt niet:** herstart de app of kies Plugins > Refresh. Kijk of het bestand echt `SKILL.md` heet, in de map `eigen-<naam>`.
- **De plugin mijn-vaardigheden staat er niet:** installeer ze onder Plugins, tabblad Personal. Ze komt uit je werkmappakket.
- **De skill doet niet wat je wil:** maak de beschrijving bovenaan concreter (wanneer gebruik je ze, wat moet eruit komen) en test opnieuw.
- **Je bent bang dat een update je skill wist:** dat gebeurt niet. De coach en je eigen vaardigheden staan los van elkaar.

### Claude

- **De upload wordt geweigerd:** de ZIP moet de map `eigen-<naam>` bevatten, met `SKILL.md` erin.
- **De skill werkt niet in een nieuw gesprek:** kijk in Customize > Skills of ze aan staat.
- **Je zette de skill in `.coach/`:** in Claude laadt die map niet. Zet ze in `projecten/eigen-skills/` en upload ze als ZIP.

## Begrippen

- **Skill (vaardigheid):** een vaste werkwijze die de AI leest wanneer ze nodig is. Denk eraan als: een draaiboek voor een terugkerende campagne.
- **Herbruikbaar:** één keer goed gemaakt, telkens opnieuw te gebruiken. Denk eraan als: een e-mailtemplate in je marketingtool.
- **Beschrijving die zegt wanneer:** de zin bovenaan de skill die de AI vertelt wanneer ze de skill moet gebruiken. Denk eraan als: de trigger van een automatisering in je mailtool.
