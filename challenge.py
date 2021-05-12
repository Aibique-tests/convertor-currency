def run():
    SELL = int(input('Introduce custom value for selling: '))
    CONST = 100
    counter = 0

    while counter < CONST:
        counter += 1
        if counter == SELL:
            txt = 'Now you can sell BTN for {}'
            print(txt.format(counter))
            break
        text = 'Price of BTN at {}'
        print(text.format(counter))


if __name__ == "__main__":
    run()