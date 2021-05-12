def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            return True


def run():
    n = int(input('write a number: '))
    if is_prime(n):
        print('It is prime')
    else:
        print('It is NOT prime')

if __name__ == "__main__":
    run()