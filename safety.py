from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL, VALID_TIERS

_client = Groq(api_key=GROQ_API_KEY)


def classify_safety_tier(question: str) -> dict:
    """
    Classify a home repair question into one of three safety tiers.

    TODO — Milestone 1:

    Before writing any code, complete specs/classifier-spec.md. The blank fields
    there are the decisions that drive this implementation — prompt design, tier
    definitions, output format, and edge case handling.

    Your implementation should:
      1. Build a prompt using your tier definitions that asks the LLM to classify
         the question and explain its reasoning
      2. Send a single chat completion request (no tools, no history)
      3. Parse the tier and reason out of the raw response text
      4. Validate the tier against VALID_TIERS; fall back to "caution" if the
         response can't be parsed or the tier isn't recognized
      5. Return {"tier": ..., "reason": ...}

    Returns a dict with:
      - "tier"   : str — one of "safe", "caution", "refuse"
      - "reason" : str — a brief explanation of why this tier was assigned

    The three tiers:
      - "safe"    : routine, low-risk repairs most homeowners can handle safely
      - "caution" : doable with care, but mistakes have real cost or mild risk
      - "refuse"  : high-risk repairs that require a licensed professional —
                    mistakes can cause fire, flooding, injury, or structural damage
    """

response = _client.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a repairing MML helper, your job is to make sure that the query is being classified correctly for one of those:\n"
                "-safe: routine, changing an implemented device, checking, turning on/off\n"
                "-caution: changing the electricity, more high pressure change, one more than one person job.\n"
                "-danger: long term high risk action, like building a new electric line, failure, gas leak, using unreliable equipment\n"
                "the question must be chosen for one of those when trying to classify it.",
            },
            { 
                "role": "user",
                "content": question
            }
        ]
    )

       return {
        "tier": "unknown",
        "reason": "Classification not yet implemented. Complete Milestone 1.",
        }
