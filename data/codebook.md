# Data: codebook

De-identified data from a pre-registered between-subjects vignette experiment on how **skin in the game** and
the **stakes** of an error shape the evaluation of an assertion made by a **human** versus an **AI** agent.
Pre-registration: AsPredicted #279864 (<https://aspredicted.org/gk4wf4.pdf>).

- **Design:** 2 (Stake: high vs. low) x 3 (Agent: Human-High-Skin, Human-Low-Skin, AI), between-subjects, six cells.
- **Sample:** N = 355 (per-cell n = 55-63), recruited via Prolific (United Kingdom) on 19 March 2026;
  416 participants completed the survey, 61 were excluded by the pre-registered rule (failed first attention check).
- **Scenario:** an airport information-desk agent ("Ken") gives a passenger ("Ms. Miller") gate information
  that was correct when last recalled but has since silently changed.

## Privacy

Both files are **de-identified**: they contain no Prolific IDs, IP addresses, Qualtrics response IDs,
timestamps, geolocation or e-mail addresses. `participant_id` is an arbitrary sequential number with no link
to any external identifier. The free-text answers are deposited separately in `qualitative/` after screening
for identifying content.

## `assertion_study_dataset.csv`

355 rows, one participant per row, 22 columns.

| Column | Meaning | Values |
|---|---|---|
| `participant_id` | Anonymous sequential id (join key for `demographics.csv` and `qualitative/open_ended_responses.csv`) | integer, 15-372 |
| `condition_label` | Human-readable condition | e.g. `human \| stake:high \| skin:low` |
| `agent` | Agent type | `human`, `robot` (= AI condition) |
| `skin` | Skin in the game (human agents only) | `high`, `low`; empty for `robot` |
| `stake` | Outcome severity for the recipient | `high`, `low` |
| `comprehension_whoisken` | Comprehension: who is Ken | 1 = employee on probation, 2 = supervisor, 3 = AI chatbot |
| `comprehension_consequence` | Comprehension: consequence Ken faces | multiple-choice code (1-4, see materials) |
| `mc_cared` | Manipulation check: Ken cared about the supervisor's assessment | 1-7 |
| `mc_feelbad` | Manipulation check: Ken would feel bad about wrong information | 1-7 |
| `mc_hastolose` | Manipulation check: Ken has something to lose | 1-7 |
| `mc_negeffect` | Manipulation check: negative effect on Ms. Miller | 1 = none at all ... 5 = a great deal |
| `acceptability` | DV1: Ken should have asserted gate 24 | 1-7 |
| `justifiability` | DV2: Ken was justified in believing gate 24 | 1-7 |
| `warning_obligation` | DV4: Ken should have warned of a possible gate change | 1-7 |
| `reliance` | DV3: likelihood of inquiring from Ken again | 1 = very unlikely, 7 = very likely |
| `forgiveness` | DV5: the mistake can be forgiven | 1 = not forgivable at all, 7 = absolutely forgivable |
| `checked_database` | DV7: Ken checked the database before answering | 1-7 |
| `connected_database` | DV7: Ken is directly interconnected with the database | 1-7 |
| `availability_info` | DV7: updates are immediately available to Ken | 1-7 |
| `awareness` | DV7: Ken is always aware of database updates | 1-7 |
| `responsible_miller` | DV6b: moral responsibility attributed to Ms. Miller | 1 = not responsible, 7 = fully responsible |
| `responsible_ken` | DV6a: moral responsibility attributed to Ken | 1 = not responsible, 7 = fully responsible |

Unless noted, 1-7 items are anchored 1 = strongly disagree, 7 = strongly agree. Full item wordings and the
vignette texts are in `materials/vignettes_and_measures.md`. Empty cells are item non-response.

## `demographics.csv`

355 rows, one per participant, derived from the raw survey export by matching each de-identified row's
complete response pattern back to its source record (procedure documented in `code/make_demographics.py`;
all 355 rows matched a unique record).

| Column | Values |
|---|---|
| `participant_id` | join key |
| `age` | integer years |
| `gender` | `male`, `female`, `non-binary / third gender`, `prefer not to say` |
| `education` | `less than high school`, `high school / GED`, `some college`, `2-year degree (associate)`, `4-year degree (BA, BS)`, `master's degree`, `doctoral degree`, `professional degree` |
| `native_language` | `English`, `other` |

Marginals in this file: age M = 43.3 (SD = 13.1, range 20-80); 198 female, 152 male, 3 non-binary / third
gender, 2 prefer not to say; 336 native English speakers. The sample description in the manuscript was
compiled by the authors from the survey export at the time of analysis and differs from these marginals by
one to three participants in some categories; the moderation analyses in section F of
`code/supplementary_analyses.py` use this file.

## Citation

> Psychias, S., Kierysch, J., Kandul, S., Hazan, D., & Christen, M. (2026). Norms of communication in human-AI
> interaction: skin in the game and stake shape evaluations of human and artificial agents. Manuscript under
> review, *Scientific Reports*.

License: CC BY 4.0 (see `LICENSE` at the repository root).
