import time
from humanplayer import Human
from aiplayer import AI



def game_intro ():

    print("Welcome to the a game of Rock, Paper, Sissors, Lizard, Spock!")
    print("")
    time.sleep(2)
    print("The game will go on until a player wins best of three rounds.")
    print("Number keys will be used to determine which action a player would like to choose.")
    print("")
    print("")
    print("")
    print("")

def player_count (player_one, player_two):

    amount_of_players = input("How many players would you like to play with? 0, 1, or 2?\n")

    if amount_of_players == "0":
        time.sleep(1)
        player_one = AI
        player_two = AI
    elif amount_of_players == "1":
        time.sleep(1)
        player_one = Human
        player_two = AI
    elif amount_of_players == "2":
        time.sleep(1)
        player_one = Human
        player_two = Human
    else:
        print("The number of players you have selected is invalid.\nPlease reselect!")
        print("")
        print("")
        time.sleep(1)
        player_count()
    return player_one, player_two

def win_check():

    

    pass

def multiplayer_game_logic(player_one, player_two):
    
    print(f"The game has started! {player_one.name}, you go first!")
    time.sleep(1.5)

    while player_one.win == False or player_two.win == False:
        
        player_one.pick_action
        time.sleep(0.5)
        print("")
        print("")

        print(f"{player_two.name}, it is your turn!")
        player_two.pick_action
        time.sleep(0.5)



