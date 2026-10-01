# Custom Exceptions

class PolicyNotFoundException(Exception):
    pass


class InvalidPremiumException(Exception):
    pass


class PolicyExpiredException(Exception):
    pass


# Policy Class

class Policy:

    def __init__(self, policy_number, customer_name, premium, status):
        self.policy_number = policy_number
        self.customer_name = customer_name
        self.premium = premium
        self.status = status

    def pay_premium(self, amount):

        if amount < 0:
            raise ValueError("Payment cannot be negative")

        if self.status == "Expired":
            raise PolicyExpiredException("Policy is expired")

        self.premium = self.premium - amount

        print("Premium paid successfully")
        print("Remaining premium:", self.premium)

    def renew(self):

        if self.status == "Expired":
            self.status = "Active"
            print("Policy renewed successfully")
        else:
            print("Policy is already active")


# Create policies

policies = {
    "POL1001": Policy("POL1001", "Rahul", 25000, "Active"),
    "POL1002": Policy("POL1002", "Sneha", 18000, "Expired")
}


# Find Policy

def find_policy(policy_number):

    if not policy_number.startswith("POL"):
        raise ValueError("Invalid policy number")

    if policy_number not in policies:
        raise PolicyNotFoundException("Policy not found")

    return policies[policy_number]


# Main Program

try:

    policy_number = input("Enter Policy Number: ")

    policy = find_policy(policy_number)

    print("Customer:", policy.customer_name)
    print("Premium:", policy.premium)
    print("Status:", policy.status)

    amount = float(input("Enter payment amount: "))

    policy.pay_premium(amount)

except PolicyNotFoundException as e:

    print("Error:", e)

except PolicyExpiredException as e:

    print("Error:", e)

except ValueError as e:

    print("Error:", e)