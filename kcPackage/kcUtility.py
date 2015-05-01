# -*- coding: utf-8 -*-
from pymouse import PyMouse
from pykeyboard import PyKeyboard

from time import sleep
import datetime

import Foundation
import AppKit

import threading
import subprocess

import kcFetchAPI


# - - - Global Variables - - -

_LAG = 3.0
_m = PyMouse()
_k = PyKeyboard()

_place = "port"


color = dict()



"""
一般工具
"""
def uprint(msg, font_color = 'default'):
    if font_color == 'default':
        tmp = "電：{}".format( msg )
    else:
        tmp = "電：{}".format( append_color(msg, font_color) )
    print(tmp)

def uerror(msg):
    uprint(msg, 'red')

def append_color(msg, font_color = 'default'):
    return '{}{}{}'.format(color[font_color], msg, color['default'])

def unknown_command(command):
    uerror('unknown command: ' + command)

def change_scene(funcName):
    map( funcName, [0] )

def set_place(player, new_place):
    global _place
    if new_place == 'port' and not _place == 'port':
        get_focus_game()
        _sleep(1.5)
        kcFetchAPI.fetch_api_response(player, 'port')
        get_focus_terminal()
    _place = new_place
    uprint("Place は " + append_color(new_place, 'yellow') + " に変更しました")

def get_place():
    return _place

def set_lag(player, new_latency):
    global _LAG
    try:
        new = float(new_latency)
    except ValueError:
        new = _LAG
    _LAG = new
    uprint("Lag は " + append_color(_LAG, 'yellow') + " に変更しました")

def get_lag():
    return _LAG

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]

def _sleep(sleep_sec):
    if sleep_sec > 0.7:
        uprint("少々お待ちください ("+ str(sleep_sec) + "s)", 'gray')
    sleep(sleep_sec)

"""
撥音效相關

原版 Python 做不到，需要第三方 library 支援
但我們只很少撥音效，故使用 overhead 較高的 subprocess 來呼叫 OSX terminal 的 afplay 指令撥音即可
"""
class AudioThread(threading.Thread):
    def __init__(self, thread_name, audio_path):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.audio_path = audio_path
    def run(self):
        # print "Starting " + self.name
        subprocess.call(['afplay', self.audio_path])
        # print "Exiting " + self.name

def play_audio(audio_path):
    audio_thread = AudioThread("Thread-1", audio_path)
    audio_thread.start()



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

def scroll_down(arg_vertical = -20):
    _m.scroll(vertical = arg_vertical)  # Scrolls up 3 ticks

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
    # print get_time_stamp() + "input_string(): " + msg
    _k.type_string(msg)

def keydown_ctrl_a_and_wait(sleep_sec):
    # print get_time_stamp() + "keydown(): ctrl + a"
    _k.press_key('Command')
    _k.tap_key('a')
    _k.release_key('Command')
    _sleep(sleep_sec)

def keydown_ctrl_c_and_wait(sleep_sec):
    # print get_time_stamp() + "keydown(): ctrl + c"
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
    # 顯示在 terminal 的顏色
    # http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
    global color
    color['default'] = "\033[m"
    color['green']   = "\033[1;32m"
    color['red']     = "\033[1;31m"
    color['orange']  = "\033[33m"
    color['yellow']  = "\033[1;33m"
    color['gray']    = "\033[1;30m"
    color['blue']    = "\033[1;34m"
    color['purple']  = "\033[1;35m"
    color['cyan']    = "\033[1;36m"
main()
