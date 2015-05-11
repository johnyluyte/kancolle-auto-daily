# -*- coding: utf-8 -*-
import kcUtility as u
import kcShipData
from kcCommand import cmd

""" [腳本]

> "c1 akagi"
自動找出代號為 "akagi" 的艦娘位置，並將之更換為旗艦(c1)

"""

def is_on_expedition(ship_current_id):
    result = False
    # 由  1 ~ 100 修正回 0 ~ 99 來查表
    ship_current_id -= 1
    # print local_id
    local_id = int(player.ships[ship_current_id].local_id)

    # 檢查該艦娘是否在第 2 ~ 4 艦隊，且該艦隊正在遠征
    for i in xrange(1, 4):
        # print player.decks[i].ships
        # print player.decks[i].mission
        if local_id in player.decks[i].ships:
            if not player.decks[i].mission[0] == 0:
                result = True
    return result

def run(player_, position, nick_name):
    global player
    player = player_

    # 取得艦娘在目前的排組中，在 local_id 的順位在"第幾個"，此值並非 local_id，值應為 1 ~ 100
    ship_current_id = player.get_ship_current_id_by_nick_name(nick_name)
    if ship_current_id is None:
        return False
    # 檢查此艦娘是否空著，如果正在遠征的話就不切換
    if is_on_expedition(ship_current_id) is True:
        u.uerror(nick_name + "は今遠征中、変更できないです")
        return False

    # 計算一下此艦娘在第幾頁的第幾個
    tmp = abs(player.ships_count - ship_current_id) + 1
    page = ((tmp-1) // 10) + 1
    number = tmp % 10
    # print "count: ", player.ships_count, "current_id: ", ship_current_id, "tmp: ", tmp
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
    u.uprint('ソート順は {}new{} をセットしてください'.format(u.color['cyan'], u.color['default']))

    target = cmd['hensei']

    # 選擇第 1 ~ 6 位艦娘
    do_action(target[position], 0.4)

    # 遊戲會記錄選擇上一個頁面，所以要先回到第一頁
    do_action(target['q'], 0.1)

    # 選擇艦娘所在頁面
    tmp = list()
    total_page = ((player.ships_count-1) // 10) + 1
    if page == total_page:
        # 在最後一頁
        tmp.append(target['w'])
    elif page == total_page - 1:
        # 在倒數第二頁
        tmp.append(target['w'])
        tmp.append(target['f'])
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

    for i in tmp:
        do_action(i, 0.15)

    # 選擇在此頁面的第 N 個艦娘
    number = str(number)
    do_action(target[number], 0.2)
    do_action(target['yes'], 0.01)


def do_action(cmd, sleep_time = 0.05):
    if not cmd[0].strip() == '':
        u.uprint(cmd[0])
    u.click_and_wait(cmd[2], sleep_time)

