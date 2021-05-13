def run():
    KM = 1609344
    MILE = 1 /KM

    client_choice = int(input("""
    Welcome to KimMil Calculator!
    Tell me, which choice should I calculate:
    1) From Miles to kilometers
    2) From Kilometers to Miles
    """))

    if client_choice == 1:
        miles_quantity = int(input('Miles to be converted: '))
        km = round(miles_quantity * KM, 2)
        txt = '{} miles are {} kilometers'
        print(txt.format(miles_quantity, km))
    elif client_choice == 2:
        km_quantity = int(input('Kilometers to be converted: '))
        miles = km_quantity * MILE
        txt = '{} kilometers are {} miles'
        print(txt.format(km_quantity, miles))
    else:
        print('Please choose 1 or 2 option')


if __name__ == "__main__":
    run()