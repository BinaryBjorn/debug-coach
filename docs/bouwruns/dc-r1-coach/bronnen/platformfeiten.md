# Platformfeiten (onderzocht 15/10/2026, met bron per feit)

De bouwer heeft geen internet. Alles wat de missies en skills over ChatGPT en Claude beweren, komt uit dit bestand. Wat hier niet staat, beweert de coach niet (dan: "[TODO: nagaan]").

## ChatGPT

| # | Feit | Bron |
|---|---|---|
| C1 | De ChatGPT-desktopapp (macOS en Windows) heeft linksboven een keuze ChatGPT of Codex; onder ChatGPT bovenaan een schakelaar **Chat** of **Work**. Work is een agent voor langere taken en afgewerkte documenten, spreadsheets en presentaties. | help.openai.com/articles/20001275 (ChatGPT Work and Codex), release notes 09/07 en 16/07/2026 |
| C2 | In de desktopapp kan Work met je toestemming **een lokale map openen** en lokale bestanden en desktop-apps gebruiken. Op web en mobiel kan Work niet aan bestanden op je computer. | help.openai.com/articles/20001275 (FAQ "Can Work use files on my computer?") |
| C3 | **Plugins** (sinds 07/2026) bundelen skills en apps; installeren via **Plugins** in de zijbalk. Een plugin kan enkel skills bevatten. Gebruiken: automatisch als relevant, of met `@naam`. | help.openai.com/articles/20001256 |
| C4 | Een **lokale catalogus** in een map: `.agents/plugins/marketplace.json` in de geopende map (repo-catalogus); na herstart van de app verschijnt de catalogus in de Plugins Directory en kan je de plugin installeren. Vorm hieronder. Bewezen op Pro (proef 15/10, in Work). | developers.openai.com/plugins/build/plugins (sectie "Build your own curated plugin list", "Install a local plugin manually") |
| C5 | Portable pluginmanifest: `plugin.json` in de pluginmap met `$schema` `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`, `name` (kebab-case), `version`, `description`; skills worden ontdekt in `skills/<naam>/SKILL.md` (frontmatter `name`, `description`). | developers.openai.com/plugins/build/plugins |
| C6 | Een Claude-plugin met enkel skills kan bij OpenAI ingediend worden; productnamen in skills vervangen door neutrale taal ("het model"); `commands`, `hooks`, `userConfig` worden niet ondersteund. | developers.openai.com/plugins/guides/submit-claude-plugin |
| C7 | **Eigen GPT's** kunnen persoonlijke accounts (Free, Go, Plus, Pro) niet meer maken of publiceren; GPT's worden vervangen door plugins. | help.openai.com/articles/8798878 |
| C8 | **Projecten**: chats, bestanden en instructies samen; Plus: 25 bestanden per project, max 10 tegelijk uploaden; projectinstructies via ••• > Project settings. Gedeelde projecten gebruiken enkel projectgeheugen. | help.openai.com/articles/10169521 |
| C9 | **Training**: voor Free, Plus en Pro kan OpenAI gesprekken gebruiken om modellen te verbeteren als de instelling **"Improve the model for everyone"** aan staat (Instellingen > Data controls). | help.openai.com/articles/10169521 (FAQ), help.openai.com/articles/7730893 |
| C10 | **Audio uploaden** (sinds 06/10/2026, betaalde plannen): WAV, MP3, OGG, WebM (enkel audio), FLAC, AAC, M4A, MP4 (enkel audio), tot 512 MB; transcript, samenvatting, vragen, vervolgmail. | release notes 06/10/2026, help.openai.com/articles/8555545 |
| C11 | **Outlook Email/Calendar-apps**: acties vragen Microsoft-toestemming van een Entra-beheerder van de organisatie; een persoonlijk Hotmail-account is nergens bevestigd. | help.openai.com/articles/12512241 |
| C12 | **Computer Use** in de desktopapp met Work en Codex, macOS en Windows; op Windows werkt het in de voorgrond (het neemt muis en toetsenbord over), op macOS kan het op de achtergrond. Plugin "Computer Use" installeren; op macOS toestemming Schermopname en Toegankelijkheid. | developers.openai.com/codex/app/computer-use |
| C13 | Work kan taken uitvoeren op **websites waar je inlogt** in de ingebouwde browser (Plus en Pro); ChatGPT toont het inlogscherm, jij vult zelf in. | release notes ("ChatGPT Work can now complete tasks on signed-in websites") |
| C14 | **ChatGPT voor Word, Excel en PowerPoint**: een add-in via Microsoft Marketplace, op alle plannen. | release notes 17/09/2026 |
| C15 | Persoonlijke **Skills** in de zijbalk zijn algemeen beschikbaar voor Business, Enterprise, Edu; skills in een plugin uit een lokale catalogus werken (proef 15/10). | help.openai.com/articles/20001256 (FAQ), proef 15/10 |
| C16 | `AGENTS.md` in de geopende map wordt gelezen als projectbrein (KOMPAS-marker, twee keer bevestigd op het demo-account, 15/10). Bevestigd in Work via de plugin op Plus (ronde 3). | P1 |
| C17 | Plugins > Add biedt op Plus: Create plugin, **Add a marketplace**, Upload plugin archive, Add custom MCP server, Record a skill. Een lokale catalogus verschijnt onder het tabblad **Personal**; de lijst toont de pluginnaam (`name`). "Add a marketplace" aanvaardt een publieke GitHub-repo in het **Claude-formaat** (`.claude-plugin/marketplace.json`): met `BinaryBjorn/debug-coach` verscheen onder Personal de catalogus `debug-marketing` (naam uit het manifest) met de plugin `debug-coach`. Velden in het venster: Source, Git ref (standaard main), Sparse paths. Verwijderen of bijwerken: tandwiel (Manage) > Settings > Plugins > tabblad Marketplace: **Upgrade** en een prullenbak; de lijst werkt pas bij na **Refresh**. | P2, P2b, 15/10 |
| C18 | Missie 4 via Outlook.com in de ingebouwde browser werkt (proef P4, 15/10): de gebruiker logt zelf in, ChatGPT zoekt met een datumfilter (`received:<van>..<tot> "<onderwerp>"`) en bouwt een tijdlijn. Geopende mails krijgen de status gelezen. | P4 |
| C19 | Computer Use van ChatGPT mag de ChatGPT-app zelf niet bedienen ("not allowed to use the app 'com.openai.codex' for safety reasons"); op macOS werkt het op de achtergrond, dus de handelingen zijn niet zichtbaar in een schermopname. | P3, 15/10 |

### Vorm van `.agents/plugins/marketplace.json` (C4)

```json
{
  "name": "mijn-werkmap",
  "plugins": [
    {
      "name": "mijn-vaardigheden",
      "source": { "source": "local", "path": "./.coach/mijn-vaardigheden" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity",
      "interface": { "displayName": "Mijn vaardigheden" }
    }
  ]
}
```

`source.path` is relatief tot de map die `.agents/` bevat (de werkmap) en begint met `./`. De catalogusnaam is `mijn-werkmap` (botst niet met de GitHub-catalogus `debug-marketing`). De coach zelf staat niet in deze catalogus: die komt via GitHub (C17). De lijst toont `name`, niet `displayName`.

## Claude

| # | Feit | Bron |
|---|---|---|
| K1 | Cowork bestaat op desktop, web en mobiel; sinds 06/10/2026 draaien nieuwe Cowork-taken op Pro en Max standaard in de cloud. Lokale mappen werken enkel via de desktopapp. | support.claude.com/en/articles/15520349 |
| K2 | Plugin installeren in Cowork: **Customize > Plugins > Add marketplace**, met `owner/repo` of de GitHub-URL; updaten met **Check for updates** of **Sync automatically**. Geen `/plugin`-commando in Cowork. | claude.com/docs/cowork/guide/plugins |
| K3 | Claude-pluginmanifest: `.claude-plugin/plugin.json` (`name`, `description`, `version`, `author`); catalogus `.claude-plugin/marketplace.json` met `plugins[].source`. | huidige repo `debug-coach` (fase 1), gevalideerd met `claude plugin validate` op 15/10 |
| K4 | De Microsoft 365-connector van Claude werkt enkel met een werkaccount (Entra) en vraagt eenmalige toestemming van een Global Administrator. | support.claude.com/en/articles/12542951 |
| K5 | Het formulier (`show_widget`) in Cowork is niet officieel gedocumenteerd en hangt volgens gebruikersmeldingen soms; vragen in de chat zijn de standaard, het formulier een extra. | onderzoek 15/10 |
| K7 | Eigen skills in Claude (Free, Pro, Max): **Customize > Skills > Upload a skill**, een ZIP van de skillmap (mapnaam = skillnaam, `SKILL.md` erin); daarna aan/uit te zetten. Een skill **opnemen** kan op Pro, Max en Team in Cowork op de Mac. | support.claude.com/en/articles/12512180, /12512198 |
| K8 | Claude Computer Use (Claude-desktopapp, tabblad Code) kan de ChatGPT-app bedienen en tegelijk met `screencapture -v -R<x,y,b,h>` enkel het ChatGPT-venster opnemen; klikposities binnen 2 punten exact. Het recht Schermopname moet naar de ingebouwde Claude Code-app (`~/Library/Application Support/Claude/claude-code/<versie>/.../claude.app`), niet enkel naar Claude.app; na een update mogelijk opnieuw. De video start ±0,29 s na het commando: meten aan de eerste beeldwissel. Een zwevend Claude-paneel kan over het venster liggen: buiten het opnamegebied houden. | P5, 15/10 |
| K6 | Een skill uit een plugin met beide manifesten draait in Claude Code met `--plugin-dir` (proef 15/10). | proef 15/10 |
