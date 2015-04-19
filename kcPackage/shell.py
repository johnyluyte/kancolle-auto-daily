# -*- coding: utf-8 -*-
from kcUtility import _color
from kcUtility import uerror
from kcUtility import uprint
from kcUtility import unknown_command
from kcUtility import set_place
from kcUtility import get_place
from kcUtility import get_focus_game
from kcUtility import get_focus_terminal
from kcUtility import click_and_wait
from kcUtility import click_no_wait

from kcCommand import get_current_available_cmds
from kcCommand import get_place_of_command
from kcCommand import exec_single_command

from kcScript import exec_script

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
        if player.get_ship_local_id(arg) == None:
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
            player.print_info_ships_count()
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
        uprint("Place = " + _color['yellow'] + get_place() + _color['default'])
        uprint("available commands = " + str(sorted(get_current_available_cmds())))
        return True
    elif inp == "":
        global _user_input
        _user_input = "ok"
        return False



def check_command(input_):
    """
    @ input_  : (string) 使用者輸入的字串
    @ return  :
        將使用者輸入的字串切割，並檢查第一個 word[0] 是否為合法的指令(Command)，
        如果正常的話就執行，不回傳
        如果非合理指令，就不動作並回傳 False
        e.g.
            input_ = "get akagi"
            則我們檢查 word[0]，也就是 "get" 是否為合法的指令。
    """
    input_ = input_.split()
    command = input_[0]
    if len(input_)>1:
        args = input_[1:]

    place = get_place_of_command(command)
    if place is None:
        unknown_command(command)
        return False

    if len(input_)>1:
        exec_script(player, place, command, args)
    else:
        exec_single_command(player, place, command)



def main():
    uprint("あわわわ、びっくりしたのです。")
    set_place("port")

    global _user_input

    while True:
        _user_input = raw_input(_color['green'] + "電：提督、ご命令を" + _color['default'] + " > ")

        if is_handled_by_predefined_func(_user_input) is True:
            continue

        check_command(_user_input)


if __name__ == '__main__':
    main()
