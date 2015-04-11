# -*- coding: utf-8 -*-
import json

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
def parseQuest(jsonData):
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

