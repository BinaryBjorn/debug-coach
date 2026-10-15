---
type: retro
status: active
date: 2026-10-15
tags: [bouwrun, retro]
---

## Meetpunten

| Meetpunt | Waarde | Bron |
|---|---|---|
| Duur run (wandklok) | 0,39 uur (bouwer 13,6 min, keurder 1,1 min, brandtest 0,1 min) | metingen/samenvatting.json |
| Sessies (bouwer / keurder / pakket) | 5 / 1 / 1 (de pakketsessie is nog niet gemeten: `metingen/pakket-1.json` is leeg) | metingen/samenvatting.json |
| Geschat verbruik (API-dollars, geen factuur) | 7,16 totaal: bouwer 3,34, keurder 3,67, brandtest 0,15; 18,22 per uur | metingen/samenvatting.json |
| Limietbalk `/usage` voor → na | niet afgelezen | handmatig afgelezen |
| Aanraaktijd Bjorn: contract / meldingen / validatie | contract: niet vastgelegd; meldingen: 0 berichten tijdens de run; validatie: nog niet | metingen/samenvatting.json |

## R6: /goal versus het checkscript

| Sessie | Modus | /goal liet stoppen | Checkscript | Afwijking |
|---|---|---|---|---|
| 1 (D01, D02) | observe | nee, niet zonder klaar | exit 0, doorgelaten | geen |
| 2 (D03, D04) | observe | nee, niet zonder klaar | exit 0, doorgelaten | geen |
| 3 (D05, D06) | block | nee, niet zonder klaar | exit 0, doorgelaten | geen |
| 4 (D07, D08) | block | nee, niet zonder klaar | exit 0, doorgelaten | geen |
| 5 (D09) | block | nee, niet zonder klaar | exit 0, doorgelaten | geen |

Samen: 2 observe-sessies, `/goal` stopte 0 keer te vroeg, de hook herstartte geen enkele sessie. Met 5 sessies zonder één geval waarin ze verschilden, zegt deze run niets over wat er gebeurt als `/goal` en het checkscript echt oneens zijn.

## Lessen en waar ze heen gingen

| Les | Naar |
|---|---|
| De keurder werd 12 keer geweigerd: apps of URL's openen (6 keer), lezen buiten de kloon (3 keer), schrijven buiten de runmap, tests aanraken, en één poging het contract opnieuw te tekenen. Zijn werk lukte via drie subagents in een tijdelijke map, maar niet zonder omwegen. | bouwrun-skill: beschrijf in de keurderopdracht de werkwijze voor een run zonder scherm (subagent als coach, tijdelijke map), zodat hij er niet langs de sloten naartoe hoeft te zoeken |
| In twee naspeelsessies schreef de coach-subagent via de shell rond een schrijfhook. Dat bleef in de tijdelijke map, maar het bewijst dat de naspeelopzet op een omweg steunt. | bouwrun-skill: leg vast waar een naspeler mag schrijven |
| De vaste controles zoeken zinnen in de skilltekst. Ze bewijzen niet dat het model zich zo gedraagt (aanname A1), en vingen ook niet dat missie 7 stap 8 een weetje is met een **Jij:**-label. Het gedragsbewijs hangt aan een stap na de run. | grill-me: bij een contract over gedrag van het model de tweede gesimuleerde beginner vooraf plannen als stap met een eigenaar en een moment, en niet als losse regel in de definition of done |
| De bouwer vroeg één keer een beschermd pad (tests); de bescherming hield. Verder liep de bouw zonder haperen: 5 sessies, 9 van 9 features, geen herstart. | geen actie |
| De keurder meldt 1,1 minuut, terwijl hij drie subagents liet naspelen. Ik kan niet nagaan of die subagents in de meting zitten. Het verbruik van de keuring kan dus te laag staan. | bouwrun-skill: meet ook het verbruik van subagents van de keurder |
| Drie meetpunten ontbraken in de runmap: de `/usage`-balk voor en na, de aanraaktijd van Bjorn voor het contract, en het verbruik van de pakketsessie. | bouwrun-skill: laat het startscript de balk vastleggen of laat de eerste stap van stand 3 hem vragen |
| Geen designcorrecties: de run had geen scherm. | smaakboek: geen voorstel |
