# -*- coding: utf-8 -*-
import kcUtil as g
import kcGPS as gps



def init():
    g.gprint("電：あははは、びっくりしたのです。")
    g.gprint("電：あ、提督さん、ごめんなさいなのです。")
    g.gprint("電：私たちは今どこにいますか？")
    # inp = raw_input("電：提督、ご命令ください\n > ")
    g.place = "port"
    g.gprint("電：母港ですね、わかりました。")


def error_cmd_goto():
    g.gprint(C_LIGHTRED + "電：unknown argv for goto: " + C_DEFAULT)
    msg = "電：available places for cmd goto: \n"
    for item in gps.pos[g.place]:
     msg += item + " "
    g.gprint(msg)





"""
指令集：


修改目前所在頁面
place (port, hensei, refill, kaisou, ndock, factory, fight, senjyou)

移動到某個頁面
goto (port, hensei, refill, kaisou, ndock, factory, fight)

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
    g.place = new_place
    update_avail_cmds()
    g.gprint("電：私たちは今は " + g.place + " にいます")



# http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
C_DEFAULT="\033[m"
C_GREEN="\033[32m"
C_LIGHTGREEN="\033[1;32m"
C_LIGHTRED="\033[1;31m"

""""""


init()
update_avail_cmds()

while True:
    inp = raw_input(C_LIGHTGREEN + "電：提督、ご命令ください" + C_DEFAULT + "\n > ")

    if inp == "exit" or inp =="bye":
        g.gprint("電：お疲れ様でした、明日も頑張ってください。")
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
        g.gprint(C_LIGHTRED + "電：unknown command: " + cmd + C_DEFAULT)
        # msg = "電：available commands: \n"
        # for item in avail_cmds:
        #     msg += item + " "
        # g.gprint(msg)
        continue

    # 檢查參數
    if cmd == 'place':
        # 印出目前畫面位置
        if len(argv) == 1:
            g.gprint("電：私たちは今は " + g.place + " にいます")
        # 指定目前畫面位置
        else:
            change_place(argv[1])
    elif cmd in cmd_which_change_place:
        g.get_focus_game()
        g.click_no_wait(gps.pos[g.place][cmd])
        change_place(cmd)
        g.get_focus_terminal()
    elif cmd in cmd_no_arg:
        g.get_focus_game()
        g.click_no_wait(gps.pos['general'][cmd])
        g.get_focus_terminal()
    else:
        g.get_focus_game()
        g.click_no_wait(gps.pos[g.place][cmd])
        g.get_focus_terminal()

"""
    elif cmd == "goto":
        if len(argv) == 1:
            error_cmd_goto()
            continue

        newPlace = argv[1]
        coordination = gps.pos[g.place].get(newPlace, None)
        if(coordination is None):
            error_cmd_goto()
        else:
            g.get_focus_game()
            g.click_no_wait(coordination)
            g.place = newPlace
            g.get_focus_terminal()
 """

    # filter quest  (設定 chrome dev filter)

