# -*- coding: utf-8 -*-
import kcUtility as u

from kcCommand import cmd

""" [腳本]

> "c1 akagi"
自動找出代號為 "akagi" 的艦娘位置，並將之更換為旗艦(c1)

"""

def run(player_, position, nick_name):
    global player
    player = player_

    local_id = player.get_ship_local_id(nick_name)
    if local_id is None:
        print "Cannot find kanmusu with nick_name: ", nick_name
        return

    # 計算一下此艦娘在第幾頁的第幾個
    tmp = abs(player.ships_count - local_id) + 1
    page = ((tmp-1) // 10) + 1
    number = tmp % 10
    # print "Page: ", page, "N.O: ", number

    u.get_focus_game()
    main(position, page, number)
    u.get_focus_terminal()


def main(position, page, number):
    """
    @ position : 要換到艦隊的第幾個位置（c1 ~ c6）
    @ page     : 該艦娘在第幾頁
    @ number   : 該艦娘在該頁第幾個
    """
    target = cmd['hensei']


    do_action(target[position][0], target[position][2], 0.3)

    # 遊戲會記錄選擇上一個艦娘時的頁面，所意要先回到第一頁
    do_action(target['q'][0], target['q'][2], 0.1)

    tmp = list()
    if (player.ships_count // 10) + 1 == page:
        # 在最後一頁
        tmp.append(target['w'])
    elif player.ships_count // 10 == page:
        # 在倒數第二頁
        tmp.append(target['w'])
        tmp.append(target['f'])
    # elif page == 1:
    #     tmp.append(target['a'])
    elif page == 2:
        tmp.append(target['s'])
    elif page == 3:
        tmp.append(target['d'])
    elif page == 4:
        tmp.append(target['f'])
    elif page == 5:
        tmp.append(target['g'])
    elif page == 6:
        tmp.append(target['g'])
        tmp.append(target['f'])
    elif page == 7:
        tmp.append(target['g'])
        tmp.append(target['f'])
        tmp.append(target['f'])
    elif page == 8:
        tmp.append(target['g'])
        tmp.append(target['f'])
        tmp.append(target['f'])
        tmp.append(target['f'])
    # elif page == 9:
    #     tmp = target['a']
    # elif page == 10:
    #     tmp = target['a']

    for i in tmp:
        do_action(i[0], i[2], 0.1)

    number = str(number)
    do_action(target[number][0], target[number][2], 0.2)
    do_action(target['yes'][0], target['yes'][2], 0.01)


def do_action(cmd_msg, cmd_pos, sleep_time):
    u.uprint(cmd_msg)
    u.click_and_wait(cmd_pos, sleep_time)

