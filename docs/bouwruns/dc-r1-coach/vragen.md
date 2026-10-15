%% Vragen blokkeren nooit. Elke vraag heeft de vier velden; zonder standaardkeuze is het geen wachtrijvraag maar een stopvraag (master §6). %%

## V1 · De hook blokkeert .claude-plugin
**Vraag:** mag de hook voor beschermde paden `.claude-plugin/` doorlaten en enkel `.claude/` beschermen?
**Waarom het ertoe doet:** C01 vraagt om het oude `.claude-plugin/plugin.json` in de root te wissen, en de hook weigert elk schrijfcommando op dat pad. Latere features kunnen ook aan `.claude-plugin/marketplace.json` raken (via Edit lukt dat wel).
**Toegepaste standaard:** C01 op geblokkeerd; het bestand blijft staan; de hook niet omzeild.
**Bij een ander antwoord verandert:** één `git rm` en C01 is klaar.
