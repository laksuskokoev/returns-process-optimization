# Functional requirements (draft)

| ID | Priority | Requirement | Acceptance criteria |
|---|---|---|---|
| FR-01 | Must | Structured return request with order ID and reason | Required fields validated, ticket ID returned |
| FR-02 | Must | Auto-check eligibility against versioned policy | Approved eligibility rules covered by unit tests |
| FR-03 | Must | Route uncertain/high-risk cases to manual review | Every exception receives queue item and reason |
| FR-04 | Must | Display ticket lifecycle and SLA | Status timestamps and 48h SLA visible per case |
| FR-05 | Must | Record every decision in audit log | Actor, timestamp, policy version and outcome recorded |
| FR-06 | Should | Push refund request to payment system | Idempotent request with retry/failure status |
| FR-07 | Should | Notify customer about status changes | Notification events captured for delivery monitoring |

## Non-functional requirements
- NFR-01: Access control by role; only authorized workers can override decisions.
- NFR-02: Do not expose payment or personal details in dashboards.
- NFR-03: Idempotency and error handling for refund integration.
- NFR-04: Auditability and retention periods subject to business/legal review.

## Stakeholders and questions
Product owner: what problem has priority? Support: common exception reasons? Finance: settlement schedule? Legal/compliance: auto-refund limits? Engineers: integrations and failure modes?
