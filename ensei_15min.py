# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import datetime

m = PyMouse()
k = PyKeyboard()


# - - - Global Variables - - -
# 每個步驟之間，等待的秒數（也就是預期的網路延遲時間）
gl_lag = 3
# 整個 MAC 螢幕的長、寬
x_dim, y_dim = m.screen_size()
# Get focus off terminal
m.click(250, 350, 1)



# 狂點擊某個位置
def click_for_N_seconds(position, sleep_sec, n_sec):
    """
    每隔 sleep_sec 就點擊一次 position，持續 n_sec 秒
    因為是狂點擊的關係，sleep_sec 可以不用跟 gl_lag 一樣沒關係
    """
    period = n_sec // sleep_sec
    for i in range(period):
        print get_time_stamp() + "clickForNSeconds(): [" + str(position[0]) + "," + str(position[1]) + "]"
        m.click(position[0], position[1])
        time.sleep(sleep_sec)

# 將伺服器延遲時間算入的最普通的正常點擊方式
def click_then_wait(position, sleep_sec):
    """
    點擊 position 之後睡眠 sleep_sec 秒，給予伺服器緩衝時間
    """
    print get_time_stamp() + "click_then_wait(): [" + str(position[0]) + "," + str(position[1]) + "]"
    m.click(position[0], position[1])
    time.sleep(sleep_sec)



# 15 分鐘遠征計畫
def ensei_15min():
    # 遠征快要回來了
    # 需要點擊進入一個地方再出來，才會更新遠征狀態
    click_then_wait([300, 400], gl_lag)
    click_then_wait([300, 400], gl_lag)
    # 觀看完遠征結果：狂點 [1010,280]  12 秒
    click_for_N_seconds([1010,280], 1, 20)
    # 主畫面中點擊補給補給 [300, 400]
    click_then_wait([300, 400], gl_lag)
    # 點選第二艦隊 [420, 300]
    click_then_wait([420, 300], gl_lag)
    # 打勾勾選擇第二艦隊所有船艦 [355, 300]
    click_then_wait([355, 300], gl_lag)
    # 按右下角一次補給完成 [933, 610]
    click_then_wait([933, 610], gl_lag)
    # 左上角回到主畫面 [300, 250]
    click_then_wait([300, 250], gl_lag)
    # 出擊 [444, 444]
    click_then_wait([444, 444], gl_lag)
    # 選擇遠征 [900, 400]
    click_then_wait([900, 400], gl_lag + 2)
    # 選擇第一關的第一個地圖 [600, 350]
    # click_then_wait([600, 350], gl_lag + 2)
    # 選擇第一關的第五個地圖 [600, 470]
    click_then_wait([600, 470], gl_lag + 2)
    # 選擇決定 [915, 620]
    click_then_wait([915, 620], gl_lag + 1)
    # 選擇預設的第二艦隊，出發 [875, 622]
    click_then_wait([875, 622], gl_lag + 1)
    # 點擊安全地點直到出發動畫結束 [1010,280] 12 秒
    click_for_N_seconds([1010,280], 1, 12)
    # 點擊左上角回母港 [300, 250]
    click_then_wait([300, 250], gl_lag)
    # 等待 15 分鐘

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]


def count_down(minute_left):
    for i in range(minute_left):
        print get_time_stamp() + "waiting.. " + str(minute_left - i) + " minutes left."
        click_then_wait([1010,280], 1)
        time.sleep(59)

def main():
    while True:
        ensei_15min()
        count_down(90)

main()

