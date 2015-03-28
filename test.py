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
m.click(x_dim/5, y_dim/5, 1)


# - - - 各按鈕座標位置 - - -

# 主畫面
# 補給按鈕
btn_main_hokyuu_x = x_dim * 0.24
btn_main_hokyuu_y = y_dim * 0.51


for i in range(5):
    m.click(btn_main_hokyuu_x, btn_main_hokyuu_y, 1)
    print "click [" , str(btn_main_hokyuu_x), "," , str(btn_main_hokyuu_y), "]"
    time.sleep(gl_expected_lag)


# k.type_string('Hello, World!')


