"""
Mr.kataei 2/19/2022
"""


class Player:
    def __init__(self, name: str):
        """
        :param name: name of player
        """
        self.name: str = name
        self.turn: bool = False     # at first not player turn

    def change_turn(self):
        """
        :return: change player turn
        """
        if self.turn:
            self.turn = False
        else:
            self.turn = True


def __init__():
    pass