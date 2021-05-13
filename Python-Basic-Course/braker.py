def run():
    # for counter in range(1000):
    #     if counter % 2 != 0:
    #         continue
    #     print(counter)
    # for i in range(10000):
    #     print(i)
    #     if i == 3456:
    #         break
    txt = input("Write a text: ")
    for letter in txt:
        if letter == 'o':
            break
        print(letter)


if __name__ == "__main__":
    run()