# -*- coding: utf-8 -*-
import sys
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
            start_pos = 0
            end_pos = 4
        # 印出某個指定的艦隊狀態
        elif deck_id > 0 and deck_id < 5 and (self.decks[deck_id-1] is not None):
            start_pos = deck_id-1
            end_pos = deck_id
        else:
            u.uerror("[Player][print_info_decks] Invalid deck_id")
            return
            # self.decks[deck_id-1].print_info()

        for i in range(start_pos,end_pos):
            if self.decks[i] is None: continue
            # self.decks[i].print_info()
            result = self.decks[i].get_info()
            fleet_name = result['name'].encode('utf-8')
            print(u.append_color(fleet_name, 'cyan'))
            msg = ''
            for local_id in result['ships']:
                if local_id == -1: continue
                for ship in self.ships:
                    if ship is None: break
                    if ship.local_id == local_id:
                        cond = ship.cond
                        if cond < 20:
                            cond = u.append_color(cond, 'red')
                        elif cond < 30:
                            cond = u.append_color(cond, 'orange')
                        elif cond >= 50:
                            cond = u.append_color(cond, 'yellow')

                        # 如果是印出全部艦隊的話，印簡易的資訊就好
                        if deck_id == 5:
                            msg += u.append_color(ship.name, 'yellow') + '(' + str(cond) + '), '
                        # 如果是印出特定艦隊的話，印詳細的資訊
                        else:
                            tmp = self._get_hp_and_next_ha(ship.nowhp, ship.maxhp)
                            repair_time = self._get_repair_time(ship)
                            value = (repair_time, tmp[0], ship.lv, ship.name, tmp[1])

                            msg += '(' + str(cond) + ') '
                            msg += self._format_damaged_ships_and_repair_time(value)
                            msg += '\n'
            print(msg[:-1])
            print("任務" + str(result['mission']))


    def print_info_ndocks(self, player, dock_id = 5):
        if self.ndocks[0] is None:
            u.uerror("[Player][print_info_ndocks] Not initialized")
            return
        # 印出所有的修船廠狀態
        if dock_id == 5:
            for i in range(0,2):
                if self.ndocks[i] is None: continue
                info = self.ndocks[i].get_info(player)
                print("第" + str(info['ndock_id']) + "修船廠(" + info['state'] + ")：" + info['name_count_down'])
        # 印出某個指定的修船廠狀態
        # elif dock_id > 0 and dock_id < 5 and (self.ndocks[dock_id-1] is not None):
            # self.ndocks[dock_id-1].print_info_short(player)
        else:
            u.uerror("[Player][print_info_ndocks] Invalid dock_id")

    def print_info_ndocks_auto_repair(self, player):
        info = [{} for _ in xrange(2)]

        for i in range(0,2):
            if self.ndocks[i] is None: continue
            info[i] = self.ndocks[i].get_info(player)

        msg = "入渠 1:" + info[0]['name_count_down'] + " 2:" + info[1]['name_count_down']
        sys.stdout.write( "\r{}".format(msg) )
        sys.stdout.flush()

        seconds_left = [info[0]['seconds_left'] ,info[1]['seconds_left']]
        return seconds_left

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
        msg = self.ships_count
        if self.ships_count > 95:
            msg = u.append_color(self.ships_count, 'red')
        print "艦娘保有数：", msg


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
            u.uerror("この艦娘が艦隊にいないです {}".format(nick_name) )
        else:
            official_name = None
            for ship in self.ships:
                if ship.nick_name == nick_name:
                    official_name = ship.name
                    break
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
        if sub_hp == 0:
            return(0,0,0)

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


    def _get_hp_and_next_ha(self, nowhp, maxhp):
        hp = str(nowhp)+"/"+str(maxhp)
        div = float(nowhp) / float(maxhp)
        if div == 1:
            next_ha = '';
        elif div <= 0.25:
            hp += ' 大破'
            hp = u.append_color(hp, 'red')
            # 計算距離下一個破還差多少 hp
            next_ha = u.append_color('!!!', 'red')
        elif div <= 0.5:
            hp += ' 中破'
            hp = u.append_color(hp, 'orange')
            next_ha = u.append_color('+'+str(nowhp - int(maxhp/4.0)), 'red')
        elif div <= 0.75:
            hp += ' 小破'
            next_ha = u.append_color('+'+str(nowhp - int(maxhp/2.0)), 'orange')
        else:
            next_ha = '+'+str(nowhp - int(maxhp/2.0))
        return (hp, next_ha)

    def get_damaged_ships_and_repair_time(self):
        damaged_ships = list()
        for ship in self.ships:
            if ship is None: break
            # print ship.name, ship.nowhp, ship.maxhp
            if not ship.nowhp == ship.maxhp:
                if ship.stype is None:
                    u.uerror("Missing stype, local_id:{0:>4d}, lv = {1:>3d}".format(ship.local_id, player.ship.lv) )
                    continue
                repair_time = self._get_repair_time(ship)
                # 幫大破小破上色
                tmp     = self._get_hp_and_next_ha(ship.nowhp, ship.maxhp)
                hp      = tmp[0]
                next_ha = tmp[1]

                damaged_ships.append( (repair_time, hp, ship.lv, ship.name, next_ha) )

        damaged_ships.sort(reverse=True)
        for value in damaged_ships:
            msg = self._format_damaged_ships_and_repair_time(value)
            u.uprint(msg)
        u.uprint('怪我している艦娘は {} 人います'.format(u.append_color(len(damaged_ships), 'cyan')))


    def _format_damaged_ships_and_repair_time(self, value):
        # 幫修理時間上色
        repair_time = '{:0>2d}:{:0>2d}:{:0>2d}'.format(value[0][0], value[0][1], value[0][2])
        if not value[0][0] == 0:
            if value[0][0] == 1:
                repair_time = u.append_color(repair_time, 'yellow')
            else:
                repair_time = u.append_color(repair_time, 'red')

        msg = '{repair_time:>8s}, lv{lv:>2d} {name} ({hp}) {next}'.format(repair_time=repair_time, lv=value[2], name=u.append_color(value[3], 'cyan'), hp=value[1], next=value[4])
        return msg


