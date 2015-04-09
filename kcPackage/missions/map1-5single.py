# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime

m = PyMouse()
k = PyKeyboard()


# - - - Global Variables - - -
# 每個步驟之間，等待的秒數（也就是預期的網路延遲時間）
gl_lag = 4

# 將伺服器延遲時間算入的最普通的正常點擊方式
def click_then_wait(position, sleep_sec):
    """
    點擊 position 之後睡眠 sleep_sec 秒，給予伺服器緩衝時間
    """
    print get_time_stamp() + "click_then_wait(): [" + str(position[0]) + "," + str(position[1]) + "]"
    m.click(position[0], position[1])
    time.sleep(sleep_sec)


def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]


def main():
    while True:
        click_then_wait([644,443], gl_lag)
        # 燃料低於 threshold
        # 或是船艦超過 97 隻就停止練等

main()

