# -*- coding: utf-8 -*-
import kcCommand as c

from kcUtility import _color
from kcUtility import uerror
from kcUtility import uprint
from kcUtility import set_place
from kcUtility import get_place
from kcUtility import get_focus_game
from kcUtility import get_focus_terminal
from kcUtility import click_no_wait

from kcFetchAPI import fetch_api_response

from kcClasses.player import Player


"""
refill f5 need qwasdf
"""


player = Player()
_user_input = None



def is_handled_by_predefined_func(inp):
    """
    針對使用者輸入的指令做預處理
    如果預處理就解決了，return True
    如果無法處理，return False
    """
    if inp == "exit" or inp =="bye":
        uprint("お疲れ様でした、明日も頑張ってください")
        exit()
    # 抓取 json API
    elif inp.startswith('api') and len(inp.split()) == 2:
        arg = inp.split()[1]
        if arg == 'quest' or arg == 'q':
            get_focus_game()
            fetch_api_response(player, 'questlist')
            get_focus_terminal()
            return True
        elif arg == 'port' or arg == 'p':
            get_focus_game()
            fetch_api_response(player, 'port')
            get_focus_terminal()
            return True
        else:
            return False
    # 顯示從 json API 得來的資料
    elif inp.startswith('get') and len(inp.split()) == 2:
        arg = inp.split()[1]
        if player.get_ship(arg) == None:
            return False
        else:
            return True
    elif inp.startswith('data') and len(inp.split()) == 2:
        arg = inp.split()[1]
        if arg == 'quest' or arg == 'q':
            return True
        elif arg == 'port' or arg == 'p':
            return True
        elif arg == 'deck' or arg == 'd':
            player.print_info_decks()
            return True
        elif arg == 'ndock' or arg == 'n':
            player.print_info_ndocks()
            return True
        elif arg == 'event' or arg == 'e':
            # 即將到來的事件（修復、遠征、建造）
            return True
        elif arg == 'ship' or arg == 's':
            for i in range(1,101):
                if i % 10 == 1:
                    print "[", i, "]"
                player.print_info_ships(i)
            return True
        elif arg == 'material' or arg == 'r': # Resource
            player.print_info_materials()
            return True
        elif arg == 'myfleet' or arg == 'm':
            return True
        else:
            return False
    elif inp.startswith('place'):
        # 印出目前場景
        if len(inp.split()) == 1:
            uprint("私たちは今 " + get_place() + " にいます")
        # 指定目前場景
        else:
            set_place(inp.split()[1])
        return True
    elif inp == "cmd" or inp == '?':
        uprint("Place = " + _color['yellow'] + get_place() + _color['default'] + ", available commands = " + str(sorted(c.get_current_available_cmds())))
        return True
    elif inp == "":
        global _user_input
        _user_input = "ok"
        return False


def exec_command(command):
    pass


def parse_command(place ,command, args_list = None):
    cmd_msg  = c.cmd[place][command][0]
    cmd_type = c.cmd[place][command][1]
    cmd_pos  = c.cmd[place][command][2]

    # type 0 滑鼠點擊乙次：
    if cmd_type == 0:
        get_focus_game()
        uprint(cmd_msg)
        click_no_wait(cmd_pos)
        get_focus_terminal()
    # type 1 滑鼠點擊乙次(會切換場景)：
    elif cmd_type == 1:
        get_focus_game()
        uprint(cmd_msg)
        click_no_wait(cmd_pos)
        set_place(command)
        get_focus_terminal()
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
        uerror("unknown cmd_type: " + cmd_type)


def handle_command(inp):
    tmp = inp.split()
    command = tmp[0]
    if len(tmp)>1:
        args = tmp[1:]

    # 別忘了這些 if elif 的順序也代表了指令優先順序
    if command in c.cmd[get_place()].keys():
        place = get_place()
    elif command in c.cmd['general'].keys():
        place = 'general'
    else:
        uerror("unknown command: " + command)
        return False

    if len(tmp)>1:
        parse_command(place, command, args)
    else:
        parse_command(place, command)


def init():
    uprint("あわわわ、びっくりしたのです。")
    set_place("port")


def main():
    init()

    while True:
        global _user_input
        _user_input = raw_input(_color['green'] + "電：提督、ご命令を" + _color['default'] + " > ")

        if is_handled_by_predefined_func(_user_input) is True:
            continue

        handle_command(_user_input)

main()
