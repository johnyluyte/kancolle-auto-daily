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
# 也就是說，square 的 x座標和 pymouse 的 x 座標一樣，而 square 的 y 座標加上 100 等於 pymouse 的 y 座標
# 因此我們在 square.js 內，要補充說明這點，才能達到所見即所得的效果
# 另外，square 預設長度為 17px, 加上去不掉的 border 2px, 總長度為 19px，預設點擊時顯示的是左上角的座標
# 由左上角開始不容易推估 square 內其他位置的座標
# 故 square.js 除了上述那點外，也應該印出自己“中心點的座標”，使用者比較好推斷 square 內其他位置的大約座標


