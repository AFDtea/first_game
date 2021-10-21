import random

user_wins = 0
comp_wins = 0

options = ['rock', 'paper', 'scissors']

def play():
    while True:
        # user = input("Type Rock/Paper/Scissors or Q to quit.").lower()
        user = input("rock/paper/scissors: ").lower()

        if user == 'q':
            break

        if user not in options:
            continue

        comp = random.randint(0, 2)
        comp_guess = options[comp]
        # print(f'Computer chose {comp_guess}.')
        print(f'Troll chose {comp_guess}.')
        if user == 'rock' and comp_guess == 'scissors':
            print("You win!")
            # user_wins += 1
            # continue
            return True
        elif user == 'paper' and comp_guess == 'rock':
            print("You win!")
            # user_wins += 1
            # continue
            return True
        elif user == 'scissors' and comp_guess == 'paper':
            print("You win!")
            # user_wins += 1
            # continue
            return True
        elif user == 'rock' and comp_guess == 'rock':
            print("Tie. Go again.")
            continue
        elif user == 'paper' and comp_guess == 'paper':
            print("Tie. Go again.")
            continue
        elif user == 'scissors' and comp_guess == 'scissors':
            print("Tie. Go again.")
            continue
        else:
            print("You lost!")
            # comp_wins += 1
            return False
