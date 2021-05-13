import random

def comparative(computer_choice, computer_points, client_points):
    print(computer_points)
    print(client_points)
    client_choice = input('Choose a weapon: ')

    if computer_choice == client_choice:
        print('draw!')

    if client_choice == 'Paper':
        if computer_choice == 'Rock':
            print('You win! +1 for you')
            client_points.append(1)
            return client_points
        if computer_choice == 'Scissors':
            print('You loose! +1 for computer')
            computer_points.append(1)
            return computer_points
    if client_choice == 'Rock':
        if computer_choice == 'Paper':
            print('You loose! +1 for computer')
            computer_points.append(1)
            return computer_points
        if computer_choice == 'Scissors':
            print('You win! +1 point for you')
            client_points.append(1)
            return client_points
    if client_choice == 'Scissors':
        if computer_choice == 'Rock':
            print('You loose! +1 for computer')
            computer_points.append(1)
            return computer_points
        if computer_choice == 'Paper':
            print('You win! +1 point for you')
            client_points.append(1)
            return client_points


def run():
    tools = ['Rock','Scissors','Paper']
    computer_points = []
    client_points = []
    print("""
    Welcome to P-R-S game!
    Please choose a tool. Example:
    Rock | Scissors | Paper
    Good luck!
    """)

    while len(computer_points) < 3 and len(client_points) <3:
        computer_choice = random.choice(tools)
        comparative(computer_choice, computer_points, client_points)

    if len(computer_points) == 3:
        print('Game Ove. You lose')
    if len(client_points) == 3:
        print('Congratulations!! You won !')



if __name__ == "__main__":
    run()