import random
import time

#snakes and ladders positions
snakes = {16: 6, 48: 30, 62: 19, 64: 60, 79: 19, 93: 68, 95: 24, 97: 76}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

#Player positions
player_pos = [0, 0]
player_names = ["Player 1", "Player 2"]

def roll_dice():
    return random.randint(1, 6)

def move_player(player_index):
    input(f"{player_names[player_index]}, press Enter to roll the dice...")
    dice = roll_dice()
    print(f"{player_names[player_index]} rolled a {dice}!")
    
    player_pos[player_index] += dice
    
    #Check for snakes or ladders
    if player_pos[player_index] in snakes:
        print(f"Oh no! {player_names[player_index]} got bitten by a snake!")
        player_pos[player_index] = snakes[player_pos[player_index]]
    elif player_pos[player_index] in ladders:
        print(f"Yay! {player_names[player_index]} climbed a ladder!")
        player_pos[player_index] = ladders[player_pos[player_index]]
    
    #Check if player crossed 100
    if player_pos[player_index] > 100:
        player_pos[player_index] = 100 - (player_pos[player_index] - 100)
    
    print(f"{player_names[player_index]} is now on square {player_pos[player_index]}\n")
    time.sleep(1)

def check_winner():
    for i, pos in enumerate(player_pos):
        if pos == 100:
            return i
    return -1

# Game Loop
print("Welcome to Snake and Ladder Game!\n")
time.sleep(1)

while True:
    for i in range(2):
        move_player(i)
        winner = check_winner()
        if winner != -1:
            print(f" {player_names[winner]} wins the game! ")
            exit()
