# -*- coding: utf-8 -*-

# 艦隊資訊
class Deck(object):
    def __init__(self, name, ships, mission):
        self.name = name
        self.ships = ships
        self.mission = mission

    def get_info(self):
        result = dict()
        result['name'] = self.name
        result['ships'] = self.ships
        result['mission'] = self.mission
        return result

    def print_info(self):
        print(self.name)
        print("船隻" + str(self.ships))
        print("任務" + str(self.mission))

