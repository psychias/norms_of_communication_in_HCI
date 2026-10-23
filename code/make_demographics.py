"""Derivation of data/demographics.csv (documentation; not runnable without the private raw export).

The public dataset (data/assertion_study_dataset.csv) was de-identified before deposit and carries no
demographic columns. For the exploratory age/gender moderation checks (Methods, robustness analysis ix)
the demographic items were re-attached to the de-identified rows by matching each participant's complete
response pattern (all 15 rated items plus assigned agent and stake) against the raw Qualtrics export.
Every one of the 355 analytic participants matched exactly one unique response pattern.

The raw export contains Prolific IDs, IP addresses and geolocation and is therefore NOT part of this
repository. This script documents the procedure so that it can be audited; running it requires the
path to the raw export in the environment variable RAW_EXPORT.

Output columns:
  participant_id   anonymous id, identical to data/assertion_study_dataset.csv
  age              integer years
  gender           male | female | non-binary / third gender | prefer not to say
  education        less than high school | high school / GED | some college | 2-year degree (associate) |
                   4-year degree (BA, BS) | master's degree | doctoral degree | professional degree
  native_language  English | other
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data', 'assertion_study_dataset.csv')
OUT = os.path.join(HERE, '..', 'data', 'demographics.csv')
RAW = os.environ.get('RAW_EXPORT')

GENDER = {1: 'male', 2: 'female', 3: 'non-binary / third gender', 4: 'prefer not to say'}
EDUCATION = {1: 'less than high school', 2: 'high school / GED', 3: 'some college',
             4: '2-year degree (associate)', 5: '4-year degree (BA, BS)', 6: "master's degree",
             7: 'doctoral degree', 8: 'professional degree'}
LANGUAGE = {1: 'English', 2: 'other'}

# Qualtrics exported each of the six vignette blocks with its own copy of every item; the copies are
# collapsed into one column per item here. Column stems as they appear in the export.
BLOCKS = {
    'mc_cared': 'Manipulation_check1', 'mc_feelbad': 'Manipulation_check2',
    'mc_hastolose': 'Manipulation_check3', 'mc_negeffect': 'Manipulation_check4',
    'acceptability': 'acceptability', 'justifiability': 'justifiability',
    'warning_obligation': 'acceptability_should', 'reliance': 'reliance',
    'forgiveness': 'forgiveness', 'checked_database': 'checked_database',
    'awareness': 'awareness', 'responsible_miller': 'responsible_miller',
}
IRREGULAR = {
    'connected_database': ['connected_database', 'connected_database.1', 'connected_database.2',
                           'connected_database.3', 'connection_database', 'connected_database.4'],
    'availability_info': ['availability_info', 'availability_info.1', 'available_info',
                          'availability_info.2', 'availability_info.3', 'availability_info.4'],
    'responsible_ken': ['responsible_ken', 'responsible_ken.1', 'responsible_ken.2',
                        'responsible_ken.3', 'responsible_Ken', 'responsible_ken.4'],
}


def main():
    if not RAW or not os.path.exists(RAW):
        raise SystemExit("Set RAW_EXPORT to the path of the raw Qualtrics export (not distributed).")
    df = pd.read_csv(DATA)
    raw = pd.read_csv(RAW, low_memory=False).iloc[2:].reset_index(drop=True)  # drop Qualtrics header rows
    co = pd.DataFrame(index=raw.index)
    for k, stem in BLOCKS.items():
        co[k] = np.nan
        for c in [stem] + [f'{stem}.{i}' for i in range(1, 6)]:
            co[k] = co[k].fillna(pd.to_numeric(raw[c], errors='coerce'))
    for k, cols in IRREGULAR.items():
        co[k] = np.nan
        for c in cols:
            co[k] = co[k].fillna(pd.to_numeric(raw[c], errors='coerce'))
    co['agent'] = raw['agent'].str.strip().str.lower()
    co['stake'] = raw['stake'].astype(str).str.strip().str.lower()
    for c in ['Age', 'Gender', 'Education', 'Language']:
        co[c] = pd.to_numeric(raw[c], errors='coerce')

    keys = list(BLOCKS) + list(IRREGULAR)
    sig = lambda r: tuple(-9 if pd.isna(r[c]) else float(r[c]) for c in keys)
    index = {}
    for i, r in co.iterrows():
        index.setdefault((r['agent'], r['stake']) + sig(r), []).append(i)

    rows, matched = [], 0
    for _, r in df.iterrows():
        cand = index.get((r['agent'], r['stake']) + sig(r), [])
        ok = len(cand) >= 1 and all(co.loc[cand, c].nunique() <= 1 for c in ['Age', 'Gender', 'Education', 'Language'])
        if ok:
            matched += 1
            c = co.loc[cand[0]]
            rows.append(dict(participant_id=int(r['participant_id']),
                             age=int(c['Age']) if pd.notna(c['Age']) else '',
                             gender=GENDER.get(c['Gender'], ''),
                             education=EDUCATION.get(c['Education'], ''),
                             native_language=LANGUAGE.get(c['Language'], '')))
        else:
            rows.append(dict(participant_id=int(r['participant_id']), age='', gender='', education='', native_language=''))
    out = pd.DataFrame(rows)
    out.to_csv(OUT, index=False, encoding='utf-8', lineterminator='\n')
    print(f"matched {matched}/{len(df)}; written {OUT}")


if __name__ == '__main__':
    main()
