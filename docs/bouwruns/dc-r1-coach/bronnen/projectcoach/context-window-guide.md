# Understanding the Context Window

The most important thing to know about working with Claude Code.

---

## What Is the Context Window?

Every AI has a working memory limit called the "context window." It's the total amount of text Claude can hold in mind during a conversation.

**Think of it like:** A desk. The bigger the desk, the more papers you can spread out. But once it's full, things start falling off.

---

## What Fills the Context Window

| What | How Much Space |
|------|---------------|
| Your messages | Some |
| Claude's responses | Some |
| Files Claude reads | A lot |
| CLAUDE.md (loaded every session) | Always loaded |
| Rules (`.claude/rules/`) | Always loaded |

The longer the conversation, the fuller the window gets.

---

## What Happens When It's Full

1. Claude starts giving more generic answers
2. It may "forget" earlier instructions
3. It may ignore your brand voice or context files
4. Quality drops silently — you might not notice right away

**Think of it like:** A brainstorm session at hour 5. Everyone's tired, repeating themselves, and missing details.

---

## How to Manage Context

### `/clear` — Start Fresh

Resets the conversation. Your files stay, but the conversation is gone.

**When:** Between tasks. Every time. Make it a reflex.

**Think of it like:** Erasing the whiteboard between meetings.

### `/compact` — Summarize and Continue

Claude summarizes the conversation so far and continues with the summary. You keep progress but free up space.

**When:** Mid-task, when the conversation is getting long but you're not done yet.

**Think of it like:** Meeting minutes — instead of replaying the full 2-hour meeting, everyone reads the summary and keeps going.

### `/rewind` — Go Back in Time

Rolls back to a previous point in the conversation. Your files stay as they are.

**When:** Claude took a wrong turn and you want to try a different approach.

**Think of it like:** Ctrl+Z for your conversation.

---

## The Golden Rule

**One task = one conversation.**

Write a post → `/clear` → Plan a calendar → `/clear` → Analyze data.

If a task runs long, use `/compact` to make space. If Claude goes wrong, use `/rewind` to undo.

---

## Context Window Tips

1. **Keep CLAUDE.md short** — It loads every session. Under 200 lines (official target).
2. **Don't paste huge documents into chat** — Put them in files, let Claude read them.
3. **Be concise** — Short, clear messages use less context than long, rambling ones.
4. **Use context files** — Instead of explaining your brand every time, put it in a file.
5. **Watch for quality drops** — If Claude starts giving generic answers, it's time for `/clear` or `/compact`.
