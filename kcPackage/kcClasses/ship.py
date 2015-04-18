# -*- coding: utf-8 -*-
from kcUtility import _color

from kcShipData import get_ship_name

class Ship(object):
    def __init__(self, own_id, sortno, lv, nowhp, maxhp, cond, karyoku, raisou, taiku, soukou, kaihi, taisen, sakuteki, lucky):
        self.own_id = own_id
        self.sortno = sortno
        self.lv = lv
        self.nowhp = nowhp
        self.maxhp = maxhp
        self.cond = cond
        self.karyoku = karyoku
        self.raisou = raisou
        self.taiku = taiku
        self.soukou = soukou
        self.kaihi = kaihi
        self.taisen = taisen
        self.sakuteki = sakuteki
        self.lucky = lucky

    def print_info(self):
        msg = str(self.own_id) + "\t" + str(self.sortno) +  "\t" + str(self.lv) + "\t"
        name = str(get_ship_name(self.sortno))
        if name == 'None':
            msg += _color['red'] + name + _color['default']
        else:
            msg += name
        print(msg)
        # print("own_id " + str(self.own_id))
        # print("sortno " + str(self.sortno))
        # print("lv " + str(self.lv))
        # print("nowhp " + str(self.nowhp))
        # print("maxhp " + str(self.maxhp))
        # print("cond " + str(self.cond))
        # print("karyoku " + str(self.karyoku))
        # print("raisou " + str(self.raisou))
        # print("taiku " + str(self.taiku))
        # print("soukou " + str(self.soukou))
        # print("kaihi " + str(self.kaihi))
        # print("taisen " + str(self.taisen))
        # print("sakuteki " + str(self.sakuteki))
        # print("lucky " + str(self.lucky))
