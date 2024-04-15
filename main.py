import random

def guessing_game():

    minimum = random.randint(1, 500)
    maximum = random.randint(1, 500)

    if maximum < minimum:
        temp = minimum
        minimum = maximum
        maximum = temp

    number = random.randint(minimum, maximum)
    tries = 0

    while True and tries < 5:
        print(f"From the range of {minimum} and {maximum}")
        guess = int(input("Enter Your Guess: "))

        if guess == number:
            break

        if guess < number:
            print("\nHigher!", end=" ")
        else:
            print("\nLower!", end=" ")

        print("guess again")
        tries += 1

    if tries == 5:
        print("You lose")

def main():
    guessing_game()


if __name__ == "__main__":
    main()