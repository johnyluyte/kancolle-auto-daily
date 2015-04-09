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
        msg = get_time_stamp() + "clickForNSeconds(): [" + str(position[0]) + "," + str(position[1]) + "]\n"
        fileHandler.write(msg)
        print msg
        m.click(position[0], position[1])
        time.sleep(sleep_sec)

# 將伺服器延遲時間算入的最普通的正常點擊方式
def click_then_wait(position, sleep_sec):
    """
    點擊 position 之後睡眠 sleep_sec 秒，給予伺服器緩衝時間
    """
    msg = get_time_stamp() + "click_then_wait(): [" + str(position[0]) + "," + str(position[1]) + "]\n"
    fileHandler.write(msg)
    print msg
    m.click(position[0], position[1])
    time.sleep(sleep_sec)



# 15 分鐘遠征計畫
def ensei_15min():
    # 遠征快要回來了
    # 需要點擊進入一個地方再出來，才會更新遠征狀態
    # 觀看完遠征結果：狂點 [1010,280]  12 秒
    click_for_N_seconds([55,552], 1, 12)
    # 主畫面中點擊補給補給 [300, 400]
    click_then_wait([80,345], gl_lag)
    # 點選第二艦隊 [420, 300]
    click_then_wait([180,220], gl_lag)
    # 打勾勾選擇第二艦隊所有船艦 [355, 300]
    click_then_wait([120,221], gl_lag)
    # 按右下角一次補給完成 [933, 610]
    click_then_wait([701,538], gl_lag)
    # 左上角回到主畫面 [300, 250]
    click_then_wait([71,178], gl_lag)
    # 出擊 [444, 444]
    click_then_wait([211,358], gl_lag)
    # 選擇遠征 [900, 400]
    click_then_wait([678,332], gl_lag)
    # 選擇第一關的第一個地圖 [600, 350]
    # click_then_wait([600, 350], gl_lag + 2)
    # 選擇第一關的第三個地圖 [600, 470]
    click_then_wait([279,333], gl_lag)
    # 選擇決定 [915, 620]
    click_then_wait([687,538], gl_lag)
    # 選擇預設的第二艦隊，出發 [875, 622]
    click_then_wait([397,224], gl_lag )
    click_then_wait([639,543], gl_lag )
    # 點擊安全地點直到出發動畫結束 [1010,280] 12 秒
    click_for_N_seconds([55,552], 1, 12)
    # 點擊左上角回母港 [300, 250]
    click_then_wait([71,178], gl_lag)
    # 等待 15 分鐘

def get_time_stamp():
    current_time = str(datetime.datetime.now()).split('.')[0] # 2015-03-29 20:18:08
    return "[" + current_time[5:] + "] " # [03-29 20:18:08]


def count_down(minute_left):
    for i in range(minute_left):
        print get_time_stamp() + "waiting.. " + str(minute_left - i) + " minutes left."
        # 按下戰績表示，再按左下角回主畫面，是最能確定回主畫面的方法，是最好的 beacon 選擇
        click_then_wait([167,147], 1)
        time.sleep(30)
        click_then_wait([55,552], 1)
        time.sleep(30)

def main():
    while True:
        ensei_15min()
        count_down(19)


fileHandler = None
fileName = str(datetime.datetime.now()).split('.')[0]
fileHandler = open("log/ensei_" + fileName,"a")



# click_then_wait([632,375], gl_lag + 1)
main()

