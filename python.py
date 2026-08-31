import random
number = random.randint(1, 10)
guess = int(input("Guess the number from 1 to 10: "))
def ask_random_number():
    guess = int(input("Guess the number from 1 to 10: "))
    return guess
while guess != number:
    guess = ask_random_number()