# obj.values() | obj.items()
def run():
    obj = {
        'Hola': 'Hola mundo',
        'Adios': 'Adios mundo',
        'Tardes': 'Buenas Tardes',
        'Noches': 'Buenas Noches'
    }
    answer = input('Choose a time: ')
    print(obj[answer])
    print(obj.values())
    print(obj.items())

if __name__ == "__main__":
    run()