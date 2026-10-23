"""Supplementary robustness analyses for

  Psychias, Kierysch, Kandul, Hazan & Christen, "Norms of communication in human-AI
  interaction: skin in the game and stake shape evaluations of human and artificial agents".

Reproduces, from the deposited dataset (data/assertion_study_dataset.csv), every exploratory
and supplementary statistic reported in the manuscript and its Supplementary Information.
The roman numerals refer to the list of robustness analyses in the Methods ("Analytic
approach", exploratory analyses):

  A.  Holm-Bonferroni sensitivity analysis over the m=18 exploratory-test family (i)
  B.  Low-stake-only responsibility-gap check (vi)
  C.  Acceptability floor-composition logistic models (ii; Supplementary Fig. S1)
  D.  Warning-obligation (DV4) 2x3 ANOVA (Results; Supplementary Fig. S3)
  E.  TOST equivalence, HLS vs AI, all four outcomes, bound d = 0.4 (vii)
  E2. Equivalence-bound sensitivity sweep (viii)
  F.  Age/gender moderation of the agent effects (ix) -- uses data/demographics.csv
  G.  Within-stake severity -> forgiveness, and G2 -> responsibility (x)
  I.  Within-AI construal -> responsibility (xi)
  H.  Inter-item correlation matrix (xii; Supplementary Fig. S4)
  J.  Bayesian (JZS) evidence for the primary-measure outcome-effect nulls (iii)
  K.  Tobit (left-censored) reanalysis of the floored acceptability item (v)
  L.  Bayesian (JZS) counterpart to the HLS-vs-AI equivalence tests, H2 (iv)
  M.  Fisher exact tests on the qualitative expectation-validation counts (xiii; Supplementary Table S6)
  N.  Composite reliability: Cronbach alpha (+bootstrap CI), McDonald omega, inter-item r (xiv)
  O.  Agent (human vs AI) manipulation-check proxy: comprehension classification + convergent DV7 (xiv)

The confirmatory (pre-registered) statistics reported in the manuscript are NOT produced
here; they were computed according to the pre-registered analysis plan (AsPredicted #279864).

Requires: pandas, numpy, scipy, statsmodels, patsy (see requirements.txt).
Run from anywhere:  python code/supplementary_analyses.py
"""
import os
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols, logit
import statsmodels.api as sm

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data', 'assertion_study_dataset.csv')
DEMOGRAPHICS = os.path.join(HERE, '..', 'data', 'demographics.csv')

df = pd.read_csv(DATA)
df['acond'] = df.apply(lambda r: 'AI' if r['agent'] == 'robot'
                       else ('HHS' if r['skin'] == 'high' else 'HLS'), axis=1)
df['gap'] = df['responsible_ken'] - df['responsible_miller']
z = df[['acceptability', 'justifiability', 'reliance', 'forgiveness']].apply(stats.zscore)
df['composite'] = z.mean(axis=1)
assert len(df) == 355


def anova3(dv, data):
    m = ols(f'{dv} ~ C(stake, Sum) * C(acond, Sum)', data=data.dropna(subset=[dv])).fit()
    return sm.stats.anova_lm(m, typ=3)


def t2(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    x = x[~np.isnan(x)]; y = y[~np.isnan(y)]
    t, p = stats.ttest_ind(x, y)
    sp = np.sqrt(((len(x) - 1) * x.var(ddof=1) + (len(y) - 1) * y.var(ddof=1)) / (len(x) + len(y) - 2))
    return t, p, (x.mean() - y.mean()) / sp


print("== A. Holm-Bonferroni over the exploratory family ==")
fam = {}
a = anova3('forgiveness', df)
fam['forgiveness: stake'] = a.loc['C(stake, Sum)', 'PR(>F)']
fam['forgiveness: agent'] = a.loc['C(acond, Sum)', 'PR(>F)']
fam['respKen: agent'] = anova3('responsible_ken', df).loc['C(acond, Sum)', 'PR(>F)']
fam['gap: agent omnibus'] = anova3('gap', df).loc['C(acond, Sum)', 'PR(>F)']
for c in ['HHS', 'HLS', 'AI']:
    fam[f'gap vs 0, {c}'] = stats.ttest_1samp(df[df.acond == c]['gap'].dropna(), 0).pvalue
ai, hum = df[df.acond == 'AI'], df[df.acond != 'AI']
for dv in ['connected_database', 'checked_database', 'justifiability', 'forgiveness']:
    fam[f'within-AI stake: {dv}'] = t2(ai[ai.stake == 'high'][dv], ai[ai.stake == 'low'][dv])[1]
for dv in ['checked_database', 'connected_database', 'availability_info', 'awareness']:
    fam[f'AI vs human: {dv}'] = t2(ai[dv], hum[dv])[1]
fam['composite: agent'] = anova3('composite', df).loc['C(acond, Sum)', 'PR(>F)']
a = anova3('warning_obligation', df)
fam['warning DV4: stake'] = a.loc['C(stake, Sum)', 'PR(>F)']
fam['warning DV4: agent'] = a.loc['C(acond, Sum)', 'PR(>F)']
ks = sorted(fam, key=lambda k: fam[k]); m = len(ks); prev = 0
for i, k in enumerate(ks):
    adj = min(1.0, max(prev, (m - i) * fam[k])); prev = adj
    print(f"  {k:38s} p={fam[k]:.3g}  Holm-adj={adj:.3g}  {'SURVIVES' if adj < .05 else '--'}")

print("\n== B. Responsibility gap vs 0, low-stake cells only ==")
for c in ['HHS', 'HLS', 'AI']:
    g = df[(df.stake == 'low') & (df.acond == c)]['gap'].dropna()
    t, p = stats.ttest_1samp(g, 0)
    print(f"  {c}: M={g.mean():.2f}, t({len(g)-1})={t:.2f}, p={p:.4f}, p_bonf3={min(1, p*3):.4f}")

print("\n== C. Acceptability floor-composition logistic (LR tests) ==")
df['acc_floor'] = (df['acceptability'] == 1).astype(int)
mfull = logit('acc_floor ~ C(stake) * C(acond)', data=df).fit(disp=0)
madd = logit('acc_floor ~ C(stake) + C(acond)', data=df).fit(disp=0)
mst = logit('acc_floor ~ C(stake)', data=df).fit(disp=0)
mag = logit('acc_floor ~ C(acond)', data=df).fit(disp=0)
print(f"  floor rate = {df['acc_floor'].mean():.3f}")
print(f"  stake:       chi2(1)={2*(madd.llf-mag.llf):.2f}, p={stats.chi2.sf(2*(madd.llf-mag.llf),1):.4f}")
print(f"  agent:       chi2(2)={2*(madd.llf-mst.llf):.2f}, p={stats.chi2.sf(2*(madd.llf-mst.llf),2):.4f}")
print(f"  interaction: chi2(2)={2*(mfull.llf-madd.llf):.2f}, p={stats.chi2.sf(2*(mfull.llf-madd.llf),2):.4f}")

print("\n== D. Warning obligation (DV4) 2x3 ANOVA ==")
a = anova3('warning_obligation', df)
ss_res = a.loc['Residual', 'sum_sq']
for src in ['C(stake, Sum)', 'C(acond, Sum)', 'C(stake, Sum):C(acond, Sum)']:
    eta = a.loc[src, 'sum_sq'] / (a.loc[src, 'sum_sq'] + ss_res)
    print(f"  {src:30s} F={a.loc[src,'F']:.2f}, p={a.loc[src,'PR(>F)']:.4g}, eta2={eta:.3f}")
hi, lo = df[df.stake == 'high']['warning_obligation'], df[df.stake == 'low']['warning_obligation']
sp = np.sqrt(((len(hi)-1)*hi.var() + (len(lo)-1)*lo.var()) / (len(hi)+len(lo)-2))
print(f"  M_high={hi.mean():.2f} (SD={hi.std():.2f}), M_low={lo.mean():.2f} (SD={lo.std():.2f}), d={(hi.mean()-lo.mean())/sp:.2f}")

print("\n== E. TOST equivalence, HLS vs AI, bound d=0.4 ==")
def tost(x, y, d_bound):
    x, y = x.dropna(), y.dropna()
    nx, ny = len(x), len(y)
    sp = np.sqrt(((nx-1)*x.var() + (ny-1)*y.var()) / (nx+ny-2))
    se = sp * np.sqrt(1/nx + 1/ny)
    diff, delta = x.mean() - y.mean(), d_bound * sp
    p1 = stats.t.sf((diff + delta) / se, nx+ny-2)
    p2 = stats.t.cdf((diff - delta) / se, nx+ny-2)
    return diff / sp, max(p1, p2)
hls = df[df.acond == 'HLS']
for dv in ['reliance', 'acceptability', 'justifiability', 'forgiveness']:
    d, p = tost(hls[dv], ai[dv], 0.4)
    print(f"  {dv:15s}: d={d:.3f}, TOST p={p:.4f} -> {'EQUIVALENT' if p < .05 else 'not established'}")

print("\n== E2. Equivalence-bound sensitivity (tightest passing bound, HLS vs AI) ==")
grid = np.round(np.arange(0.20, 0.81, 0.01), 2)
for dv in ['reliance', 'acceptability', 'justifiability', 'forgiveness']:
    passing = [b for b in grid if tost(hls[dv], ai[dv], b)[1] < .05]
    tightest = f"d={min(passing):.2f}" if passing else "none in [0.20, 0.80]"
    print(f"  {dv:15s}: observed d={tost(hls[dv], ai[dv], 0.4)[0]:+.3f}, "
          f"tightest equivalence bound {tightest}")

print("\n== G. Within-stake severity -> forgiveness (verification constant) ==")
for stake in ['high', 'low']:
    sub = df[df.stake == stake].dropna(subset=['mc_negeffect', 'forgiveness'])
    r, p = stats.pearsonr(sub['mc_negeffect'], sub['forgiveness'])
    print(f"  stake={stake:4s}: r(perceived severity, forgiveness) = {r:+.3f}, p={p:.4f}, n={len(sub)}")

print("\n== G2. Within-stake severity -> Ken responsibility (verification constant) ==")
for stake in ['high', 'low']:
    sub = df[df.stake == stake].dropna(subset=['mc_negeffect', 'responsible_ken'])
    r, p = stats.pearsonr(sub['mc_negeffect'], sub['responsible_ken'])
    print(f"  stake={stake:4s}: r = {r:+.3f}, p={p:.4f}, n={len(sub)}")

print("\n== I. Within-AI construal -> responsibility (framing-sensitivity proxy) ==")
ai = df[df.acond == 'AI']
sub = ai.dropna(subset=['connected_database', 'availability_info', 'awareness', 'responsible_ken'])
c = sub[['connected_database', 'availability_info', 'awareness']].mean(axis=1)
r, p = stats.pearsonr(c, sub['responsible_ken'])
print(f"  r(connectivity construal, responsible_ken) = {r:+.3f}, p={p:.4f}, n={len(sub)}")

print("\n== H. Inter-item correlation matrix (pairwise complete) ==")
items = ['acceptability', 'justifiability', 'reliance', 'warning_obligation', 'forgiveness',
         'responsible_ken', 'responsible_miller', 'checked_database', 'availability_info']
print(df[items].corr().round(2).to_string())

print("\n== F. Age/gender moderation (de-identified demographics) ==")
if not os.path.exists(DEMOGRAPHICS):
    print("  demographics file not found at", DEMOGRAPHICS, "-- skipped")
else:
    dem = pd.read_csv(DEMOGRAPHICS)
    df = df.merge(dem[['participant_id', 'age', 'gender']], on='participant_id', how='left')
    df['Age'] = pd.to_numeric(df['age'], errors='coerce')
    df['Gender'] = df['gender']
    matched = int(df['Age'].notna().sum())
    print(f"  matched {matched}/355; age M={df['Age'].mean():.2f}, SD={df['Age'].std():.2f}")
    sub = df.dropna(subset=['Age']).copy()
    sub['age_c'] = sub['Age'] - sub['Age'].mean()
    for dv in ['acceptability', 'justifiability', 'reliance', 'forgiveness']:
        aa = sm.stats.anova_lm(ols(f'{dv} ~ C(acond, Sum) * age_c', data=sub.dropna(subset=[dv])).fit(), typ=3)
        print(f"  Agent x Age,    {dv:15s}: F={aa.loc['C(acond, Sum):age_c','F']:.2f}, p={aa.loc['C(acond, Sum):age_c','PR(>F)']:.4f}")
    g = df[df['Gender'].isin(['male', 'female'])].copy()
    for dv in ['acceptability', 'justifiability', 'reliance', 'forgiveness']:
        aa = sm.stats.anova_lm(ols(f'{dv} ~ C(acond, Sum) * C(Gender, Sum)', data=g.dropna(subset=[dv])).fit(), typ=3)
        key = [ix for ix in aa.index if ':' in ix][0]
        print(f"  Agent x Gender, {dv:15s}: F={aa.loc[key,'F']:.2f}, p={aa.loc[key,'PR(>F)']:.4f}")


# === J. Bayesian evidence for the primary-measure outcome (stake) nulls ===
# JZS default two-sample Bayes factor (Rouder et al. 2009), prior scale r = 0.707.
from scipy.integrate import quad as _quad
def bf10_two_sample(t, n1, n2, r=0.707):
    nu = n1 + n2 - 2; N = n1 * n2 / (n1 + n2)
    null = (1 + t**2 / nu) ** (-(nu + 1) / 2)
    def integrand(g):
        return ((1 + N*g*r**2) ** -0.5
                * (1 + t**2 / ((1 + N*g*r**2) * nu)) ** (-(nu + 1) / 2)
                * (2*np.pi) ** -0.5 * g**-1.5 * np.exp(-1 / (2*g)))
    alt, _ = _quad(integrand, 0, np.inf)
    return alt / null

print("\n== J. Bayesian evidence for outcome (stake) effect, high vs low (JZS r=0.707) ==")
for grp, mask in [('humans', df.agent == 'human'), ('AI', df.agent == 'robot')]:
    sub = df[mask]
    for dv in ['acceptability', 'justifiability', 'reliance']:
        hi = sub[sub.stake == 'high'][dv].dropna(); lo = sub[sub.stake == 'low'][dv].dropna()
        t, p = stats.ttest_ind(hi, lo)
        bf10 = bf10_two_sample(t, len(hi), len(lo))
        tag = ('null (BF01>3)' if 1/bf10 > 3 else 'alt (BF10>3)' if bf10 > 3 else 'inconclusive')
        print(f"  {grp:6s} {dv:15s}: t={t:+.2f}, BF10={bf10:6.2f}, BF01={1/bf10:6.2f}  -> {tag}")

# === K. Tobit (left-censored at the floor) for acceptability ===
import patsy
_L = 1.0
def _tobit_ll(formula, data):
    y, X = patsy.dmatrices(formula, data, return_type='dataframe')
    y = y.values.ravel(); Xm = X.values; cens = y <= _L; k = Xm.shape[1]
    def negll(par):
        b = par[:k]; s = np.exp(par[k]); mu = Xm @ b; z = (y - mu) / s
        ll = np.where(cens, stats.norm.logcdf((_L - mu) / s),
                      -np.log(s) - 0.5*np.log(2*np.pi) - 0.5*z**2)
        return -ll.sum()
    from scipy.optimize import minimize
    b0 = np.linalg.lstsq(Xm, y, rcond=None)[0]
    res = minimize(negll, np.r_[b0, np.log(y.std())], method='BFGS', options={'maxiter': 2000})
    return -res.fun, res.success
def _lr(full, red, data, ddf):
    lf, ok1 = _tobit_ll(full, data); lr_, ok2 = _tobit_ll(red, data)
    s = 2*(lf - lr_); return s, stats.chi2.sf(s, ddf), (ok1 and ok2)

print("\n== K. Tobit (left-censored at floor=1) for acceptability: LR tests ==")
s, p, ok = _lr('acceptability ~ C(stake)*C(acond)', 'acceptability ~ C(stake)+C(acond)', df, 2)
print(f"  Stake x Agent interaction: chi2(2)={s:.2f}, p={p:.4f}  (ANOVA p=.011)")
s, p, _ = _lr('acceptability ~ C(stake)+C(acond)', 'acceptability ~ C(acond)', df, 1)
print(f"  Stake main (added):        chi2(1)={s:.2f}, p={p:.4f}  (ANOVA p=.035)")
s, p, _ = _lr('acceptability ~ C(stake)+C(acond)', 'acceptability ~ C(stake)', df, 2)
print(f"  Agent main (added):        chi2(2)={s:.2f}, p={p:.4f}  (ANOVA p=.416)")


# === L. Bayesian counterpart to the HLS-vs-AI equivalence tests (H2) ===
# Same JZS two-sample BF as section J, applied to the low-skin-human vs AI contrast,
# so the equivalence story (TOST, Results) and the null story share one frame.
print("\n== L. Bayesian evidence for HLS vs AI (mirror of the TOST equivalence table) ==")
_hls = df[df.acond == 'HLS']
for dv in ['reliance', 'acceptability', 'justifiability', 'forgiveness']:
    x = _hls[dv].dropna(); y = ai[dv].dropna()
    t, _ = stats.ttest_ind(x, y)
    bf10 = bf10_two_sample(t, len(x), len(y))
    tag = ('equivalence (BF01>3)' if 1/bf10 > 3 else 'difference (BF10>3)' if bf10 > 3 else 'inconclusive')
    print(f"  {dv:15s}: BF10={bf10:6.2f}, BF01={1/bf10:6.2f}  -> {tag}")


# === M. Inferential tests on the qualitative expectation-validation ===
# Fisher exact on the reported single-rater category counts (Supplementary Table S6) x skin condition.
# Denominators are the human cell sizes (HHS=120, HLS=111; Table 1). Per-response codes
# are not recoverable, so these test the *reported* counts; single-rater caveat stands.
print("\n== M. Fisher exact on qualitative expectation-validation (reported counts) ==")
_nH, _nL = 120, 111
for name, h, l in [('C1 verify-independently', 37, 32),
                   ('C2 distrust/unreliable', 42, 53),
                   ('C6 re-engage', 26, 20)]:
    OR, p = stats.fisher_exact([[h, _nH - h], [l, _nL - l]])
    print(f"  {name:24s}: high {h}/{_nH}={h/_nH:.2f}, low {l}/{_nL}={l/_nL:.2f}, OR={OR:.2f}, p={p:.3f}")

# === N. Composite leniency index reliability (omega + alpha CI) ===
print("\n== N. Composite leniency reliability (acceptability, justifiability, reliance, forgiveness) ==")
_items = ['acceptability', 'justifiability', 'reliance', 'forgiveness']
_X = df[_items].dropna(); _k = len(_items)
_alpha = _k / (_k - 1) * (1 - _X.var(ddof=1).sum() / _X.sum(axis=1).var(ddof=1))
_avg_r = _X.corr().values[np.triu_indices(_k, 1)].mean()
_rng = np.random.default_rng(20260714)
def _cron(d):
    return _k / (_k - 1) * (1 - d.var(ddof=1).sum() / d.sum(axis=1).var(ddof=1))
_boot = [_cron(_X.iloc[_rng.integers(0, len(_X), len(_X))]) for _ in range(2000)]
from statsmodels.multivariate.factor import Factor
_Z = (_X - _X.mean()) / _X.std(ddof=0)
_L = np.asarray(Factor(_Z.values, n_factor=1, method='ml').fit().loadings).ravel()
_omega = (_L.sum()**2) / ((_L.sum()**2) + (1 - _L**2).sum())
print(f"  Cronbach alpha={_alpha:.3f} (95% boot CI [{np.percentile(_boot,2.5):.3f}, {np.percentile(_boot,97.5):.3f}])")
print(f"  McDonald omega={_omega:.3f}, avg inter-item r={_avg_r:.3f}")

# === O. Agent (human vs AI) manipulation-check proxy ===
print("\n== O. Agent manipulation-check proxy (comprehension x assigned agent) ==")
_correct = (((df.agent == 'human') & (df.comprehension_whoisken == 1)) |
            ((df.agent == 'robot') & (df.comprehension_whoisken == 3))).sum()
print(f"  correct agent classification: {_correct}/{len(df)} = {_correct/len(df)*100:.1f}%")
_ai = df[df.agent == 'robot']['availability_info']; _hu = df[df.agent == 'human']['availability_info']
_sp = np.sqrt(((len(_ai)-1)*_ai.var() + (len(_hu)-1)*_hu.var()) / (len(_ai)+len(_hu)-2))
print(f"  convergent DV7 availability_info AI vs human: d={(_ai.mean()-_hu.mean())/_sp:.2f}")
