# Ecommerce RFM Analytics


> **Demo data notice:** The datasets and chart assets added for this repository are synthetic examples generated for demonstration. They are not real customer or transaction records.

Python and SQL analytics for e-commerce revenue, customer segmentation, and RFM-based customer behavior analysis.

## Project contents
- `scripts/analytics_engine.py` — analytics workflow
- `sql/rfm_cohort_analysis.sql` — SQL analysis examples
- `data/` — customer and order data
- `dashboards/` — dashboard and generated outputs
- `reports/` — executive findings

## Run
```bash
pip install -r requirements.txt
python scripts/analytics_engine.py
```

**Note:** The churn-risk label is a recency-based heuristic, not a trained predictive model. Some source customer records may not match an order.

## Analysis report
See [reports/portfolio_report.md](reports/portfolio_report.md) for the report structure, business questions, interpretation caveats, and recommended next actions.
