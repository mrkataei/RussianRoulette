"""
Mr.kataei 2/19/2022
"""
from time import sleep
import random
from GamePlay.gun import Gun
from GamePlay.player import Player


class Play:
    def __init__(self, first_player: str, sec_player: str):
        """
        :param first_player: name of first player
        :param sec_player: name od sec player
        """
        self._first_player = Player(name=first_player)  # create object of player
        self._sec_player = Player(name=sec_player)
        self.who_first()    # lets roll the dice for turn
        self.__gun = Gun()
        self._magazine = self.__gun.get_magazine()

    def who_first(self):
        """
        :return: random player turn
        """
        if random.randint(0, 1):
            self._first_player.turn = True
        else:
            self._sec_player.turn = True

    def run(self):
        """
        :return:
        """
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
