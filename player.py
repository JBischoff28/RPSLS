import time


class Player:

    def __init__(self, player_type, actions):
        self.name = "Player One"
        self.type = player_type
        self.action = actions
        self.set_name()

    def set_name(self):

        name_check = input("Would you like to keep the generic player name?\n")
        print("")
        time.sleep(1)

        valid_answer = False

        while valid_answer == False:

            if name_check == "Yes" or name_check == "yes" or name_check == "Y" or name_check == "y":
                valid_answer = True
            elif name_check == "No" or name_check == "no" or name_check == "N" or name_check == "n":
                self.name = input("What is this player's name?\n")
                print("")
                time.sleep(1.5)
                print(f"Player One has been renamed to {self.name}.")
                valid_answer = True
            else:
                print("Invalid answer! Please reselect.")
                valid_answer = False




player_one = Player("Temp", "Temp")