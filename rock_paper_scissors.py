# Setting the start of game , either we going to play or not, depending on  decision of player .
import random

start = 'Y'
end = 'N'
print(f"Do you want to play 'Rock, Paper, Scissors'?"
      f"Type [Y]es or [N]o ")
player_answer = input().upper()
while player_answer != 'N':
    # Setting the input data
    rock = 'r'
    paper = 'p'
    scissors = 's'
    cpu_move = ''
    # Game conditions for one player
    player_1_move = input(f'Choose between [r]ock, [p]aper or [s]cissors: ')
    if player_1_move == 'r':
        player_move = 'Rock'
    elif player_1_move == 'p':
        player_move = 'Paper'
    elif player_1_move == 's':
        player_move = 'Scissors'
    else:
        print("Invalid input: Try again.....")
        continue
    cpu_move = random.randint(1, 3)
    if cpu_move == 1:
        cpu_move = 'Rock'
    elif cpu_move == 2:
        cpu_move = 'Paper'
    elif cpu_move == 3:
        cpu_move = 'Scissors'
    print(f"The computer chose {cpu_move}.")
    if (player_move == rock and cpu_move == scissors)\
            or (player_move == scissors and cpu_move == paper)\
            or (player_move == paper and cpu_move == rock):
        print("You Win")
    elif player_move == cpu_move:
        print("Draw")
    else:
        print("You Lose")

    print(f"Do you want to play 'Rock, Paper, Scissors' again....?"
          f"Type [Y]es or [N]o ")
    player_answer = input().upper()
