# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime

import Foundation
import AppKit

import subprocess

import json
import kcJSON

def pbcopy(s):
    # "Copy string argument to clipboard"
    board = AppKit.NSPasteboard.generalPasteboard()
    board.declareTypes_owner_([AppKit.NSStringPboardType], None)
    newStr = Foundation.NSString.stringWithString_(s)
    newData = newStr.nsstring().dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
    board.setData_forType_(newData, AppKit.NSStringPboardType)

def pbpaste():
    # "Returns contents of clipboard"
    board = AppKit.NSPasteboard.generalPasteboard()
    content = board.stringForType_(AppKit.NSStringPboardType)
    return content


m = PyMouse()
k = PyKeyboard()


# - - - Global Variables - - -
gl_total_quest_page = 0

# 每個步驟與伺服器之間，等待的秒數（也就是預期的網路延遲時間）
gl_lag = 2
# Get focus off terminal
m.click(250, 350, 1)


# 將伺服器延遲時間算入的最普通的正常點擊方式
def click_then_wait(position, sleep_sec):
    """
    點擊 position 之後睡眠 sleep_sec 秒，給予伺服器緩衝時間
    """
    click_no_wait(position)
    time.sleep(sleep_sec)
def click_no_wait(position):
    print get_time_stamp() + "click(): [" + str(position[0]) + "," + str(position[1]) + "]"
    m.click(position[0], position[1])

def keydown_then_wait(keys, sleep_sec):
    keydown_no_wait(keys)
    time.sleep(sleep_sec)

def keydown_no_wait(keys):
    print get_time_stamp() + "keydown(): " + str(keys)
    k.press_keys(keys)

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]



# 任務一覽第 N 頁按鈕位置
btn_page1 = [355,563]
btn_page2 = [406,564]
btn_page3 = [455,563]
btn_page4 = [514,563]
btn_page5 = [563,561]
btn_pages = [btn_page1, btn_page2, btn_page3, btn_page4, btn_page5]


def main():
    global gl_total_quest_page

    click_then_wait([80,770], 0.5)
    click_then_wait([500,770], 0.5)
    # keydown_then_wait(['Command','a'], 0.2) 不需要全選，直接複製即可複製 responsive 的內容!
    keydown_then_wait(['Command','c'], 0.1)

    # dataFromClipboard = pbpaste().encode('utf-8')
    dataFromClipboard = pbpaste()
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

    # Clear clipboard ?
    # pbcopy("---12345---")
    # subprocess.call(["pbcopy", "<", "/dev/null"])
    # subprocess.call(["pbcopy < /dev/null"])

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
click_then_wait(btn_pages[0], gl_lag)
main()

for i in range(1, gl_total_quest_page):
    click_then_wait(btn_pages[i], gl_lag)
    main()

print "任務完了"


