import random


# -----------------------------
# GAME STATE
# -----------------------------

health = 100
score = 0
inventory = []


# -----------------------------
# WELCOME
# -----------------------------

def welcome():
    print("=" * 40)
    print("       TEXT ADVENTURE GAME")
    print("=" * 40)
    print("Welcome, brave adventurer!")


# -----------------------------
# SHOW STATUS
# -----------------------------

def show_status():
    print("\n========== STATUS ==========")
    print("Health:", health)
    print("Score:", score)

    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Inventory: Empty")

    print("============================")


# -----------------------------
# FOREST
# -----------------------------

def forest():
    global score

    print("\n🌲 You enter a mysterious forest.")
    print("You see an old tree.")

    event = random.choice(["key", "nothing"])

    if event == "key":
        print("You discover a golden key!")
        inventory.append("key")
        score += 20

    else:
        print("You search the tree but find nothing.")

    input("\nPress Enter to continue...")


# -----------------------------
# CAVE
# -----------------------------

def cave():
    global health
    global score

    print("\n🕳️ You enter a dark cave.")
    print("Suddenly, a monster appears!")

    choice = input("Do you want to fight or run? ").lower()

    if choice == "fight":

        damage = random.randint(10, 40)
        health -= damage

        print("\n⚔️ You fight the monster!")
        print("The monster damages you by", damage)

        if health <= 0:
            health = 0
            print("💀 You have been defeated.")
            return False

        else:
            print("You defeat the monster!")
            score += 50
            return True

    elif choice == "run":

        print("\n🏃 You escape from the cave.")
        return True

    else:

        print("\nInvalid choice.")
        return True


# -----------------------------
# TREASURE ROOM
# -----------------------------

def treasure_room():
    global score

    print("\n🏆 You enter the treasure room.")

    if "key" in inventory:

        print("You use the golden key.")
        print("The treasure chest opens!")
        print("💰 You found a huge treasure!")

        score += 100

        return True

    else:

        print("The treasure room is locked.")
        print("You need a golden key.")

        return False


# -----------------------------
# POTION
# -----------------------------

def find_potion():
    global health
    global score

    print("\n🧪 You discover a magic potion.")

    inventory.append("potion")

    print("Potion added to inventory.")

    choice = input("Do you want to drink it? (yes/no): ").lower()

    if choice == "yes":

        health += 30

        if health > 100:
            health = 100

        inventory.remove("potion")

        print("❤️ Your health is now:", health)

        score += 10


# -----------------------------
# GAME OVER
# -----------------------------

def game_over():
    print("\n================================")
    print("           GAME OVER")
    print("================================")

    print("Final Score:", score)
    print("Final Health:", health)


# -----------------------------
# MAIN GAME
# -----------------------------

def start_game():

    welcome()

    forest()

    show_status()

    find_potion()

    show_status()

    result = cave()

    if not result:
        game_over()
        return

    show_status()

    treasure_room()

    show_status()

    print("\n🎉 Adventure Completed!")
    print("Final Score:", score)


# -----------------------------
# START PROGRAM
# -----------------------------

start_game()