import time



def game_intro ():

    print("Welcome to the a game of Rock, Paper, Sissors, Lizard, Spock!")
    print("")
    time.sleep(2)
    print("The game will go on until a player wins best of three rounds.")
    print("Number keys will be used to determine which action a player would like to choose.")
    print("")
    print("")
    print("")

def player_count ():

    amount_of_players = input("How many players would you like to play with? 0, 1, or 2?\n")

    if amount_of_players == "0":
        time.sleep(1)
        pass
    elif amount_of_players == "1":
        time.sleep(1)
        pass
    elif amount_of_players == "2":
        time.sleep(1)
        pass
    else:
        print("The number of players you have selected is invalid.\nPlease reselect!")
        print("")
        time.sleep(1)
        player_count()

game_intro()
player_count()