class Policy:

    def __init__(self, policy_number, customer_name, policy_type, premium):
        self.policy_number = policy_number
        self.customer_name = customer_name
        self.policy_type = policy_type
        self.premium = premium

    def display(self):
        print("Policy Number:", self.policy_number)
        print("Customer:", self.customer_name)
        print("Policy Type:", self.policy_type)
        print("Premium:", self.premium)


# Create object
policy1 = Policy("POL1001", "Rahul", "Life", 25000)

# Call method
policy1.display()


#Encapsulation
class Claim:

    def __init__(self, claim_id, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def update_amount(self, amount):
        if amount > 0:
            self.__amount = amount


claim1 = Claim("C101", 50000)

print(claim1.get_amount())

claim1.update_amount(75000)

print(claim1.get_amount())


#Inheritance
class Employee:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display(self):
        print(self.employee_id, self.name)


class Agent(Employee):

    def sell_policy(self):
        print("Selling insurance policy")


class ClaimsOfficer(Employee):

    def process_claim(self):
        print("Processing claim")


# Agent object
agent = Agent(101, "Rahul")

agent.display()
agent.sell_policy()


# Claims Officer object
officer = ClaimsOfficer(102, "Sneha")

officer.display()
officer.process_claim()


#Abstraction
from abc import ABC, abstractmethod


class Insurance(ABC):

    @abstractmethod
    def buy_policy(self):
        pass


class LifeInsurance(Insurance):

    def buy_policy(self):
        print("Life insurance policy purchased")


class HealthInsurance(Insurance):

    def buy_policy(self):
        print("Health insurance policy purchased")


# Objects
life = LifeInsurance()
health = HealthInsurance()

life.buy_policy()
health.buy_policy()


#Polymorphism
class LifePolicy:

    def calculate_premium(self):
        return 25000


class HealthPolicy:

    def calculate_premium(self):
        return 18000


class MotorPolicy:

    def calculate_premium(self):
        return 12000


policies = [
    LifePolicy(),
    HealthPolicy(),
    MotorPolicy()
]

for policy in policies:
    print(policy.calculate_premium())