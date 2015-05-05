# -*- coding: utf-8 -*-
import threading
import subprocess

import kcUtility as u
from kcCommand import cmd
from kcCommand import exec_single_command

""" [腳本]

> "map321"
自動出擊地圖 3-2-1

"""

class SikuliThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_status = None
    def run(self):
        # 由於我們是從 shell.py 進入的，故應使用 shell.py 之相對路徑，而非 sikuli_1_1.py 的
        self.thread_status = subprocess.check_call(['/Applications/SikuliX.app/run', '-r', 'kcScripts/map3_2_1.sikuli'])

def run(player):
    u.get_focus_game()
    main(player)
    u.get_focus_terminal()

def main(player):
    u.set_place(player, 'port', update_api=False)
    do_action(player, u.get_place(), 'fight')
    do_action(player, u.get_place(), 'pve', u.get_lag())
    do_action(player, u.get_place(), 'd')
    do_action(player, u.get_place(), '2')
    do_action(player, u.get_place(), 'y')
    do_action(player, u.get_place(), 'tatakau')

    t = SikuliThread("t1")
    t.start()

    while(True):
        # print t.thread_status
        if t.thread_status == 0:
            break;
        # spam 陣形一，"陣形 - 単縦陣(水雷特化)"，為了不讓 console 印出，訊息設成""
        u.click_and_wait(cmd['tatakau']['1'][2], 0)
        u._sleep(3, print_=False)

    # 戰鬥結束，回到母港
    u.uprint('出撃終了です、補給します', 'yellow')
    u.set_place(player, 'port')
    do_action(player, u.get_place(), 'refill', u.get_lag())
    do_action(player, u.get_place(), 'all', 1)
    do_action(player, u.get_place(), 'matome', u.get_lag())
    do_action(player, u.get_place(), 'hensei')
    u.uprint('作戦 {} 遂行完了です'.format(u.append_color('sikuri_1_1', 'cyan')))


def do_action(player, place, command, sleep_time=1.2):
    exec_single_command(player, place, command, sleep_time)
