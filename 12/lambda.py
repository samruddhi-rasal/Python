calculate_discount = lambda premium: premium * 0.90

print(calculate_discount(50000))


policies = [
    {"name": "Policy A", "premium": 50000},
    {"name": "Policy B", "premium": 30000},
]

discounted = list(
    map(
        lambda p: {
            **p,
            "discounted_premium": p["premium"] * 0.90
        },
        policies
    )
)

print(discounted)


policies = [
    {"name": "Policy A", "premium": 50000, "coverage": 1500000},
    {"name": "Policy B", "premium": 30000, "coverage": 800000},
]
high_coverage = list(
    filter(
        lambda p: p["premium"] > 40000,
        policies
    )
)

print(high_coverage)



sorted_policies = sorted(
    policies,
    key=lambda p: p["premium"],
    #reverse=True
)

print(sorted_policies)