def run():
    IL = int(input('Give an inferior limit point: '))
    SL = int(input('Give a superior limit point: '))

    while True:
        point = int(input('Introduce a random point: '))

        if point < IL:
            print('You number is under the limit')
        if point > SL:
            print('Your number is over the limit')
        if IL < point < SL:
            print('Your number is between the limits')
        if point == IL or point == SL:
            print('Your number is on one of the limits')


if __name__ == "__main__":
    run()