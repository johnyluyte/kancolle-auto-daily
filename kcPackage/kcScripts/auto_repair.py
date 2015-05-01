# -*- coding: utf-8 -*-
import kcUtility as u
import shell

from kcCommand import cmd
from kcCommand import exec_single_command

""" [腳本]

> "auto repair"
進入自動維修模式，監看 ndock 與受傷的艦娘，一發現 ndock 空著且有受傷的艦娘，就將之放進維修

"""

injured_kanmusu = list()
empty_dock = [True, True]


def run(player):
    u.get_focus_game()
    main(player)
    u.get_focus_terminal()

def main(player):
    global injured_kanmusu
    global empty_dock

    # 先回 port，更新 API
    # u.set_place(player, 'place')
    # 檢查是否有空的 ndock 與受傷的艦娘
    do_action(player, u.get_place(), 'ndock', u.get_lag())
    do_action(player, u.get_place(), 'port', u.get_lag())

    # player.print_info_ndocks(player)

    all_healed = False
    while all_healed is False:
        # 檢查受傷的艦娘
        injured_kanmusu = list()
        for i in xrange(100):
            if player.ships[i] is None:
                break
            elif player.ships[i].dmghp > 0:
                injured_kanmusu.append(player.ships[i].name)
        # 檢查空的維修廠
        for i in xrange(2):
            if player.ndocks[i].state == 0:
                empty_dock[i] = True
            else:
                empty_dock[i] = False
        # 到 ndock 將受傷的艦娘放入
        if (True in empty_dock) and (len(injured_kanmusu) > 1):
            put_into_ndock(player)
        elif (len(injured_kanmusu) == 0) or (len(injured_kanmusu) == 1):
            all_healed = True
        # 監看並等待維修時間差不多結束
        else:
            seconds_left = player.print_info_ndocks_auto_repair(player)
            if seconds_left[0] < 59 or seconds_left[1] < 59:
                print ""
                do_action(player, u.get_place(), 'ndock', u.get_lag())
                do_action(player, u.get_place(), 'port', u.get_lag())
        u.sleep(1)
    u.uprint('全部修理完了です')


def put_into_ndock(player):
    global injured_kanmusu
    global empty_dock
    fast_sleep = 1.7

    print('ドック = ', empty_dock)
    # msg = ''
    # for i in injured_kanmusu:
    #     msg += i + ','
    # u.uprint('怪我している艦娘たち：' + u.append_color(msg, 'green') )
    player.get_damaged_ships_and_repair_time()
    u.get_focus_terminal()
    u.scroll_down()
    u.get_focus_game()

    do_action(player, u.get_place(), 'ndock', u.get_lag())

    if empty_dock[0] is True:
        # 從最上面修 (大破、中破)
        do_action(player, u.get_place(), 'dock1', fast_sleep)
        do_action(player, u.get_place(), '1', fast_sleep)
    elif empty_dock[1] is True:
        # 從最下面修 (擦傷、小破)
        do_action(player, u.get_place(), 'dock2', fast_sleep)
        count = len(injured_kanmusu)
        if count > 9:
            count = 0
        do_action(player, u.get_place(), str(count), fast_sleep)

    # 回到 port，更新 API
    do_action(player, u.get_place(), 'repair', fast_sleep)
    do_action(player, u.get_place(), 'hai', fast_sleep)
    do_action(player, u.get_place(), 'port', u.get_lag())
    player.print_info_ndocks(player)
    u.get_focus_terminal()
    u.scroll_down()
    u.get_focus_game()

def do_action(player, place, command, sleep_time):
    exec_single_command(player, place, command, sleep_time)
