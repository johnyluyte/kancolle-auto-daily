# -*- coding: utf-8 -*-
import kcUtility as u

from kcCommand import cmd

""" [腳本]

> "f1 daily"
自動按照每日任務的需求，分別補充每一艘第一艦隊 (f1) 船艦的燃油以及彈藥

"""

def run(player_, fleet):
    u.get_focus_game()
    main(player_, fleet)
    u.get_focus_terminal()


def main(player_, fleet):
    global target
    target = cmd['refill']


    # choose fleet
    do_action(target[fleet], 0.1)
    get_index_by_fleet = {'f1':0, 'f2':1, 'f3':2, 'f4':3}
    empty_ships_in_fleet = player_.decks[get_index_by_fleet.get(fleet, None)].ships.count(-1)
    ships_in_fleet = 6 - empty_ships_in_fleet
    u.uprint( "この艦隊は {}{}{} 人います".format(u.color['yellow'], ships_in_fleet, u.color['default']) )

    for i in xrange(1, ships_in_fleet + 1):
        # pass
        seperate_hokyuu(str(i))


def seperate_hokyuu(ship_pos):
    do_action(target[ship_pos], 0)
    do_action(target['oil'], u._LAG)
    do_action(target[ship_pos], 0)
    do_action(target['bullet'], u._LAG)

def do_action(cmd, sleep_time = 0.05):
    if not cmd[0].strip() == '':
        u.uprint(cmd[0])
    u.click_and_wait(cmd[2], sleep_time)
