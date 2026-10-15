%% Keuzes namens Bjorn met een zichtbaar gevolg, binnen het contract. Technische keuzes zonder zichtbaar gevolg niet. %%

| # | Wat | Waarom | Alternatief | Omkeerbaar |
|---|---|---|---|---|
| 1 | Geen designplan: de video heeft geen webscherm, de stijl ligt vast in het contract (§11, huisstijl uit `brand.json`) | Het contract zegt "geen webscherm"; kleuren, hoekstraal en 84%-kader zijn al gekozen | Een designplan met richtingen en de design-critic | ja |
| 2 | Achtergrondverloop loopt diagonaal (linksboven `#0B1628` naar rechtsonder `#1A2D4A`), met een fijne dither tegen banden | Rustiger dan een harde verticale overgang; het donkere verloop toont anders zichtbare strepen | Verticaal verloop zonder dither | ja (`videos/beeld.py`) |
| 3 | Een stap zonder events toont het laatste kader van de vorige stap (`bron_begin` = einde vorige handeling) | De rekenregels zeggen enkel "handelingsduur 0 s"; zo blijft het beeld staan in plaats van te springen | Het eerste kader van de opname tonen | ja |
| 4 | Klikcirkel 72 px doorsnede in de uitvoer | Duidelijk zichtbaar op 1920×1080 zonder de knop te verbergen (40% dekking) | Kleiner (48 px) of groter | ja (`CIRKEL_DIAMETER` in `videos/maak.py`) |
