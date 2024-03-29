# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime

m = PyMouse()
k = PyKeyboard()


# - - - Global Variables - - -
# 每個步驟與伺服器之間，等待的秒數（也就是預期的網路延遲時間）
gl_lag = 0.1
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
    print get_time_stamp() + "click_no_wait(): [" + str(position[0]) + "," + str(position[1]) + "]"
    m.click(position[0], position[1])

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]

def main():
    click_then_wait([190,238], gl_lag)
    click_then_wait([191,267], gl_lag)
    click_then_wait([189,300], gl_lag)
    click_then_wait([188,332], gl_lag)
    click_then_wait([189,362], gl_lag)
    click_then_wait([188,391], gl_lag)
    click_then_wait([189,420], gl_lag)
    click_then_wait([190,447], gl_lag)
    click_then_wait([188,481], gl_lag)
    click_then_wait([189,511], gl_lag)
    click_then_wait([706,529], gl_lag)

main()

