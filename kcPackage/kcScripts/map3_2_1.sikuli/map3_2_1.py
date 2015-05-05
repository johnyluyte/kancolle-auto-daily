# -*- coding: utf-8 -*-
print "\033[1;33m[ Sikuri Map 3-2-1 Started]\033[m"

sleep(20)


# 第一戰可能有兩種情形
while(1):
    # 沒全滅敵人，不追擊
    if(exists("tuigekisezu.png")):
        click("tuigekisezu.png")
        wait("tettai.png", 80)
        click("tettai.png")
        break
    # 全滅敵人，偵測是否回到母港了
    elif(exists("tettai.png")):
        click("tettai.png")
        break
    sleep(0.1)

wait("fight.png",30)

print "\033[1;33m[ Sikuri Map 3-2-1 Finished ]\033[m"
