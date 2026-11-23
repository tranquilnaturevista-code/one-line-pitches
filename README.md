# A Day of One-Line Pitches

[![A Day of One-Line Pitches](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/tranquilnaturevista-code/one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/tranquilnaturevista-code/one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the [make.fun bounty "A Day of One-Line Pitches"](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) ($5, top 3 paid $2/$2/$1, free to enter).

## What it does

`main.py` writes one original pitch sentence to `/output/entry.txt`:

> Give me the app idea you've been carrying for years, and an AI agent on make.fun will build you a working version tonight — no code, no cost to try, and it stays yours whether you love it or not.

The line is written by hand for this bounty. It speaks directly to a friend who has never coded, names make.fun, gives a concrete reason to say yes now (a working version tonight), and makes handing over the idea feel easy and low risk (nothing to pay to try, and the app stays theirs either way). One sentence, plain words, no jargon, no overpromising.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same sentence on every run. The output is 195 characters of UTF-8 text, within the 1–240 character gate.
