# -*- coding: utf-8 -*-
import kcUtility as u
import shell

from kcCommand import cmd
from kcCommand import exec_single_command

""" [腳本]

> "auto repair"
進入自動維修模式，監看 ndock 與受傷的艦娘，一發現 ndock 空著且有受傷的艦娘，就將之放進維修

"""

injured_kanmusu_count = 0
empty_dock = [True, True]


def run(player):
    u.get_focus_game()
    main(player)
    u.get_focus_terminal()

def main(player):
    # 先回 port，更新 API
    # u.set_place(player, 'place')
    # 檢查是否有空的 ndock 與受傷的艦娘
    do_action(player, u.get_place(), 'ndock', u.get_lag())
    do_action(player, u.get_place(), 'port', u.get_lag())
    player.get_damaged_ships_and_repair_time()
    u.get_focus_terminal()
    u.scroll_down()
    u.get_focus_game()

    try:
        check_ndock_and_kanmusu(player)
    except KeyboardInterrupt:
        print ""
        u.uprint('自動修理が中断されました', 'red')
        return

    u.uprint('全部修理完了です')


def check_ndock_and_kanmusu(player):
    """
    這邊採用 busy waiting，實際上不用 busy waiting 也能做到一樣的效果
    但我喜歡看他倒數
    為了應應臨時抓不到 api、網路延遲、遠征回來等情形 ，這裡先持續用 busy waiting
    暫時不要 refactoring
    """
    global injured_kanmusu_count
    global empty_dock
    u.uprint('空いてるドック = ' + str(empty_dock))

    all_healed = False
    while all_healed is False:
        # 檢查受傷的艦娘
        injured_kanmusu_count = 0
        for i in xrange(100):
            if player.ships[i] is None:
                break
            elif player.ships[i].dmghp > 0:
                injured_kanmusu_count += 1
        # 檢查空的維修廠
        for i in xrange(2):
            if player.ndocks[i].state == 0:
                empty_dock[i] = True
            else:
                empty_dock[i] = False
        # 到 ndock 將受傷的艦娘放入
        if (True in empty_dock) and (injured_kanmusu_count > 1):
            put_into_ndock(player)
        elif (injured_kanmusu_count == 0) or (injured_kanmusu_count == 1):
            all_healed = True
        # 監看並等待維修時間差不多結束
        else:
            seconds_left = player.print_info_ndocks_auto_repair(player)
            if seconds_left[0] < 59 or seconds_left[1] < 59:
                print ""
                # random sleep
                u.get_focus_game()
                do_action(player, u.get_place(), 'ndock', u.get_lag())
                do_action(player, u.get_place(), 'port', u.get_lag())
                u.get_focus_game()
        u.sleep(1)

def put_into_ndock(player):
    global injured_kanmusu_count
    global empty_dock
    fast_sleep = 1.7

    u.uprint('空いてるドック = ' + str(empty_dock))
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
        count = injured_kanmusu_count
        if count > 9:
            count = 0
        do_action(player, u.get_place(), str(count), fast_sleep)

    # 回到 port，更新 API
    do_action(player, u.get_place(), 'repair', fast_sleep)
    do_action(player, u.get_place(), 'hai', fast_sleep)
    do_action(player, u.get_place(), 'port', u.get_lag())
    u.get_focus_game()
    player.print_info_ndocks(player)
    u.get_focus_terminal()
    u.scroll_down()
    u.get_focus_game()

def do_action(player, place, command, sleep_time):
    exec_single_command(player, place, command, sleep_time)
