# -*- coding: utf-8 -*-
from kcUtility import uerror

from kcShipData import get_ship_key


class Player(object):
    def __init__(self):
        self.materials  = None
        self.decks      = [None, None, None, None]
        self.ndocks     = [None, None, None, None]
        self.ships      = [None] * 100  # 意義同上，建立 1 個含有 100 個 None 的 list

    def print_info_materials(self):
        if self.materials is None:
            uerror("[Player][print_info_materials] Not initialized")
            return
        self.materials.print_info()

    def print_info_decks(self, deck_id = 5):
        if self.decks[0] is None:
            uerror("[Player][print_info_decks] Not initialized")
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
            uerror("[Player][print_info_decks] Invalid deck_id")

    def print_info_ndocks(self, dock_id = 5):
        if self.ndocks[0] is None:
            uerror("[Player][print_info_ndocks] Not initialized")
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
            uerror("[Player][print_info_ndocks] Invalid dock_id")

    """
    TODO: 應該改成輸入船的名字也可以印出來!?
    總之這邊先做成    用 list 的 index  來搜尋，先全部印出來，意思到就好
    """
    def print_info_ships(self, ship_in_list = 1):
        if self.ships[0] is None:
            uerror("[Player][print_info_ships] Not initialized")
            return
        # 印出某個指定的船狀態，以在 list 的順序印出來，
        if ship_in_list > 0 and ship_in_list <= 100:
            if self.ships[ship_in_list-1] is not None:
                self.ships[ship_in_list-1].print_info()
            else:
                return
        else:
            uerror("[Player][print_info_ships] Invalid ship_in_list")

    def get_ship(self, nick_name):
        # 輸入艦娘的綽號（譬如 denchan），透過對照表找到 denchan 對應的圖鑑號碼
        key = get_ship_key(nick_name)
        print "[get_ship] key = ", key
        result = None
        if key is not False:
            # 從 data api 裡面找找看有沒有哪隻艦娘的圖鑑號碼跟輸入的相同，取得其 own_id (即“是第幾隻得到的”)
            for index,value in enumerate(self.ships):
                if value is None:
                    break
                # print index, value.sortno, key
                if str(value.sortno) == str(key):
                    # 要加一，因為 list 從 [0] 開始
                    result = index + 1
        # not found
        print "[get_ship] nick_name = ", nick_name ," result = " , result
        return result

