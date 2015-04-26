# -*- coding: utf-8 -*-
import kcUtility as u

from kcCommand import cmd

""" [腳本]

> "f1 all"
補充第一艦隊 (f1) 船艦所有的燃油及彈藥

"""

def run(fleet):
    u.get_focus_game()
    main(fleet)
    u.get_focus_terminal()


def main(fleet):
    global target
    target = cmd['refill']

    do_action(target[fleet], 0.1)
    do_action(target['all'], 0.1)
    do_action(target['matome'], u._LAG)


def do_action(cmd, sleep_time = 0.05):
    if not cmd[0].strip() == '':
        u.uprint(cmd[0])
    u.click_and_wait(cmd[2], sleep_time)
