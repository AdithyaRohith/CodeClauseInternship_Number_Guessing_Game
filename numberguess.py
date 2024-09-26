import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Guess the number I've picked (between 1 and 100).")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Great job! You found the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guess_number_game()
