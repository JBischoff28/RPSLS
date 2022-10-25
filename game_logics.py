import time
from humanplayer import Human
from aiplayer import AI



def game_intro ():

    print("Welcome to the a game of Rock, Paper, Scissors, Lizard, Spock!")
    print("")
    time.sleep(2)
    print("The game will go on until a player wins best of three rounds.")
    print("Number keys will be used to determine which action a player would like to choose.")
    print("")
    print("")
    print("")
    print("")

def player_count ():

    amount_of_players = input("How many players would you like to play with? 0, 1, or 2?\n")

    if amount_of_players == "0":
        time.sleep(1)
        print("")
        ai_game_logic()
    elif amount_of_players == "1":
        time.sleep(1)
        print("")
        singleplayer_game_logic()
    elif amount_of_players == "2":
        time.sleep(1)
        print("")
        multiplayer_game_logic()
    else:
        print("The number of players you have selected is invalid.\nPlease reselect!")
        print("")
        print("")
        time.sleep(1)
        player_count()

def win_check(player_one, player_two, player_one_pick, player_two_pick):

    print(f"{player_one.name} picked {player_one_pick} and {player_two.name} picked {player_two_pick}")

    if player_one_pick == player_two_pick:
        print("This round is a tie! Starting next round...")
        pass
    elif player_one_pick != player_two_pick and player_one_pick == "Rock":
        if player_two_pick == "Scissors" or player_two_pick == "Lizzard":
            print(f"{player_one.name} wins the round!")
            print("")
            print("")
            player_one.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
        else:
            print(f"{player_two.name} wins the round!")
            print("")
            print("")
            player_two.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
    elif player_one_pick != player_two_pick and player_one_pick == "Scissors":
        if player_two_pick == "Paper" or player_two_pick == "Lizard":
            print(f"{player_one.name} wins the round!")
            print("")
            print("")
            player_one.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
        else:
            print(f"{player_two.name} wins the round!")
            print("")
            print("")
            player_two.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
    elif player_one_pick != player_two_pick and player_one_pick == "Paper":
        if player_two_pick == "Rock" or player_two_pick == "Spock":
            print(f"{player_one.name} wins the round!")
            print("")
            print("")
            player_one.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
        else:
            print(f"{player_two.name} wins the round!")
            print("")
            print("")
            player_two.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
    elif player_one_pick != player_two_pick and player_one_pick == "Lizard":
        if player_two_pick == "Paper" or player_two_pick == "Spock":
            print(f"{player_one.name} wins the round!")
            print("")
            print("")
            player_one.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
        else:
            print(f"{player_two.name} wins the round!")
            print("")
            print("")
            player_two.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
    elif player_one_pick != player_two_pick and player_one_pick == "Spock":
        if player_two_pick == "Scissors" or player_two_pick == "Rock":
            print(f"{player_one.name} wins the round!")
            print("")
            print("")
            player_one.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)
        else:
            print(f"{player_two.name} wins the round!")
            print("")
            print("")
            player_two.add_score()
            time.sleep(0.75)
            player_one.display_score(player_two)

    if player_one.score == 2:
        print(f"{player_one.name} is the WINNER in the best of three!")
        player_one.win = True
        player_two.win = True
    elif player_two.score == 2:
        print(f"{player_two.name} is the WINNER in the best of three!")
        player_two.win = True
        player_one.win = True
    else:
        player_one.win = False
        player_two.win = False
        pass

def multiplayer_game_logic():
    
    print("Creating player one...")
    print("")
    player_one = Human()

    time.sleep(1)

    print("Creating player two...")
    print("")
    player_two = Human()

    print(f"This match is between {player_one.name} and {player_two.name}.")
    print("")
    print("")
    print("")
    print(f"The game has started! {player_one.name}, you go first!")
    time.sleep(1.5)

    while player_one.win == False or player_two.win == False:
        
        player_one.display_actions()
        print(f"{player_one.name}, it is your turn!")
        player_one_pick = player_one.pick_action()
        time.sleep(0.5)
        print("")
        print("")

        player_two.display_actions()
        print(f"{player_two.name}, it is your turn!")
        player_two_pick = player_two.pick_action()
        time.sleep(0.5)
        print("")
        print("")

        win_check(player_one, player_two, player_one_pick, player_two_pick)
    
    print("")
    print("")
    play_again()

def singleplayer_game_logic():

    player_one = Human()
    player_two = AI()

    print(f"This match is between {player_one.name} and {player_two.name}.")
    print("")
    print("")
    print("")
    print(f"The game has started! {player_one.name}, you go first!")
    time.sleep(1.5)

    while player_one.win == False or player_two.win == False:
        
        player_one.display_actions()
        player_one_pick = player_one.pick_action()
        time.sleep(0.5)
        print("")
        print("")

        time.sleep(1)

        print(f"{player_two.name}, it is your turn!")
        time.sleep(1.5)
        player_two_pick = player_two.ai_action_select()
        time.sleep(0.5)
        print("")
        print("")

        win_check(player_one, player_two, player_one_pick, player_two_pick)
    
    print("")
    print("")
    play_again()

def ai_game_logic():

    player_one = AI()
    player_two = AI()

    print(f"This match is between {player_one.name} and {player_two.name}.")
    print("")
    print("")
    print("")
    print(f"The game has started! {player_one.name}, you go first!")
    time.sleep(1.5)

    while player_one.win == False or player_two.win == False:
        
        player_one_pick = player_one.ai_action_select()
        time.sleep(0.5)
        print("")
        print("")

        time.sleep(3)

        print(f"{player_two.name}, it is your turn!")
        player_two_pick = player_two.ai_action_select()
        time.sleep(0.5)
        print("")
        print("")

        win_check(player_one, player_two, player_one_pick, player_two_pick)

    print("")
    print("")
    play_again()

def play_again():

    print("")
    print("")
    print("")
    print("Thank you for playing a game of Rock, Paper, Scissors, Lizard, Spock!")

    play_check = input("Would you like to play again?")

    if play_check == "Yes" or play_check == "yes" or play_check == "y" or play_check == "Y":

        print("Awesome! Hold tight while we set up another match!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        print("")
        print("")

        player_count()

    elif play_check == "No" or play_check == "no" or play_check == "n" or play_check == "N":

        print("See ya later!")
        quit()

    else:
        print("Invalid response! Please reselect.")
        play_again()
