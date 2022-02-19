"""
Mr.kataei 2/19/2022
"""
import random


class Gun:
    def __init__(self):
        """
        the gun has magazine with 6 empty and reload it at first for put 1 bullet in magazine
        """
        self.__magazine = [False] * 6
        self.reload()

    def get_magazine(self):
        """
        :return: array of bool, get randomly bullet in magazine
        """
        return self.__magazine

    def reload(self):
        self.__magazine = [False] * 6
        self.__magazine[random.randint(0, 5)] = True

