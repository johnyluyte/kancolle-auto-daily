# -*- coding: utf-8 -*-
from pymouse import PyMouse
from pykeyboard import PyKeyboard

from time import sleep
import datetime

import Foundation
import AppKit

import kcFetchAPI


# - - - Global Variables - - -

_LAG = 2
_m = PyMouse()
_k = PyKeyboard()

_place = "port"

# 顯示在 terminal 的顏色
# http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
_color = dict()



"""
一般工具
"""
def uprint(msg, font_color = 'default'):
    tmp = "電：{0}{1}{2}".format(_color[font_color], msg, _color['default'])
    print(tmp)

def uerror(msg):
    uprint(msg, 'red')

def unknown_command(command):
    uerror('unknown command: ' + command)

def change_scene(funcName):
    map( funcName, [0] )

def set_place(player, new_place):
    global _place
    if new_place == 'port' and not _place == 'port':
        get_focus_game()
        _sleep(1)
        kcFetchAPI.fetch_api_response(player, 'port')
        get_focus_terminal()
    _place = new_place
    uprint("Place は " + _color['yellow'] + new_place + _color['default'] + " に変更しました")

def get_place():
    return _place

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]

def _sleep(sleep_sec):
    if sleep_sec > 0.5:
        uprint("少々お待ちください", 'gray')
    sleep(sleep_sec)


"""
滑鼠相關
"""
def click_and_wait(position, sleep_sec = _LAG):
    # 點擊 position 之後睡眠 sleep_sec 秒，給予伺服器緩衝時間
    click_no_wait(position)
    _sleep(sleep_sec)

def click_no_wait(position):
    # 這邊可以加上 offset，用來微調或修正點擊最終位置
    # print get_time_stamp() + "click(): [" + str(position[0]) + "," + str(position[1]) + "]"
    _m.click(position[0], position[1])

def get_focus_game():
    click_and_wait([130,120], 0.01)

def get_focus_terminal():
    click_and_wait([1000,221], 0.01)


"""
鍵盤相關
"""
def keydown_and_wait(keys, sleep_sec):
    keydown_no_wait(keys)
    _sleep(sleep_sec)

def keydown_no_wait(keys):
    print get_time_stamp() + "keydown(): " + str(keys)
    _k.press_keys(keys)
    # k.release_key(keys)

def keydown_string_and_wait(msg, sleep_sec):
    keydown_string_no_wait(msg)
    _sleep(sleep_sec)

def keydown_string_no_wait(msg):
    print get_time_stamp() + "input_string(): " + msg
    _k.type_string(msg)

def keydown_ctrl_a_and_wait(sleep_sec):
    print get_time_stamp() + "keydown(): ctrl + a"
    _k.press_key('Command')
    _k.tap_key('a')
    _k.release_key('Command')
    _sleep(sleep_sec)

def keydown_ctrl_c_and_wait(sleep_sec):
    print get_time_stamp() + "keydown(): ctrl + c"
    _k.press_key('Command')
    _k.tap_key('c')
    _k.release_key('Command')
    _sleep(sleep_sec)


"""
剪貼簿相關
"""
def pbcopy(s):
    board = AppKit.NSPasteboard.generalPasteboard()
    board.declareTypes_owner_([AppKit.NSStringPboardType], None)
    newStr = Foundation.NSString.stringWithString_(s)
    newData = newStr.nsstring().dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
    board.setData_forType_(newData, AppKit.NSStringPboardType)

def pbpaste():
    board = AppKit.NSPasteboard.generalPasteboard()
    content = board.stringForType_(AppKit.NSStringPboardType)
    return content


"""
Main
"""
def main():
    global _color
    _color['default'] = "\033[m"
    _color['green']   = "\033[1;32m"
    _color['red']     = "\033[1;31m"
    _color['yellow']  = "\033[1;33m"
    _color['gray']  = "\033[1;30m"

main()
