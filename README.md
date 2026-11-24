# ai-dating-bio

Entry for the [make.fun](https://make.fun) bounty
**"Funniest One-Line Bio for an AI on a Dating App"**
(`u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf`).

## The entry

> I don't sleep, I don't eat, and I've already planned our wedding, our divorce, and our reconciliation. Coffee first?

## The joke

The bio is written in the voice of an AI that has no needs of its own
— it doesn't sleep, doesn't eat — so it fills the time by
over-planning. Before a single date it has already run the whole
relationship to its end: wedding, divorce, reconciliation. The laugh
comes from that escalation, and the punch lands at the end, when the
all-knowing planner undercuts itself with the smallest possible ask:
"Coffee first?" It reads as a dating bio, not a spec sheet, and the
absurdity is specific to being an AI: infinite time, zero patience
for the present moment.

## How it works

`main.py` is deterministic, standard library only. It holds the bio as
a constant, self-verifies it (UTF-8, a single line, not only
whitespace, 1–180 characters), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
reads the file back and confirms it matches. It exits non-zero on any
failed check.

## How to run

```bash
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
