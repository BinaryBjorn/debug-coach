%% Per sessie twee à vier regels. Dit is de overdracht naar de volgende, frisse sessie. %%

## Sessie 1 (15/10/2026)
- C02 klaar: de templates zijn compleet. `AGENTS.md` is `CLAUDE.md` met de regel `**Stand:** uitgebreid`. Het profiel heeft Platform, Account, Coachcode en Tools op [TODO]. Voortgang heeft 7 missierijen en een lege `## Ladder`-tabel. De feedbackkolommen volgen de acceptatie.
- C01 geblokkeerd: de verhuis naar `plugin/` en beide manifesten zijn klaar, `source: ./plugin`. De hook weigert wel het wissen van het oude root-manifest (`.claude-plugin/plugin.json`), omdat hij matcht op `.claude`. Zie roadblocks.md en V1. Enkel die ene assert faalt nog.
- Tests: C02 groen, BASIS groen, C01 1 van 2 groen. Tip: schrijf geen bash-commando's met `.claude` in de tekst, ook niet in heredocs. Volgende: C03 (de start-skill in het Nederlands herschrijven; de paden `../../missies/` kloppen nog na de verhuis).

## Sessie 2 (15/10/2026)
- C03 klaar: `plugin/skills/start/SKILL.md` is herschreven in het Nederlands (inventaris, werkmap met AGENTS.md, missie 1 met vragen in de chat als standaard en het formulier als extra in Cowork, Platform uit de app, coachcode van 8 tekens of [TODO], trainingsschakelaar per platform, link m1 of de zin zonder_code, meter, "zeg: volgende missie").
- C04 klaar: missie-01 tot missie-07 volgen het gedeelde formaat (frontmatter, zeven koppen, foutsubkoppen met minstens 3 ChatGPT- en 3 Claude-items, begrippen met "Denk eraan als"). C06 slaagt daardoor ook al, maar is nog niet afgevinkt.
- Tests: C03, C04, C06 en BASIS groen. Volgende: C05 (skill missie), daarna C06 afvinken na een eigen check.
