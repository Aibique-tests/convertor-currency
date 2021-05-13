import random
def generator():
    upper_list = ['A', 'B','C', 'D', 'E', 'F', 'G']
    low_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(',')']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    characters = upper_list + low_list + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)
    
    password = ''.join(password)
    return password


def run():
    password = generator()
    txt = 'Your new password is {}'
    print(txt.format(password))


if __name__ == "__main__":
    run()