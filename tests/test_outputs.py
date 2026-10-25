from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_rfm_outputs_are_consistent():
    rfm_path = ROOT / "dashboards" / "rfm_segmented_output.csv"
    summary_path = ROOT / "dashboards" / "kpi_summary.json"
    assert rfm_path.exists() and summary_path.exists()
    rfm = pd.read_csv(rfm_path)
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert len(rfm) == summary["customers_analyzed"]
    assert rfm["customer_id"].notna().all()
    assert rfm["recency_days"].ge(0).all()
    assert rfm["frequency"].ge(1).all()
