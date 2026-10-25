-- RFM and churn analysis query
WITH customer_orders AS (
    SELECT o.customer_id, c.country, COUNT(o.order_id) AS total_orders,
           SUM(o.net_amount_eur) AS total_spend, MAX(o.order_date) AS last_purchase_date
    FROM orders_data o LEFT JOIN customers_data c ON o.customer_id = c.customer_id
    GROUP BY o.customer_id, c.country
), rfm_scores AS (
    SELECT customer_id, country, total_orders, total_spend, last_purchase_date,
           DATEDIFF('day', last_purchase_date, '2026-08-15') AS recency_days
    FROM customer_orders
)
SELECT customer_id, country, recency_days, total_orders, total_spend,
       CASE WHEN recency_days <= 60 AND total_orders >= 5 THEN 'VIP Champion'
            WHEN recency_days > 120 THEN 'Churn Risk' ELSE 'Active Regular' END AS customer_cohort
FROM rfm_scores ORDER BY total_spend DESC;
