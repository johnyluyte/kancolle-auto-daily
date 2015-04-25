# -*- coding: utf-8 -*-
import kcUtility as u


from kcCommand import cmd

""" [腳本]

> "f1 daily"
自動按照每日任務的需求，分別補充每一艘第一艦隊 (f1) 船艦的燃油以及彈藥

"""

def run(fleet):
    u.get_focus_game()
    main(fleet)
    u.get_focus_terminal()


def main(fleet):
    global target
    target = cmd['refill']

    # choose fleet
    do_action(target[fleet][0], target[fleet][2], 0.1)

    for i in xrange(1,7):
        seperate_hokyuu(str(i))


def seperate_hokyuu(ship_pos):
    do_action(target[ship_pos][0],target[ship_pos][2], 0)
    do_action(target['oil'][0],target['oil'][2], u._LAG)
    do_action(target[ship_pos][0],target[ship_pos][2], 0)
    do_action(target['bullet'][0],target['bullet'][2], u._LAG)


def do_action(cmd_msg, cmd_pos, sleep_time):
    u.uprint(cmd_msg)
    u.click_and_wait(cmd_pos, sleep_time)
