# -*- coding: utf-8 -*-
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
