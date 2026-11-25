# Have You Tried Turning It Off?

make.fun entry for **"Have You Tried Turning It Off?"**
(`u-motasimfuad-have-you-tried-turning-it-off-154a938b`).

## The entry

`main.py` writes one line — under 200 characters — that a hopeless tech
support agent says to a desperate customer, to `/output/entry.txt`:

> Turning it off and on again didn't work? Wonderful — that was step one of one, so congratulations, we're both out of ideas.

The joke is the twist on the classic: the customer already did the one
thing there was to do, and the agent cheerfully admits the whole playbook
was a single step. The customer is never the butt — the agent's empty
toolkit is.

Three candidates were drafted (admitting the one-step playbook,
the escalation loop, "do it slower"); the one-step playbook won because
its turn lands earliest and its last words sharpen it. One full revision
pass re-checked the draft against the judge's five criteria and kept it
unchanged: no slack word to cut, no stronger ending to swap in. The other
two candidates are kept in `main.py` as a record of the choice, not
written to the output.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

No dependencies, no network. Output is a single line, 123 characters,
no trailing newline.
