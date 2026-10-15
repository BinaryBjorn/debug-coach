%% Bevroren bij het tekenen. %%

| Feature | Wat de check bewijst | Wat hij níet bewijst (voor de keurder) |
|---|---|---|
| D01 | De regel voor een nieuwe start staat in start | Dat het model ze volgt: keurder speelt `start` na op een vers pakket (`python3 scripts/bouw_werkmap.py`) |
| D02 | De regel "niets in dezelfde beurt" en de verbeterstap staan in missie en uitdaging | Gedrag: keurder speelt missie 2 na en kijkt of de coach wacht |
| D03 | Elke routestap heeft Jij/De coach | Of de verdeling klopt |
| D04 | Bevestigingsregel, menupad missie 7, opnieuw uploaden bij niveau 3 | Gedrag bij "ik vind de knop niet" |
| D05 | Feedbackvragen en letterlijkheid | Gedrag: keurder rondt een missie af en kijkt of de rij pas na het antwoord komt |
| D06 | Uitlegregel per stand | Toon |
| D07 | Geen link tussen backticks | |
| D08 | Vraag-eerst en geen technische waarden | |
| D09 | Kopiëren en plakken in missie 3 | |

Basistest `python3 tests/regressie.py`: BASIS, C01 tot C13 en V01 tot V08 moeten groen blijven (bij de start groen; C01 werd bij het aanvaarden van R1 opgelost).
