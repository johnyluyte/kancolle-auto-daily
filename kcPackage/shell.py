# -*- coding: utf-8 -*-
import kcUtility as u

import kcCommand
import kcScript
import kcFetchAPI
import kcShipData
import kcZukan
import kcGear

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
O 計算維修時間、倍數、危機有資料？  抓出艦隊種類
O fetch vpngate file
O 全自動維修
O auto_repair 的 lag 沒做用?
O cat ?
O api except 要自動 retry，先點 network
O 距離下一個破還差多少 HP
O condition

O 對潛裝備在誰身上
1. cat item 列出所有裝備(名稱:數量，排序，數量越少加顏色，方便我自己判斷)
如果沒有在艦娘身上的裝備，會顯示在哪裡!?
不用擔心，slot_item.json 會列出所有裝備，但要記得重新登入抓取
2. cat gear 列出重要裝備(水雷、聲納、烈雲)
缺點，需要重新登入才能抓到 slot_item.json

O sikuli
/Applications/SikuliX.app/run -r ~/myScript.sikuli
O 減少 sikuli 比對的範圍

O CAT 加上 裝備連擊、春季Event

腳本：
O 把遠征前用 1-1 弄得閃亮亮
O 自動 3-2-1 course

O greasemonkey

zukan 是不是太小題大作，我們只需要 stype，是否可直接從 api_start2 獲取?
第一艦隊名稱

更新 slot_item.json
random sleep in scripts to avoid detecter

阿部 chrome extension
防止 kancolle error niki 的 chrome extension?
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
    elif inp.startswith('api') and len(inp.split()) == 2:
        # 抓取 json API
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
        # 重新讀取 kcShipData
        kcShipData.load_csv()
        # 清空 network 監看紀錄，以免量太大導致 chrome dev tool 延遲或錯誤
        u.get_focus_game()
        u.click_and_wait([50,700], 0.05)
        u.get_focus_terminal()
        return True
    elif inp.startswith('save') and len(inp.split()) == 3:
        # 將目前第一艦隊的建娘組合存入 kcShipData 的 fleet
        u.set_place(player, 'hensei')
        kcCommand.exec_single_command(player, u.get_place(), 'port', u.get_lag())
        args = inp.split()
        kcShipData.save_current_fleets(player, args[1], args[2], player.decks[0].ships)
        kcShipData.load_csv()
        return True
    elif inp.startswith('map11'):
        kcScript.exec_sikuli(player ,'1-1')
        return True
    elif inp.startswith('map21'):
        kcScript.exec_sikuli(player ,'2-1')
        return True
    elif inp.startswith('map22'):
        kcScript.exec_sikuli(player ,'2-2')
        return True
    elif inp.startswith('map321'):
        kcScript.exec_sikuli(player ,'3-2-1')
        return True
    elif inp.startswith('auto') and len(inp.split()) == 2:
        arg = inp.split()[1]
        if arg == 'repair' or arg == 'r':
            # 自動維修
            kcScript.exec_script(player, 'auto', 'repair', None)
            return True
    elif inp.startswith('cat') and len(inp.split()) == 2:
        # 顯示從 json API 得來的資料
        arg = inp.split()[1]
        if arg == '?':
            print('cat [arguments]:')
            print("[deck] [d] - 印出四個艦隊編成")
            print("[ndock] [n] - 印出維修工廠狀態")
            print("[ship] [s] - 印出所有船艦狀態")
            print("[material] [r] - 印出目前擁有的資源")
            print("[names] [name] - 印出四個艦隊編成")
            print("[fleets] [f] - 印出使用者自行編列的艦隊編成")
            print("[damage] [dmg] - 印出受傷的船艦與預期維修時間")
            print("[gearall] [ga] - 印出所有裝備與所持的艦娘")
            print("[gear] [g] - 印出貴重裝備與所持的艦娘")
            return True
        elif arg == 'deck' or arg == 'd':
            # 印出四個艦隊狀態
            player.print_info_decks()
            return True
        elif arg == 'd1' or arg == 'd1':
            # 印出第一個艦隊狀態
            player.print_info_decks(deck_id=1)
            return True
        elif arg == 'ndock' or arg == 'n':
            # 印出維修工廠狀態
            player.print_info_ndocks(player)
            return True
        elif arg == 'ship' or arg == 's':
            # 印出所有船艦狀態
            for i in range(1,101):
                if i % 10 == 1:
                    print "[", i, "]"
                player.print_info_ships(i)
            player.print_info_ships_count()
            return True
        elif arg == 'material' or arg == 'r': # Resource
            # 印出目前擁有的資源
            player.print_info_materials()
            return True
        elif arg == 'names' or arg == 'name':
            # 印出艦娘的暱稱
            kcShipData.cat_name()
            return True
        elif arg == 'fleets' or arg == 'f':
            # 印出使用者自行編列的艦隊編成
            kcShipData.cat_fleets()
            return True
        elif arg == 'damage' or arg == 'dmg':
            # 印出所有受傷的艦娘資訊與預期維修時間
            player.get_damaged_ships_and_repair_time()
            return True
        elif arg == 'gearall' or arg == 'ga':
            kcGear.print_all_gears()
            return True
        elif arg == 'gear' or arg == 'g':
            kcGear.print_important_gears()
            return True
        else:
            return False
    elif inp.startswith('lag'):
        # 印出目前 LAG
        if len(inp.split()) == 1:
            u.uprint("サーバーとの予測レイテンシは " + u.append_color(str(u.get_lag()),'yellow') + " 秒です")
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
    elif inp == '?':
        u.uprint("Place = " + u.append_color(u.get_place(),'yellow') + ", Lag = " + u.append_color(u.get_lag(),'yellow'))
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
            input_ = "c1 akagi"
            則我們檢查 word[0]，也就是 "c1" 是否為合法的指令。
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
    kcGear.main()

    u.uprint("あわわわ、びっくりしたのです。")
    # set_place("port")

    while True:
        _user_input = raw_input(u.append_color('電：提督、ご命令を','green') + " > ")

        if is_handled_by_predefined_func(_user_input) is True:
            continue

        check_command(_user_input)


if __name__ == '__main__':
    main()
