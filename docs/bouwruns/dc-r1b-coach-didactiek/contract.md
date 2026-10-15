---
type: bouwcontract
status: getekend
date: 2026-10-15
getekend: 2026-10-15 (Bjorn, chat: "yes, meteen starten aub")
project: Debug-Marketing
tags: [bouwrun, contract, debug-coach, bijsturing]
---

> [!important] Bijsturing van R1 in blok 1 van [Debug Coach](../../plans/spec-debug-coach-blok-1.md)
> Bjorn stuurde R1 bij op 15/10 na de validatie en de gesimuleerde beginner ([verslag](../blok-1-validatie/gesimuleerde-beginner.md)). Bouwt in `debug-coach` op de tak `bouwrun/dc-r2-videopijplijn` (bevat R1 en R2, C01 al opgelost bij het aanvaarden). Python 3.9, geen pakketten.

## Contractkaart

> [!question] Teken of stuur bij
> **Wat er gebouwd wordt:** de coach leert de beginner het werk zelf te doen in plaats van het voor hem te doen: hij laat de gebruiker kiezen en zelf de vraag stellen, controleert "klaar als" echt, vraagt de feedback letterlijk, verwelkomt een nieuwe werkmap als nieuwe start, en legt per missie ongevraagd een begrip uit. Plus vier kleine punten.
> **Outputtype:** feature (skills en missiebestanden van de plugin).
> **Scenario's:** S1, S2, S4 en S5 van R1, aangescherpt.
> **Niet in deze run:** de videopijplijn, de site, nieuwe missies.
> **Aannames met de meeste impact:** A1 regels in de skilltekst sturen het gedrag van het model (getest door een tweede gesimuleerde beginner na de run).
> **Designrichting:** geen scherm.
> **Keten:** losse run, op de tak `bouwrun/dc-r2-videopijplijn`.
> **Budget:** 3 uur, 10 sessies.
> **Enkel jij kunt beantwoorden:** niets.

## 1. Doel

De lat van de proef is "zelfstandig leren met AI werken". De gesimuleerde beginner haalde alle missies, maar omdat de coach het werk deed. Na deze run stelt de gebruiker zelf de vraag en verbetert de coach die.

## 2. Scenario's (uit het verslag van de gesimuleerde beginner)

- **S1'** Een vers werkmappakket (alle missies op `open`, profiel `status: leeg`) is een **nieuwe start**: welkom, tabel van de werkmap, uitleg projectbrein en context; na missie 1 altijd de meter.
- **S2'** Bij een missie maakt de coach **niets in dezelfde beurt als het voorstel**. De gebruiker kiest (dossier, bestand, onderwerp) en stelt zelf de vraag; de coach verbetert die vraag (wat ontbreekt: wie, wat, voor wie, vorm, bronnen) en voert pas daarna uit. In elke route staat per stap wie ze doet: **Jij:** of **De coach:**.
- **S2''** In de stand uitgebreid legt de coach per missie minstens één begrip uit `## Begrippen` uit, ongevraagd, met "Denk eraan als:"; in de stand kort één zin per nieuw begrip.
- **S3'** "Klaar als": wat buiten de chat gebeurt (uploaden, een instelling, testen in een nieuw gesprek) telt pas als de gebruiker bevestigt dat hij het deed. Het menupad staat in het missiebestand, de coach gokt het nooit.
- **S4'** De feedbackrij: de coach stelt de twee vragen ("Wat was onduidelijk?" en "Waar liep je vast?"), schrijft enkel het letterlijke antwoord, en schrijft de rij pas in de beurt na het antwoord. Nooit verzinnen: dit bestand gaat naar Bjorn.
- **S5'** Klein: de voortgangslink als gewone tekst (klikbaar, niet als code); vóór verwijderen of overschrijven eerst vragen; nooit technische waarden tegen de gebruiker ("je platform staat op Claude", niet "`claude`"); missie 3 legt uit hoe je de tekst van een mail kopieert en plakt.

## 3. Niet-doelen

- Geen nieuwe missies of features; de bestaande tests van R1 en R2 blijven groen (basistest).
- Geen wijziging aan `videos/`, `scripts/` of de gedeelde formaten.

## 4. Aannames

| # | Aanname | Soort | Bron | Zekerheid | Impact | Hoe getest | Omkeerbaar |
|---|---|---|---|---|---|---|---|
| A1 | Expliciete regels in SKILL.md (met de exacte zinnen hieronder) veranderen het gedrag van het model merkbaar | technisch | verslag gesimuleerde beginner | middel | hoog | keurder speelt na; tweede gesimuleerde beginner na de run | ja |

### Inputkaart

| Gegeven | Bron | Hoe de run eraan komt | Gezien | Wie | Hoe vaak |
|---|---|---|---|---|---|
| Verslag gesimuleerde beginner | blok-1-validatie | `docs/bouwruns/dc-r1b-coach-didactiek/bronnen/gesimuleerde-beginner.md` | ja | Claude | eenmalig |
| Bestaande plugin | tak `bouwrun/dc-r2-videopijplijn` | de kloon | ja | repo | eenmalig |

## 5. Outputtype

**Feature.** De keurder speelt `start` na op een vers werkmappakket en een missie op `werkmap-missie7/`, en kijkt of de coach wacht op de keuze en de vraag van de gebruiker.

## 6. Technische vorm

| Onderdeel | Vorm | Waarom (in effect) | Afgewezen |
|---|---|---|---|
| Regels | In `plugin/skills/start/SKILL.md`, `missie/SKILL.md`, `uitdaging/SKILL.md` en de templates `CLAUDE.md`/`AGENTS.md`, met de zinnen die de tests zoeken | Beide apps lezen dezelfde regels | Een aparte regelset per app |
| Routes | Elke genummerde stap onder `## Route ChatGPT` en `## Route Claude` begint met `**Jij:**` of `**De coach:**`; elke route heeft minstens één `**Jij:**`-stap | De gebruiker ziet wat hij zelf doet | Vrije tekst |
| Menupaden | Enkel uit `bronnen/platformfeiten.md` van R1 (missie 7: `Customize > Skills > Upload a skill`) | Nooit gokken | |

## 7. Features

Zie `features.json` (D01 tot D09). Checks: `python3 tests/feature.py D0N`. Basistest: `python3 tests/regressie.py` (BASIS, C01 tot C13, V01 tot V08).

## 8. Testplan

Zie `testplan.md`.

## 9. Definition of done

- Elke feature klaar of geblokkeerd met reden; basistest groen.
- Keurder speelt S1', S2', S3', S4' na.
- Na de run: een tweede gesimuleerde beginner (zelfde persona, zelfde opzet) door missie 1 tot 7; doel: de gebruiker stelt in minstens 5 van de 7 missies zelf de vraag, geen verzonnen feedbackrij, missie 7 niet klaar zonder bevestiging.

## 10. Budget

3 uur, 10 sessies, 2 features per sessie, bouwer en keurder `opus`.

## 11. Designrichting

Geen scherm.

## 12. Keten

Losse run. Start na het tekenen meteen, op de tak `bouwrun/dc-r2-videopijplijn` (`--na dc-r2-videopijplijn --bouw-op vorige`). Daarna: R1, R2 en R1b samen naar main.
