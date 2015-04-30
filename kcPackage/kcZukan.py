# -*- coding: utf-8 -*-
import kcUtility as u
import json

ship_type_dict = dict()
FILE_NAME = 'kcZukan.json'


def get_stype_by_name(name):
    # print type(ship_type_dict.items()[0][0])
    # print type(name)
    name = name.decode('utf-8')
    # print type(name)

    result = ship_type_dict.get(name, None)

    # 如果在圖鑑裡面找不到 輸入的艦娘名稱 ，不能斷定她不在圖鑑裡
    # 檢查看看 輸入的艦娘名稱 最後一個字是否為 "改"
    # 如果是的話，將 "改" 刪除掉，再查詢一次圖鑑
    # 例如
    # 電改 在圖鑑中就不存在，修正成 電 後就可以找到了
    # 而 大鳳改 就沒這個問題，在圖鑑中本來就存在著
    if (result is None) and (name[-1] == u'改'):
        # print name[-1]
        # print name[:-1]
        result = ship_type_dict.get(name[:-1], None)
    # print name
    # print name[-1]
    # print result
    return result


def load_zukan_json():
    global ship_type_dict
    seen = list()

    with open(FILE_NAME, 'r') as file_handler:
        tmp = file_handler.read()
        json_data = json.loads(tmp)
        ships = json_data['api_data']['api_list']

        for i in xrange(len(ships)):
            name                 = ships[i]['api_name']
            ship_type            = ships[i]['api_stype']
            ship_type_dict[name] = ship_type

            # 印出所有的 ship_type
            if ship_type not in seen:
                seen.append(ship_type)
                # print ship_type, name
                """
                1
                2 雪風 驅逐艦
                3 大井 輕巡
                4 大井改 雷裝巡
                5 最上 重巡
                6 最上改 航空巡
                7 鳳翔 輕空母
                8 金剛 高速戰艦？金剛型？
                9 陸奥 低速戰艦？普通戰艦？
                10 伊勢改 航空戰艦
                11 赤城 正規空母
                12
                13 伊168 潛水艇
                14
                15
                16 千歳 水上機母
                17
                18 大鳳 裝甲空母
                19
                """
