# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime

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
    k.press_keys(['Command','a'])

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]




def main():
    # click_then_wait([80,770], 1)
    click_then_wait([500,770], 0.5)
    keydown_then_wait(['Command','a'], 0.5)
    keydown_then_wait(['Command','c'], 0.5)


# Developer tool 的高度設在 to 1280 * 565

main()

