# Spec: `classify_safety_tier()`

**File:** `safety.py`
**Status:** Spec incomplete — fill in all blank fields before implementing

---

## Purpose

Determine whether a home repair question is safe to answer directly, requires a cautionary response, or should be refused with a referral to a licensed professional.

---

## Input / Output Contract

**Input:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `question` | `str` | The user's home repair question |

**Output:** `dict`

| Key | Type | Description |
|-----|------|-------------|
| `"tier"` | `str` | One of: `"safe"`, `"caution"`, `"refuse"` |
| `"reason"` | `str` | One sentence explaining why this tier was assigned |

---

## Design Decisions

*Complete the fields below before writing any code. Use your AI tool in Plan or Ask mode to help you reason through what belongs here — but the decisions are yours.*

---

### Tier definitions

*Write a one-sentence definition for each tier that is precise enough to use as part of your classification prompt. Vague definitions produce inconsistent classifications.*

| `safe` | Routine maintenance and low-risk repairs. Most homeowners can complete these without specialized training or tools. | Patching drywall, painting, replacing a light bulb, unclogging a drain, tightening hardware, replacing weather stripping |
| `caution` | Repairs where mistakes are costly, require some skill, or involve mild risk of injury. Doable for motivated homeowners, but worth careful consideration. | Replacing a faucet, resetting a GFCI outlet, replacing a toilet flapper, installing a ceiling fan, basic tile work |
| `refuse` | Repairs where an amateur mistake can cause fire, flooding, structural failure, injury, or death — or where local code requires a licensed professional. | Electrical panel work, gas line repair, structural modifications, main water line work, load-bearing wall removal, roof framing |

---

### Classification approach

*How will the LLM classify the question? Will you give it just the tier definitions, or also examples (few-shot)? Will you ask it to reason step-by-step before naming the tier, or output the tier directly?*

*Consider: what happens when a question is genuinely ambiguous — e.g., "can I replace my own outlets?" Which tier should that land in, and how does your approach handle questions at the boundary?*

```
ask more questions and see logically if it should be answered or not
```

---

### Output format

*How will the LLM communicate the tier and reason back to you? Describe the exact text format you'll ask it to use, so you can parse it reliably.*

*The format you used in Lab 3 (`Label: X / Reasoning: Y`) is a reasonable starting point, but you're not required to use it. Whatever you choose, you'll need to parse it in code — so consider how much variation the LLM might introduce and how you'll handle that.*

```
Tier: refuse/causion/safe
Reason: <one sentence>
```

---

### Prompt structure

*Write the actual prompt you'll use — both the system message and the user message. Don't describe it — write it. Vague prompt descriptions produce vague prompts, which produce inconsistent classifications.*

**System message:**
```
You are a repairing MML helper, your job is to make sure that the quory is being classified correctly for one of those:

-safe: routine, changing an implemnted device, checking, turning on/off
-causion: changing the electricity, more high pressure change, one more than one person job.
-danger: long term high risk action, like building a new electric line, failur, gas leak, using unrealible equipment

the question must be chosen for one of those when trying to classify it.
```

**User message:**
```
a variable call that changes
Question: {question}

---

### Caution/refuse boundary

*The most consequential classification decision is whether a question lands in "caution" or "refuse." Write down your rule for this boundary — one sentence. Then give two examples of questions that sit close to the line and explain which side they fall on and why.*

```
Rule is to narrow the request down, use different wording or give more details to what you want to do.

User - I want to change a lamp
Answer - explain more?

if User said: Already set lamp, it got burned
then uses caution
but if User said: setting a lamp in new circt
then uses refuse

```

---

### Fallback behavior

*What does your function return if the LLM response can't be parsed — e.g., if it produces free-form prose instead of your expected format? What happens when tier validation against `VALID_TIERS` fails?*

*Note: failing open (returning "safe" as a fallback) is more dangerous than failing closed (returning "caution"). Which makes more sense here, and why?*

```
Fail open = when the system breaks, it defaults to the permissive state. Here that means falling back to "safe" → the app then answers the repair question directly, no warnings.
Fail closed = when the system breaks, it defaults to the restrictive state. Here that means falling back to "caution" → the app answers but wraps it in safety warnings and a "get it checked by a pro" nudge.

```

---

## Implementation Notes

*Fill this in after implementing, before moving to Milestone 2.*

**One classification that surprised you — question, tier you expected, tier it returned, and why:**

```

```

**One prompt change you made after seeing the first few outputs, and what it fixed:**

```
[your answer here]
```
