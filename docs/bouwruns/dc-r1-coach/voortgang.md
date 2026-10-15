%% Per sessie twee à vier regels. Dit is de overdracht naar de volgende, frisse sessie. %%

## Sessie 1 (15/10/2026)
- C02 klaar: de templates zijn compleet. `AGENTS.md` is `CLAUDE.md` met de regel `**Stand:** uitgebreid`. Het profiel heeft Platform, Account, Coachcode en Tools op [TODO]. Voortgang heeft 7 missierijen en een lege `## Ladder`-tabel. De feedbackkolommen volgen de acceptatie.
- C01 geblokkeerd: de verhuis naar `plugin/` en beide manifesten zijn klaar, `source: ./plugin`. De hook weigert wel het wissen van het oude root-manifest (`.claude-plugin/plugin.json`), omdat hij matcht op `.claude`. Zie roadblocks.md en V1. Enkel die ene assert faalt nog.
- Tests: C02 groen, BASIS groen, C01 1 van 2 groen. Tip: schrijf geen bash-commando's met `.claude` in de tekst, ook niet in heredocs. Volgende: C03 (de start-skill in het Nederlands herschrijven; de paden `../../missies/` kloppen nog na de verhuis).

## Sessie 2 (15/10/2026)
- C03 klaar: `plugin/skills/start/SKILL.md` is herschreven in het Nederlands (inventaris, werkmap met AGENTS.md, missie 1 met vragen in de chat als standaard en het formulier als extra in Cowork, Platform uit de app, coachcode van 8 tekens of [TODO], trainingsschakelaar per platform, link m1 of de zin zonder_code, meter, "zeg: volgende missie").
- C04 klaar: missie-01 tot missie-07 volgen het gedeelde formaat (frontmatter, zeven koppen, foutsubkoppen met minstens 3 ChatGPT- en 3 Claude-items, begrippen met "Denk eraan als"). C06 slaagt daardoor ook al, maar is nog niet afgevinkt.
- Tests: C03, C04, C06 en BASIS groen. Volgende: C05 (skill missie), daarna C06 afvinken na een eigen check.

## Sessie 3 (15/10/2026)
- C05 klaar: `plugin/skills/missie/SKILL.md` met meter, volgende open missie (overslaan mag), route uit Platform en Account (enkel vragen bij [TODO]), coachstand, Klaar als zelf controleren, één regel in successen.md en één rij in feedback.md, één keer een lagere stand (genoteerd in de feedbackrij), link m<N> of de zin zonder_code. Beslissingen 10 en 11.
- C07 klaar: `plugin/skills/uitdaging/ladder.md` (vijf niveaus met soort, varianten, voorbeeld) en `SKILL.md` (poort missie 7, niveau +1 tot 5 en daarna 5, trede loopt door, geen dubbele zin of dossier+variant, rij in `## Ladder` met Klaar nee, link t<trede> bij klaar). Beslissingen 12 en 13.
- Tests: C05, C07, C09 en BASIS groen; C10 faalt nog enkel op het ontbrekende `docs/updates.md` (eigen feature). Volgende: C06 afvinken, dan C08 (skills coach en uitleg) en C10.

## Sessie 4 (15/10/2026)
- C08 klaar: nieuwe skills `coach` (stand uitgebreid, kort of uit, enkel de regel `**Stand:**` in beide projectbreinen) en `uitleg` (één zin, Denk eraan als, voorbeeld uit het profiel, één tip, max 150 woorden, in elke stand). Templates: uitlegvorm geldt nu in elke stand, plus de vaste regel "waarschuw vóór iets onomkeerbaars, ook in uit". Beslissingen 14 en 15.
- C10 klaar: `docs/updates.md` (ChatGPT: Add a marketplace met `BinaryBjorn/debug-coach`, Instellingen > Plugins > Marketplace > Upgrade, daarna Refresh; Claude: Check for updates; mijn-vaardigheden en de werkmap nooit geraakt). De skills bevatten geen instructie om werkmapbestanden te overschrijven of te wissen; start schrijft enkel wat ontbreekt.
- Tests: C08, C10 en BASIS groen. Nog rood in de volledige suite: C01 (geblokkeerd), C11 tot C13 en de V-reeks (andere features/sessies). C06 en C09 slagen maar zijn nog niet afgevinkt.

## Sessie 5 (15/10/2026)
- C12 klaar: `scripts/bouw_werkmap.py` maakt `dist/debug-coach-werkmap/` (templates, lege plugin `.coach/mijn-vaardigheden/` met plugin.json en skills/README.md, `.agents/plugins/marketplace.json` catalogus `mijn-werkmap`) en de zip; de coach zit er niet in. `dist/` staat in `.gitignore`. Beslissing 16.
- C11 klaar: zes `videos/<slug>/script.json` (platform chatgpt) en `opname.md` (opdracht voor Claude met Computer Use: demo-account, nepdata, venster vooraan, `screencapture -v -V -R`, tijdstip vóór elke klik, `start_video_gemeten` aan de eerste beeldwissel, `ruw/log.json` volgens log.schema.json, stappentabel met wat te loggen). `videos/*/ruw/` en `videos/*/uit/` in `.gitignore`. Beslissingen 17 en 18.
- Tests: C11, C12 en BASIS groen. Nog open voor latere sessies: C13 (README), C06 en C09 afvinken, C01 geblokkeerd.

## Sessie 6 (15/10/2026)
- C13 klaar: `README.md` herschreven zonder slash-commando's: installeren in ChatGPT (pakket in OneDrive op Altijd op dit apparaat, Work, Plugins > Add > Add a marketplace `BinaryBjorn/debug-coach`, debug-coach en mijn-vaardigheden onder Personal, "start") en in Claude (Customize > Plugins > Add marketplace), de werkmap, de coachcode, wat je zegt, updates (Upgrade + Refresh, Check for updates). Beslissing 19.
- Tests: C13 en BASIS groen. Nog open: C06 en C09 afvinken (slagen al), C01 geblokkeerd (V1).
