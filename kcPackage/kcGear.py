# -*- coding: utf-8 -*-
import kcUtility as u

import json

# key = sortno, value = GearData
gear_data = dict()

# key = local_id, value = sortno
local_id_to_sortno = dict()

class GearData(object):
    total_count = 0
    def __init__(self, sortno, name):
        self.name    = name    # 這個種類裝備名稱的名稱(eg: 20.3cm連装砲)
        self.sortno  = sortno  # 不同種類裝備的有唯一的 sortno，可用來判斷是否為同種裝備(eg: 6)
        self.count   = 0       # 玩家擁有這個裝備的數量(eg: 23)
        self.who_has = list()  # 擁有這個裝備的艦娘們(eg: )
        # local_id             # "每一個"裝備都有自己唯一的 local id(eg: 134)


def print_important_gears():
    important_gears = [
        # 主副砲
        '[0] 試製46cm連装砲',
        '[0] 15.5cm三連装副砲',
        '[0] OTO 152mm三連装速射砲',

        # 対空武器
        '[1] 91式高射装置',
        '[1] 10cm連装高角砲(砲架)',
        '[1] 12cm30連装噴進砲',

        # ソナー、爆雷'
        '[2] 九四式爆雷投射機',
        '[2] 三式爆雷投射機',
        '[2] 九三式水中聴音機',

        # 戦闘機'
        '[3] 紫電改二',
        '[3] 烈風',
        '[3] 天山(六〇一空)',
        '[3] 流星',
        '[3] 流星改',
        '[3] 零式艦戦62型(爆戦)',
        '[3] 彗星一二型甲',

        # 電探、その他'
        '[4] 21号対空電探',
        '[4] プリエーゼ式水中防御隔壁',
        '[4] 三式弾',
    ]
    print_all_gears(important_gears)

def print_all_gears(important_gears=None):
    result = list()
    for sortno,gearData in gear_data.items():
        if gearData.count == 0: continue
        elif important_gears is None:
            result.append( (gearData.name, gearData))
        else:
            for important_gear in important_gears:
                if (gearData.name == important_gear[4:]):
                    result.append( (important_gear, gearData))
                    break;
            # if any(gearData.name in important_gear for important_gear in important_gears):
            #     result.append(gearData)
            continue;

    # ([3] 烈風 , GearData(name, sortno, count, who_has() ))
    result.sort()

    sort_title = ['主副砲', '対空武器', 'ソナー、爆雷', '戦闘機', '電探、その他']
    sort_title_now = -1
    for tuple_ in result:
        # print sort_title_now, tuple_[0][1]
        if (not tuple_[0][1] == str(sort_title_now)) and (not important_gears == None):
            sort_title_now += 1
            print('\n{}'.format(u.append_color('### ' + sort_title[sort_title_now] + '###', 'cyan')) )

        gearData = tuple_[1]
        print('{}, {}'.format(u.append_color(tuple_[0], 'yellow'), u.append_color(gearData.count, 'green')))
        if not len(gearData.who_has) == 0:
            msg = ''
            for ship_name in gearData.who_has:
                msg += u.append_color(ship_name, 'default') + ','
            print(msg)


def clear_who_has():
    global gear_data
    # 先清空原先 gear_data 字典內的 who_has 欄位
    # count 欄位不可清除，因為 port 抓到的是"裝在艦娘身上的裝備"，而非"玩家所有裝備"
    for sortno,gearData in gear_data.items():
        gearData.who_has[:] = []

def update_gear_data_by_local_id(local_id, ship_name, ship_lv):
    unknown_sortno = 0
    sortno = local_id_to_sortno.get(local_id, None)
    if sortno is None:
        unknown_sortno += 1
        if unknown_sortno > 50:
         u.uerror('unknown_sortno > 50, please update item_slot.' )
        return
    gear = gear_data[sortno]
    ship_name_and_lv = ship_name + "(" + str(ship_lv) + ")"
    if ship_name_and_lv not in gear.who_has:
        gear.who_has.append(ship_name_and_lv)

def load_slot_item_json():
    global local_id_to_sortno
    with open('kcPlayerGear.json', 'r') as file_handler:
        tmp = file_handler.read()
        json_data = json.loads(tmp)
        for gear in json_data['api_data']:
            local_id = gear['api_id']
            sortno   = gear['api_slotitem_id']
            local_id_to_sortno[local_id] = sortno
            gear_data[sortno].count += 1
    # for local_id,sortno in local_id_to_sortno.items():
    #     print local_id, sortno, gear_data[sortno].name
    # print 'total = ', len(local_id_to_sortno) , 'items'

def load_api_start2_gear_json():
    global gear_data

    with open('kcOfficialGear.json', 'r') as file_handler:
        tmp = file_handler.read()
        json_data = json.loads(tmp)
        # gears =
        # length = len(gears)
        for gear in json_data['api_mst_slotitem']:
            if gear['api_sortno'] == 0: continue
            sortno = gear['api_id']
            name   = gear['api_name'].encode('utf-8')
            # print(type(name))
            g = GearData(sortno, name)
            gear_data[sortno] = g
    # for sortno,gearData in gear_data.items():
    #     print sortno, gearData.name

def main():
    # 先讀取官方的裝備名稱與 ID 表格，此表格可得知 sortno -> name 的關係
    load_api_start2_gear_json()
    # 再讀取遊戲開始時玩家的 slot_item，可得知 local_id -> sortno 的關係
    load_slot_item_json()
    # 最後讀取 port 的裝備，可得知艦娘裝備的 local_id


if __name__ == '__main__':
    main()
