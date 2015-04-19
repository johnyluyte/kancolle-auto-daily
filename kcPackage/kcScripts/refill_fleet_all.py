# -*- coding: utf-8 -*-
from kcUtility import uprint
from kcUtility import get_focus_game
from kcUtility import get_focus_terminal
from kcUtility import click_and_wait
from kcUtility import click_no_wait
from kcUtility import _LAG

from kcCommand import cmd

""" [腳本]

> "f1 all"
補充第一艦隊 (f1) 船艦所有的燃油及彈藥

"""

def run(fleet):
    get_focus_game()
    main(fleet)
    get_focus_terminal()


def main(fleet):
    global target
    target = cmd['refill']

    do_action(target[fleet][0], target[fleet][2], 0.1)
    do_action(target['all'][0], target['all'][2], 0.1)
    do_action(target['matome'][0], target['matome'][2], _LAG)


def do_action(cmd_msg, cmd_pos, sleep_time):
    uprint(cmd_msg)
    click_and_wait(cmd_pos, sleep_time)
