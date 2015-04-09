# -*- coding: utf-8 -*-
import kcUtil as g

import json
import kcJSON

# - - - Global Variables - - -
gl_total_quest_page = 0

# Get focus off terminal
g.click_and_wait([250,250], 0.1)

# 任務一覽第 N 頁按鈕位置
btn_page1 = [355,563]
btn_page2 = [406,564]
btn_page3 = [455,563]
btn_page4 = [514,563]
btn_page5 = [563,561]
btn_pages = [btn_page1, btn_page2, btn_page3, btn_page4, btn_page5]


def main():
    global gl_total_quest_page

    g.click_and_wait([80,770], 0.5)
    g.click_and_wait([500,770], 0.5)
    # keydown_then_wait(['Command','a'], 0.2) 不需要全選，直接複製即可複製 responsive 的內容!
    g.keydown_and_wait(['Command','c'], 0.1)

    # dataFromClipboard = pbpaste().encode('utf-8')
    dataFromClipboard = g.pbpaste()
    myJson = dataFromClipboard[7:]

    # Workaround 解決複製兩次 json 的情形（做了多次實驗依然找不出原因，先放棄追究原因）
    # 檢查是否有出現 重複複製兩次 的情形，如果有的話，要把第二個 json 拿掉
    # server 回傳的 json 開頭都是 "svdata="" ，而我們剛剛 [7:] 照理說已經把 "svdata=" 刪掉了
    # 如果剩下的字串還有 "svdata=" 表示複製到第二次
    if not myJson.count("svdata=")==0:
        myJson = myJson.split("svdata=")[0]
        # print myJson

    json_data = json.loads(myJson)
    gl_total_quest_page = kcJSON.parseQuest(json_data)
    print "gl_total_quest_page = ", gl_total_quest_page

"""
    print("api_result:" + str(json_data['api_result']))
    for i in range(2):
        print("[ 第 " + str(i+1) + " 修復ドック ]")
        print("使用中：" + str(json_data['api_data'][i]['api_state']))
        print("艦娘ID：" + str(json_data['api_data'][i]['api_ship_id']))
        print("修復時間(EPOCH)：" + str(json_data['api_data'][i]['api_complete_time']))  # epoch
        print("修復時点(GMT+9)：" + str(json_data['api_data'][i]['api_complete_time_str']))
"""


# Developer tool 的高度設在 to 1280 * 565


# 先進 questlist 第一頁，解析第一頁任務，順便看看總共有幾頁（gl_total_quest_page）
g.click_and_wait(btn_pages[0], g.gl_lag)
main()

for i in range(1, gl_total_quest_page):
    g.click_and_wait(btn_pages[i], g.gl_lag)
    main()

g.gfinish()


