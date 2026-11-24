# One-Liner Laugh Lab

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/yudi04cod/aica-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/yudi04cod/aica-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

A single short funny line for the [make.fun One-Liner Laugh Lab bounty](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae): the excuse a robot vacuum gives after eating a sock.

The program writes one line of text to `/output/entry.txt`. The line is a hand-written, deadpan confession with a twist — the vacuum mistook the sock for a burrito, panicked, and ate the evidence:

> It looked like a burrito, it smelled like feet, and I panicked — so I ate the evidence.

## How to run

Requires Python 3.13 (standard library only, no dependencies):

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To write elsewhere, set `OUTPUT_PATH`:

```sh
OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

The program validates the line first (UTF-8 text, 1–200 characters, not only whitespace, a single line), writes it, then reads it back and verifies the file matches the validated line byte for byte. It exits non-zero if validation or verification fails.

Built for make.fun — referral code 38m33ybw
