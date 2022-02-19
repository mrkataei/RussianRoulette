from time import sleep
import random
from player import Player
from gun import Gun


class Play:
    def __init__(self, first_player: str, sec_player: str):
        self._first_player = Player(name=first_player)
        self._sec_player = Player(name=sec_player)
        self.who_first()
        self.__gun = Gun()
        self._magazine = self.__gun.get_magazine()

    def who_first(self):
        if random.randint(0, 1):
            self._first_player.turn = True
        else:
            self._sec_player.turn = True

    def run(self):
        for index, bullet in enumerate(self._magazine):
            if self._first_player.turn:
                print(self._first_player.name, 'is shooting..')
                if bullet:
                    print(self._first_player.name, 'fucked up!')
                    break
                print('so close!')
                sleep(2)
            if self._sec_player.turn:
                print(self._sec_player.name, 'is shooting..')
                if bullet:
                    print(self._sec_player.name, ' Fucked up!')
                    break
                print('so close!')
                sleep(2)
            print(6 - index, "Bullets remain ...", "\n------------------------------------------")
            if index > 2:
                print('The end is near ... ')
                sleep(5)
            self._first_player.change_turn()
            self._sec_player.change_turn()
