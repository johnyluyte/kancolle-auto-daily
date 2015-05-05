# -*- coding: utf-8 -*-
print "\033[1;33m[ Sikuri Map 1-1 Started ]\033[m"


# 假設第一戰一定Ｓ勝利，若沒勝利，這腳本會出問題
# 直接選擇進擊
wait("singeki.png", 120)
click("singeki.png")

# 第二戰可能有兩種情形
while(1):
    # 沒全滅敵人，不追擊
    if(exists("tuigekisezu.png")):
        click("tuigekisezu.png")
        wait("fight.png", 80)
        break
    # 全滅敵人，偵測是否回到母港了
    elif(exists("fight.png")):
        break
    sleep(0.1)

print "\033[1;33m[ Sikuri Map 1-1 Finished ]\033[m"
