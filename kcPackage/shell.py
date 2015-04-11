# -*- coding: utf-8 -*-
import kcUtil as g
import kcCommand as c

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

quest+ q,w
"""


def init():
    g.gprint("あわわわ、びっくりしたのです。")
    change_place("hensei")



cmd_no_arg = c.cmd['general'].keys()
cmd_with_arg = ['place']
avail_cmds = list()

# 當遇到下列指令時，要順便改變 g.place 的值
cmd_which_change_place = ['port', 'hensei', 'refill', 'kaisou', 'ndock', 'factory', 'fight', 'senseki', 'quest']


def update_avail_cmds():
    global avail_cmds
    avail_cmds = list()
    avail_cmds = c.cmd[g.place].keys()
    avail_cmds += cmd_no_arg + cmd_with_arg


def change_place(new_place):
    g.gprint(c.cmd[g.place][new_place][0])
    g.place = new_place
    update_avail_cmds()


# http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
C_DEFAULT="\033[m"
C_GREEN="\033[32m"
C_LIGHTGREEN="\033[1;32m"
C_LIGHTRED="\033[1;31m"




init()
update_avail_cmds()

while True:
    tmp = raw_input(C_LIGHTGREEN + "電：提督、ご命令を" + C_DEFAULT + " > ")

    if tmp == "exit" or tmp =="bye":
        g.gprint("お疲れ様でした、明日も頑張ってください。")
        exit() # Exit
    elif tmp == "cmd" or tmp == '?':
        print avail_cmds
        continue
    elif tmp == "":
        tmp = "ok"

    argv = tmp.split()
    inp = argv[0]

    # 檢查是否為合法的指令
    if inp not in avail_cmds:
        g.gprint(C_LIGHTRED + "unknown command: " + inp + C_DEFAULT)
        # msg = "電：available commands: \n"
        # for item in avail_cmds:
        #     msg += item + " "
        # g.gprint(msg)
        continue

    # 檢查參數
    # 別忘了這些 if elif 的順序也代表了指令優先順序
    if inp == 'place':
        # 印出目前畫面位置
        if len(argv) == 1:
            g.gprint("私たちは今は " + g.place + " にいます")
        # 指定目前畫面位置
        else:
            change_place(argv[1])
    # 切換場景的指令（編成、補給、工廠..）
    elif inp in cmd_which_change_place:
        g.get_focus_game()
        g.click_no_wait(c.cmd[g.place][cmd][1])
        change_place(cmd)
        g.get_focus_terminal()
    # 每個場景自己的專屬指令（f1, f2, c1, s1, a, s, d, f..）
    elif inp in c.cmd[g.place].keys():
        g.get_focus_game()
        g.click_no_wait(c.cmd[g.place][cmd])
        g.get_focus_terminal()
    # 到處都可下的一般指令（ok, c, ..）
    elif inp in cmd_no_arg:
        g.get_focus_game()
        g.gprint(c.cmd['general'][cmd][0])
        g.click_no_wait(c.cmd['general'][cmd][1])
        g.get_focus_terminal()
    else:
        g.gprint(C_LIGHTRED + "ELSEESSESLEE unknown command: " + cmd + C_DEFAULT)



    # filter quest  (設定 chrome dev filter)

