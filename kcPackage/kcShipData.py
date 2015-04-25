# -*- coding: utf-8 -*-
import kcUtility as u

kanmusuIndex = dict()
fleetIndex = dict()
# kanmusuIndex['337'] = ('電改', 'denchan')

def get_ship_name_by_id(id):
    """
    輸入艦娘的圖鑑號碼，回傳該艦娘的官方名稱

    @ id: 艦娘的圖鑑號碼
    @ return:
        有找到：回傳艦娘的官方名稱
        沒找到：回傳 None
    """
    name = kanmusuIndex.get(str(id), None)
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
    name = kanmusuIndex.get(str(id), None)
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
    for key,value in kanmusuIndex.items():
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
    for key,value in kanmusuIndex.items():
        if value[0] == ship_name:
            nick_name = value[1]
            break
    return nick_name

"""
def get_ship_zukan_id_by_nick_name(nick_name):
    ""
    輸入艦娘的暱稱，回傳該艦娘的圖鑑號碼

    @ nick_name: 艦娘的暱稱
    @ return:
         有找到: 回傳該艦娘的圖鑑號碼
         沒找到: 回傳 False
    ""
    found = False
    for key, value in kanmusuIndex.items():
        # ('337', ('電改', 'denchan'))
        if value[1] == nick_name:
            found = key
            break
    # print "[get_ship_key] found = ", found
    return found
"""

def print_csv_data():
    file_name = "kcShipData.csv"
    try:
        file_handler = open(file_name)
    except:
        u.uerror("could not open file", file_name)
        exit()

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
                fields = line.split(',')
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

    file_handler.close()
    return

def print_fleets_data():
    for key, value in fleetIndex.items():
        msg = "{0}{1} {2}{3}{4} \n".format(u.color['yellow'], key, u.color['cyan'], value[0], u.color['default'])
        for i in xrange(1,7):
            name_unicode = value[i].decode('utf-8')
            name_format = u'{:\u3000<8s}'.format(name_unicode)
            msg += str(i) + "." + (name_format).encode('utf-8')
            if i % 2 == 0:
                msg += "\n"
        print msg

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

    found = fleetIndex.get(fleet_nick_name, None)
    if found is None:
        u.uerror("この名前の艦隊がないんです")
        return False
    msg =  "第 " + fleet_position[1] + " 艦隊を" + u.color['yellow'] + found[0] + u.color['default'] + "に変更します"
    u.uprint(msg)
    result = found[1:]
    return result


def main():
    global kanmusuIndex
    global fleetIndex

    file_name = "kcShipData.csv"
    try:
        file_handler = open(file_name)
    except:
        u.uerror("[kcShipData] could not open csv file" + file_name)
        exit()

    state = 'fleets'
    for line in file_handler:
        if state == 'fleets':
            if line.rstrip() == "@ User defeined ID":
                state = 'ships'
                continue
            elif line.startswith("#") or line.strip() == '':
                continue;

            fields = line.split(',')
            key        = fields[0].strip()
            fleet_name = fields[1].strip()
            fleet1     = fields[2].strip()
            fleet2     = fields[3].strip()
            fleet3     = fields[4].strip()
            fleet4     = fields[5].strip()
            fleet5     = fields[6].strip()
            fleet6     = fields[7].strip()
            fleetIndex[key] = (fleet_name, fleet1, fleet2, fleet3, fleet4, fleet5, fleet6)
        elif state == 'ships':
            if line.startswith("#") or line.strip() == '' or line.startswith('@'):
                continue;
            fields = line.split(',')
            id_     = fields[0].strip()
            name    = fields[1].strip()
            nick_name   = fields[2].strip()
            # planes   = fields[3].strip()
            # print id_, name, nick_name
            kanmusuIndex[id_] = (name, nick_name)

    file_handler.close()
    # _print_dict()





def _print_dict():
    for key, value in kanmusuIndex.items():
        print key, ":", value[0], value[1]



# if __name__ == '__main__':
#     main()

main()


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

