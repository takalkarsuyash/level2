import random
number = random.randint(1, 100)
print("Guess a number between 1 and 100.")
guess_count = 0
while True:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess == number:
        print(f"Congratulations! You guessed the number in {guess_count} tries.")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
