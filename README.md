# Debug Coach

Leer werken met AI op je eigen werk. Zeven missies, elk met een echt resultaat voor jouw job, en een coach die uitlegt wat de AI doet en waarom, tot je hem niet meer nodig hebt. Daarna gaat het verder op een ladder van uitdagingen.

De coach werkt in twee apps: **ChatGPT** (Work, in de desktopapp) en **Claude** (Cowork, in de desktopapp). Je typt nergens een commando: je zegt gewoon wat je wilt, zoals "start" of "volgende missie".

## Installeren in ChatGPT

1. **Zet het werkmappakket in OneDrive.** Pak `debug-coach-werkmap.zip` uit in een map in je OneDrive. Klik met de rechtermuisknop op die map en kies **Altijd op dit apparaat bewaren**, zodat ChatGPT de bestanden echt kan lezen.
2. **Open de map in Work.** Open de ChatGPT-desktopapp, ga naar Work en kies de uitgepakte map als werkmap.
3. **Voeg de coach toe.** Ga naar **Plugins > Add > Add a marketplace**. Vul bij Source in: `BinaryBjorn/debug-coach`. Laat Git ref op `main`.
4. **Installeer `debug-coach`.** Onder het tabblad **Personal** verschijnt de catalogus `debug-marketing` met de plugin `debug-coach`. Klik op installeren.
5. **Installeer `mijn-vaardigheden`.** Onder **Personal** staat ook de catalogus `mijn-werkmap` uit je werkmap, met de plugin `mijn-vaardigheden`. Installeer ook die. Ze is nog leeg: in missie 7 komen hier je eigen vaardigheden in. Zie je ze niet, herstart dan de app.
6. **Zeg "start".** Begin een nieuw gesprek in je werkmap en zeg: start. De coach zet je werkmap klaar en leert jou kennen: dat is missie 1.

## Installeren in Claude

1. **Kies een werkmap.** Open de Claude-desktopapp, ga naar Cowork en kies een map in je OneDrive als werkmap (het uitgepakte werkmappakket, of een lege map).
2. **Voeg de coach toe.** Ga naar **Customize > Plugins > Add marketplace** en vul `BinaryBjorn/debug-coach` in.
3. **Installeer `debug-coach`.** Kies in de catalogus `debug-marketing` de plugin `debug-coach` en installeer ze.
4. **Zeg "start".** Begin een nieuw gesprek in je werkmap en zeg: start.

In Claude heb je `mijn-vaardigheden` niet nodig: je eigen vaardigheden komen daar in `projecten/eigen-skills/` en onder Customize > Skills.

## Je werkmap

De werkmap is van jou. De coach staat er niet in en vult ze enkel aan: zeg je opnieuw "start", dan voegt hij toe wat ontbreekt en overschrijft hij nooit een bestand dat er al staat.

| Bestand | Waarvoor |
|---|---|
| `AGENTS.md` | Het projectbrein voor ChatGPT: wat de AI elke keer eerst leest over jou en over hoe de coach werkt |
| `CLAUDE.md` | Hetzelfde projectbrein, voor Claude |
| `ik/profiel.md` | Wie je bent: rol, dossiers, werkwijze, stijl, je platform en je coachcode |
| `voortgang.md` | Waar je staat in de zeven missies, en je ladder van uitdagingen |
| `feedback.md` | Na elke missie een korte rij. Dit bestand deel je met Bjorn, nooit inhoud uit je werk |
| `successen.md` | Wat werkte: de vraag en het resultaat, om later te hergebruiken |
| `projecten/` | Je projecten per onderwerp (missie 2) |
| `.coach/mijn-vaardigheden/` | De plugin met je eigen vaardigheden (missie 7, ChatGPT) |

## De coachcode

Je coachcode bestaat uit 8 tekens, letters en cijfers. Je vindt ze op je startplanpagina. De coach vraagt ze in missie 1 en zet ze in `ik/profiel.md`. Na elke missie geeft hij je een voortgangslink met die code, zodat je de stap op het platform kunt afvinken.

Heb je de code niet bij de hand, dan kan het later: zeg dan "mijn coachcode is ..." met je 8 tekens. De link bevat enkel je code en de stap, nooit inhoud uit je werk.

## Wat je zegt

- **start**: de werkmap klaarzetten en missie 1 doen, of zien waar je staat.
- **volgende missie**: de volgende open missie. Overslaan mag.
- **geef me een uitdaging**: na missie 7, de volgende trede op de ladder.
- **leg uit**: een begrip in gewone taal.
- **zet de coach op kort** of **zet de coach uit**: minder uitleg (zeg "uitgebreid" om terug te gaan).

## Updates

Een nieuwe versie van de coach komt via de catalogus op GitHub. Een update vervangt enkel de coach. Je werkmap (`ik/`, `projecten/`, `feedback.md`, `successen.md`, `voortgang.md`) en `mijn-vaardigheden` worden nooit geraakt.

- **ChatGPT:** open **Instellingen > Plugins**, tabblad **Marketplace**, en klik bij `debug-marketing` op **Upgrade**. Klik daarna op **Refresh**: de lijst toont de nieuwe versie pas dan.
- **Claude:** ga naar **Customize > Plugins**, kies de catalogus en klik op **Check for updates**. Of zet **Sync automatically** aan.

Begin daarna een nieuw gesprek in je werkmap. Meer uitleg, ook voor wie de coach uitbrengt: [docs/updates.md](docs/updates.md).
