from player import Player
import time
import getpass


class Human(Player):

    def __init__(self):
        super().__init__()
        self.name = "Player"
        self.set_name()

    def pick_action(self):

        selected_action = getpass.getpass(f"{self.name}, enter a number to select an action: ")

        if selected_action == "0":
            selected_action = self.action_list[0]
            time.sleep(0.5)
            print(f"{self.name} has made a selection!")
            return selected_action
        elif selected_action == "1":
            selected_action = self.action_list[1]
            time.sleep(0.5)
            print(f"{self.name} has made a selection!")
            return selected_action
        elif selected_action == "2":
            selected_action = self.action_list[2]
            time.sleep(0.5)
            print(f"{self.name} has made a selection!")
            return selected_action
        elif selected_action == "3":
            selected_action = self.action_list[3]
            time.sleep(0.5)
            print(f"{self.name} has made a selection!")
            return selected_action
        elif selected_action == "4":
            selected_action = self.action_list[4]
            time.sleep(0.5)
            print(f"{self.name} has made a selection!")
            return selected_action
        else:
            print("Invalid response. Please choose a valid option!")
            time.sleep(1)
            self.pick_action()
