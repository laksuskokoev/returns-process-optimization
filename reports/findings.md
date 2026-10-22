# Case findings — simulated only

## Problem
Returns require manual registration, evidence checking, supervisor approval and batch refunds. We modeled changes to reduce queue and manual handling time.

## KPI comparison

| KPI | AS-IS modeled | TO-BE scenario |
|---|---:|---:|
| Mean cycle time (hours) | 60.54 | 34.51 |
| p90 cycle time (hours) | 92.69 | 66.12 |
| Completed within 48 hours (%) | 39.58 | 64.92 |

Modeled cycle time reduction: **43.0%**. Labor handling capacity: **245.93 hours** freed across 1200 simulated cases, equivalent to **221,340 RUB** at assumed 900 RUB/hour. These are NOT realized financial savings.

## Recommendation
First instrument stage timestamps, then pilot rules-based routing for low-risk complete cases while manually reviewing exceptions. Run controlled pilot with safeguards: duplicate refunds, fraud risk, complaint rates and incorrect approvals. Do not claim ROI until fixed/integration costs and observed outcomes are available.

## Limitations
TO-BE values are assumptions applied to synthetic baseline data; evidence of actual improvement does not exist. See `docs/assumptions.md`.
