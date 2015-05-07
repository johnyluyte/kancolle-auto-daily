# -*- coding: utf-8 -*-
print "\033[1;33m[ Sikuri Started (Plan B) ]\033[m"

sleep(20)

while(1):
    # 無論如何都選擇 撤退(只打一戰)
    if(exists("tettai.png")):
        click("tettai.png")
    # 無論如何都 不進入夜戰
    elif(exists("tuigekisezu.png")):
        click("tuigekisezu.png")
    # 偵測是否回到母港了
    elif(exists("fight.png")):
        break
    sleep(2)

print "\033[1;33m[ Sikuri Finished (Plan B) ]\033[m"
