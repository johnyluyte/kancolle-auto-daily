# 用尺量螢幕，算出每個按鈕的大致位置，然後丟入此程式，即可算出與總螢幕寬的比例
# 按鈕的 x 坐標為（由左往右量）
# 按鈕的 y 坐標為（由下往上量）
# 螢幕總寬 x_dim 約 28.7 公分
# 螢幕總高 y_dim 約 17.8 公分

inpX = raw_input("enter X cm (L to R): ")
inpY = raw_input("enter Y cm (D to U): ")

ansX = round((float(inpX) / 28.7), 2)
ansY = round((float(inpY) / 17.8), 2)

print 'offset =', ansX, ansY

# 之後在主程式就可藉由下面方式，得到此按鈕的“坐標”
# 補給按鈕
# x_dim, y_dim = m.screen_size()
# btn_main_hokyuu_x = x_dim * 0.24  (上面的 ansX)
# btn_main_hokyuu_y = y_dim * 0.51  (上面的ansY)
# m.click(btn_main_hokyuu_x, btn_main_hokyuu_y, 1)
