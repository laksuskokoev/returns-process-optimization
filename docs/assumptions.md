# Data and methodology

All case-level records in this repository are synthetic. A seeded generator was used to create 1,200 simulated cases; the CSV is committed for reproducibility. Approximately 64% were randomly classified as standard, the rest as exception cases. Baseline stage duration samples are truncated Gaussian distributions; TO-BE stage durations are hypothetical multipliers of baseline times. Labor minutes are modeled separately; assumed blended loaded labor cost: 900 RUB/hour. No external customer records are used.

**Limitations:** TO-BE is a scenario, not a measured intervention; there is no causal evidence of effectiveness, no integration costs, no measured error/complaint impact, and no complete ROI. Cost saving is modeled labor capacity only, not booked cash savings. Rounding is at row level (3 decimals) and report display (2 decimals). SLA is total ticket cycle time <=48 hours. p90 uses nearest-rank definition.
