
class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.turn: bool = False

    def change_turn(self):
        if self.turn:
            self.turn = False
        else:
            self.turn = True
