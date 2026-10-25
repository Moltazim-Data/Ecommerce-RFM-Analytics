from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def main():
    orders = pd.read_csv(ROOT / "data/orders_data.csv")
    amount = "order_value" if "order_value" in orders.columns else "net_amount_eur"
    orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
    orders[amount] = pd.to_numeric(orders[amount], errors="coerce")
    orders = orders.dropna(subset=["customer_id", "order_id", "order_date", amount])
    if "status" in orders.columns:
        orders = orders[orders["status"].astype(str).str.lower() != "returned"]
    ref = orders["order_date"].max() + pd.Timedelta(days=1)
    rfm = orders.groupby("customer_id").agg(
        recency_days=("order_date", lambda s: (ref - s.max()).days),
        frequency=("order_id", "nunique"), monetary_value=(amount, "sum")
    ).reset_index()
    def segment(row):
        if row["recency_days"] <= 30 and row["frequency"] >= 5: return "Champions"
        if row["recency_days"] > 120: return "At Risk"
        if row["frequency"] >= 5: return "Loyal Customers"
        return "Potential Loyalists"
    rfm["rfm_segment"] = rfm.apply(segment, axis=1)
    rfm.to_csv(ROOT / "dashboards/rfm_segmented_output.csv", index=False)
    summary = {"customers_analyzed": int(len(rfm)), "orders_analyzed": int(len(orders)),
               "revenue": round(float(orders[amount].sum()), 2),
               "average_order_value": round(float(orders[amount].mean()), 2),
               "segment_counts": {str(k): int(v) for k, v in rfm["rfm_segment"].value_counts().items()},
               "data_note": "Synthetic demonstration data; not actual business results."}
    (ROOT / "dashboards/kpi_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
