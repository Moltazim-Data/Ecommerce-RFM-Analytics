# Ecommerce RFM Analytics — Demo Run Summary

> **Data note:** These results are calculated from synthetic demonstration data generated for this repository. They are not actual customer or sales results.

- Orders in dataset: 240
- Returned orders excluded: 12
- Orders analyzed: 228
- Customers analyzed: 80
- Revenue in source currency: 59,031.00
- Average order value: 258.91

## RFM segment counts
- At Risk: 4
- Potential Loyalists: 76

## Method
Recency is calculated from the day after the latest valid order date. Frequency counts distinct non-returned orders per customer. Monetary value is the sum of order value. Segment thresholds are illustrative and should be reviewed for the business context.

## Limitations
The generated dataset is a portfolio demonstration sample. Segment definitions and results should not be interpreted as findings about a real ecommerce business.
