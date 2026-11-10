# Prioritized delivery backlog

| Priority | Work item | Dependencies | How to validate |
|---|---|---|---|
| P0 | Instrument timestamps for each stage | Event taxonomy, data pipeline | 95%+ coverage on pilot cases |
| P0 | Structured return request form | Frontend and support | Required fields tested |
| P0 | Eligibility rules and exception routing | Legal, risk, support | Sample cases reviewed and signed off |
| P1 | Agent dashboard and SLA alerts | Status API | No cases silently disappear from queues |
| P1 | Refund API integration | Finance and payment team | Repeated events never pay twice |
| P2 | User status notifications | Message bus / templates | Track delivery failures |

**Pilot proposal:** launch to a small random subset of eligible returns; compare cycle time, SLA, errors, wrongful approvals and complaints against holdout. Freeze KPI definitions before launch.
