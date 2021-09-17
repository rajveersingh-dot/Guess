import random


def main():
    min = 0
    max = 100
    randomInt = random.randrange(min, max)
    numOfGuessesLeft = 10
    guess = None

    while True:
        try:
            if numOfGuessesLeft > 0:
                guess = int(input("Enter your Guess: "))
        except ValueError:
            print("Wrong input!!!\nNumbers only.")
            continue

if __name__ == '__main__':
    main()
