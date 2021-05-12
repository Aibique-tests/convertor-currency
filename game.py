# We have to guess the computer chose
import random


def run():
    computer_n = random.randint(1,100)
    client_n = int(input('Choose a number from 1 to 100: '))
    while computer_n != client_n:
        if client_n < computer_n:
            print('Look for a bigger number')
        else:
            print("Look for a smaller number")
        client_n = int(input('Choose a new number: '))
    print('You win !!')


if __name__ == "__main__":
    run()