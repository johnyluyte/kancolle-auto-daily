# -*- coding: utf-8 -*-
import kcUtility as u

import kcCommand
import kcScript
import kcFetchAPI

from kcClasses.player import Player

"""
TODO:
列出所有有 nick_name 的船
列出所有 fleet 的名稱
change fleet (6 ships)
quest
How to handle chrome dev tool unstable (periodicaly clear network monitor?)
"""

def is_handled_by_predefined_func(inp):
    """
    針對使用者輸入的指令做預處理
    如果預處理就解決了，return True
    如果無法處理，return False
    """
    if inp == "exit" or inp =="bye":
        u.uprint("お疲れ様でした、明日も頑張ってください")
        exit()
    # 抓取 json API
    elif inp.startswith('api') and len(inp.split()) == 2:
        arg = inp.split()[1]
        if arg == 'quest' or arg == 'q':
            u.get_focus_game()
            kcFetchAPI.fetch_api_response(player, 'questlist')
            u.get_focus_terminal()
            return True
        elif arg == 'port' or arg == 'p':
            u.get_focus_game()
            kcFetchAPI.fetch_api_response(player, 'port')
            u.get_focus_terminal()
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
            u.uprint("私たちは今 " + u._color['yellow'] + u.get_place() + u._color['default'] + " にいます")
        # 指定目前場景
        else:
            u.set_place(player, inp.split()[1])
        return True
    elif inp == "cmd" or inp == '?':
        u.uprint("Place = " + u._color['yellow'] + u.get_place() + u._color['default'])
        u.uprint("available commands = " + str(sorted(kcCommand.get_current_available_cmds())))
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

    place = kcCommand.get_place_of_command(command)
    if place is None:
        u.unknown_command(command)
        return False

    if len(input_)>1:
        kcScript.exec_script(player, place, command, args)
    else:
        kcCommand.exec_single_command(player, place, command)




def main():
    global _user_input
    global player
    player = Player()

    u.uprint("あわわわ、びっくりしたのです。")
    # set_place("port")

    while True:
        _user_input = raw_input(u._color['green'] + "電：提督、ご命令を" + u._color['default'] + " > ")

        if is_handled_by_predefined_func(_user_input) is True:
            continue

        check_command(_user_input)


if __name__ == '__main__':
    main()
