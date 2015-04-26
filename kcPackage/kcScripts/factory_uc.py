# -*- coding: utf-8 -*-
import kcUtility as u

from kcCommand import cmd

""" [腳本]

> "build uc"
用 UC 的背景音樂建造裝備
> "dock1 uc"
用 UC 的背景音樂取得 dock1 新建好的艦娘

"""

def run(command):
    u.get_focus_game()
    main(command)
    u.get_focus_terminal()

def main(command):
    global target
    target = cmd['factory']

    u.uprint("電の本気を見るのです！")
    u.play_audio('audio/honkiwomiru.mp3')
    u.sleep(2.5)
    u.play_audio('audio/uc.mp3')
    u.sleep(2)
    for i in xrange(5, 0, -1):
        u.uprint( "完全勝利するまで {}{}{} 秒です".format(u.color['cyan'], i, u.color['default']) )
        u.sleep(1.1)
    do_action(target[command])
    u.uprint("(o・ω・)ｏワクワク♪")
    u.sleep(10)


def do_action(cmd, sleep_time = 0.05):
    if not cmd[0].strip() == '':
        u.uprint(cmd[0])
    u.click_and_wait(cmd[2], sleep_time)
