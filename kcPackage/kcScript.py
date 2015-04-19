# -*- coding: utf-8 -*-
from kcUtility import uprint
from kcUtility import uerror
from kcUtility import unknown_command

import kcScripts.change_ship
import kcScripts.refill_fleet_daily
import kcScripts.refill_fleet_all


def exec_script(player, place, command, args):
    if place == 'hensei':
        change_ship_cmds = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']
        if (command in change_ship_cmds) and len(args) == 1:
            # "c1 akagi"
            kcScripts.change_ship.run(player, command, args[0])
    elif place == 'refill':
        fleet_cmds = ['f1', 'f2', 'f3', 'f4']
        if (command in fleet_cmds) and len(args) == 1:
            if args[0] == 'daily':
                kcScripts.refill_fleet_daily.run(command)
            elif args[0] == 'all':
                kcScripts.refill_fleet_all.run(command)
    else:
        unknown_command(command)
