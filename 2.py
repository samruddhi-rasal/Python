import random

best_score = None

while True:

    print("\n===================================")
    print("       NUMBER GUESSING GAME")
    print("===================================")

    print("\nChoose Difficulty Level:")
    print("1. Easy   (1 - 50, 10 attempts)")
    print("2. Medium (1 - 100, 7 attempts)")
    print("3. Hard   (1 - 500, 10 attempts)")

    # Difficulty selection
    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3): "))

            if choice in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # Set difficulty
    if choice == 1:
        maximum = 50
        max_attempts = 10
        difficulty = "Easy"

    elif choice == 2:
        maximum = 100
        max_attempts = 7
        difficulty = "Medium"

    else:
        maximum = 500
        max_attempts = 10
        difficulty = "Hard"

    # Generate secret number
    secret_number = random.randint(1, maximum)

    attempts = 0
    won = False

    print("\n-----------------------------------")
    print("Difficulty:", difficulty)
    print("Guess a number between 1 and", maximum)
    print("Maximum attempts:", max_attempts)
    print("-----------------------------------")

    # Game loop
    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            # Validate range
            if guess < 1 or guess > maximum:
                print(f"Please enter a number between 1 and {maximum}.")
                continue

        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        attempts += 1

        # Correct guess
        if guess == secret_number:
            won = True

            print("\n🎉 Congratulations!")
            print("You guessed the correct number.")
            print("Number:", secret_number)
            print("Attempts:", attempts)

            # Score calculation
            score = (max_attempts - attempts + 1) * 10

            print("Score:", score)

            # Best score
            if best_score is None or score > best_score:
                best_score = score
                print("🏆 New Best Score!")

            else:
                print("Best Score:", best_score)

            break

        # Hint: very close
        elif abs(guess - secret_number) <= 5:
            if guess < secret_number:
                print("🔥 Very Close! But Too Low!")
            else:
                print("🔥 Very Close! But Too High!")

        # Normal hints
        elif guess < secret_number:
            print("Too Low! Try Again.")

        else:
            print("Too High! Try Again.")

        # Show remaining attempts
        remaining = max_attempts - attempts

        if remaining > 0:
            print("Attempts remaining:", remaining)

    # If player loses
    if not won:
        print("\n❌ Game Over!")
        print("You used all", max_attempts, "attempts.")
        print("The correct number was:", secret_number)

        if best_score is not None:
            print("Your Best Score:", best_score)

    # Play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again in ["yes", "y"]:
            break

        elif play_again in ["no", "n"]:
            print("\n===================================")
            print("Thanks for playing! 👋")
            print("Final Best Score:", best_score)
            print("===================================")
            exit()

        else:
            print("Please enter yes or no.")