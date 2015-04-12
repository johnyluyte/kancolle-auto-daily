# -*- coding: utf-8 -*-

# 使用者輸入
USER_INPUT = None

# 每個步驟與伺服器之間，等待的秒數（也就是預期的網路延遲時間）
LAG = 2

# 目前所在的畫面
PLACE = "port"


# 顯示在 terminal 的顏色
# http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
COLOR_DEFAULT="\033[m"
COLOR_LIGHTGREEN="\033[1;32m"
COLOR_LIGHTRED="\033[1;31m"
COLOR_LIGHTYELLOW="\033[1;33m"



# 修船廠資訊
class Ndock(object):
    def __init__(self, ndock_id, state, ship_id, complete_time, complete_time_str):
        self.ndock_id = ndock_id
        self.state = state
        self.ship_id = ship_id
        self.complete_time = complete_time
        self.complete_time_str = complete_time_str
    def print_info(self):
        print("第 " + str(self.ndock_id) + " 修船廠")
        print("狀態：" + str(self.state))
        print("船艦：" + str(self.ship_id))
        print("完成時間E：" + str(self.complete_time))
        print("完成時間H：" + str(self.complete_time_str))

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
        print("own_id " + str(self.own_id))
        print("sortno " + str(self.sortno))
        print("lv " + str(self.lv))
        # print("nowhp " + str(self.nowhp))
        # print("maxhp " + str(self.maxhp))
        # print("cond " + str(self.cond))
        print("karyoku " + str(self.karyoku))
        print("raisou " + str(self.raisou))
        # print("taiku " + str(self.taiku))
        # print("soukou " + str(self.soukou))
        # print("kaihi " + str(self.kaihi))
        # print("taisen " + str(self.taisen))
        # print("sakuteki " + str(self.sakuteki))
        # print("lucky " + str(self.lucky))



class Material(object):
    def __init__(self, itemsValue):
        self.items  = [["燃料",0], ["彈藥",0], ["鋼材",0], ["機材",0], ["高速建造",0], ["高速修復",0], ["建造資材",0], ["改修資材",0]]
        for i in range(len(self.items)):
            self.items[i][1] = itemsValue[i]

    def print_info(self):
        for tmp in self.items:
            print(tmp[0] + ": " + str(tmp[1]))


class Player(object):
    def __init__(self):
        self.materials  = None
        self.decks      = [None, None, None, None]
        self.ndocks     = [None, None, None, None]
        self.ships      = [None] * 100  # 同上，建立 1 個含有 100 個 None 的 list

    def print_info_materials(self):
        if self.materials is not None:
            self.materials.print_info()

    def print_info_decks(self, deck_id = 5):
        # 印出所有的艦隊狀態
        if deck_id == 5:
            for i in range(0,4):
                if self.decks[i] is None: continue
                self.decks[i].print_info()
        # 印出某個指定的艦隊狀態
        elif deck_id > 0 and deck_id < 5 and (self.decks[deck_id-1] is not None):
            self.decks[deck_id-1].print_info()
        else:
            print "[Player][print_info_decks] Invalid deck_id"

    def print_info_ndocks(self, dock_id = 5):
        # 印出所有的修船廠狀態
        if dock_id == 5:
            for i in range(0,4):
                if self.ndocks[i] is None: continue
                self.ndocks[i].print_info()
        # 印出某個指定的修船廠狀態
        elif dock_id > 0 and dock_id < 5 and (self.ndocks[dock_id-1] is not None):
            self.ndocks[dock_id-1].print_info()
        else:
            print "[Player][print_info_ndocks] Invalid deck_id"

    """
    TODO: 應該改成輸入船的名字也可以印出來!?
    總之這邊先做成    用 list 的 index  來搜尋，先意思到就好
    """
    def print_info_ships(self, ship_in_list = 1):
        # 印出某個指定的船狀態，以在 list 的順序印出來，
        if ship_in_list > 0 and ship_in_list <= 100 and (self.ships[ship_in_list-1] is not None):
            self.ships[ship_in_list-1].print_info()
        else:
            print "[Player][print_info_ships] Invalid deck_id"

player = Player()

