%% Per sessie twee à vier regels. Dit is de overdracht naar de volgende, frisse sessie. %%

## Sessie 1 (15/10/2026)
- C02 klaar: de templates zijn compleet. `AGENTS.md` is `CLAUDE.md` met de regel `**Stand:** uitgebreid`. Het profiel heeft Platform, Account, Coachcode en Tools op [TODO]. Voortgang heeft 7 missierijen en een lege `## Ladder`-tabel. De feedbackkolommen volgen de acceptatie.
- C01 geblokkeerd: de verhuis naar `plugin/` en beide manifesten zijn klaar, `source: ./plugin`. De hook weigert wel het wissen van het oude root-manifest (`.claude-plugin/plugin.json`), omdat hij matcht op `.claude`. Zie roadblocks.md en V1. Enkel die ene assert faalt nog.
- Tests: C02 groen, BASIS groen, C01 1 van 2 groen. Tip: schrijf geen bash-commando's met `.claude` in de tekst, ook niet in heredocs. Volgende: C03 (de start-skill in het Nederlands herschrijven; de paden `../../missies/` kloppen nog na de verhuis).
