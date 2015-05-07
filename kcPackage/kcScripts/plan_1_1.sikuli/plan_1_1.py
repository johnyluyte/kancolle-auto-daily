# -*- coding: utf-8 -*-
import sys
print "\033[1;33m[ Sikuri Started (Plan A) ]\033[m"

sleep(20)

region_fleets = Region(8,102,307,459)
region_general   = Region(103,228,635,251)

cyuuha_detected = False
daiha_detected = False

while(1):
    # 無論如何都選擇 進擊
    if(region_general.exists("singeki.png")) and (daiha_detected is False):
        click("singeki.png")
    elif(region_general.exists("tettai.png")) and (daiha_detected is True):
        click("tettai.png")
    elif(region_fleets.exists("cyuuha.png")):
        if(cyuuha_detected is False):
            cyuuha_detected = True
            print "--------------"
            print "\033[33m 中破 detected、まだ大丈夫です \033[m"
            print "--------------"
            sys.stdout.flush()
    elif(region_fleets.exists(Pattern("daiha.png").similar(0.81))):
        if(daiha_detected is False):
            daiha_detected = True
            print "--------------"
            print "\033[1;31m 大破 detected、戦闘が終わったらすぐ撤退します \033[m"
            print "--------------"
            sys.stdout.flush()
    # 無論如何都 不進入夜戰
    elif(region_general.exists("tuigekisezu.png")):
        click("tuigekisezu.png")
    # 偵測是否回到母港了
    elif(region_general.exists("fight.png")):
        break
    sleep(0.5)

print "\033[1;33m[ Sikuri Finished (Plan A) ]\033[m"
