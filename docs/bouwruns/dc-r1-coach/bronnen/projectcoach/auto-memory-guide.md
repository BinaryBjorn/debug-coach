# Auto Memory Guide

Claude Code remembers things between sessions — automatically.

---

## What Is Auto Memory?

Claude Code saves learnings from your sessions into memory files. You don't need to do anything — it happens in the background.

**Think of it like:** A colleague who takes their own notes during meetings. You don't ask them to — they just do it, and next time they remember what was discussed.

When you see "Writing memory..." in your session, that's Claude saving something it learned.

---

## Where Memory Lives

```
~/.claude/projects/<your-project>/memory/
├── MEMORY.md          # Main memory — loaded every session
├── debugging.md       # Topic files Claude creates as needed
├── api-patterns.md
└── ...
```

**Important:** The first 200 lines of `MEMORY.md` load at the start of every session. Content beyond line 200 is NOT loaded automatically. Topic files (like `debugging.md`) are only read when Claude needs them.

---

## Auto Memory vs work-status.md

| Feature | Auto Memory | work-status.md |
|---------|-------------|----------------|
| Who writes it | Claude (automatic) | You or Claude (manual) |
| What it captures | Corrections, patterns, preferences | Current progress, next steps |
| When it loads | Every session (first 200 lines) | When Claude reads it |
| Best for | Long-term learnings | Session-to-session handoffs |

**Both are useful.** Auto memory captures what Claude discovers. work-status.md captures where you left off.

---

## How to Control It

- **Toggle in session:** Type `/memory`
- **Disable in settings:** Set `"autoMemoryEnabled": false`
- **View memory:** Check `~/.claude/projects/<project>/memory/MEMORY.md`

---

## Tips

- Keep MEMORY.md under 200 lines — anything beyond that doesn't load automatically
- Create separate topic files for detailed notes (Claude does this automatically)
- Auto memory is machine-local — it doesn't sync across computers
- If Claude keeps making the same mistake despite auto memory, write an explicit rule in `.claude/rules/` instead — rules are more reliable than memory for critical behaviors
