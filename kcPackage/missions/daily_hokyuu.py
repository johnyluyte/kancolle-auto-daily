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
    print get_time_stamp() + "click_no_wait(): [" + str(position[0]) + "," + str(position[1]) + "]"
    m.click(position[0], position[1])

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]

def seperate_hokyuu(fleet_position):
    click_no_wait(fleet_position)
    click_then_wait([630,540], gl_lag)
    click_no_wait(fleet_position)
    click_then_wait([773,543], gl_lag)


def main():
    seperate_hokyuu([158,262])
    seperate_hokyuu([162,318])
    seperate_hokyuu([158,369])
    seperate_hokyuu([159,419])
    seperate_hokyuu([164,482])
    seperate_hokyuu([167,518])

main()

