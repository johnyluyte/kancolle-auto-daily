# -*- coding: utf-8 -*-
import kcUtility as u
import kcGlobal as g

import json

import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()


"""
{
  "api_result": 1,
  "api_result_msg": "成功",
  "api_data": {
    "api_material": [
      {
        "api_member_id": 12130401,
        "api_id": 1,
        "api_value": 7590
      },
      ...
    ],
    "api_deck_port": [
      {
        "api_member_id": 12130401,
        "api_id": 1,
        "api_name": "第1艦隊",
        "api_name_id": "",
        "api_mission": [
          0,
          0,
          0,
          0
        ],
        "api_flagship": "0",
        "api_ship": [
          378,
          76,
          189,
          93,
          29,
          2
        ]
      },
    ],
    "api_ndock": [
      {
        "api_member_id": 12130401,
        "api_id": 1,
        "api_state": 1,
        "api_ship_id": 41,
        "api_complete_time": 1428825495179,
        "api_complete_time_str": "2015-04-12 16:58:15",
        "api_item1": 25,
        "api_item2": 0,
        "api_item3": 48,
        "api_item4": 0
      },
    ],
    "api_ship": [
      {
        "api_id": 1,
        "api_sortno": 337,
        "api_ship_id": 237,
        "api_lv": 27,
        "api_nowhp": 30,
        "api_maxhp": 30,
        "api_cond": 65,
        "api_karyoku": [
          29,
          49
        ],
        "api_raisou": [
          79,
          79
        ],
        "api_taiku": [
          40,
          49
        ],
        "api_soukou": [
          49,
          49
        ],
        "api_kaihi": [
          57,
          89
        ],
        "api_taisen": [
          33,
          59
        ],
        "api_sakuteki": [
          15,
          39
        ],
        "api_lucky": [
          12,
          59
        ],
      },
  }
}
"""

def parse_port(jsonData):
    meta = jsonData['api_data']

    material = meta['api_material']
    tempList = list()
    for i in range(len(material)):
        tempList.append(material[i]['api_value'])
    g.player.materials = g.Material(tempList)
    g.player.print_info_materials()

    deck = meta['api_deck_port']
    for i in range(len(deck)):
        name              = deck[i]['api_name']
        ships             = deck[i]['api_ship']
        mission           = deck[i]['api_mission']
        g.player.decks[i] = g.Deck(name, ships, mission)
    g.player.print_info_decks()

    ndock = meta['api_ndock']
    for i in range(2):
        ndock_id          = ndock[i]['api_id']
        state             = ndock[i]['api_state']
        ship_id           = ndock[i]['api_ship_id']
        complete_time     = ndock[i]['api_complete_time']
        complete_time_str = ndock[i]['api_complete_time_str']
        g.player.ndocks[i] = g.Ndock(ndock_id, state, ship_id, complete_time, complete_time_str)
    g.player.print_info_ndocks()


    ships = meta['api_ship']
    for i in range(len(ships)):
        own_id          = ships[i]['api_id']
        sortno          = ships[i]['api_sortno']
        lv              = ships[i]['api_lv']
        nowhp           = ships[i]['api_nowhp']
        maxhp           = ships[i]['api_maxhp']
        cond            = ships[i]['api_cond']
        karyoku         = ships[i]['api_karyoku'][0]
        raisou          = ships[i]['api_raisou'][0]
        taiku           = ships[i]['api_taiku'][0]
        soukou          = ships[i]['api_soukou'][0]
        kaihi           = ships[i]['api_kaihi'][0]
        taisen          = ships[i]['api_taisen'][0]
        sakuteki        = ships[i]['api_sakuteki'][0]
        lucky           = ships[i]['api_lucky'][0]
        g.player.ships[i] = g.Ship(own_id, sortno, lv, nowhp, maxhp, cond, karyoku, raisou, taiku, soukou, kaihi, taisen, sakuteki, lucky)
    g.player.print_info_ships(5)



"""
{
  "api_data": {
    "api_count": 17,
    "api_page_count": 4,
    "api_disp_page": 3,
    "api_list": [
      {
        "api_no": 256,
        "api_category": 2,
        "api_type": 6,
        "api_state": 1,
        "api_title": "「潜水艦隊」出撃せよ！",
        "api_detail": "潜水艦戦力を中核とした艦隊で中部海域哨戒線へ反復出撃、敵戦力を漸減せよ！",
        "api_get_material": [
          0,
          600,
          0,
          0
        ],
        "api_bonus_flag": 1,
        "api_progress_flag": 0,
        "api_invalid_flag": 0
      },
"""
def parse_questlist(jsonData):
    meta = jsonData['api_data']
    # print json.dumps(data)
    print "檢查任務第," , meta['api_disp_page'], "頁，共", meta['api_page_count'], "頁。"
    quests = meta['api_list']

    # 每一頁一定會有五個欄位，沒有任務的欄位會是 -1，這邊用 (1,6) 只是為了程式方便
    for i in range(1,6):
        quest = quests[i-1]
        if quest == -1:
            print i, "N/A " # 此欄位沒有任務
        else:
            """
            **api_state** 任務狀況，
                1 代表任務有顯示出來，但沒有選取
                2 代表目前有被選取，會顯示”遂行中”
                3 代表任務已完成，可以領獎
            """
            state = quest['api_state']
            state_msg = "      "
            if state == 1:
                pass
            elif state == 2:
                state_msg = "執行中"
            elif state == 3:
                state_msg = "已完成"
            state_msg += " "

            # **api_progress_flag** 目前進度，1 代表 50%，2 代表 80%
            progress = quest['api_progress_flag']
            if progress == 1:
                state_msg += "50%"
            elif progress == 2:
                state_msg += "80%"
            else:
                state_msg += "   "
            state_msg += " "

            msg = ""
            # 任務編號
            # msg += "No." + str(quest['api_no']) + " "
            msg += state_msg + " " + (quest['api_title'].encode('utf-8'))

            print i, msg

    # 回傳 總共有幾頁
    return meta['api_page_count']


def set_chrome_dev_filter(filter):
    m.click(80, 685, 1)
    time.sleep(0.01)
    k.press_key('Command')
    k.tap_key('a')
    k.release_key('Command')
    time.sleep(0.01)
    k.type_string(filter)
    time.sleep(0.2)

def copy_api_response_from_chrome_dev():
    u.click_and_wait([80,770], 0.3)
    u.click_and_wait([500,770], 0.1)
    # keydown_then_wait(['Command','a'], 0.2) 不需要全選，直接複製即可複製 responsive 的內容!
    k.press_key('Command')
    k.tap_key('c')
    k.release_key('Command')
    time.sleep(0.01)


def fetch_api_response(filter):
    # 設定 filter
    set_chrome_dev_filter(filter)
    # 複製 response
    copy_api_response_from_chrome_dev()

    dataFromClipboard = u.pbpaste()

    try:
        json_data = json.loads(dataFromClipboard[7:])
    except:
        print("Failed to fecth API, no valid JSON available")
        return False

    if filter == 'questlist':
        global gl_total_quest_page
        gl_total_quest_page = parse_questlist(json_data)
        print "gl_total_quest_page = ", gl_total_quest_page
    elif filter == 'port':
        parse_port(json_data)


"""
    # Workaround 解決複製兩次 json 的情形（做了多次實驗依然找不出原因，先放棄追究原因）
    # 檢查是否有出現 重複複製兩次 的情形，如果有的話，要把第二個 json 拿掉
    # server 回傳的 json 開頭都是 "svdata="" ，而我們剛剛 [7:] 照理說已經把 "svdata=" 刪掉了
    # 如果剩下的字串還有 "svdata=" 表示複製到第二次
    if not myJson.count("svdata=")==0:
        myJson = myJson.split("svdata=")[0]
        # print myJson
"""

