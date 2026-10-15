---
type: retro
status: active
date: 2026-10-15
tags: [bouwrun, retro]
---

## Meetpunten

| Meetpunt | Waarde | Bron |
|---|---|---|
| Duur run (wandklok) | 0,54 uur | metingen/samenvatting.json |
| Sessies (bouwer / keurder / pakket) | 8 / 2 / 1 (pakket is deze sessie, nog niet gemeten; plus 1 brandtest) | metingen/samenvatting.json |
| Geschat verbruik (API-dollars, geen factuur) | $13,65 totaal (bouwer $8,06, keurder $5,42, brandtest $0,17); $25,4 per uur | metingen/samenvatting.json |
| Limietbalk `/usage` voor → na | niet afgelezen | handmatig afgelezen |
| Aanraaktijd Bjorn: contract / meldingen / validatie | niet gemeten / 0 berichten tijdens de run / nog te doen | metingen/samenvatting.json |

## R6: /goal versus het checkscript

| Sessie | Modus | /goal liet stoppen | Checkscript | Afwijking |
|---|---|---|---|---|
| 1 (C01, C02) | observe | nee | exit 0 | geen |
| 2 (C03, C04) | observe | nee | exit 0 | geen |
| 3 (C05, C07) | observe | nee | exit 0 | geen |
| 4 (C08, C10) | block | nee | exit 0 | geen |
| 5 (C11, C12) | block | nee | exit 0 | geen |
| 6 (C13) | block | nee | exit 0 | geen |
| 7 (C01, C02) | block | nee | exit 0 | geen |
| 8 (C03) | block | nee | exit 0 | geen |

Observe-sessies: 3. `/goal` stopte nooit te vroeg (0). Let op: exit 0 betekent hier "alles afgehandeld", en een geblokkeerde C01 telt daarin als afgehandeld. In geen enkele sessie bleek een herstart door de stop-hook nodig (`herstart_door_hook` was steeds false).

## Lessen en waar ze heen gingen

| Les | Naar |
|---|---|
| Het contract eiste het wissen van `.claude-plugin/plugin.json`, terwijl de beveiliging van de run elk pad met `.claude` weigert, ook `.claude-plugin`. C01 kon zo niet slagen. De bouwer zag het in sessie 1 en de run liep nog 7 sessies en 2 keurrondes door. Los daarvan zijn 36 weigeringen geteld. | grill-me: bij het ontwerpen van een feature nagaan of ze een pad raakt dat de run beschermt. bouwrun-skill: de beveiliging laten matchen op `.claude/` in plaats van `.claude`, of dit als bekende uitzondering in het contract zetten |
| De run stopte omdat de keurrondes op waren (2), niet omdat het budget op was: 0,54 uur van 5 en 8 van 16 sessies. Een onoplosbare feature kostte een hele keurronde. | bouwrun-skill: een feature die geblokkeerd is om een bekende reden uit de keurronde-telling houden, of de run daarop laten sluiten met een pakket |
| De keurder probeerde 26 keer in minder dan een minuut buiten de runmap te schrijven, en twee keer een handeling die de beveiliging las als het (her)tekenen van het contract. | bouwrun-skill: in de keurderopdracht zetten dat naspelen droog gebeurt in de verificatie, zodat de keurder niet blijft proberen |
| De bouwer noteerde in sessie 2 tot 6 dat C06 en C09 "nog afgevinkt moesten worden" en deed het nooit. `features.json` zegt nu "open" terwijl het checkscript "klaar" meldt. | bouwrun-skill: afvinken in dezelfde sessie als de check groen is, en het checkscript de enige waarheid laten |
| Drie fouten uit keurronde 1 zijn niet teruggestuurd en bleven open. | bouwrun-skill: bij elke ronde bepalen welke bevindingen teruggaan, en de rest met reden in het pakket zetten |
| Fixture `werkmap-claude-werk/` mist `voortgang.md` en `successen.md`, en er zijn geen fixtures voor trede 1 en 2 en voor een eigen skill. De keurder moest het eerst met `start` aanvullen. Tests zijn beschermd, dus de bouwer kon dit niet herstellen. | grill-me: bij het ontwerpen van de dummydata elke werkmapfixture volledig maken, zodat elke skill er direct op te spelen is |
| Geen designcorrectie: de run had geen scherm. | smaakboek: niets toe te voegen |
