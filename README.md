# Norms of communication in human-AI interaction: skin in the game and stake shape evaluations of human and artificial agents

Replication package for the manuscript by Stylianos Psychias, Jana Kierysch, Serhiy Kandul, Danit Hazan and
Markus Christen (University of Zurich, Digital Society Initiative; Tel Aviv University), under review at
*Scientific Reports*.

The study is a pre-registered between-subjects vignette experiment (N = 355; Prolific, UK) testing how an
agent's personal exposure to the consequences of an error ("skin in the game") and the severity of the
error's consequences for the recipient ("stake") shape how people evaluate a mistaken assertion made by a
human versus an artificial intelligence (AI) agent. An airport information-desk agent gives a passenger gate
information that was correct when last recalled but has since silently changed. We crossed the stake of the
error (high vs. low) with the agent's identity (human with high skin in the game, human with low skin in the
game, or AI) and measured the assertion's acceptability, justifiability and willingness to rely on the agent
again, together with secondary judgments (warning obligation, forgiveness, responsibility, perceived database
connectivity) and open-ended reasons.

- Pre-registration: AsPredicted #279864, <https://aspredicted.org/gk4wf4.pdf> (see `materials/preregistration.md`)
- Project: Norms in Language-based Human-AI Interaction (NIHAI), <https://talkingtobots.net/>
- Contact: stylianos.psychias@uzh.ch

## Contents

```
data/
  assertion_study_dataset.csv     de-identified analytic dataset (355 x 22)
  demographics.csv                de-identified demographics (age, gender, education, native language)
  codebook.md                     variable dictionary and sample description
code/
  supplementary_analyses.py       reproduces every exploratory / supplementary statistic in the manuscript
  make_demographics.py            documents how demographics.csv was derived (needs the private raw export)
  expected_output.txt             reference output of supplementary_analyses.py
  LICENSE                         MIT (code)
qualitative/
  open_ended_responses.csv        verbatim free-text reasons (355), joined to condition and participant id
  category_scheme.md              category definitions (C1-C7), coding procedure, expectation-validation counts
materials/
  vignettes_and_measures.md       six vignettes, comprehension and manipulation checks, all item wordings
  survey_instrument_qualtrics_export.docx   the complete survey as administered
  preregistration.md              registration details and confirmatory vs. exploratory split
CITATION.cff, LICENSE (CC BY 4.0 for data, materials and documentation), requirements.txt
```

## Reproducing the analyses

Confirmatory analyses (2 x 3 ANOVAs on acceptability, justifiability and reliance; Bonferroni-corrected
agent contrasts; manipulation-check t-tests) follow the pre-registered plan and can be run directly on
`data/assertion_study_dataset.csv` with any statistics package. The exploratory and supplementary analyses
reported in the manuscript and the Supplementary Information are reproduced by one script:

```bash
pip install -r requirements.txt
python code/supplementary_analyses.py
```

The script prints sections A-O (Holm-Bonferroni family, floor-composition logistic, warning-obligation ANOVA,
TOST equivalence and bound sweep, age/gender moderation, within-stake severity correlations, inter-item
correlations, Bayesian JZS tests, Tobit reanalysis, Fisher exact tests, composite reliability and the agent
manipulation-check proxy). `code/expected_output.txt` holds the reference output; a fresh run should
reproduce it to the printed precision.

## Ethics

The experimental protocol was reviewed by the Ethics Committee of the Faculty of Medicine of the University
of Zurich, which granted the study an exempt status as no specific ethical risk was associated with the
experiment. All methods were carried out in accordance with the relevant guidelines and regulations,
including the Declaration of Helsinki. Informed consent was obtained from all participants before the start
of the survey. No personal data were collected, and the deposited files contain no identifying information.

## Funding

This study was performed as part of the module "Teamwork on Digital Transformation Challenges" of the Master's
program DSI/LAO Digital Skills at the University of Zurich and received support from the CHANCE/HERA project
"Norms in Language-based Human-AI Interaction (NIHAI)" (SNSF grant number 10HR11_222969/1).

## How to cite

Psychias, S., Kierysch, J., Kandul, S., Hazan, D., & Christen, M. (2026). Norms of communication in human-AI
interaction: skin in the game and stake shape evaluations of human and artificial agents. Manuscript under
review, *Scientific Reports*. Replication package: <https://github.com/psychias/norms_of_communication_in_HCI>.

See `CITATION.cff` for machine-readable metadata.

## License

Data, materials and documentation: [CC BY 4.0](LICENSE). Code: [MIT](code/LICENSE).
