#12.md


import pandas as pd

# Load CSV
df = pd.read_csv("policies.csv")

print("ORIGINAL DATA")
print(df)


# 1. High Coverage Policies
high_coverage = df[
    df["Coverage"] > 1000000
]

print("\nHIGH COVERAGE POLICIES")
print(high_coverage)


# 2. 10% Premium Discount
df["DiscountedPremium"] = df["Premium"].apply(
    lambda x: x * 0.90
)

print("\nAFTER 10% DISCOUNT")
print(df[["PolicyID", "Premium", "DiscountedPremium"]])


# 3. Premium Category
df["PremiumCategory"] = df["Premium"].apply(
    lambda x: "High" if x >= 50000 else "Normal"
)

print("\nPREMIUM CATEGORY")
print(df[["PolicyID", "Premium", "PremiumCategory"]])


# 4. Sort by Premium
sorted_df = df.sort_values(
    by="Premium",
    ascending=False
)

print("\nSORTED BY PREMIUM")
print(sorted_df)


# 5. Average Premium by Product
avg_premium = df.groupby("Product")["Premium"].mean()

print("\nAVERAGE PREMIUM BY PRODUCT")
print(avg_premium)


# 6. Average Coverage by Product
avg_coverage = df.groupby("Product")["Coverage"].mean()

print("\nAVERAGE COVERAGE BY PRODUCT")
print(avg_coverage)


# 7. Active Policies
active_policies = df[
    df["Status"] == "Active"
]

print("\nACTIVE POLICIES")
print(active_policies)


# 8. Active + Coverage > 20 Lakhs
high_active = df[
    (df["Status"] == "Active") &
    (df["Coverage"] > 2000000)
]

print("\nACTIVE POLICIES WITH COVERAGE > 20 LAKHS")
print(high_active)


# 9. 15% Special Discount
df["SpecialPremium"] = df["Premium"].apply(
    lambda x: x * 0.85
)

print("\n15% SPECIAL DISCOUNT")
print(df[["PolicyID", "Premium", "SpecialPremium"]])


# 10. Risk Category
df["RiskCategory"] = df["Age"].apply(
    lambda age:
        "Senior" if age > 50
        else "Middle" if age >= 35
        else "Young"
)

print("\nRISK CATEGORY")
print(df[["PolicyID", "Age", "RiskCategory"]])


# 11. Sort by Coverage
coverage_sorted = df.sort_values(
    by="Coverage",
    ascending=False
)

print("\nSORTED BY COVERAGE")
print(coverage_sorted[["PolicyID", "Customer", "Coverage"]])