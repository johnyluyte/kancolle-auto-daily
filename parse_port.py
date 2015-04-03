# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime
from Foundation import *
from AppKit import *
import json

# Sets the clipboard to a string
def pbcopy(s):
 pb = NSPasteboard.generalPasteboard()
 pb.declareTypes_owner_([NSStringPboardType], None)
 newStr = NSString.stringWithString_(s)
 newData = newStr.nsstring().dataUsingEncoding_(NSUTF8StringEncoding)
 pb.setData_forType_(newData, NSStringPboardType)

# Gets the clipboard contents
def pbpaste():
 pb = NSPasteboard.generalPasteboard()
 content = pb.stringForType_(NSStringPboardType)
 return content


m = PyMouse()
k = PyKeyboard()


# - - - Global Variables - - -
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




def main():
    click_then_wait([80,770], 1)
    click_then_wait([500,770], 1)
    keydown_then_wait(['Command','a'], 0.2)
    keydown_then_wait(['Command','c'], 0.2)

    dataFromClipboard = pbpaste().encode('utf-8')
    myJson = dataFromClipboard[7:]
    dataFromClipboard = None
    json_data = json.loads(myJson)

    print("api_result:" + str(json_data['api_result']))
    for i in range(2):
        print("[ 第 " + str(i+1) + " 修復ドック ]")
        print("使用中：" + str(json_data['api_data'][i]['api_state']))
        print("艦娘ID：" + str(json_data['api_data'][i]['api_ship_id']))
        print("修復時間(EPOCH)：" + str(json_data['api_data'][i]['api_complete_time']))  # epoch
        print("修復時点(GMT+9)：" + str(json_data['api_data'][i]['api_complete_time_str']))



# Developer tool 的高度設在 to 1280 * 565

main()

