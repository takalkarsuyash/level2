#number guesser
import random
print("Enter the range of numbers (minimum and maximum):")
min_num = int(input("Minimum: "))
max_num = int(input("Maximum: "))
number = random.randint(min_num, max_num)
print(f"Guess a number between {min_num} and {max_num}.")
guess_count = 0
while True:
    guess = int(input("Enter your guess: "))
    guess_count +1
    if guess == number:
        print(f"Congratulations! You guessed the number in {guess_count} tries.")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")

    else:
        print("Your guess is too high. Try again.")
