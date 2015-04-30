# -*- coding: utf-8 -*-
import math

import kcUtility as u
import kcShipData

class Player(object):
    def __init__(self):
        self.materials   = None
        self.decks       = [None, None, None, None]
        self.ndocks      = [None, None, None, None]
        self.ships       = [None] * 100  # 意義同上，建立 1 個含有 100 個 None 的 list
        self.ships_count = 0

    def print_info_materials(self):
        if self.materials is None:
            u.uerror("[Player][print_info_materials] Not initialized")
            return
        self.materials.print_info()

    def print_info_decks(self, deck_id = 5):
        if self.decks[0] is None:
            u.uerror("[Player][print_info_decks] Not initialized")
            return
        # 印出所有的艦隊狀態
        if deck_id == 5:
            for i in range(0,4):
                if self.decks[i] is None: continue
                self.decks[i].print_info()
        # 印出某個指定的艦隊狀態
        elif deck_id > 0 and deck_id < 5 and (self.decks[deck_id-1] is not None):
            self.decks[deck_id-1].print_info()
        else:
            u.uerror("[Player][print_info_decks] Invalid deck_id")

    def print_info_ndocks(self, dock_id = 5):
        if self.ndocks[0] is None:
            u.uerror("[Player][print_info_ndocks] Not initialized")
            return
        # 印出所有的修船廠狀態
        if dock_id == 5:
            for i in range(0,4):
                if self.ndocks[i] is None: continue
                self.ndocks[i].print_info()
        # 印出某個指定的修船廠狀態
        elif dock_id > 0 and dock_id < 5 and (self.ndocks[dock_id-1] is not None):
            self.ndocks[dock_id-1].print_info()
        else:
            u.uerror("[Player][print_info_ndocks] Invalid dock_id")

    """
    TODO: 應該改成輸入船的名字也可以印出來!?
    總之這邊先做成    用 list 的 index  來搜尋，先全部印出來，意思到就好
    """
    def print_info_ships(self, ship_in_list = 1):
        if self.ships[0] is None:
            u.uerror("[Player][print_info_ships] Not initialized")
            return
        # 印出某個指定的船狀態，以在 list 的順序印出來，
        if ship_in_list > 0 and ship_in_list <= 100:
            if self.ships[ship_in_list-1] is not None:
                self.ships[ship_in_list-1].print_info()
            else:
                return
        else:
            u.uerror("[Player][print_info_ships] Invalid ship_in_list")

    def print_info_ships_count(self):
        print "艦娘總數為：", self.ships_count


    def get_max_level_ship_with_same_nick_name(self, nick_name):
        # 從 self.ships[] 裡面找找看哪隻艦娘的圖鑑號碼跟 input 相同，取得該艦娘目前的順位 (即"在目前這 100 隻建娘內，排第幾隻，注意其與 local_id 不同之處”)
        max_level = 0
        current_id = None
        for index,value in enumerate(self.ships):
            if value is None:
                break
            if (value.nick_name == nick_name) and (int(value.lv) > max_level):
                # 要加一，因為 self.ships 從 [0] 開始，故 self.ships[0] 實際上是第一艘船
                max_level = int(value.lv)
                current_id = index + 1
        return current_id

    def get_ship_current_id_by_nick_name(self, nick_name):
        current_id = self.get_max_level_ship_with_same_nick_name(nick_name)
        if current_id is None:
            u.uerror("この名前の艦娘が艦隊にいないようです")
        else:
            official_name = kcShipData.get_ship_name_by_nick_name(nick_name)
            msg = "{c1:s}{name:s}({nick:s}){c2:s}さんですね、わかりました".format(c1=u.color['yellow'], c2=u.color['default'], name=official_name, nick=nick_name)
            u.uprint(msg)
        return current_id



    """
    維修時間相關
    """

    def _get_repair_time(self, ship):
        """
        1
        2  驅逐艦
        3  輕巡
        4  雷裝巡
        5  重巡
        6  航空巡
        7  輕空母
        8  高速戰艦？金剛型？
        9  低速戰艦？普通戰艦？
        10 航空戰艦
        11 正規空母
        12
        13 潛水艇
        14
        15
        16 水上機母
        17
        18 裝甲空母

        -- 倍率 --
        0.5 潜水艦
        1.0 駆逐艦・軽巡洋艦・重雷装巡洋艦・練習巡洋艦・水上機母艦・潜水空母・揚陸艦
        1.5 重巡洋艦・航空巡洋艦・金剛型戦艦・軽空母・潜水母艦
        2.0 戦艦・航空戦艦・正規空母・装甲空母・工作艦
        """
        stype  = ship.stype
        lv     = ship.lv
        sub_hp = ship.maxhp - ship.nowhp

        if stype == 13:
            bailitu = 0.5
        elif (stype == 2) or (stype == 3) or (stype == 4) or (stype == 16):
            bailitu = 1
        elif (stype == 5) or (stype == 6) or (stype == 7) or (stype == 8):
            bailitu = 1.5
        else:
            bailitu = 2

        """
        「Lv1～11」：(Lv * 10) * 倍率 * 減少HP + 30 (秒)
        「Lv12～」 ：(Lv * 5 + a) * 倍率 * 減少HP + 30 (秒)
        a = [ √(Lv - 11) ] * 10 + 50 （[ ] 内は小数点以下切り捨て）
        """
        if lv < 12:
            repair_seconds = (lv * 10) * bailitu * sub_hp + 30
        else:
            a = int( math.sqrt(lv - 11) ) * 10 + 50
            # print 'a = ' + str(a)
            repair_seconds = (lv * 5 + a) * bailitu * sub_hp + 30

        # 從 7615 秒 轉成 02:06:55 格式
        hour = int(repair_seconds // 3600) # 先 cast 成 int，以免整除時出現 1.0 等
        minute = int(repair_seconds % 3600 // 60)
        second = int(repair_seconds % 60)

        # msg  = '{:0>2s}:{:0>2s}:{:0>2s}'.format(str(hour), str(minute), str(second))
        return (hour, minute, second)


    def get_damaged_ships_and_repair_time(self):
        damaged_ships = list()
        for ship in self.ships:
            if ship is None: break
            if not ship.nowhp == ship.maxhp:
                repair_time = self._get_repair_time(ship)
                # 幫大破小破上色
                hp = str(ship.nowhp)+"/"+str(ship.maxhp)
                div = float(ship.nowhp) / float(ship.maxhp)
                # print div
                if div < 0.25:
                    hp += ' 大破'
                    hp = u.append_color(hp, 'red')
                elif div < 0.5:
                    hp += ' 中破'
                    hp = u.append_color(hp, 'orange')

                damaged_ships.append( (repair_time, hp, ship.lv, ship.name) )

        damaged_ships.sort(reverse=True)

        for value in damaged_ships:
            # 幫修理時間上色
            repair_time = '{:0>2d}:{:0>2d}:{:0>2d}'.format(value[0][0], value[0][1], value[0][2])
            if not value[0][0] == 0:
                if value[0][0] == 1:
                    repair_time = u.append_color(repair_time, 'yellow')
                else:
                    repair_time = u.append_color(repair_time, 'red')

            msg = '{:>8s}, {} lv{:>2d} ({})'.format(repair_time, u.append_color(value[3], 'cyan'), value[2], value[1])
            u.uprint(msg)
        u.uprint('怪我している艦娘は {} 人います'.format(u.append_color(len(damaged_ships), 'cyan')))


