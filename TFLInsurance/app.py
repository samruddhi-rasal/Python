#8.md

import json

FILE = "policies.json"


# READ ALL POLICIES
def get_all_policies():

    try:
        with open(FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# CREATE POLICY
def create_policy():

    policy_number = input("Enter policy number: ")
    customer_name = input("Enter customer name: ")
    premium = float(input("Enter premium: "))

    if not policy_number.startswith("POL"):
        print("Invalid policy number")
        return

    if premium <= 0:
        print("Invalid premium")
        return

    policies = get_all_policies()

    # Check duplicate
    for policy in policies:
        if policy["policy_number"] == policy_number:
            print("Policy already exists")
            return

    new_policy = {
        "policy_number": policy_number,
        "customer_name": customer_name,
        "premium": premium,
        "status": "Active"
    }

    policies.append(new_policy)

    with open(FILE, "w") as file:
        json.dump(policies, file, indent=4)

    print("Policy created successfully")


# FIND POLICY
def find_policy():

    policy_number = input("Enter policy number: ")

    policies = get_all_policies()

    for policy in policies:

        if policy["policy_number"] == policy_number:
            print(policy)
            return

    print("Policy not found")


# UPDATE POLICY
def update_policy():

    policy_number = input("Enter policy number: ")

    policies = get_all_policies()

    for policy in policies:

        if policy["policy_number"] == policy_number:

            new_name = input("Enter new customer name: ")
            new_premium = float(input("Enter new premium: "))

            policy["customer_name"] = new_name
            policy["premium"] = new_premium

            with open(FILE, "w") as file:
                json.dump(policies, file, indent=4)

            print("Policy updated successfully")
            return

    print("Policy not found")


# DELETE POLICY
def delete_policy():

    policy_number = input("Enter policy number: ")

    policies = get_all_policies()

    for policy in policies:

        if policy["policy_number"] == policy_number:

            policies.remove(policy)

            with open(FILE, "w") as file:
                json.dump(policies, file, indent=4)

            print("Policy deleted successfully")
            return

    print("Policy not found")


# MAIN MENU

while True:

    print("\n--- TFL INSURANCE ---")

    print("1. Create Policy")
    print("2. Get All Policies")
    print("3. Find Policy")
    print("4. Update Policy")
    print("5. Delete Policy")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_policy()

    elif choice == "2":
        policies = get_all_policies()

        for policy in policies:
            print(policy)

    elif choice == "3":
        find_policy()

    elif choice == "4":
        update_policy()

    elif choice == "5":
        delete_policy()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")