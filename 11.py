import gc


class Customer:
    pass


class InsurancePolicy:
    pass


customer = Customer()
policy = InsurancePolicy()

customer.policy = policy
policy.customer = customer

del customer
del policy

print("Garbage collected:", gc.collect())