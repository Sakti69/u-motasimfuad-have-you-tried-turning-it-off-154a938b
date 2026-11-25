#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes one funny line — under 200 characters — that a hopeless tech
support agent says to a desperate customer, to /output/entry.txt.

Three candidate lines were drafted; the shipped one is LINE. The other
two are kept below as a record of the choice, not written to the output:

  A (shipped): the agent admits the whole playbook was one step.
     The twist lands on "step one of one": the customer already did
     the one thing there was to do, and the agent's cheerful
     "Wonderful" / "congratulations" is the uselessness — he has
     nothing left, and he is delighted about it. The customer is
     never the butt; the agent's empty toolkit is.
  B (cut): the escalation loop — transfer to someone who repeats the
     same step. Real-agent phrasing, but the joke needs the customer
     to wait through a transfer; the turn arrives late and the line
     explains itself.
  C (cut): "do it slower, so it feels like we're actually fixing
     something." Funny, but the punch is the agent performing
     competence rather than admitting he has none; weaker twist.
"""

import os

LINE = (
    "Turning it off and on again didn't work? Wonderful \u2014 that was "
    "step one of one, so congratulations, we're both out of ideas."
)

# The other two candidates, kept for the record (not shipped):
CANDIDATE_B = (
    "Okay, let's try turning it off and on again \u2014 and if that "
    "doesn't work, I'll transfer you to someone who'll ask you to turn "
    "it off and on again."
)
CANDIDATE_C = (
    "Have you tried turning it off and on again? Great \u2014 now do it "
    "slower, so it feels like we're actually fixing something."
)


def main() -> None:
    text = LINE
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
