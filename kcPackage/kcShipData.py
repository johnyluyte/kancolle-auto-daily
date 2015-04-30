# -*- coding: utf-8 -*-
import fileinput
import kcUtility as u

FILE_NAME = "kcShipData.csv"
kanmusu_dict = dict()
fleet_dict = dict()
# kanmusu_dict['337'] = ('電改', 'denchan')

def get_ship_name_by_id(id):
    """
    輸入艦娘的圖鑑號碼，回傳該艦娘的官方名稱

    @ id: 艦娘的圖鑑號碼
    @ return:
        有找到：回傳艦娘的官方名稱
        沒找到：回傳 None
    """
    name = kanmusu_dict.get(str(id), None)
    if name is not None:
        name = name[0]
    return name

def get_ship_nick_name_by_id(id):
    """
    輸入艦娘的圖鑑號碼，回傳該艦娘的暱稱

    @ id: 艦娘的圖鑑號碼
    @ return:
        有找到：回傳艦娘的暱稱
        沒找到：回傳 None
    """
    name = kanmusu_dict.get(str(id), None)
    if name is not None:
        name = name[1]
    return name

def get_ship_name_by_nick_name(nick_name):
    """
    輸入艦娘的暱稱，回傳該艦娘的官方名稱

    @ nick_name: 艦娘的暱稱
    @ return:
        有找到：回傳艦娘的官方名稱
        沒找到：回傳 None
    """
    ship_name = None
    for key,value in kanmusu_dict.items():
        if value[1] == nick_name:
            ship_name = value[0]
            break
    return ship_name

def get_nick_name_by_ship_name(ship_name):
    """
    輸入艦娘的官方名稱，回傳該艦娘的暱稱

    @ nick_name: 艦娘的官方名稱
    @ return:
        有找到：回傳艦娘的暱稱
        沒找到：回傳 None
    """
    nick_name = None
    for key,value in kanmusu_dict.items():
        if value[0] == ship_name:
            nick_name = value[1]
            break
    return nick_name


"""
# load CSV 相關
"""

def load_csv_store_ships(fields):
    index      = fields[0].strip()
    name       = fields[1].strip()
    nick_name  = fields[2].strip()
    # planes   = fields[3].strip()
    kanmusu_dict[index] = (name, nick_name)

def load_csv_store_fleets(fields):
    key        = fields[0].strip()
    fleet_name = fields[1].strip()
    fleet1     = fields[2].strip()
    fleet2     = fields[3].strip()
    fleet3     = fields[4].strip()
    fleet4     = fields[5].strip()
    fleet5     = fields[6].strip()
    fleet6     = fields[7].strip()
    fleet_dict[key] = (fleet_name, fleet1, fleet2, fleet3, fleet4, fleet5, fleet6)

def load_csv_parse(file_handler):
    state = 'fleets'
    for line in file_handler:
        if state == 'fleets':
            if line.rstrip() == "@ User defeined ID":
                state = 'ships'
                continue
            elif line.startswith("#") or line.strip() == '':
                continue;
            load_csv_store_fleets(line.split(','))
        elif state == 'ships':
            if line.startswith("#") or line.strip() == '' or line.startswith('@'):
                continue;
            load_csv_store_ships(line.split(','))

def load_csv():
    global kanmusu_dict
    global fleet_dict

    with open(FILE_NAME, 'r') as file_handler:
        load_csv_parse(file_handler)


"""
# Fleets 相關
"""

def get_fleets_data_by_fleet_nick_name(fleet_position, fleet_nick_name):
    """
        輸入要更換的艦隊位置(第 1~4 艦隊)，以及目標艦隊代號，回傳該艦隊的艦娘配置

    @ fleet_position:  要更換的艦隊位置(第 1~4 艦隊)
    @ fleet_nick_name: 艦隊代號
    @ return:
         有找到艦隊: 回傳該艦隊的艦娘配置，配置艦娘的話回傳暱稱，配置是空位的話回傳 None
                    tuple("akagi", "kaga", "den", "hibiki", None, None)
         沒找到艦隊: 回傳 False
    """

    found = fleet_dict.get(fleet_nick_name, None)
    if found is None:
        u.uerror("この名前の艦隊がないんです")
        return False
    msg =  "第 " + fleet_position[1] + " 艦隊を" + u.color['yellow'] + found[0] + u.color['default'] + "に変更します"
    u.uprint(msg)
    result = found[1:]
    return result

def cat_fleets():
    for key, value in fleet_dict.items():
        msg = "{0}{1} {2}{3}{4} \n".format(u.color['yellow'], key, u.color['cyan'], value[0], u.color['default'])
        for i in xrange(1,7):
            name_unicode = value[i].decode('utf-8')
            name_format = u'{:\u3000<8s}'.format(name_unicode)
            msg += str(i) + "." + (name_format).encode('utf-8')
            if i % 2 == 0:
                msg += "\n"
        print msg

def save_current_fleets(player, nick_name, name, ships):
    """
        將 目前編成的艦隊 新增進入 kcShipData.csv 的「我的艦隊」中

        @ fleet_nick_name:  艦隊代號
        @ fleet_name:       艦隊名稱
        @ fleet_nick_name:  tuple, (艦娘1的 local_id, 2, 3, 4, 5, 6)，空位則用 -1
                            例如 (1, 17, 425, 33, -1, -1)

        @ return:           無？
    """
    for line in fileinput.input(FILE_NAME, inplace = 1):
        print line,
        if line.startswith('# 此行勿刪，新加的艦隊會自動加在此行下面'):
            output = '  '
            format_nick_name = "{:<8s}".format(nick_name)
            format_name      = "  {:<14s}".format(name)
            output += format_nick_name + "," + format_name + ","

            for i in xrange(6):
                # 用 local_id 取得 sortno
                sortno = None
                for ship in player.ships:
                    if ship is None: break
                    if ship.local_id == ships[i]:
                        sortno = ship.sortno
                # 再用 sortno 取得 ship_name
                ship_name = get_ship_name_by_id(sortno)
                if ship_name is None:
                    ship_name = ""
                # ship_name_unicode = ship_name.decode('utf-8')
                # format_ship_name = u'{: >4s}'.format(ship_name_unicode)
                format_ship_name = '{:>8s}'.format(ship_name)
                # output += " " + format_ship_name.encode('utf-8') + ","
                output += " " + format_ship_name + ","
            print output


"""
# Cat Names 相關
"""

def cat_name_print_fields(fields):
    # id_     = fields[0].strip()
    name        = fields[1].strip()
    nick_name   = fields[2].strip()
    planes      = fields[3].strip()
    # print "{c1}{name:あ>14}{c2}{nick_name:>14s}{planes:>16s}".format(name=name, nick_name=nick_name, planes=planes, c1=u.color['yellow'], c2=u.color['default'])

    # 轉成 unicode object
    name_unicode = name.decode('utf-8')
    # 為了插入 \u3000 排版..
    name_format = u'{:\u3000<4s}'.format(name_unicode)

    msg = '{}'.format(u.color['yellow'])
    # 轉回 str object
    msg += name_format.encode('utf-8')
    msg += '{c2}{nick_name:<12s}{planes:<14s}'.format(nick_name=nick_name, planes=planes, c2=u.color['default'])
    print msg

def cat_name_parse(file_handler):
    skip = True
    for line in file_handler:
        if skip is True:
            if line.rstrip() == "@ User defeined ID":
                skip = False
        else:
            if line.startswith("#"):
                print u.color['purple'] + line.rstrip() + u.color['default']
            elif line.strip() == '':
                pass
            elif line.rstrip() == "@ Official ID":
                break
            else:
                cat_name_print_fields(line.split(','))

def cat_name():
    with open(FILE_NAME, 'r') as file_handler:
        cat_name_parse(file_handler)



"""
# 每日
201 = 敵艦隊を撃破せよ！
questIndex['403'] = '「遠征」を１０回成功させよう！'
303 = 「演習」で練度向上！
402 = 「遠征」を３回成功させよう！
503 = 艦隊大整備！
605 = 新装備「開発」指令
606 = 新造艦「建造」指令
607 = 装備「開発」集中強化！
608 = 艦娘「建造」艦隊強化！
702 = 艦の「近代化改修」を実施せよ！

# 每週
questIndex['302'] = '大規模演習'
213 = 海上通商破壊作戦
214 = あ号作戦
220 = い号作戦


256 = 「潜水艦隊」出撃せよ！

# 單發
114 = 「南雲機動部隊」を編成せよ！
118 = 「金剛」型による高速戦艦部隊を編成せよ！
121 = 「第四戦隊」を編成せよ！
128 = 「第六戦隊」を編成せよ！
146 = 改修工廠を準備せよ！
272 = 「改装防空重巡」出撃せよ！
275 = 抜錨！「第十八戦隊」
"""

