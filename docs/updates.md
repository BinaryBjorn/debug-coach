# Updates van Debug Coach

Een nieuwe versie van de coach komt altijd via de catalogus op GitHub: `BinaryBjorn/debug-coach`. Een update vervangt **enkel de coach** (de skills, de missies en de ladder). Wat van jou is, staat los ervan en wordt nooit geraakt.

## Wat een update nooit raakt

| Wat | Waar | Waarom het veilig is |
|---|---|---|
| Je profiel | `ik/` in je werkmap | De werkmap is jouw map, de coach staat er niet in |
| Je projecten | `projecten/` in je werkmap | idem |
| Feedback, successen, voortgang | `feedback.md`, `successen.md`, `voortgang.md` in je werkmap | idem; de coach vult ze enkel aan |
| Je eigen vaardigheden | de plugin `mijn-vaardigheden` (`.coach/mijn-vaardigheden/` in je werkmap) | Een aparte plugin uit je werkmappakket, niet uit de catalogus op GitHub |

**`mijn-vaardigheden` wordt nooit door een update geraakt.** Ze komt uit je eigen werkmap, niet uit `BinaryBjorn/debug-coach`. Upgrade je de coach, dan blijven je eigen skills (missie 7) staan zoals ze zijn. In Claude staan je eigen skills in `projecten/eigen-skills/` en onder Customize > Skills: ook die raakt een update niet.

Ook de start van de coach is veilig na een update: zeg je opnieuw "start", dan vult de coach enkel aan wat ontbreekt en overschrijft hij nooit een bestand dat er al staat.

## In ChatGPT (Work, desktopapp)

**De eerste keer: de coach toevoegen.**

1. Ga naar **Plugins > Add > Add a marketplace**.
2. Vul bij Source in: `BinaryBjorn/debug-coach`. Laat Git ref op `main`.
3. Onder het tabblad **Personal** verschijnt de catalogus `debug-marketing` met de plugin `debug-coach`. Installeer ze.

**Updaten.**

1. Open **Instellingen** (tandwiel, Manage) **> Plugins**, tabblad **Marketplace**.
2. Klik bij `debug-marketing` op **Upgrade**.
3. Klik daarna op **Refresh**: de lijst toont de nieuwe versie pas na Refresh.
4. Begin een nieuw gesprek in je werkmap. Zeg: start, of: volgende missie.

Klik niet op de prullenbak: die verwijdert de catalogus, en dan moet je ze opnieuw toevoegen. Ook dan blijven je werkmap en `mijn-vaardigheden` gewoon staan.

## In Claude (Cowork, desktopapp)

**De eerste keer: de coach toevoegen.** Ga naar **Customize > Plugins > Add marketplace** en vul `BinaryBjorn/debug-coach` in. Installeer de plugin `debug-coach`.

**Updaten.** Ga naar **Customize > Plugins**, kies de catalogus en klik op **Check for updates**. Wil je dat niet telkens zelf doen, zet dan **Sync automatically** aan. Begin daarna een nieuw gesprek in je werkmap.

## Voor wie de coach uitbrengt

- Een nieuwe versie gaat naar `main` van `BinaryBjorn/debug-coach`, met een hoger `version` in beide manifesten (`plugin/plugin.json` en `plugin/.claude-plugin/plugin.json`, altijd dezelfde waarde).
- De catalogus `.claude-plugin/marketplace.json` in de root wijst met `source: "./plugin"` naar de plugin; dat blijft zo, anders vinden ChatGPT en Claude de coach niet meer.
- Een nieuwe versie mag nooit een bestand in de werkmap van de gebruiker vervangen. Nieuwe templates komen er enkel bij als het bestand ontbreekt (de skill start).
