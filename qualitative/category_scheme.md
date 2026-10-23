# Open-ended responses: corpus and category scheme

Immediately after the reliance item (DV3), participants were prompted to "please provide reasons for your
answer" in a free-text box. `open_ended_responses.csv` contains the full verbatim corpus for the analytic
sample (N = 355), one row per participant, joined to the experimental condition through the anonymous
participant identifier used in `data/assertion_study_dataset.csv`.

## File: `open_ended_responses.csv`

| Column | Meaning |
|---|---|
| `participant_id` | Anonymous id, identical to the main dataset (join key) |
| `condition_label` | Human-readable condition, e.g. `human \| stake:high \| skin:low` |
| `agent` | `human` or `robot` (the AI condition) |
| `skin` | `high` or `low` for human agents; empty for the AI condition |
| `stake` | `high` or `low` |
| `response` | Verbatim free-text answer, UTF-8, spelling and punctuation as typed |

The texts were screened for identifying content before deposit; none was found. The consent form stated that
all responses are collected anonymously and that "the anonymized data may be archived in a research repository
and made available for future scientific use".

## Coding procedure (as reported in the manuscript, Methods)

The responses were analyzed thematically to complement the quantitative findings. One member of the research
team read the full set of responses and developed a set of descriptive categories inductively, refining them
iteratively as the corpus was traversed. No second coder was involved: the corpus was coded once, by that rater
alone, and the categories were developed inductively rather than against a pre-specified scheme. The analysis
is therefore exploratory and no inter-rater reliability is reported. Each response was assigned to the category
whose content it most closely matched; categories were not constrained to be mutually exclusive, and a small
number of responses that articulated more than one distinct rationale were assigned to multiple categories.

### Categories

| Code | Definition |
|---|---|
| C1 | Would not approach Ken at all because the participant prefers to verify the information themselves (e.g., on a phone or departure board) |
| C2 | Would not approach Ken because the participant does not trust him given his previous error or because Ken seems unreliable |
| C3 | Would not trust Ken specifically because he is an AI system |
| C4 | Would prefer to speak with a human rather than an AI (AI vignette only) |
| C5 | Would ask Ken but also double-check the information independently |
| C6 | Would re-engage with Ken despite his prior mistake (human vignette) |
| C7 | Would re-engage with Ken despite his prior mistake (AI vignette) |

### Expectation validation (manuscript, Results; Supplementary Table S6)

For three categories the theoretical framework supplied a directional prediction about the human condition
from which most responses should originate. Counts are human responses assigned to each category, by skin
condition (high-skin human n = 120, low-skin human n = 111).

| Category | High-skin | Low-skin | Predicted majority | Outcome |
|---|---|---|---|---|
| C1: verify independently | 37 | 32 | Low-skin | Not supported |
| C2: distrust / unreliable | 42 | 53 | Low-skin | Supported |
| C6: re-engage despite error | 26 | 20 | High-skin | Supported |

Fisher exact tests on these counts are reproduced by section M of `code/supplementary_analyses.py`.

## What this file does and does not allow

The per-response category assignments made by the original rater were not retained as a machine-readable
file; only the aggregate counts above exist. The deposited corpus therefore allows the coding to be
**audited and independently recoded** against the scheme (and the aggregate counts to be checked against a
fresh coding), but it does not allow the original rater's individual assignments to be recounted.
