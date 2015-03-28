# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()


# - - - Global Variables - - -
# 每個步驟之間，等待的秒數（也就是預期的網路延遲時間）
gl_expected_lag = 1.6
# 整個 MAC 螢幕的長、寬
x_dim, y_dim = m.screen_size()
# Get focus off terminal
# m.click(x_dim/5, y_dim/5, 1)

while True:
    inpX = raw_input("input x: ")
    inpY = raw_input("input y: ")
    if inpX == 'x' or inpY == 'x':
        break;
    m.click(float(inpX), float(inpY), 1)

# 對於 pymouse 來說，kancolle flash 的左上角約在座標 [240,175] 的位置
# 當 square.js 的設定為 (square長寬:17, row:29, col:54) 時，剛好有一 square 與 kancolle flash 的左上角相切
# 該 square 的座標為 [241,77]



# - - - 各按鈕座標位置 - - -

# 主畫面
# 補給按鈕


# btn_main_hokyuu_x = x_dim * 0.24
# btn_main_hokyuu_y = y_dim * 0.51


# for i in range(5):
#     m.click(btn_main_hokyuu_x, btn_main_hokyuu_y, 1)
#     print "click [" , str(btn_main_hokyuu_x), "," , str(btn_main_hokyuu_y), "]"
#     time.sleep(gl_expected_lag)


# k.type_string('Hello, World!')


