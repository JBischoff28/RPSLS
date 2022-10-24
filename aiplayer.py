from unicodedata import name
from player import Player
import time
import random

class AI(Player):

    def __init__(self):
        super().__init__()

    def ai_action_select(self):

        selected_action = random.choice(self.action_list)
        time.sleep(0.5)
        print(f"{self.name} has selected {selected_action}!")