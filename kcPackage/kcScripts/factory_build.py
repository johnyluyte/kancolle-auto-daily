# -*- coding: utf-8 -*-
import kcUtility as u

from kcCommand import cmd

""" [腳本]

> "build shimakaze"
自動輸入建造艦娘的配方

"""

def run(command, materials):
    u.get_focus_game()
    main(command, materials)
    u.get_focus_terminal()


def main(command, materials):
    global target
    mat_name = ['oil', 'bullet', 'steel', 'aluminum']
    target = cmd['factory']

    # dock1 shimakaze
    if command.startswith('dock'):
        default = 30
    # dock1 shimakaze
    elif command == 'kaihatu':
        default = 10

    do_action(target[command], 0.5)
    u.uprint("燃料{x}{a}{y}、弾薬{x}{b}{y}、鋼材{x}{c}{y}、ボーキ{x}{d}{y}".format(a=materials[0], b=materials[1], c=materials[2], d=materials[3], x=u.color['yellow'], y=u.color['default']) )

    # test(target, wait_)

    for i in xrange(4):
        mat = materials[i]
        name = mat_name[i]
        if u.is_number(mat) is False:
            u.uerror("Materials quanity error (is not number)")
            return False

        mat = int(mat)
        if mat > (default+620) or mat < default:
            u.uerror("Materials quanity error (default < number < default+620)")
            return False

        mat = mat - default
        if not mat == 0:
            hundred = mat // 100
            ten     = (mat % 100) // 10
            one     = (mat % 10)
            # print hundred, ten, one
            for k in xrange(hundred):
                do_action(target[name+'+100'])
            for k in xrange(ten):
                do_action(target[name+'+10'])
            for k in xrange(one):
                do_action(target[name+'+1'])


def do_action(cmd, sleep_time = 0.05):
    if not cmd[0].strip() == '':
        u.uprint(cmd[0])
    u.click_and_wait(cmd[2], sleep_time)

def test(target, wait_):
    do_action(target['oil+1'], wait_)
    do_action(target['oil-1'], wait_)
    do_action(target['oil+10'], wait_)
    do_action(target['oil-10'], wait_)
    do_action(target['oil+100'], wait_)
    do_action(target['oil-100'], wait_)
    do_action(target['bullet+1'], wait_)
    do_action(target['bullet-1'], wait_)
    do_action(target['bullet+10'], wait_)
    do_action(target['bullet-10'], wait_)
    do_action(target['bullet+100'], wait_)
    do_action(target['bullet-100'], wait_)
    do_action(target['steel+1'], wait_)
    do_action(target['steel-1'], wait_)
    do_action(target['steel+10'], wait_)
    do_action(target['steel-10'], wait_)
    do_action(target['steel+100'], wait_)
    do_action(target['steel-100'], wait_)
    do_action(target['aluminum+1'], wait_)
    do_action(target['aluminum-1'], wait_)
    do_action(target['aluminum+10'], wait_)
    do_action(target['aluminum-10'], wait_)
    do_action(target['aluminum+100'], wait_)
    do_action(target['aluminum-100'], wait_)
