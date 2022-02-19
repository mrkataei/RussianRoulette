import random


class Gun:
    def __init__(self):
        self.__magazine = [False] * 6
        self.reload()

    def get_magazine(self):
        return self.__magazine

    def reload(self):
        self.__magazine = [False] * 6
        self.__magazine[random.randint(0, 5)] = True

