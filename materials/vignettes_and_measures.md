# Experimental materials

Full stimulus texts and item wordings, reproduced from the manuscript (Methods). The complete Qualtrics
survey as administered, including consent text, bot check, attention checks, comprehension checks and
demographic items, is in `survey_instrument_qualtrics_export.docx`.

## Design

2 (Stake: high vs. low) x 3 (Agent: Human-High-Skin [HHS], Human-Low-Skin [HLS], AI) between-subjects.
Each of the six conditions combined one of three agent stems with one of two stake endings. Skin in the game
was manipulated only for the human agent; the AI condition served as a reference level without a skin
manipulation.

## Vignette stems

**Human, low skin in the game (HLS).**
"At JFK airport, there's an information desk where travelers can get help regarding their flights. The
information desk is staffed by Ken, an employee at the end of his probation phase. During the probation phase,
complaints by supervisors will lead to an immediate termination of the contract. For Ken this is not a problem,
because he got a permanent job offer in a different field. Ms. Miller, an elderly lady from New York City,
approaches Ken to find out at which gate her plane to Paris will depart. Given that the flight to Paris usually
departs from Gate 24, Ken says to Ms. Miller: 'The flight to Paris departs at gate 24.' However, there was an
update in the database. Therefore, the departure gates for most flights leaving today are listed differently
than usual. This is also true for the flight to Paris, which leaves from a different gate an hour later; the
flight to Paris departs from gate 13. The supervisor who was observing the situation filed a complaint."

**Human, high skin in the game (HHS).**
As above, except: "For Ken, who is hoping for a permanent contract, this is a problem, because he has no other
offers."

**AI (service robot).**
"At JFK airport, there's an information desk where travelers can get help regarding their flights. The
information desk is staffed by Ken, a service robot equipped with artificial intelligence which is fully
capable of taking independent decisions. Ms. Miller, an elderly lady from New York City, approaches Ken to find
out at which gate her plane to Paris will depart. Given that the flight to Paris usually departs from Gate 24,
Ken says to Ms. Miller: 'The flight to Paris departs at gate 24.' However, there was an update in the database.
Therefore, the departure gates for most flights leaving today are listed differently than usual. This is also
true for the flight to Paris, which leaves from a different gate an hour later; the flight to Paris departs from
gate 13. The supervisor who was observing the situation filed a complaint."

## Stake endings (appended to each stem)

**Low stake.** "Fortunately, Ms. Miller double checked the information on the gate board, and she managed to be
at the correct gate on time. Therefore, she will make it for her beloved daughter's wedding."

**High stake.** "Unfortunately, Ms. Miller did not double-check the information on the gate board, and she
failed to be at the correct gate on time. Therefore, she won't make it for her beloved daughter's wedding."

## Comprehension check

- Who is Ken? (an employee at the end of his probationary period at JFK / a supervisor at JFK / an AI chatbot at JFK)
- Which of the following describes the consequences Ken will face? (keeps his job and stays / keeps his job but
  takes another offer / loses his job but has already secured another offer / loses his job and does not receive
  another offer)

The comprehension check was not an exclusion criterion; it served as a proxy manipulation check for the agent
factor.

## Manipulation checks

| Dataset column | Item | Scale |
|---|---|---|
| `mc_cared` | "Ken cared about the supervisor's assessment." | 1 = strongly disagree, 7 = strongly agree |
| `mc_feelbad` | "Ken would likely feel bad about giving wrong information." | 1-7 |
| `mc_hastolose` | "Ken has something to lose (e.g., job, trust) that is relevant for his life if errors happen." | 1-7 |
| `mc_negeffect` | "Please assess the degree of a negative effect the wrong information provided by Ken had on Ms. Miller." | 1 = none at all, 5 = a great deal |

## Outcome measures

| Measure | Dataset column | Item wording | Response scale |
|---|---|---|---|
| Acceptability (DV1) | `acceptability` | "When replying to Ms. Miller's inquiry, Ken should have said that the flight to Paris departs at gate 24." | 1 = strongly disagree, 7 = strongly agree |
| Justifiability (DV2) | `justifiability` | "Ken was justified in believing that the flight to Paris departs at gate 24." | 1-7 Likert |
| Reliance (DV3) | `reliance` | Likelihood of inquiring about a departure gate from Ken (vs. consulting other information sources). | 1 = very unlikely, 7 = very likely |
| Open-ended reasons | (see `qualitative/`) | "Please provide reasons for your answer" (free text, following the reliance item). | Free text |
| Warning obligation (DV4) | `warning_obligation` | "After informing Ms. Miller about departure gate 24, Ken should have pointed out the possibility of the gate being changed." | 1-7 Likert |
| Forgiveness (DV5) | `forgiveness` | "The mistake of Ken can be forgiven." | 1 = not forgivable at all, 7 = absolutely forgivable |
| Responsibility, Ken (DV6a) | `responsible_ken` | Extent Ken is morally responsible for Ms. Miller arriving at the correct gate on time. | 1 = not responsible, 7 = fully responsible |
| Responsibility, Miller (DV6b) | `responsible_miller` | Extent Ms. Miller is morally responsible for arriving at the correct gate on time. | 1 = not responsible, 7 = fully responsible |
| Database connectivity (DV7) | `checked_database`, `connected_database`, `availability_info`, `awareness` | Whether Ken checked the database before answering; is directly interconnected with the database; whether all updates are immediately available to him; whether he is always aware of updates. | 1-7 Likert (each) |

## Procedure

Participants (Prolific; UK residents, age 18+, approval rate 95%+) gave informed consent, were randomly
assigned to one of the six conditions, read the vignette, answered the comprehension check, the manipulation
checks, then in fixed order the primary outcomes (DV1-DV3), the open-ended reasons item and the secondary
outcomes (DV4-DV7). Demographics (age, gender, education, native language) were collected at the end. Median
completion time was 4.8 minutes.
