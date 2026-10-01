import pandas as pd

# Step 1: Load CSV
df = pd.read_csv("policies.csv")

print("========== ORIGINAL DATA ==========")
print(df)


# Step 2: High Coverage Policies
high_coverage = df[
    df["Coverage"] > 1000000
]

print("\n========== HIGH COVERAGE ==========")
print(high_coverage)


# Step 3: 10% Discount
df["DiscountedPremium"] = df["Premium"].apply(
    lambda premium: premium * 0.90
)


# Step 4: Premium Category
df["PremiumCategory"] = df["Premium"].apply(
    lambda premium:
        "High" if premium >= 50000
        else "Normal"
)


# Step 5: Sort by Premium
sorted_policies = df.sort_values(
    by="Premium",
    ascending=False
)

print("\n========== SORTED BY PREMIUM ==========")
print(sorted_policies)


# Step 6: Average Premium by Product
avg_premium = df.groupby("Product")["Premium"].mean()

print("\n========== AVERAGE PREMIUM ==========")
print(avg_premium)


# Step 7: Average Coverage by Product
avg_coverage = df.groupby("Product")["Coverage"].mean()

print("\n========== AVERAGE COVERAGE ==========")
print(avg_coverage)


# Step 8: Active Policies
active_policies = df[
    df["Status"] == "Active"
]

print("\n========== ACTIVE POLICIES ==========")
print(active_policies)


# Bonus 1: Active + High Coverage
active_high_coverage = df[
    (df["Status"] == "Active") &
    (df["Coverage"] > 2000000)
]

print("\n========== ACTIVE + HIGH COVERAGE ==========")
print(active_high_coverage)


# Bonus 2: 15% Discount
df["SpecialPremium"] = df["Premium"].apply(
    lambda premium: premium * 0.85
)


# Bonus 3: Risk Category
df["RiskCategory"] = df["Age"].apply(
    lambda age:
        "Senior" if age > 50
        else "Middle" if age >= 35
        else "Young"
)


# Bonus 4: Sort by Coverage
sorted_by_coverage = df.sort_values(
    by="Coverage",
    ascending=False
)

print("\n========== SORTED BY COVERAGE ==========")
print(sorted_by_coverage)


# Final DataFrame
print("\n========== FINAL DATA ==========")
print(df)