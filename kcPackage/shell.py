# -*- coding: utf-8 -*-
import kcGlobal as g
import kcUtility as u
import kcCommand as c

"""
pvt
pve
pvp

jin1~5
left
right
"""

def is_handled_by_predefined_func(inp):
    """
    針對使用者輸入的指令做預處理
    如果預處理就解決了，return True
    如果無法處理，return False
    """
    if inp == "exit" or inp =="bye":
        u.uprint("お疲れ様でした、明日も頑張ってください。")
        exit() # Exit
    elif inp.startswith('place'):
        # 印出目前場景
        if len(inp.split()) == 1:
            u.uprint("私たちは今 " + g.PLACE + " にいます")
        # 指定目前場景
        else:
            u.change_place(inp.split()[1])
        return True
    elif inp == "cmd" or inp == '?':
        u.uprint("Place = " + g.COLOR_LIGHTYELLOW+ g.PLACE + g.COLOR_DEFAULT + ", available commands = " + str(sorted(c.get_current_available_cmds())))
        return True
    elif inp == "":
        g.USER_INPUT = "ok"
        return False


def exec_command(command):
    pass


def parse_command(place ,command, args_list = None):
    cmd_msg  = c.cmd[place][command][0]
    cmd_type = c.cmd[place][command][1]
    cmd_pos  = c.cmd[place][command][2]

    # type 0 滑鼠點擊乙次：
    if cmd_type == 0:
        u.get_focus_game()
        u.uprint(cmd_msg)
        u.click_no_wait(cmd_pos)
        u.get_focus_terminal()
    # type 1 滑鼠點擊乙次(會切換場景)：
    elif cmd_type == 1:
        u.get_focus_game()
        u.uprint(cmd_msg)
        u.click_no_wait(cmd_pos)
        u.change_place(command)
        u.get_focus_terminal()
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
        u.uprint(g.COLOR_LIGHTRED + "unknown cmd_type: " + cmd_type + g.COLOR_DEFAULT)


def handle_command(inp):
    tmp = inp.split()
    command = tmp[0]
    if len(tmp)>1:
        args = tmp[1:]

    # 別忘了這些 if elif 的順序也代表了指令優先順序
    if command in c.cmd[g.PLACE].keys():
        place = g.PLACE
    elif command in c.cmd['general'].keys():
        place = 'general'
    else:
        u.uprint(g.COLOR_LIGHTRED + "unknown command: " + command + g.COLOR_DEFAULT)
        return False

    if len(tmp)>1:
        parse_command(place, command, args)
    else:
        parse_command(place, command)


def init():
    u.uprint("あわわわ、びっくりしたのです。")
    u.change_place("port")


def main():
    init()

    while True:
        g.USER_INPUT = raw_input(g.COLOR_LIGHTGREEN + "電：提督、ご命令を" + g.COLOR_DEFAULT + " > ")

        if is_handled_by_predefined_func(g.USER_INPUT) is True:
            continue

        handle_command(g.USER_INPUT)

        # filter quest  (設定 chrome dev filter)


main()