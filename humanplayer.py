from player import Player
import time
import getpass


class Human(Player):

    def __init__(self, player_type):
        super().__init__(player_type)

    def pick_action(self):

        selected_action = getpass.getpass("Enter a number to select an action!\n")

        if selected_action == "0":
            time.sleep(0.5)
            print(f"{self.name} selected Rock!")

player_one = Human("Human")
player_one.pick_action()