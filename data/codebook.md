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

Category labels follow the answer options of the survey instrument in their original order
(`materials/survey_instrument_qualtrics_export.docx`, block "Demographics").

### Note on the sample description in the manuscript

The sample description in the Methods section of the submitted manuscript was compiled separately from the
survey export at the time of writing and differs from the marginals of this file by one to three participants
in some categories. The values in this file are the ones that correspond to the 355 participants in
`assertion_study_dataset.csv` (every row matched one unique raw record) and should be treated as the
authoritative description of the analytic sample. The discrepancy has no bearing on any reported test: no
analysis in the manuscript conditions on education or native language, and the age/gender moderation
analyses (section F of `code/supplementary_analyses.py`, Supplementary Information) are computed from this
file. The authors will align the Methods paragraph with these values at the next opportunity.

| Measure | Manuscript (Methods) | This file (N = 355) |
|---|---|---|
| Age, M (SD), range | 43.14 (12.96), 20-80 | 43.32 (13.13), 20-80 |
| Gender: female / male / non-binary or third gender / prefer not to say | 199 / 151 / 3 / 2 | 198 / 152 / 3 / 2 |
| Native language: English / other | 336 / 19 | 336 / 19 |
| 4-year degree (BA, BS) | 138 | 136 |
| High school / GED | 62 | 65 |
| Master's degree | 60 | 60 |
| Some college | 56 | 56 |
| Doctoral degree | 14 | 14 |
| 2-year degree (associate) | 13 | 14 |
| Professional degree | 8 | 6 |
| Less than high school | 4 | 4 |

## Citation

> Psychias, S., Kierysch, J., Kandul, S., Hazan, D., & Christen, M. (2026). Norms of communication in human-AI
> interaction: skin in the game and stake shape evaluations of human and artificial agents. Manuscript under
> review, *Scientific Reports*.

License: CC BY 4.0 (see `LICENSE` at the repository root).
