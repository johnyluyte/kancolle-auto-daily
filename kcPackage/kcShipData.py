# -*- coding: utf-8 -*-

kanmusuIndex = dict()

def get_ship_name(id):
    name = kanmusuIndex.get(str(id), None)
    if name is not None:
        name = name[0]
    return name

def get_ship_key(nick_name):
    found = False
    for key in kanmusuIndex:
        if kanmusuIndex[key][1] == nick_name:
            found = key
            break
    print "[get_ship_key] found = ", found
    return found


def main():
    global kanmusuIndex

    file_name = "kcShipData.csv"
    try:
        file_handler = open(file_name)
    except:
        print ""
        exit()

    for line in file_handler:
        if line.startswith("#"):
            continue;
        fields = line.split(',')
        id_     = fields[0].strip()
        name    = fields[1].strip()
        adana   = fields[2].strip()
        # planes   = fields[3].strip()
        # print id_, name, adana
        kanmusuIndex[id_] = (name, adana)

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

