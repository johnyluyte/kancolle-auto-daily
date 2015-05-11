# -*- coding: utf-8 -*-
import fileinput
import json

import kcUtility as u


ship_data_dict = dict()
# ship_data_dict[艦娘圖鑑編號] = tuple(艦娘官方名稱, 艦娘種類(驅逐艦、巡洋艦等) )
# ship_data_dict[sortno] = tuple(ship_name, stype)
# ship_data_dict[74] = tuple('電', 2)

ship_adana_dict = dict()
# ship_adana_dict[艦娘官方名稱] = 艦娘綽號
# ship_adana_dict['電'] = den

fleet_hensei_dict = dict()
# fleet_hensei_dict[艦隊代號] = tuple(艦隊名稱, 艦娘1, 艦娘2, 艦娘3, 艦娘4, 艦娘5, 艦娘6)
# fleet_hensei_dict[ensei2] = tuple(龍田改, 睦月, 如月, 夕立, '', '', '')


def get_name_by_local_id(player, local_id):
    name = 'N/A'
    for ship in player.ships:
        if ship is None: break
        if ship.local_id == local_id:
            name = ship.name
    return name

def get_name_by_adana(adana):
    """
    輸入艦娘的暱稱，回傳該艦娘的官方名稱

    @ nick_name: 艦娘的暱稱
    @ return:
        有找到：回傳艦娘的官方名稱
        沒找到：回傳 None
    """
    for name, nick_name in ship_adana_dict.items():
        if adana == nick_name:
            return name
    return None

def get_adana_by_name(name):
    """
    輸入艦娘的官方名稱，回傳該艦娘的暱稱
    如果使用者未定義該艦娘綽號的話，就直接指定該艦娘綽號等於其官方名稱

    @ name: 艦娘的官方名稱
    @ return:
        有找到：回傳艦娘的暱稱
        沒找到：回傳艦娘的官方名稱
    """
    return ship_adana_dict.get(name, name)

def get_name_by_sortno(sortno):
    """
    輸入艦娘的圖鑑號碼，回傳該艦娘的官方名稱
    """
    return ship_data_dict.get(sortno, None)[0]

def get_stype_by_sortno(sortno):
    """
    輸入艦娘的圖鑑號碼，回傳該艦娘的船艦種類(驅逐艦、巡洋艦等)
    """
    return ship_data_dict.get(sortno, None)[1]



"""
# Fleets 相關
"""
def cat_fleets():
    """
    印出目前使用者自訂的艦隊編成(user_fleets.data)
    """
    for key, value in fleet_hensei_dict.items():
        msg = "{} {} \n".format(u.append_color(key, 'yellow'), u.append_color(value[0], 'cyan'))
        for i in xrange(1,7):
            name_format = u'{:\u3000<8s}'.format(value[i].decode('utf-8'))
            msg += str(i) + "." + (name_format).encode('utf-8')
            if i % 2 == 0:
                msg += "\n"
        print msg

def get_fleets_data_by_fleet_nick_name(fleet_position, fleet_code_name):
    """
        輸入要更換的艦隊位置(第 1~4 艦隊)，以及目標艦隊代號，回傳該艦隊的艦娘配置

    @ fleet_position:  要更換的艦隊位置(第 1~4 艦隊)
    @ fleet_code_name: 艦隊代號
    @ return:
         有找到艦隊: 回傳該艦隊的艦娘配置，配置艦娘的話回傳暱稱，配置是空位的話回傳 None
                    tuple("akagi", "kaga", "den", "hibiki", None, None)
         沒找到艦隊: 回傳 False
    """

    found = fleet_hensei_dict.get(fleet_code_name, None)
    if found is None:
        u.uerror("この名前の艦隊がないんです")
        return False
    msg =  "第 " + fleet_position[1] + " 艦隊を" + u.append_color(found[0], 'yellow') + "に変更します"
    u.uprint(msg)
    result = found[1:]
    return result

def save_current_fleets(player, code_name, ships, file_name='user_fleets.data'):
    """
        將 目前編成的艦隊 新增進入 user_fleets.data 的「我的艦隊」中

        @ fleet_code_name:  艦隊代號
        @ ships:            tuple (要儲存的艦隊的第一個艦娘的 local_id, 2, 3, 4, 5, 6)
                            空位則用 -1
                            例如 (1, 17, 425, 33, -1, -1)
        @ return:           無
    """
    for line in fileinput.input(file_name, inplace = 1):
        print line,
        if line.startswith('# 此行勿刪，新加的艦隊會自動加在此行下面'):
            output = "  {:<8s}".format(code_name) + "," + "  {:<14s}".format(code_name) + ","

            for i in xrange(6):
                if ships[i] == -1:
                    output += "        ,"
                else:
                    # 用 local_id 取得 ship_name
                    sortno = None
                    for ship in player.ships:
                        if ship is None: break
                        if ship.local_id == ships[i]:
                            ship_name = ship.name
                    output += " " + '{:>8s}'.format(ship_name) + ","
            print output
    u.uprint('艦隊編成を保存しました', 'cyan')



"""
# Cat Names 相關
"""
def cat_names(file_name='user_ships.data'):
    """
    純粹將 user_ships.data 顯示在 terminal
    """
    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            if line.startswith("#"):
                print u.color['purple'] + line.rstrip() + u.color['default']
            elif line.strip() == '':
                pass
            else:
                print_user_ships_data_fields(line.split(','))

def print_user_ships_data_fields(fields):
    name        = fields[0].strip()
    nick_name   = fields[1].strip()
    planes      = fields[2].strip()

    # 轉成 unicode object，為了插入 \u3000 排版..
    name_format = u'{:\u3000<4s}'.format(name.decode('utf-8'))
    msg = u.append_color(name_format.encode('utf-8'),'yellow')
    msg += '{nick_name:<12s}{planes:<14s}'.format(nick_name=nick_name, planes=planes)
    print msg



"""
# 初始化相關
"""
def load_user_fleets_data(file_name='user_fleets.data'):
    """
    讀取使用者定義的艦隊編成

    """
    global fleet_hensei_dict

    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            if line.startswith("#") or line.strip() == '':
                continue;
            fields  = line.split(',')
            key        = fields[0].strip()
            fleet_name = fields[1].strip()
            fleet1     = fields[2].strip()
            fleet2     = fields[3].strip()
            fleet3     = fields[4].strip()
            fleet4     = fields[5].strip()
            fleet5     = fields[6].strip()
            fleet6     = fields[7].strip()
            # print fleet_name, type(fleet_name), fleet1, type(fleet1), fleet6, type(fleet6)
            fleet_hensei_dict[key] = (fleet_name, fleet1, fleet2, fleet3, fleet4, fleet5, fleet6)

def load_user_ships_data(file_name='user_ships.data'):
    """
    讀取使用者定義的艦娘暱稱
    - name  艦娘官方名稱
    - adana 艦娘暱稱
    """
    global ship_adana_dict

    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            if line.startswith("#") or line.strip() == '':
                continue;
            fields  = line.split(',')
            name    = fields[0].strip()
            adana   = fields[1].strip()

            # print name, type(name), adana, type(adana)
            ship_adana_dict[name] = adana

def load_ship_data(file_name='kcOfficialShip.json'):
    """
    讀取 start_api2 的官方艦娘資訊，包含
    - api_sortno 圖鑑號碼
    - api_name   艦娘官方名稱
    - api_stype  艦娘船艦種類
    """
    global ship_data_dict

    with open(file_name, 'r') as file_handler:
        tmp = file_handler.read()
        json_data = json.loads(tmp)
        ships = json_data['api_mst_ship']

        for i in xrange(len(ships)):
            sortno = ships[i]['api_sortno']
            name   = ships[i]['api_name'].encode('utf-8')
            stype  = ships[i]['api_stype']
            # print name, type(name), stype, type(stype)
            ship_data_dict[sortno] = (name, stype)

def main():
    load_ship_data()
    load_user_ships_data()
    load_user_fleets_data()

    # for key, value in ship_data_dict.items():
    #     print key, value[0], value[1]
    # print len(ship_data_dict)

    # for key, value in ship_adana_dict.items():
    #     print key, value
    # print len(ship_adana_dict)


if __name__ == '__main__':
    main()