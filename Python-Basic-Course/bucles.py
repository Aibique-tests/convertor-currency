# 2 * 2 * 2 * n = 1000

def loop():
    CONST = 1000
    n = 0
    potential_2 = 2**n

    while potential_2 < CONST:
        txt = 'Potential of 2 is: {}'
        print(txt.format(potential_2))
        n = n + 1
        potential_2 = 2**n

if __name__ == "__main__":
    loop()