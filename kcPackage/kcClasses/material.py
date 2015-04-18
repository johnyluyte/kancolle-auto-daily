# -*- coding: utf-8 -*-

class Material(object):
    def __init__(self, itemsValue):
        self.items  = [["燃料",0], ["彈藥",0], ["鋼材",0], ["機材",0], ["高速建造",0], ["高速修復",0], ["建造資材",0], ["改修資材",0]]
        for i in range(len(self.items)):
            self.items[i][1] = itemsValue[i]

    def print_info(self):
        for tmp in self.items:
            print(tmp[0] + ": " + str(tmp[1]))
