# -*- coding: utf-8 -*-
"""
定義各個畫面名稱

-上方-
戰績: senseki
友軍:
圖鑑:
道具:
模樣:
任務: quest
課金:

-主要-
主畫面/回主畫面: port
編成: hensei
補給: refill
改裝: kaisou
入渠: ndock
工廠: factory
出擊: fight
"""
# 定義各個按鈕的位置

# 遊戲主畫面
# pos 是座標變數的開頭
# pos 之後的第一個 hash 是目前所在的頁面
# pos 之後的第二個 hash 是目前所在的頁面想要按的按鈕座標
pos = dict()
pos['general'] = dict()
pos['general']['ok'] = [400,500]
pos['general']['left'] = [300,350]
pos['general']['right'] = [517,343]
pos['general']['back'] = [116,550]
pos['general']['c'] = pos['general']['back']
pos['general']['jin1'] = [452,279]
pos['general']['jin2'] = [572,279]
pos['general']['jin3'] = [694,282]
pos['general']['jin4'] = [516,446]
pos['general']['jin5'] = [648,441]



# 在主要的那五個畫面之間移動時，只需用左邊那些按鈕即可
pos['main5'] = dict()
pos['main5']['port'] = [79,160]
pos['main5']['hensei'] = [29,252]
pos['main5']['refill'] = [29,303]
pos['main5']['kaisou'] = [23,358]
pos['main5']['ndock'] = [23,410]
pos['main5']['factory'] =[25,458]
pos['main5']['senseki'] = [163,155]
pos['main5']['quest'] = [556,152]

# 改變船隻排列的依據
pos['main5']['sort'] = [775,212]

# 跳到第一頁 或 最後一頁
pos['main5']['q'] = [440,557]
pos['main5']['w'] = [716,554]

# 跳到下一頁 或 上一頁
pos['main5']['a'] = [517,552]
pos['main5']['s'] = [549,551]
pos['main5']['d'] = [584,551]
pos['main5']['f'] = [619,556]
pos['main5']['g'] = [641,545]

# 選擇目前頁面第 N 個船
pos['main5']['1'] = [495,240]
pos['main5']['2'] = [497,267]
pos['main5']['3'] = [497,298]
pos['main5']['4'] = [500,334]
pos['main5']['5'] = [499,363]
pos['main5']['6'] = [499,394]
pos['main5']['7'] = [498,429]
pos['main5']['8'] = [498,453]
pos['main5']['9'] = [496,484]
pos['main5']['0'] = [497,511]


pos['port'] = dict()
pos['port']['port'] = pos['main5']['port']
pos['port']['hensei'] = [202,238]
pos['port']['refill'] = [80,315]
pos['port']['kaisou'] = [318,315]
pos['port']['ndock'] = [127,462]
pos['port']['factory'] = [275,462]
pos['port']['fight'] = [207,363]  # 出擊
pos['port']['senseki'] = pos['main5']['senseki']
pos['port']['quest'] = pos['main5']['quest']

# 編成
pos['hensei'] = dict()
for key, value in pos['main5'].items():
    pos['hensei'][key] = value
# 因為有 はずす 選項的關係，所以有些按鈕要做些微調
pos['hensei']['hazusu'] = [431,234]
pos['hensei']['1'] = [469,266]
pos['hensei']['2'] = [471,293]
pos['hensei']['3'] = [464,325]
pos['hensei']['q'] = [435,550]
pos['hensei']['w'] = [716,546]
pos['hensei']['yes'] = [716,546]
pos['hensei']['y'] = pos['hensei']['yes']
pos['hensei']['hai'] = pos['hensei']['yes']


# change fleets 艦隊
pos['hensei']['f1'] = [139,223]
pos['hensei']['f2'] = [166,222]
pos['hensei']['f3'] = [198,221]
pos['hensei']['f4'] = [226,222]
# watch status 船隻狀態
pos['hensei']['s1'] = [329,314]
pos['hensei']['s2'] = [668,317]
pos['hensei']['s3'] = [328,429]
pos['hensei']['s4'] = [672,432]
pos['hensei']['s5'] = [327,537]
pos['hensei']['s6'] = [327,537]
# change ship 切換船隻
pos['hensei']['c1'] = [413,317]
pos['hensei']['c2'] = [757,311]
pos['hensei']['c3'] = [411,431]
pos['hensei']['c4'] = [751,430]
pos['hensei']['c5'] = [410,540]
pos['hensei']['c6'] = [752,538]



# 補給
pos['refill'] = dict()
for key, value in pos['main5'].items():
    pos['refill'][key] = value
pos['refill']['a'] = [150,223]
pos['refill']['s'] = [179,220]
pos['refill']['d'] = [206,221]
pos['refill']['f'] = [239,226]
pos['refill']['g'] = [268,220]
pos['refill']['all'] = [121,223]
pos['refill']['oil'] = [641,540]
pos['refill']['bullet'] = [775,534]
pos['refill']['matome'] = [703,543]


# 改裝
pos['kaisou'] = dict()
for key, value in pos['main5'].items():
    pos['kaisou'][key] = value
pos['kaisou']['a'] = [144,212]
pos['kaisou']['s'] = [175,216]
pos['kaisou']['d'] = [201,208]
pos['kaisou']['f'] = [235,211]
pos['kaisou']['g'] = [264,211]
# 第一二三艦隊的六個人
pos['kaisou']['q'] = [206,263]
pos['kaisou']['w'] = [207,314]
pos['kaisou']['e'] = [209,367]
pos['kaisou']['r'] = [209,426]
pos['kaisou']['t'] = [205,479]
pos['kaisou']['y'] = [207,528]

pos['kaisou']['q'] = [180,548]
pos['kaisou']['w'] = [210,545]
pos['kaisou']['e'] = [246,539]

pos['kaisou']['1'] = [211,251]
pos['kaisou']['2'] = [210,282]
pos['kaisou']['3'] = [205,316]
pos['kaisou']['4'] = [205,336]
pos['kaisou']['5'] = [207,368]
pos['kaisou']['6'] = [205,399]
pos['kaisou']['7'] = [203,429]
pos['kaisou']['8'] = [206,453]
pos['kaisou']['9'] = [209,484]
pos['kaisou']['0'] = [205,509]
# pos['kaisou']['clear'] = [327,328]   # 裝備數量不同，按鈕的位置也不一樣


# 入渠
pos['ndock'] = dict()
for key, value in pos['main5'].items():
    pos['ndock'][key] = value
pos['ndock']['dock1'] = [249,268]
pos['ndock']['dock2'] = [246,342]
pos['ndock']['repair'] = [690,535]
pos['ndock']['hai'] = [503,498]
pos['ndock']['iie'] = [312,494]


# 工廠
pos['factory'] = dict()
for key, value in pos['main5'].items():
    pos['factory'][key] = value
pos['factory']['dock1'] = [614,280]
pos['factory']['dock2'] = [622,360]
pos['factory']['kaitai'] = [234,347]
pos['factory']['kaihatu'] = [214,431]
pos['factory']['haiki'] = [223,509]
pos['factory']['q'] = [218,550]
pos['factory']['w'] = [497,552]
pos['factory']['a'] = [297,549]
pos['factory']['s'] = [332,552]
pos['factory']['d'] = [364,551]
pos['factory']['f'] = [395,551]
pos['factory']['g'] = [422,553]
pos['factory']['sort'] = [586,211]
pos['factory']['1'] = [294,237]
pos['factory']['2'] = [296,266]
pos['factory']['3'] = [297,297]
pos['factory']['4'] = [296,333]
pos['factory']['5'] = [296,362]
pos['factory']['6'] = [296,395]
pos['factory']['7'] = [295,424]
pos['factory']['8'] = [296,454]
pos['factory']['9'] = [294,482]
pos['factory']['0'] = [295,518]
pos['factory']['destory'] = [699,533]



# 出擊
pos['fight'] = dict()
for key, value in pos['main5'].items():
    pos['fight'][key] = value
pos['fight']['pve'] = [232,330]
pos['fight']['pvp'] = [463,331]
pos['fight']['pvt'] = [682,330]



# 任務一覽第 N 頁按鈕位置
pos['quest'] = dict()
pos['quest']['a'] = [355,563]
pos['quest']['s'] = [406,564]
pos['quest']['d'] = [455,563]
pos['quest']['f'] = [514,563]
pos['quest']['g'] = [563,561]
pos['quest']['1'] = [739,243]
pos['quest']['2'] = [739,307]
pos['quest']['3'] = [739,376]
pos['quest']['4'] = [743,443]
pos['quest']['5'] = [746,519]
pos['quest']['port'] = pos['main5']['port']
# btn_pages = [btn_page1, btn_page2, btn_page3, btn_page4, btn_page5]



