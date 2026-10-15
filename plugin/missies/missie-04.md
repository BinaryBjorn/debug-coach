---
missie: 4
titel: Een tijdlijn uit je mails
video: geen
---

## Doel

Alles over één onderwerp van de laatste twee maanden, als tijdlijn per conclusie. Zo zie je in één oogopslag wat beslist is en wat nog openstaat.

## Resultaat

`projecten/<dossier>/tijdlijn-<onderwerp>.md`: per datum de afzender, wat er beslist of gevraagd werd, en onderaan een lijst open punten.

## Route ChatGPT

1. Zeg: volgende missie. Kies een onderwerp en een periode (bv. de laatste twee maanden).
2. Weet vooraf: mails die de AI opent, komen op gelezen te staan. Er wordt niets verstuurd, verwijderd of verplaatst.
3. Laat Work Outlook.com openen in de ingebouwde browser. Log zelf in; de AI vult nooit je wachtwoord in.
4. De AI zoekt met een datumfilter, zoals `received:<van>..<tot> "<onderwerp>"`, en leest de mails.
5. De AI bouwt de tijdlijn in de projectmap. De coach toont je wat een goede vraag bevat: welk onderwerp, welke periode, in welke vorm (per datum, per conclusie).
6. Lukt de browser niet: bewaar de mails als bestand in de projectmap of plak de tekst in de chat, en laat de AI daaruit de tijdlijn maken.

### Met een werkaccount

1. Is de Outlook-app gekoppeld (missie 3), dan zoekt de AI via die app in plaats van via de browser.

## Route Claude

1. Zeg: volgende missie. Kies een onderwerp en een periode.
2. Persoonlijk account: bewaar de mails als bestand in de projectmap of plak de tekst in de chat.
3. Cowork bouwt de tijdlijn in de projectmap: per datum de afzender, wat beslist of gevraagd werd, en de open punten.

### Met een werkaccount

1. Is de Microsoft 365-connector gekoppeld (missie 3), dan zoekt Claude via de connector in je mail.

## Klaar als

- `projecten/<dossier>/tijdlijn-<onderwerp>.md` bestaat, met minstens vijf data.
- Onderaan staat een lijst open punten.
- Er is niets veranderd in je mailbox: niets verstuurd, verwijderd of verplaatst.

## Wat kan hier fout gaan

### ChatGPT

- **De browser geeft een fout bij het openen van Outlook:** probeer één keer opnieuw. Lukt het niet, bewaar of plak je mails in de projectmap.
- **Je mails staan nu op gelezen:** dat gebeurt als de AI ze opent. Zet ze in Outlook terug op ongelezen als je dat wil.
- **De AI vindt te weinig mails:** maak de zoekterm breder of de periode langer, en vraag opnieuw.
- **De AI vraagt je wachtwoord:** geef het nooit in de chat. Log zelf in op het inlogscherm in de browser.

### Claude

- **De connector werkt niet met je account:** die werkt enkel met een werkaccount. Bewaar of plak je mails in de projectmap.
- **De tijdlijn mist data:** vraag de AI om bij elke regel de datum en de afzender uit de mail te halen, en kijk na welke mails ontbreken.
- **Plakken van veel mails wordt rommelig:** bewaar elke mail als apart bestand in de projectmap.

## Begrippen

- **Zoekopdracht:** de woorden en filters waarmee de AI in je mail zoekt. Denk eraan als: een segment in je CRM, alleen de contacten die aan de voorwaarden voldoen.
- **Tijdlijn:** gebeurtenissen op volgorde van datum, met wat er telkens besloten werd. Denk eraan als: de historiek van een deal in je CRM.
- **Bron vermelden:** bij elke regel zeggen uit welke mail het komt. Denk eraan als: een voetnoot in een rapport, zodat iedereen het kan nakijken.
