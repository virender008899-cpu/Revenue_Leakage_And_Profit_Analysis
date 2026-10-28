# Revenue Leakage & Profit Analysis

## Project Overview
This project studies the SampleSuperstore_Cleaned dataset to find where the company is losing money (revenue leakage) and how discounts, regions, and product categories affect profit.

## Dataset
- Records: 9,977 (after cleaning)
- Columns: 13 (Sales, Profit, Discount, Quantity, Category, Sub-Category, Region, etc.)
- No missing values
- 17 duplicates removed

## Business Questions
- What is the overall profit margin?
- How many transactions are loss-making?
- Which discounts are safe and which destroy profit?
- Which products or sub-categories lose money?
- Which regions are strong or weak?
- What is the risk of very high discounts?

## Key Insights
- Overall profit margin: 12.47%
- Loss-making records: 1,869 (~19%)
- Profitable discounts: 0–20%
- Dangerous discounts: ≥30% (especially 50%, 70%, 80%)
- East region is strongest, South is weakest
- Bookcases are structurally unprofitable
- 0% discount sales contribute most profit
- High discounts cause ~96,000 total losses

## Extremely Important Insights
- Less than 20% of records (high-discount sales) cause most losses
- Without East region, margin drops below 10%
- High discounts do not increase sales enough → company is “paying customers to buy”
- Profit is over-reliant on 0% discount sales
- Shifting promotions to 10–20% discount range could raise profit by 20–25%

## Recommendations
- Focus promotions in 10–20% discount range
- Avoid extreme discounts (≥30%)
- Fix unprofitable subcategories (e.g., Bookcases)
- Reduce dependency on East region
- Build a balanced discount strategy
