# Model Selection Guide

Which AI model to use for what — explained simply.

---

## The Short Version

For most work, just use **Opus** (the default in VS Code). It's the most capable model and handles everything well.

Only think about other models when:
- You're building something complex with multiple agents
- You're hitting usage limits
- You want to save costs on routine tasks

---

## The Models

| Model | Best For | Speed | Cost |
|-------|----------|-------|------|
| **Opus** | Strategy, planning, complex work | Slower | $$$ |
| **Sonnet** | Content writing, analysis, routine work | Fast | $$ |
| **Haiku** | Simple tasks, formatting, bulk work | Fastest | $ |
| **Gemini** | Research with large documents | Fast | $ |

---

## When to Use What

### Just Starting Out? Use Opus.

Opus handles everything — writing, planning, coding, analysis. For most marketing professionals, Opus alone is all you need.

### Building Something Complex?

When your project has multiple agents working together, match the model to the task:

| Task | Model | Why |
|------|-------|-----|
| Planning what to build | Opus | Needs complex reasoning |
| Writing blog posts | Sonnet | Good quality, faster, cheaper |
| Formatting data | Haiku | Simple task, very fast |
| Searching the web | Sonnet | Routine work, doesn't need Opus |
| Reviewing code | Opus or Sonnet | Needs judgment |

**Think of it like:** You don't send the CEO to make copies. Use the right person for the right job.

---

## The Hybrid Approach

For maximum efficiency, use Opus as the "brain" and cheaper models as "hands":

```
You (decide what to build)
└── Opus (plans and reviews)
    ├── Sonnet (writes content)
    ├── Haiku (does routine tasks)
    └── Sonnet (writes code)
```

This is called **tiered model architecture**. But don't set this up unless you actually need it.

---

## How to Set Model for an Agent

In your agent file (`.claude/agents/agent-name.md`), add `model` to the frontmatter:

```yaml
---
name: researcher
description: Web research specialist
model: sonnet
tools: ["WebSearch", "WebFetch", "Read"]
---
```

---

## Common Mistake

**Using Opus for everything in a multi-agent setup.**

If you have 4 agents all running Opus, you'll hit usage limits fast. Most routine tasks (web search, data formatting, file processing) work perfectly with Sonnet or Haiku.

**The rule:** Opus thinks. Cheaper models execute.
