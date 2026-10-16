---
type: validatie
status: aanvaard
date: 2026-10-15
tags: [bouwrun, validatie]
---

> [!tip] In één zin
> De videopijplijn is af: uit een ruwe opname, een kliklog en een script maakt één commando een video met kader, inzoomen, klikcirkel, stem en ondertitels. Alle 8 features zijn klaar en door de keurder bevestigd. Eén ding is alleen met een testopname geprobeerd, niet met een echte opname van Claude.

## 1. Wat er gebouwd is

Je neemt niets op en bewerkt niets. Claude neemt later ChatGPT op; daarna draait `python3 videos/maak.py videos/missie-5` en je krijgt `missie-5.mp4` met `missie-5.vtt` ernaast. Hieronder de uitkomst op een testopname.

- **Kader en achtergrond (S7a).** Het scherm staat in een kader met afgeronde hoeken op het donkerblauwe verloop van Debug Marketing.
  ![[S7a-1-begin.png|400]]
- **Inzoomen en klikcirkel (S7a).** Bij een klik zoomt het beeld in (1,8 keer) en de blauwe cirkel staat precies op de plek van de klik.
  ![[S7a-2-klik1.png|400]]
- **Een klik buiten het opgenomen scherm.** De cirkel blijft op de rand van het kader staan, half over de achtergrond. Dat volgt de afspraak, maar ziet er vreemd uit. Een echte opname hoort dit niet te hebben.
  ![[S7a-4-klik2.png|400]]
- **Stem langer dan de handeling (S7b).** Het beeld blijft op het laatste kader staan tot de zin uit is. Is de handeling langer dan de stem, dan speelt ze volledig af en komt er stilte bij de stem. Stukken zonder handeling zijn weggeknipt.
  ![[S7b-s01-bevroren.png|400]]
- **Geen stemsleutel (S7c).** Met `--stem openai` en zonder sleutel zegt het script in één regel "stem ontbreekt" en maakt toch de video, met een testtoon als stem.
- **Ondertitels en handleiding.** Eén ondertitel per stap, als apart bestand en in de mp4. `videos/README.md` beschrijft de hele keten.

Alle twaalf stilstaande beelden: ![[overzicht-S7.png|600]]

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 2. Wat de keurder vond

De keurder maakte zelf een testvideo van 20 seconden en keek stilstaande beelden en het renderplan na. Alle drie de scenario's en alle 8 features: **slaagt**. De videobestanden zijn 8,0 seconden (en 15,0 in de variant met extra randgevallen), met beeld, geluid en ondertitels even lang.

Fouten die de automatische checks misten: geen. De keurder had wel vier opmerkingen:

1. **Alleen de eerste klik per stap krijgt zoom en cirkel.** Het contract schrijft één cirkel per stap voor, maar de contractkaart beloofde "inzoomen op elke klik". Neemt Claude later twee kliks in één scriptstap op, dan blijft de tweede zonder cirkel.
2. **Een klik buiten de opname** geeft een cirkel half over de achtergrond (zie boven).
3. **Oude bestanden in `uit/` blijven staan.** De handleiding zegt dat die map telkens opnieuw wordt gemaakt, maar een stemfragment van een geschrapte stap blijft liggen. Geen gevolg voor de video.
4. **Vloeiendheid is niet bekeken.** De keurder zag losse beelden, geen afgespeelde video. Of de zoom schokt bij het schuiven van de ene klik naar de andere (rond 5,6 tot 6,0 s in de test), moet jij zien.

Boekhouding: V04 (timing) staat in `features.json` nog als "open", terwijl de check groen is en de keurder het gedrag bevestigde. De bouwer heeft het nooit afgevinkt. Dit is een administratieve fout, geen gebrek in de video.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 3. Keuzes die Barri in jouw plaats maakte

Alles is omkeerbaar. De zichtbare keuzes:

- **Geen designplan:** het contract zegt "geen webscherm" en de stijl lag al vast.
- **Verloop diagonaal** met een fijn korrelpatroon, zodat er geen strepen in het donkere blauw zitten.
- **Klikcirkel:** 72 px, 40% dekking, 0,6 seconden in beeld.
- **Inzoomen** begint 0,4 seconden vóór de klik, zodat de klik al ingezoomd valt. Volgen twee zoomstappen snel op elkaar, dan schuift het beeld ingezoomd door in plaats van tussendoor uit te zoomen.
- **Een stap zonder handeling** toont het laatste beeld van de vorige stap, in plaats van te springen.
- **Testtoon:** een zachte, hoorbare toon (440 Hz), zodat je kunt horen of de timing klopt.
- **Met de echte stem** telt de gemeten lengte van de opname, niet de schatting uit het script, zodat het beeld precies blijft staan tot de zin uit is.
- **De handleiding** zegt dat de goedgekeurde video naar de speler van de site gaat (run 3). De pijplijn uploadt zelf niets.

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 4. Vragen met de standaard die toegepast werd

Er zijn geen vragen gesteld (`vragen.md` is leeg).

**Jouw oordeel:** aanvaard / bijsturen / afwijzen

## 5. Aannames die nog niet live getoetst zijn

`aannames.md` is leeg; dit komt uit de aannames van het contract.

- **De echte opname van Claude is nog niet door de pijplijn gegaan.** Alles is getest op een testopname (nagemaakt, 120 beelden per seconde) met een kliklog in het formaat dat de proef van 15/10 gaf. Past een echte opname daar niet op, dan zie je dat pas bij de eerste opname na de keten. Zekerheid hoog, impact hoog.
- **De echte stem (OpenAI)** is niet aangeroepen: er is geen sleutel in de run. De aanvraag is alleen opgebouwd en nagekeken, niet verstuurd. Zekerheid hoog, impact middel.
- **De speler toont de ondertitels standaard aan.** Dat regelt run 3. Zekerheid middel, impact laag.

## 6. Niet gehaald

Niets uit het contract. Wat bewust buiten deze run viel: de echte opname, de echte stem en de site. De drie dingen die niet bewezen zijn staan hierboven bij punt 2 (vloeiendheid) en punt 5.

## Design

Dit is een video, geen webscherm: geen designplan, geen design-critic, dus geen scores. De richting stond vast in het contract: het verloop `#0B1628` naar `#1A2D4A`, de cirkel `#4A7CC9` en 24 px afgeronde hoeken, uit de huisstijl van Debug Marketing. De keurder zag dat dit in de beelden klopt. Open op middel of laag: geen, behalve dat de zoom nog niet als beweging bekeken is (punt 2.4).

**Designcorrectie:**

## Voorstel voor het smaakboek

Geen: er is geen designcorrectie van jou en geen smaakboek in deze werkmap. Vul je hierboven een correctie in, dan komt hier het voorstel. Pas na jouw ja gaat een regel in het smaakboek.

## 7. De run in cijfers

- **Duur:** 0,33 uur op de klok (aanraaktijd van jou tijdens de run: 0 berichten).
- **Sessies:** 4 bouwsessies (10,9 min), 1 keurder (5,8 min), 1 brandtest-sessie (0,4 min).
- **Geschat verbruik:** 5,24 API-dollars, zonder dit pakket (schatting, geen factuur). De /usage-balk voor en na is niet afgelezen.
- **Afscherming:** de bouwer werd 12 keer geweigerd door de beveiliging (beschermde paden, buiten de kloon schrijven of lezen); de keurder 1 keer, toen die het contract opnieuw wilde tekenen. Dat mag alleen jij.
- **Commits:** 4 bouwcommits (V01 en V02, V03 en V05, V06 en V07, V08), 4 startscript-commits en 1 keuringscommit.
- Meer in `retro.md`.
