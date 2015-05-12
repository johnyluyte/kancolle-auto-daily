# -*- coding: utf-8 -*-
# import datetime
print "\033[1;33m[ Sikuri Started (Plan A) ]\033[m"

sleep(10)

region_fleets  = Region(8,102,307,459)
region_general = Region(103,228,635,251)

region_fleets.setAutoWaitTimeout(0.5)
region_general.setAutoWaitTimeout(0.1)

# cyuuha_detected = False
daiha_detected = False

while True:
    # print "while  " + str(datetime.datetime.now()).split('.')[0]

    # 沒有船艦大破
    if(daiha_detected is False):
        # 選擇進擊
        if(region_general.exists("singeki.png")):
            click("singeki.png")
        # 偵測是否大破
        elif(region_fleets.exists(Pattern("daiha.png").similar(0.80))):
            daiha_detected = True
            print "\033[1;31m!!! 大破 detected、すぐ撤退します!\033[m"
    # 已經有船艦大破惹
    elif(daiha_detected is True):
        if(region_general.exists("tettai.png")):
            click("tettai.png")

    # 偵測是否中破
    # if(cyuuha_detected is False):
    #     if(region_fleets.exists(Pattern("cyuuha.png").similar(0.92))):
    #         cyuuha_detected = True
    #         print "\033[33m!!! 中破 detected、まだ大丈夫です!\033[m"

    # 無論如何都 不進入夜戰
    if(region_general.exists("tuigekisezu.png")):
        click("tuigekisezu.png")
    # 偵測是否回到母港了
    elif(region_general.exists("fight.png")):
        break

print "\033[1;33m[ Sikuri Finished (Plan A) ]\033[m"
