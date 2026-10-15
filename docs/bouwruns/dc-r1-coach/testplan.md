%% Bevroren bij het tekenen. %%

## Wat getest wordt

Elke check is `python3 tests/feature.py <ID>`: het draait de tests in `tests/` waarvan de naam het ID bevat en faalt als er nul liepen.

| Feature | Wat de check bewijst | Wat hij níet bewijst (voor de keurder) |
|---|---|---|
| C01 | Indeling, manifesten gelijk, catalogus wijst naar `./plugin` | Dat beide apps de plugin laden (P1, gesimuleerde beginner) |
| C02 | Alle templates en de verplichte regels/kolommen | Toon van de templates |
| C03 | `start` bevat elke verplichte stap en zin | Gedrag: keurder speelt `start` na op `werkmap-leeg/`, `werkmap-vreemd/` en `werkmap-missie7/` (geen overschrijving) |
| C04 | Formaat exact, taalregels, de drie herziene missies | Juistheid tegen `bronnen/platformfeiten.md` en `missies-brief.md`: keurder |
| C05 | Route-, afrond- en schrijfregels staan er | Gedrag: keurder speelt missie 2 na op `werkmap-missie7/` (chatgpt, persoonlijk) en missie 3 op `werkmap-claude-werk/` |
| C06 | Aantal en vorm van foutpunten | Of de oplossingen kloppen |
| C07 | Niveaus, regels, logformaat | Gedrag: keurder vraagt drie uitdagingen na elkaar op `werkmap-missie7/` |
| C08 | Standregel, uitlegvorm, waarschuwingsregel | Toon per stand |
| C09 | Links volgen de fixture, zin zonder code letterlijk, hash klopt | Dat R3 ze aanvaardt (T06) |
| C10 | Template-enkel-als-ontbreekt, geen overschrijfinstructies, update-doc met Upgrade, Refresh, Check for updates | Het echte updaten na de verhuis naar `plugin/` (na de keten op het demo-account) |
| C11 | Schema's, opnameopdracht voor Claude Computer Use, gitignore | De echte opname op de mini (na de keten) |
| C12 | Pakket compleet, `mijn-vaardigheden` met catalogus, coach niet in het pakket, zip bestaat | Dat Work `mijn-vaardigheden` oppikt (na de keten, zoals P1) |
| C13 | README dekt beide installaties, geen slash-commando | Leesbaarheid |

## Dummydata

`tests/fixtures/`: `werkmap-leeg/`, `werkmap-vreemd/` (twee losse bestanden), `werkmap-missie7/` (fictieve accountmanager bij een fictief installatiebedrijf, drie dossiers, vijf successen, ladder op trede 2, chatgpt, persoonlijk, coachcode `ab12cd34`), `werkmap-claude-werk/` (claude, werk, code `[TODO]`), `gedeeld/` (de vier gedeelde formaten). Geen echte namen of adressen.

## Basistest

`python3 tests/feature.py BASIS`: lekcheck op `plugin/`, `videos/`, `README.md` (weigert `hotmail.com`-adressen en woorden waarvan de sha256 op de lijst in de test staat: de naam van de proefgebruiker en van zijn werkgever; de namen zelf staan niet in de openbare repo), alle JSON in `plugin/` en `videos/` geldig, sha256 van `tests/fixtures/gedeeld/*` gelijk aan de waarden in `tests/gedeeld.sha256`. Regressie, geen features: groen bij de start.
