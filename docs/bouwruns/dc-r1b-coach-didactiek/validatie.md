---
type: validatie
status: wacht-op-bjorn
date: 2026-10-15
tags: [bouwrun, validatie]
---

> [!tip] In één zin
> Alle negen punten uit het contract zijn gebouwd en de keurder zag ze werken. Eén ding is nog open: de tweede gesimuleerde beginner, de echte proef of de coach nu de beginner zelf laat werken, is nog niet gedraaid.

## 1. Wat er gebouwd is

Er is geen scherm in deze run, dus geen screenshots. Wat je nu kunt zien is gedrag van de coach, zoals de keurder het naspeelde.

- **Een vers werkmappakket is een nieuwe start (S1').** De coach heet de gebruiker welkom, zegt dat de werkmap al klaarstaat en dat hij niets overschreef, en legt het projectbrein uit. Na missie 1 volgt altijd de meter.
- **De gebruiker kiest en vraagt zelf (S2').** De coach doet bij een missie eerst niets. De gebruiker kiest het dossier en typt zelf de vraag. De coach zet zijn verbeterde vraag naast die van de gebruiker en voert pas daarna iets uit. Elke stap in de zeven missies zegt nu **Jij:** of **De coach:**.
- **Ongevraagd uitleggen (S2'').** In de stand uitgebreid legt de coach per missie een begrip uit, met "Denk eraan als:" en een voorbeeld uit het werk van de gebruiker.
- **"Klaar als" echt controleren (S3').** Een skill uploaden of testen telt pas als de gebruiker zegt dat hij het deed. Het menupad komt letterlijk uit het missiebestand (Customize > Skills > Upload a skill). Weet de gebruiker het scherm niet te vinden, dan zegt de coach dat hij het niet zeker weet.
- **Feedback letterlijk (S4').** De coach stelt de twee vragen en schrijft de rij pas in de beurt na het antwoord, met de woorden van de gebruiker. Geen antwoord wordt `geen antwoord`.
- **Vier kleine punten (S5').** De voortgangslink is gewone, klikbare tekst. De coach vraagt eerst voor hij iets verwijdert of overschrijft. Hij toont de gebruiker geen technische waarden meer. Missie 3 legt uit hoe je een mail kopieert en plakt, voor Windows en Mac.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 2. Wat de keurder vond

Alle negen punten (D01 tot D09) slagen. De vaste controles zijn groen en de bestaande tests van R1 en R2 ook (22 van 22). De keurder speelde S1', S2', S2'', S3' en S4' na met drie aparte rollenspelers en vond niets wat de bouwer miste.

Drie opmerkingen om zelf te bekijken:
- In missie 7, route Claude, stap 8 begint met **Jij:**, maar het is een weetje en geen handeling.
- In missie 7 krijgt de gebruiker na de feedback in één bericht de meter, de link, het voorstel voor een lagere stand en de eerste uitdaging. Dat is veel in één keer.
- In de uitdaging staat voor ChatGPT het pad "Plugins > Refresh". Dat staat ook al in missie 7, maar de feitenlijst noemt het enkel bij marketplaces. Het is niet nieuw, maar het is nog niet bevestigd voor dit gebruik.

Beperking: het naspelen gebeurde met hetzelfde model in een rollenspel, niet in de echte Cowork- of ChatGPT-app. De stand kort is niet nagespeeld, enkel gecontroleerd in de tekst.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 3. Keuzes die Barri in jouw plaats maakte

1. De coach toont de verbeterde vraag naast die van de gebruiker en laat hem kiezen welke hij uitvoert, zodat de gebruiker eigenaar van de vraag blijft.
2. Zegt de gebruiker uitdrukkelijk "doe jij het maar", dan doet de coach het toch, maar toont eerst de vraag die hij zelf zou stellen. Je zet niemand vast die echt niet verder wil.
3. Bij een vers werkmappakket schrijft de coach niets en zegt dat de werkmap al klaarstaat.
4. Antwoordt de gebruiker niet op de feedbackvragen, dan schrijft de coach `geen antwoord` en geen `nee`. Dan zie jij wat echt gezegd werd.
5. Na de feedbackrij volgen in dezelfde beurt de rest van de afronding en de meter.

Alle vijf zijn gemakkelijk terug te draaien.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 4. Vragen met de standaard die toegepast werd

Geen. `vragen.md` is leeg gebleven.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 5. Aannames die nog niet live getoetst zijn

- **A1 (zekerheid middel, impact hoog):** een regel in de skilltekst verandert echt hoe het model zich gedraagt. De keurder zag het in het rollenspel, maar dat is geen bewijs. Het bewijs komt van de tweede gesimuleerde beginner, zie hieronder.

## 6. Niet gehaald

Niets van de negen punten. Wat uit het contract nog openstaat:

- **De tweede gesimuleerde beginner is niet gedraaid.** Het contract vraagt die na de run: zelfde persona, missie 1 tot 7. Doel: de gebruiker stelt in minstens 5 van de 7 missies zelf de vraag, er staat geen verzonnen feedbackrij, en missie 7 is niet klaar zonder bevestiging. Deze run kon dat niet zelf doen. Tot dat gebeurd is, staat "de coach laat de beginner zelf werken" nog niet bewezen.
- Het samenvoegen van R1, R2 en R1b naar main volgt pas na jouw oordeel.

## 7. De run in cijfers

- Duur: 0,39 uur (ongeveer 23 minuten) op een budget van 3 uur.
- Sessies: 5 bouwsessies, 1 keuring, 1 pakket, op een budget van 10.
- Geschat verbruik: 7,16 dollar in API-prijzen (geen factuur). Bouwer 3,34 dollar, keurder 3,67 dollar, brandtest 0,15 dollar.
- Berichten aan jou tijdens de run: 0.
- De beveiliging weigerde 13 keer een actie: 1 van de bouwer, 12 van de keurder (zie `retro.md`). Er is niets beschadigd.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen
