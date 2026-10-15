# The Delegation Mindset

The most important shift for working with Claude Code effectively.

---

## The Key Insight

Claude Code is not a chatbot. It's a **junior team member** you delegate work to.

The difference matters:

| Chatbot Thinking | Delegation Thinking |
|-----------------|---------------------|
| "Answer my question" | "Do this task for me" |
| "Give me ideas" | "Create this deliverable" |
| "Help me think" | "Research this and report back" |
| "What should I do?" | "Here's the goal, figure out the steps" |

---

## How to Delegate Well

### 1. Give Clear Briefs

**Bad:** "Help me with social media"
**Good:** "Write 3 LinkedIn posts about our new product launch. Casual tone. Each under 200 words. Include a call-to-action."

**Think of it like:** Briefing a freelancer. The clearer the brief, the better the output.

### 2. Provide Context Once, Reference Forever

Instead of explaining your brand voice every time:
1. Put it in `.claude/context/brand/voice.md`
2. Claude reads it automatically when relevant

**Think of it like:** You don't re-explain company values to every employee every morning. They know where to find the handbook.

### 3. Break Big Tasks into Steps

**Bad:** "Build me a complete content calendar system"
**Good:** "Let's start with a skill that writes weekly LinkedIn posts. We'll add more channels later."

**Think of it like:** You don't ask a new hire to overhaul the entire marketing strategy on day one.

### 4. Review Before Accepting

Always read what Claude creates before accepting it. It's fast but not perfect.

**Think of it like:** You'd review a junior's work before publishing it. Same principle.

### 5. Use the Right Tool for the Right Job

| Task | Best Approach |
|------|--------------|
| Something you do repeatedly | Create a skill |
| A routine automated task | Create an agent |
| Information Claude should always know | Create a context file |
| A behavior that should always apply | Create a rule |

---

## The Delegation Workflow

```
1. Brief     → Tell Claude what you need (clear, specific)
2. Watch     → Let Claude work (it reads files, searches, creates)
3. Review    → Check the output (don't auto-accept)
4. Iterate   → Give feedback if needed ("make it shorter", "wrong tone")
5. Save      → Update work-status.md before ending
```

---

## Common Delegation Mistakes

| Mistake | Fix |
|---------|-----|
| Being too vague | Be specific about format, length, tone, goal |
| Micromanaging every step | Give the goal, let Claude figure out the steps |
| Never giving feedback | "This is too formal" helps Claude adjust |
| Expecting perfection first try | Iteration is normal. First draft → feedback → final. |
| Not saving progress | Always update work-status.md |
