# -*- coding: utf-8 -*-
import kcUtility as u

from kcClasses.deck import Deck
from kcClasses.material import Material
from kcClasses.ndock import Ndock
from kcClasses.ship import Ship

import json
import hashlib

last_hash = None

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

def _parse_port(player, jsonData):
    meta = jsonData['api_data']

    material = meta['api_material']
    tempList = list()
    for i in range(len(material)):
        tempList.append(material[i]['api_value'])
    player.materials = Material(tempList)
    # player.print_info_materials()

    deck = meta['api_deck_port']
    for i in range(len(deck)):
        name              = deck[i]['api_name']
        ships             = deck[i]['api_ship']
        mission           = deck[i]['api_mission']
        player.decks[i] = Deck(name, ships, mission)
    # player.print_info_decks()

    ndock = meta['api_ndock']
    for i in range(2):
        ndock_id          = ndock[i]['api_id']
        state             = ndock[i]['api_state']
        ship_id           = ndock[i]['api_ship_id']
        complete_time     = ndock[i]['api_complete_time']
        complete_time_str = ndock[i]['api_complete_time_str']
        player.ndocks[i]  = Ndock(ndock_id, state, ship_id, complete_time, complete_time_str)
    # player.print_info_ndocks()

    # 先清空 player ships
    for i in xrange(100):
        player.ships[i] = None
    ships = meta['api_ship']
    count = len(ships)
    player.ships_count = count
    for i in xrange(count):
        local_id        = ships[i]['api_id']
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
        player.ships[i] = Ship(local_id, sortno, lv, nowhp, maxhp, cond, karyoku, raisou, taiku, soukou, kaihi, taisen, sakuteki, lucky)
        if player.ships[i].name is None:
            u.uprint("Missing name for local_id:{0:>4d}, lv = {1:>3d}".format(player.ships[i].local_id, player.ships[i].lv) , 'red')
        if player.ships[i].stype is None:
            u.uprint("Missing stype for local_id:{0:>4d}, lv = {1:>3d}".format(player.ships[i].local_id, player.ships[i].lv) , 'red')


    # for i in range(1,101):
    #     if i % 10 == 1:
    #         print "[", i, "]"
    #     player.print_info_ships(i)

    u.uprint("port API 解析完了です", 'cyan')

    return player


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
def _parse_questlist(jsonData):
    meta = jsonData['api_data']
    # print json.dumps(data)
    print "檢查任務第" , meta['api_disp_page'], "頁，共", meta['api_page_count'], "頁。"
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
                state_msg = u.append_color('執行中', 'yellow')
            elif state == 3:
                state_msg = u.append_color('已完成', 'yellow')
            state_msg += ' '

            # **api_progress_flag** 目前進度，1 代表 50%，2 代表 80%
            progress = quest['api_progress_flag']
            if progress == 1:
                state_msg += u.append_color('50%', 'cyan')
            elif progress == 2:
                state_msg += u.append_color('80%', 'cyan')
            else:
                state_msg += "   "
            state_msg += " "

            msg = ""
            # 任務編號
            # msg += "No." + str(quest['api_no']) + " "
            # msg += state_msg + " " + quest['api_title']
            # print type(msg), type(state_msg), type(quest['api_title'])
            msg += state_msg + " " + (quest['api_title'].encode('utf-8'))

            print i, msg

    # 回傳 總共有幾頁
    return meta['api_page_count']


def _set_chrome_dev_filter(filter):
    # 將 chrome dev tool 調整到 800 * 567 px
    # 先點 network
    u.click_and_wait([160,670], 0.1)
    # 點 filter 欄位
    u.click_and_wait([80,720], 0.1)
    # 輸入 filter
    u.keydown_ctrl_a_and_wait(0.1)
    u.keydown_string_and_wait(filter, 0.2)

def _copy_api_response_from_chrome_dev():
    u.click_and_wait([80,770], 0.6)
    u.scroll_down()
    u.click_and_wait([500,770], 0.05)
    u.keydown_ctrl_c_and_wait(0.1)
    # 清空 network 監看紀錄，以免量太大導致 chrome dev tool 延遲或錯誤
    # u.click_and_wait([50,700], 0.05)


def _is_same_as_last_fetch(json_data):
    global last_hash
    md5 = hashlib.md5()
    md5.update(str(json_data))
    this_hash = md5.digest()
    if last_hash == this_hash:
        u.uerror("Didn't update Json due two same hash value")
        return True
    last_hash = this_hash
    return False


def fetch_api_response(player, filter):
    # 清空 clipboard
    u.pbcopy("NA")

    # 設定 filter
    _set_chrome_dev_filter(filter)
    # 複製 response
    _copy_api_response_from_chrome_dev()

    dataFromClipboard = u.pbpaste()

    try:
        json_data = json.loads(dataFromClipboard[7:])
    except:
        u.uerror("Failed to fecth Kancolle API")
        u.uerror("Data: {0}".format(dataFromClipboard))
        return 'fail_to_fetch'

    # 與上個 JSON 是否擁有相同的 hash，有的話就更新
    if _is_same_as_last_fetch(json_data) is True:
        return 'same_as_last'

    try:
        if filter == 'questlist':
            global gl_total_quest_page
            gl_total_quest_page = _parse_questlist(json_data)
            print "gl_total_quest_page = ", gl_total_quest_page
        elif filter == 'port':
            _parse_port(player, json_data)
    except:
        u.uerror("Failed to parse Kancolle API")
        # u.uerror("Data: {0}".format(dataFromClipboard))
        return 'fail_to_parse'

