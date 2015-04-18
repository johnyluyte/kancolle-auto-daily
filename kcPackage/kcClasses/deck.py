# -*- coding: utf-8 -*-

# 艦隊資訊
class Deck(object):
    def __init__(self, name, ships, mission):
        self.name = name
        self.ships = ships
        self.mission = mission
    def print_info(self):
        print(self.name)
        print("船隻" + str(self.ships))
        print("任務" + str(self.mission))

