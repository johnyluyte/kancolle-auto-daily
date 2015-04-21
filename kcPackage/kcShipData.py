# -*- coding: utf-8 -*-

kanmusuIndex = dict()
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
    name = None
    for key,value in kanmusuIndex.items():
        if value[1] == nick_name:
            name = value[0]
            break
    return name

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

def main():
    global kanmusuIndex

    file_name = "kcShipData.csv"
    try:
        file_handler = open(file_name)
    except:
        print ""
        exit()

    for line in file_handler:
        if line.startswith("#") or line.strip() == '':
            continue;
        fields = line.split(',')
        id_     = fields[0].strip()
        name    = fields[1].strip()
        nick_name   = fields[2].strip()
        # planes   = fields[3].strip()
        # print id_, name, nick_name
        kanmusuIndex[id_] = (name, nick_name)

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

