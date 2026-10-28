
#======================================================================
import os

import pandas as pd

# Load dataset
file_path = "Data/SampleSuperstore.csv"
df = pd.read_csv(file_path)

# Basic dataset info
print("Dataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nFirst 5 Rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nUnique Values Per Column:\n", df.nunique())

# Duplicate records
duplicates = df[df.duplicated(keep=False)]
print("\nFirst 5 duplicate records:\n", duplicates.head(5).to_string(index=False))

# Dataset summary
print("\nDataset Summary:\n", df[["Sales", "Quantity", "Discount", "Profit"]].describe())

# Profit checks
print("\nNegative Profit Records:", (df["Profit"] < 0).sum())
print("Zero Profit Records:", (df["Profit"] == 0).sum())

# Discount values
print("\nDiscount Values:", sorted(df["Discount"].unique()))

# Profit by discount level
discount_analysis = df.groupby("Discount").agg(
    Total_Records=("Profit", "count"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean")
).reset_index()

print("\nProfit by Discount Level:\n", discount_analysis.sort_values("Discount").to_string(index=False))
print("\nDiscount Levels Ranked by Total Profit:\n", discount_analysis.sort_values("Total_Profit").to_string(index=False))

# High discount (70%) analysis
high_discount = df[df["Discount"].round(2) == 0.70].copy()
result = high_discount.groupby("Sub-Category").agg(
    Records=("Profit", "size"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean")
).round(2)

print("\n70% Discount Summary")
print("Total Records:", len(high_discount))
print("Total Sales:", high_discount["Sales"].sum())
print("Total Profit:", high_discount["Profit"].sum())
print("Average Profit:", high_discount["Profit"].mean())

print("\nSubcategory Analysis at 70% Discount:\n", result.sort_values("Total_Profit").to_string(index=False))

# Duplicate cleaning impact
print("\nDuplicate Rows:", df.duplicated().sum())


print("\nRemoving duplicate rows...")

# Remove duplicates
df_clean = df.drop_duplicates()

print("Cleaned Dataset Shape:", df_clean.shape)
# after cleaning 
# Rechecking the sales and profit 
# to identify their impact on data 
# Basic info again
print("\nColumn Names:", df_clean.columns.tolist())
print("\nMissing Values:\n", df_clean.isnull().sum())
print("\nUnique Values Per Column:\n", df_clean.nunique())

# Summary stats
print("\nDataset Summary:\n", df_clean[["Sales", "Quantity", "Discount", "Profit"]].describe())

# Profit checks
print("\nNegative Profit Records:", (df_clean["Profit"] < 0).sum())
print("Zero Profit Records:", (df_clean["Profit"] == 0).sum())

# Discount analysis after cleaning
discount_analysis_clean = df_clean.groupby("Discount").agg(
    Total_Records=("Profit", "count"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean")
).reset_index()

print("\nProfit by Discount Level (Cleaned):\n", discount_analysis_clean.sort_values("Discount").to_string(index=False))

# Profit margin comparison
print("\nOverall Profit Margin (Cleaned):", (df_clean['Profit'].sum() / df_clean['Sales'].sum()) * 100)

# 70% discount segment after cleaning
d_clean = df_clean[df_clean['Discount'] == 0.70]
print("\n70% Discount Segment Profit Margin (Cleaned):", (d_clean['Profit'].sum() / d_clean['Sales'].sum()) * 100)

# create an new cleaned csv 
os.makedirs("Cleaned_data", exist_ok=True)

df_clean.to_csv("Cleaned_data/SampleSuperstore_Cleaned.csv", index=False)

print("Cleaned CSV saved successfully!")