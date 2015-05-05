# -*- coding: utf-8 -*-
# from kcUtility import _color
import kcUtility as u
import kcShipData
import kcZukan

class Ship(object):
    def __init__(self, local_id, sortno, lv, nowhp, maxhp, cond, karyoku, raisou, taiku, soukou, kaihi, taisen, sakuteki, lucky):
        self.local_id  = local_id
        self.sortno    = sortno
        self.lv        = lv
        self.nowhp     = nowhp
        self.maxhp     = maxhp
        self.cond      = cond
        self.karyoku   = karyoku
        self.raisou    = raisou
        self.taiku     = taiku
        self.soukou    = soukou
        self.kaihi     = kaihi
        self.taisen    = taisen
        self.sakuteki  = sakuteki
        self.lucky     = lucky
        # 建娘的官方名字
        self.name      = kcShipData.get_ship_name_by_id(self.sortno)
        if self.name is None:
            u.uprint("Missing name, local_id:{0:>4d}, lv:{1:>3d}".format(self.local_id, self.lv) , 'red')

        self.nick_name = kcShipData.get_ship_nick_name_by_id(self.sortno)

        if self.name is None:
            self.stype = None
        else:
            self.stype = kcZukan.get_stype_by_name(self.name)
        self.dmghp     = self.maxhp - self.nowhp

        if self.stype is None:
            u.uprint("Missing stype, local_id:{0:>4d}, lv:{1:>3d}".format(self.local_id, self.lv) , 'red')

    def print_info(self):
        msg = str(self.local_id) + "\t" + str(self.sortno) +  "\t" + str(self.lv) + "\t"
        name = self.name
        if name is None:
            msg += u.color['red'] + "Could not find name" + u.color['default']
        else:
            msg += name
        print(msg)
        # print("local_id " + str(self.local_id))
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
