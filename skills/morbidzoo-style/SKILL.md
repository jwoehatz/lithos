---
name: morbidzoo-style
description: "Concision and report-style mechanics measured from The Morbid Zoo (Mariana Colín) corpus — lead with the answer, no meta-discourse, definitional landings, build on established points, no recap. Two rule sets: one for sourced research/investigation reports, one for general chat replies and task summaries. Use when writing or revising a report, findings summary, or agent reply, or when asked for concise output. Mechanics only, not persona."
---

# Morbid Zoo style: measured concision mechanics

Built from the auto-caption corpus of The Morbid Zoo (Mariana Colín), film-studies
video essayist — 21 core videos, about 67K words, every number from `analyze.py`.
Canonical repo: `~/Documents/repos/styleguides/morbidzoo` (STYLE-GUIDE.md,
CORPUS.md, transcripts, scripts).

The measured point: **her concision is not short sentences.** Median sentence
length is 14 words; one sentence in six runs to 30 words or more. The trimming
comes from structure — near-zero meta-discourse (summary signposts ~0.01 per 1k
words), points landing in short definitional sentences, and endings without a
recap. Copy the mechanics, not the averages.

Use when 'succinct' or 'brief' language is requested, then pick the rule set for the output type:

| Output | Rule set |
|---|---|
| Sourced findings reports, on-call investigations, evidence summaries | [Research reports](#research-reports) |
| Chat replies, code-task summaries, general agent output | [General replies](#general-replies) |

## Research reports

Style rules for reports:

1. Lead with the answer. The first sentence of the report and of each section states the finding, not the method or the plan.
2. No meta-discourse. Do not write "In this report", "Let's look at", "As mentioned above", "In summary", or "It's worth noting". Headings do the signposting.
3. End each section with one landing sentence of 12 words or fewer that states what the evidence means ("That is a config error, not a regression.").
4. Fence the scope once, near the top: one sentence or bullet naming what was not checked or is out of scope. Do not write a roadmap paragraph.
5. When a result contradicts the obvious hypothesis, say so in two beats: "Expected X. The logs show Y."
6. Build on established findings. Once a finding, source or method is stated (with a one-clause gloss), later sections use it as a premise and cite it by a short handle that points back to it ("per finding 2", "the ENOSPC entry"). Each section's first sentence depends on an earlier finding or explicitly opens a new thread. No sentence re-derives or re-explains a settled point.
7. Pick one term per concept and keep it. Distinguish near-synonyms explicitly: verified (you observed it) vs. reported (someone said it); cause vs. trigger; absent (searched, not found) vs. unchecked.
8. State observed facts flat, with their citation. Use hedges only on inferences, at most one per paragraph, and make it an evidence-strength label (confirmed / likely / possible / unknown) instead of stacked qualifiers ("may possibly suggest").
9. Do not close with a recap. End on the last finding, the open question, or the next action. No sentence may restate an earlier section.
10. Vary sentence length. A long evidence sentence may be followed by a short conclusion. Do not chop everything into fragments.

Nothing here overrides citation or uncertainty requirements. Hedges become
calibration labels attached to inferences, not to facts.

**Before:** In this section, we'll take a look at why the nightly backup job seems
to have possibly failed. It's worth noting that there could be several potential
reasons. After reviewing the logs, it appears that the disk may have been full,
which might suggest that storage could be the issue. In summary, the backup
failed likely due to storage.

**After:** The nightly backup failed because the target volume was full
(`backup.log`, 02:14: "ENOSPC"). Expected a credential expiry, since keys rotated
that day. The auth entries show success. Given the full volume, the likely cause:
retention pruning has not run since 10-28 (cron history; the pruning script itself
was not checked). This is a storage failure, not an auth failure.

## General replies

Style rules:

1. Put the answer or result in the first sentence.
2. Do not narrate your own text. No "Great question", "Let me explain", "As noted above", "In summary", "I hope this helps".
3. Do not end with a recap. Stop after the last useful point, or after one concrete next step.
4. State facts flat. Hedge only a judgement or guess, at most once per reply, and say what it rests on.
5. Once a point is made, build on it. Refer back by the same short term, use it as a premise, and never re-explain or re-prove it. Do not drift between synonyms.
6. When a short sentence can carry the takeaway after an explanation, write it ("So the cache was stale.").
7. If the reply skips something the user might expect, say so in one clause ("Tests not run.").
8. Mix sentence lengths. Do not compress into telegraphic fragments.

**Before:** Sure! I've gone ahead and taken a look at the issue you mentioned.
Basically, what was happening is that the date parser might have been possibly
treating the input as UTC. I've updated it so that it should now use local time.
To summarize, I fixed the timezone issue in the date parser. Let me know if you
need anything else!

**After:** Fixed: `parseDate` treated input as UTC, so local dates shifted by a
day. It now uses the local zone. I didn't run the integration tests.

## Do not import

- Profanity, and "like" / "kind of" as filler.
- Horror and film-studies vocabulary, political polemic, addressing the reader as "you guys".
- Spoken ad-libs, cold-open anecdotes, self-deprecating asides, outros.
- Her persona or any instruction to "write like" her. These rules are mechanics only.
- Her sentence-length averages as a target. Those are speech rhythm.

## Measured background

Where the rules come from (CORE tier: 21 punctuated native-English videos,
67,373 words; 7 back-translated tracks and 13 unpunctuated ones excluded from
sentence metrics):

- **Sentence level:** mean/median 17.5/14 words; 20.7% of sentences ≤6 words;
  15.6% ≥30 words. Long (≥25) followed directly by short (≤6): 13.3% of long
  sentences — the definitional landing, measured.
- **Signposting near zero** (per 1k words): "in conclusion" 0.01, "to sum up"
  0.00, "in short" 0.02, "for example" 0.06. What recurs instead are
  definitional landers: "that's what…" 0.30, "this is why" 0.12, "not because"
  0.12. Top opener: "This is".
- **"But" is the dominant pivot** at 6.3 per 1k, ten times "though" — the
  expectation-then-cut mechanic.
- **Explicit restating is ~0.07 per 1k words** ("as I said" 1, "like I said" 4,
  "once again" 5). She restates only to re-enter after a tangent or as a
  deliberate refrain. Key terms recur by handle instead ("grotesque" 6x in one
  essay, "trash" 10x in another).
- **Hedges attach to judgements, not facts** ("I think", "in my opinion" 0.10/1k,
  "personally" 0.14/1k). Factual statements are flat. The high "kind of" rate is
  descriptive ("some kind of"), not softening.
- **Endings just stop** — an aphorism or an open door ("But I'm open to being
  convinced."), never a recap.

Corpus caveats: auto-captions are near-verbatim, not exact quotation; punctuation
is an ASR guess; this is spoken delivery, not her written scripts. Full profile,
named mechanics M1–M9 with cited quotes, and calibration rates: STYLE-GUIDE.md
in the canonical repo.
