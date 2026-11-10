"""Reproducible analysis of a *simulated* returns process; standard library only."""
from pathlib import Path
import csv, json, statistics
ROOT = Path(__file__).resolve().parents[1]
STAGES = ("intake", "verify", "decision", "refund")
COST_PER_HOUR_RUB = 900  # Assumed blended labor cost; not measured.

def load_cases(path=ROOT / "data" / "returns_cases_synthetic.csv"):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for field in row:
            if field not in ("case_id", "route"):
                row[field] = float(row[field])
    return rows

def total_hours(row, mode):
    return sum(row[f"{mode}_{stage}_h"] for stage in STAGES)

def summarize(rows):
    if not rows:
        raise ValueError("No cases")
    def metrics(segment):
        base = [total_hours(r, "as_is") for r in segment]
        target = [total_hours(r, "to_be") for r in segment]
        old_min = sum(r["as_is_handle_min"] for r in segment)
        new_min = sum(r["to_be_handle_min"] for r in segment)
        def stat(v):
            v = sorted(v)
            # nearest-rank percentile, explicitly stated in the report
            return {"mean_h":round(statistics.mean(v),2), "p90_h":round(v[max(0, (9*len(v)+9)//10-1)],2),
                    "sla_48h_pct":round(100*sum(x<=48 for x in v)/len(v),2)}
        return {"cases":len(segment),"as_is":stat(base),"to_be":stat(target),
                "handling_hours_saved":round((old_min-new_min)/60,2),
                "labor_savings_rub":round((old_min-new_min)/60*COST_PER_HOUR_RUB,2)}
    all_stats=metrics(rows)
    all_stats["mean_cycle_time_reduction_pct"]=round(100*(1-all_stats["to_be"]["mean_h"]/all_stats["as_is"]["mean_h"]),2)
    return {"all":all_stats,"standard":metrics([r for r in rows if r["route"]=="standard"]),
            "exception":metrics([r for r in rows if r["route"]=="exception"]),
            "assumptions":{"labor_cost_rub_per_hour":COST_PER_HOUR_RUB,"sla_hours":48,
                           "scenario":"Simulated TO-BE, not observed after rollout"}}

def main():
    result=summarize(load_cases())
    out=ROOT/"reports"/"summary.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result["all"],ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
