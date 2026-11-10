-- PostgreSQL. Assume CSV imported into returns_cases with the same column names.
-- Route-specific time and costs are modeled, not observed intervention results.
WITH cycle AS (
 SELECT route,
  as_is_intake_h + as_is_verify_h + as_is_decision_h + as_is_refund_h AS as_is_h,
  to_be_intake_h + to_be_verify_h + to_be_decision_h + to_be_refund_h AS to_be_h,
  as_is_handle_min, to_be_handle_min
 FROM returns_cases
)
SELECT route, count(*) AS case_count,
 round(avg(as_is_h)::numeric, 2) AS baseline_mean_hours,
 round(avg(to_be_h)::numeric, 2) AS simulated_target_mean_hours,
 round(100.0 * avg((as_is_h <= 48)::int), 2) AS baseline_sla_pct,
 round(100.0 * avg((to_be_h <= 48)::int), 2) AS simulated_sla_pct,
 round(sum(as_is_handle_min - to_be_handle_min)::numeric / 60, 2) AS hours_saved,
 round(sum(as_is_handle_min - to_be_handle_min)::numeric / 60 * 900, 2) AS modeled_labor_savings_rub
FROM cycle GROUP BY route ORDER BY route;
