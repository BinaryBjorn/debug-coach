---
type: retro
status: active
date: 2026-10-15
tags: [bouwrun, retro]
---

## Meetpunten

| Meetpunt | Waarde | Bron |
|---|---|---|
| Duur run (wandklok) | 0,33 uur | metingen/samenvatting.json |
| Sessies (bouwer / keurder / pakket) | 4 / 1 / 1 (pakket nog niet in de meting; ook 1 brandtest-sessie van 0,4 min) | metingen/samenvatting.json |
| Geschat verbruik (API-dollars, geen factuur) | 5,24 totaal zonder pakket (bouwer 3,51; keurder 1,57; brandtest 0,16); 16,0 per uur | metingen/samenvatting.json |
| Limietbalk `/usage` voor → na | niet afgelezen | handmatig afgelezen |
| Aanraaktijd Bjorn: contract / meldingen / validatie | contract: niet gemeten; meldingen: 0 berichten tijdens de run; validatie: nog niet gebeurd | metingen/samenvatting.json |

Duur per rol: bouwer 10,9 min, keurder 5,8 min, brandtest 0,4 min. Budget van het contract: 4 uur, 12 sessies; gebruikt: 0,33 uur en 4 bouwsessies.

## R6: /goal versus het checkscript

Alle drie observe-sessies en de blokkerende sessie 4: het checkscript gaf exit 0 en `/goal` liet niet te vroeg stoppen (0 keer van 3). Geen afwijking.

| Sessie | Modus | /goal liet stoppen | Checkscript | Afwijking |
|---|---|---|---|---|
| 1 (V01, V02) | observe | nee | exit 0 | geen |
| 2 (V03, V05) | observe | nee | exit 0 | geen |
| 3 (V06, V07) | observe | nee | exit 0 | geen |
| 4 (V08) | block | nee | exit 0 | geen |

Kanttekening: V04 werd in geen enkele sessie gebouwd of afgevinkt (`features.json` staat nog op open), terwijl elk checkscript exit 0 gaf. Zie de eerste les.

## Lessen en waar ze heen gingen

| Les | Naar |
|---|---|
| V04 stond in `features.json` nog op open, terwijl de check groen was en de keurder het gedrag bevestigde (duur 8,0 s en 15,0 s). De bouwer pakte het niet apart op en vinkte het nooit af; de keurder moest het in de boekhouding opmerken. Een feature die al door een eerdere sessie gedekt is, moet de bouwer expliciet afvinken of als gedekt noteren. | bouwrun-skill (regel voor de bouwer: loop voor het einde `features.json` na) |
| Het hook weigert elk schrijfcommando met het woord `tests` erin, ook `testsrc2` (een ffmpeg-bron). De bouwer verloor beurten en bedacht omwegen (`smptehdbars`, `t?sts/...`) om proefbeelden te maken. Zo'n woordfilter zou op het pad moeten letten, niet op het woord. | bouwrun-skill (hook van de beschermde paden verfijnen) |
| Lezen buiten de kloon wordt geweigerd. Proefbeelden moeten eerst naar een tijdelijke map in de kloon. Dat kostte weigeringen (6 voor lezen of schrijven buiten de kloon en 6 voor beschermde paden, bij de bouwer). | bouwrun-skill (zeg het in het sessieoverzicht van de bouwer, `voortgang.md` deed het al) |
| De keurder probeerde het contract opnieuw te tekenen en werd geweigerd, terecht: enkel Bjorn tekent. Waarom de keurder dat probeerde, staat niet in de run; de les is dat de keurderopdracht dit uitdrukkelijk moet verbieden. | bouwrun-skill (keurderopdracht: noem uitdrukkelijk dat contract en getekende bestanden onaantastbaar zijn) |
| Het contract zei "inzoomen op elke klik" op de kaart, maar de rekenregels geven één cirkel per stap. Dat kwam pas in de keuring aan het licht. | grill-me (laat de contractkaart en de rekenregels op tegenstrijdigheid nalopen voor het tekenen) |
| De keurder kon de zoombeweging niet als beweging beoordelen, alleen losse kaders. Vloeiendheid hangt dus altijd van Bjorns nakijken af. | vakkennis video (eventueel een korte clip van de zoom bij het pakket, voor een volgende run) |
| Een opname is nooit door de pijplijn gehaald; de fixtures bootsen ze na. Het eerste echte log kan breken op een detail dat de test niet kent. | vakkennis video (eerste echte opname na de keten nakijken en deze retro aanvullen) |
| Er was geen designcorrectie van Bjorn en er is geen smaakboek in deze werkmap; er is daarom geen voorstel voor het smaakboek. | smaakboek (niets te doen) |
