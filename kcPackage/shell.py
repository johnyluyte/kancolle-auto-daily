# -*- coding: utf-8 -*-
import kcUtility as u

import kcCommand
import kcScript
import kcFetchAPI
import kcShipData
import kcZukan

from kcClasses.player import Player

"""
TODO:
O 列出所有有 nick_name 的船
O 列出所有 fleet 的名稱
O change fleet (6 ships)，主力部隊、遠征部隊、閃亮亮部隊
O How to handle chrome dev tool unstable (periodicaly clear network monitor?)
O dock1 shimakaze
O dock1 250 0 200 0
O kaihatu sonar
O kaihatu 20 50 10 110
O dock1 uc
O build uc
O 修正 file open with
O save fleet_nick_name fleet_name
scrapy fetch vpngate file
skuik
greasemonkey

腳本：
把遠征前用 1-1 弄得閃亮亮
計算維修時間、倍數、危機有資料？  抓出艦隊種類
全自動維修
自動 3-2-1 course
自動遠征
自動每日任務
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
    elif inp.startswith('refresh') and len(inp.split()) == 1:
        kcShipData.load_csv()
        # 清空 network 監看紀錄，以免量太大導致 chrome dev tool 延遲或錯誤
        u.get_focus_game()
        u.click_and_wait([50,700], 0.05)
        u.get_focus_terminal()
        return True
    elif inp.startswith('save') and len(inp.split()) == 3:
        u.set_place(player, 'hensei')
        kcCommand.exec_single_command(player, u.get_place(), 'port')
        args = inp.split()
        kcShipData.save_current_fleets(player, args[1], args[2], player.decks[0].ships)
        kcShipData.load_csv()
        return True
    elif inp.startswith('sikuli'):
        import subprocess
        subprocess.call(['/Applications/SikuliX.app/run', '-r', 'test.sikuli'])
        return True
    # 顯示從 json API 得來的資料
    elif inp.startswith('cat') and len(inp.split()) == 2:
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
        elif arg == 'names' or arg == 'name':
            kcShipData.cat_name()
            return True
        elif arg == 'fleets' or arg == 'f':
            kcShipData.cat_fleets()
            return True
        elif arg == 'damage' or arg == 'dmg':
            player.get_damaged_ships_and_repair_time()
            return True
        else:
            return False
    elif inp.startswith('lag'):
        # 印出目前 LAG
        if len(inp.split()) == 1:
            u.uprint("サーバーとの予測レイテンシは " + u.append_color(u.get_lag(),'yellow') + " 秒です")
        # 指定目前 LAG
        else:
            u.set_lag(player, inp.split()[1])
        return True
    elif inp.startswith('place'):
        # 印出目前場景
        if len(inp.split()) == 1:
            u.uprint("私たちは今 " + u.append_color(u.get_place(),'yellow') + " にいます")
        # 指定目前場景
        else:
            u.set_place(player, inp.split()[1])
        return True
    elif inp == "cmd" or inp == '?':
        u.uprint("Place = " + u.append_color(u.get_place(),'yellow'))
        u.uprint("available commands = " + str(sorted(kcCommand.get_current_available_cmds())))
        return True
    elif inp == "":
        global _user_input
        _user_input = "ok"
        u.play_audio('kcAudio/nanodesu.mp3')
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
    kcShipData.load_csv()
    kcZukan.load_zukan_json()

    u.uprint("あわわわ、びっくりしたのです。")
    # set_place("port")

    while True:
        _user_input = raw_input(u.append_color('電：提督、ご命令を','green') + " > ")

        if is_handled_by_predefined_func(_user_input) is True:
            continue

        check_command(_user_input)


if __name__ == '__main__':
    main()
