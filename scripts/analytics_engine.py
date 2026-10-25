import pandas as pd
import numpy as np

def main():
    print("=== RUNNING E-COMMERCE ANALYTICS ENGINE ===")
    orders = pd.read_csv("data/orders_data.csv")
    customers = pd.read_csv("data/customers_data.csv")
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    df = orders.merge(customers, on='customer_id', how='left')
    ref_date = pd.to_datetime('2026-08-15')
    rfm = df.groupby('customer_id').agg({
        'order_date': lambda x: (ref_date - x.max()).days,
        'order_id': 'count',
        'net_amount_eur': 'sum'
    }).reset_index()
    rfm.columns = ['customer_id', 'recency_days', 'frequency', 'monetary_eur']
    def segment(row):
        if row['frequency'] >= 5 and row['monetary_eur'] > 500:
            return 'VIP Champion'
        elif row['recency_days'] > 120:
            return 'At Risk / Churned'
        elif row['frequency'] >= 2:
            return 'Loyal Customer'
        return 'Recent / One-Time'
    rfm['segment'] = rfm.apply(segment, axis=1)
    rfm.to_csv("dashboards/rfm_segmented_output.csv", index=False)
    print("RFM Segmentation complete. Output saved to dashboards/rfm_segmented_output.csv")

if __name__ == "__main__":
    main()
