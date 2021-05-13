# Colombian. Mexivan, Argentinian Pesos
menu = """
Welcome to convertor TopiTop :D

1 - Colombian Pesos
2 - Argentinian Pesos
3 - Mexican Pesos

Choose an Option:
"""
option = int(input(menu))

def operation(dollar_value):
    currency = float(input('Please, introduce a currency: '))
    dollar = str(round(currency/dollar_value, 2))
    print('You have $'+ dollar + ' dollars')

if option == 1:
    operation(2875)
elif option == 2:
    operation(65)
elif option == 3:
    operation(24)
else:
    print('Error Error ... Option not found! D:')