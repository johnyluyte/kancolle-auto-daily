# -*- coding: utf-8 -*-
from pymouse import PyMouse
from pykeyboard import PyKeyboard

import time
import datetime

import Foundation
import AppKit

import kcGlobal as g


# - - - Global Variables - - -

m = PyMouse()
k = PyKeyboard()


# 複製字串到 MAC 的剪貼簿
def pbcopy(s):
    # "Copy string argument to clipboard"
    board = AppKit.NSPasteboard.generalPasteboard()
    board.declareTypes_owner_([AppKit.NSStringPboardType], None)
    newStr = Foundation.NSString.stringWithString_(s)
    newData = newStr.nsstring().dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
    board.setData_forType_(newData, AppKit.NSStringPboardType)

# 從 MAC 的剪貼簿取出字串
def pbpaste():
    # "Returns contents of clipboard"
    board = AppKit.NSPasteboard.generalPasteboard()
    content = board.stringForType_(AppKit.NSStringPboardType)
    return content



# 將伺服器延遲時間算入的最普通的正常點擊方式
def click_and_wait(position, sleep_sec = g.LAG):
    """
    點擊 position 之後睡眠 sleep_sec 秒，給予伺服器緩衝時間
    """
    click_no_wait(position)
    time.sleep(sleep_sec)

def click_no_wait(position):
    # 這邊可以加上 offset，用來微調或修正點擊最終位置
    # print get_time_stamp() + "click(): [" + str(position[0]) + "," + str(position[1]) + "]"
    m.click(position[0], position[1])

def keydown_and_wait(keys, sleep_sec):
    keydown_no_wait(keys)
    time.sleep(sleep_sec)

def keydown_no_wait(keys):
    print get_time_stamp() + "keydown(): " + str(keys)
    k.press_keys(keys)

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]


def uprint(msg):
    print "電：", msg

# def finish():
    # gprint("任務完了")

def get_focus_game():
    click_and_wait([130,120], 0.1)

def get_focus_terminal():
    click_and_wait([1000,221], 0.1)

def change_place(new_place):
    g.PLACE = new_place
    uprint("Place は " + new_place + " に変更しました")