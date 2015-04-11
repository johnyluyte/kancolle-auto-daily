# -*- coding: utf-8 -*-
import kcUtil as g
import kcCommand as c

# http://apple.stackexchange.com/questions/9821/can-i-make-my-mac-os-x-terminal-color-items-according-to-syntax-like-the-ubuntu
C_DEFAULT="\033[m"
C_GREEN="\033[32m"
C_LIGHTGREEN="\033[1;32m"
C_LIGHTRED="\033[1;31m"

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




cmd_no_arg = c.cmd['general'].keys()
cmd_with_arg = ['place']
avail_cmds = list()

# 當遇到下列指令時，要順便改變 g.place 的值
cmd_which_change_place = ['port', 'hensei', 'refill', 'kaisou', 'ndock', 'factory', 'fight', 'senseki', 'quest']



def init():
    g.gprint("あわわわ、びっくりしたのです。")
    change_place("port")


def update_avail_cmds():
    global avail_cmds
    avail_cmds = list()
    avail_cmds = c.cmd[g.place].keys()
    avail_cmds += cmd_no_arg + cmd_with_arg


def change_place(new_place):
    g.place = new_place
    update_avail_cmds()


def is_handled_by_predefined_func(inp):
    """
    針對使用者輸入的指令做預處理
    如果預處理就解決了，return True
    如果無法處理，return False
    """
    if inp == "exit" or inp =="bye":
        g.gprint("お疲れ様でした、明日も頑張ってください。")
        exit() # Exit
    elif inp.startswith('place'):
        # 印出目前場景
        if len(inp.split()) == 1:
            g.gprint("私たちは今 " + g.place + " にいます")
        # 指定目前場景
        else:
            change_place(argv[1])
        return True
    elif inp == "cmd" or inp == '?':
        g.gprint("available commands = " + avail_cmds)
        return True
    elif inp == "":
        inp = "ok"
        return False

"""
def is_legal_command(inp):
    if inp not in avail_cmds:
        g.gprint(C_LIGHTRED + "unknown command: " + inp + C_DEFAULT)
        return False
    return True
"""


def exec_command(command):
    pass

def parse_command(place ,command, args_list = None):
    cmd_msg  = c.cmd[place][command][0]
    cmd_type = c.cmd[place][command][1]
    cmd_pos  = c.cmd[place][command][2]

    # type 0 滑鼠點擊乙次：
    if cmd_type == 0:
        g.get_focus_game()
        g.gprint(cmd_msg)
        g.click_no_wait(cmd_pos)
        g.get_focus_terminal()
    # type 1 滑鼠點擊乙次(會切換場景)：
    elif cmd_type == 1:
        g.get_focus_game()
        g.gprint(cmd_msg)
        g.click_no_wait(cmd_pos)
        change_place(command)
        g.get_focus_terminal()
    # type 2 一系列的滑鼠點擊：
    elif cmd_type == 2:
        pass
    # type 3 滑鼠點擊乙次，有 callback：
    elif cmd_type == 3:
        pass
    # type 4 滑鼠點擊乙次(會切換場景)，有 callback：
    elif cmd_type == 4:
        pass
    else:
        g.gprint(C_LIGHTRED + "unknown cmd_type: " + cmd_type + C_DEFAULT)


def is_legal_command(inp):
    # 別忘了這些 if elif 的順序也代表了指令優先順序

    tmp = inp.split()
    command = tmp[0]
    if len(tmp)>1:
        args = tmp[1:]

    # 檢查每個場景自己的專屬指令（f1, f2, c1, s1, a, s, d, f..）
    if command in c.cmd[g.place].keys():
        place = g.place
    elif command in c.cmd['general'].keys():
        place = 'general'
    else:
        g.gprint(C_LIGHTRED + "unknown command: " + command + C_DEFAULT)
        return False

    if len(tmp)>1:
        parse_command(place, command, args)
    else:
        parse_command(place, command)




init()
update_avail_cmds()



while True:
    inp = raw_input(C_LIGHTGREEN + "電：提督、ご命令を" + C_DEFAULT + " > ")

    if is_handled_by_predefined_func(inp) is True:
        continue

"""
    if is_legal_command(inp.split()[0]) is False:
        continue
"""

    parse_command(inp)



    # filter quest  (設定 chrome dev filter)

