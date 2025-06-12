import random

print(" Advanced Number Guessing Game")

score = 0

while True:
    secret_number = random.randint(1, 20)
    tries = 0
    max_tries = 5

    print("\nGuess a number between 1 and 20! (You have", max_tries, "tries)")

    while tries < max_tries:
        try:
            guess = int(input("Your guess: "))
            tries += 1

            if guess == secret_number:
                print("Great! You guessed the correct number!")
                score += 1
                break
            elif guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

    if guess != secret_number:
        print("You lost! The correct number was:", secret_number)

    print("Your current score:", score)

    again = input("Do you want to play again? (yes / no): ")
    if again.lower() != "yes":
        print("Game over. Final score:", score)
        break