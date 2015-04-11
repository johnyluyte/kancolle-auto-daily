# -*- coding: utf-8 -*-
import kcUtil as g
import kcGPS as gps



"""
統一選取艦隊的地方用 f1 ~ f5

dock1item
dock2item
hai
iie

port
touch
hide = port
show = port

kaisou
clear2
clear3
clear4
clear1
修正 f1~f5
"""



def init():
    g.gprint("あははは、びっくりしたのです。")
    g.gprint("あ、提督さん、ごめんなさいなのです。")
    g.gprint("私たちは今どこにいますか？")
    # inp = raw_input("電：提督、ご命令ください\n > ")
    change_place("hensei")
    g.gprint("母港ですね、わかりました。")


def error_cmd_goto():
    g.gprint(C_LIGHTRED + "unknown argv for goto: " + C_DEFAULT)
    msg = "available places for cmd : \n"
    for item in gps.pos[g.place]:
     msg += item + " "
    g.gprint(msg)





"""
指令集：


修改目前所在頁面
place (port, hensei, refill, kaisou, ndock, factory, fight, senjyou)

移動到某個頁面
(port, hensei, refill, kaisou, ndock, factory, fight)

"""

cmd_no_arg = gps.pos['general'].keys()
cmd_with_arg = ['place']
avail_cmds = list()

# 當遇到下列指令時，要順便改變 g.place 的值
cmd_which_change_place = ['port', 'hensei', 'refill', 'kaisou', 'ndock', 'factory', 'fight', 'senseki', 'quest']


def update_avail_cmds():
    global avail_cmds
    avail_cmds = list()
    avail_cmds = gps.pos[g.place].keys()
    avail_cmds += cmd_no_arg + cmd_with_arg


def change_place(new_place):
    g.gprint(gps.pos[g.place][new_place][0])
    g.place = new_place
    update_avail_cmds()
    # g.gprint("私たちは今は " + g.place + " にいます")



# http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
C_DEFAULT="\033[m"
C_GREEN="\033[32m"
C_LIGHTGREEN="\033[1;32m"
C_LIGHTRED="\033[1;31m"

""""""


init()
update_avail_cmds()

while True:
    inp = raw_input(C_LIGHTGREEN + "電：提督、ご命令を" + C_DEFAULT + " > ")

    if inp == "exit" or inp =="bye":
        g.gprint("お疲れ様でした、明日も頑張ってください。")
        exit() # Exit
    elif inp == "cmd" or inp == '?':
        print avail_cmds
        continue
    elif inp == "":
        inp = "ok"

    argv = inp.split()
    cmd = argv[0]

    # 檢查是否為合法的指令
    if cmd not in avail_cmds:
        g.gprint(C_LIGHTRED + "unknown command: " + cmd + C_DEFAULT)
        # msg = "電：available commands: \n"
        # for item in avail_cmds:
        #     msg += item + " "
        # g.gprint(msg)
        continue

    # 檢查參數
    # 別忘了這些 if elif 的順序也代表了指令優先順序
    if cmd == 'place':
        # 印出目前畫面位置
        if len(argv) == 1:
            g.gprint("私たちは今は " + g.place + " にいます")
        # 指定目前畫面位置
        else:
            change_place(argv[1])
    # 切換場景的指令（編成、補給、工廠..）
    elif cmd in cmd_which_change_place:
        g.get_focus_game()
        g.click_no_wait(gps.pos[g.place][cmd][1])
        change_place(cmd)
        g.get_focus_terminal()
    # 每個場景自己的專屬指令（f1, f2, c1, s1, a, s, d, f..）
    elif cmd in gps.pos[g.place].keys():
        g.get_focus_game()
        g.click_no_wait(gps.pos[g.place][cmd])
        g.get_focus_terminal()
    # 到處都可下的一般指令（ok, c, ..）
    elif cmd in cmd_no_arg:
        g.get_focus_game()
        g.gprint(gps.pos['general'][cmd][0])
        g.click_no_wait(gps.pos['general'][cmd][1])
        g.get_focus_terminal()
    else:
        g.gprint(C_LIGHTRED + "ELSEESSESLEE unknown command: " + cmd + C_DEFAULT)



    # filter quest  (設定 chrome dev filter)

