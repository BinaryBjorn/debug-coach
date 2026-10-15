# Missie-formaat (gedeeld, byte-gelijk in debug-coach en website-debug-marketing)

Elk missiebestand heet `missie-0N.md` (N = 1 tot 7) en volgt exact deze grammatica. De coach leest het, de site ontleedt het.

## Frontmatter (verplicht, in deze volgorde)

```
---
missie: <1-7>
titel: <tekst>
video: <slug uit videos/ of geen>
---
```

`video` is een slug (`welkom`, `klaarzetten`, `missie-3`, `missie-5`, `missie-7`, `coach-uitzetten`) of het woord `geen`. De URL staat nooit in de missie: de site koppelt slug aan URL in `src/lib/coach/config.js`.

## Koppen (verplicht, exact, in deze volgorde, niveau 2)

1. `## Doel`
2. `## Resultaat`
3. `## Route ChatGPT`
4. `## Route Claude`
5. `## Klaar als`
6. `## Wat kan hier fout gaan`
7. `## Begrippen`

Onder `## Route ChatGPT` en `## Route Claude`: een genummerde lijst van stappen. Optioneel daaronder een subkop `### Met een werkaccount` met extra stappen.

Onder `## Wat kan hier fout gaan`: exact twee subkoppen `### ChatGPT` en `### Claude`, elk een lijst van items in de vorm `- **<probleem>:** <oplossing>`. Minstens drie items onder ChatGPT, minstens twee onder Claude.

Onder `## Klaar als`: een lijst; elk item is controleerbaar in de werkmap of in het gesprek.

Onder `## Begrippen`: items `- **<begrip>:** <één zin>. Denk eraan als: <vergelijking>.`

## Taal

Nederlands (Vlaams mag), je-vorm, geen em dash (—), geen slash-commando's ("zeg: volgende missie" in plaats van "typ /missie").

# Profielregels (in `ik/profiel.md`, sectie `## Werkwijze`)

```
- **Platform:** chatgpt | claude | [TODO]
- **Account:** werk | persoonlijk | [TODO]   (een korte noot tussen haakjes erna mag)
- **Coachcode:** <8 tekens [a-z0-9]> | [TODO]
- **Tools:** <tekst> | [TODO]
```

Regex per regel: `^- \*\*Platform:\*\* (chatgpt|claude|\[TODO\])$`, `^- \*\*Account:\*\* (werk|persoonlijk|\[TODO\])( \(.+\))?$`, `^- \*\*Coachcode:\*\* ([a-z0-9]{8}|\[TODO\])$`.

# Ladder-log (in `voortgang.md`, onder de kop `## Ladder`)

```
| Trede | Niveau | Datum | Uitdaging | Klaar |
|---|---|---|---|---|
| 1 | 1 | 15/10/2026 | <één zin> | ja |
```

Trede = volgnummer, loopt door zonder einde (stap `t<trede>` in de voortgangslink). Niveau = 1 tot 5 uit `ladder.md`; na niveau 5 blijft het niveau 5 en loopt de trede door. Een nieuwe uitdaging mag niet dezelfde zin hebben als een eerdere rij, en niet hetzelfde dossier en hetzelfde soort als de vorige rij.
