# -*- coding: utf-8 -*-
import kcUtility as u
import kcShipData
import kcCommand

import kcScripts.change_ship
import kcScripts.refill_fleet_daily
import kcScripts.refill_fleet_all


def exec_script(player, place, command, args):
    if place == 'hensei':
        change_ship_cmds = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']
        change_fleet_cmds = ['f1', 'f2', 'f3', 'f4']
        if (command in change_ship_cmds) and len(args) == 1:
            # "c1 akagi"
            kcScripts.change_ship.run(player, command, args[0])
        if (command in change_fleet_cmds) and len(args) == 1:
            # "f1 kobe"
            # 自動找出代號為 "kobe" 的艦隊編列，並將第一艦隊(f1) 更換成代號艦隊所編列的艦娘
            # kcScripts.change_fleet.run(player, command, args[0])

            # 找出該艦隊的所有艦娘位置
            result = kcShipData.get_fleets_data_by_fleet_nick_name(command, args[0])
            if result is False:
                return False;
            # 切換成該艦隊 (f1 ~ f4)
            kcCommand.exec_single_command(player, place, command)
            u._sleep(0.1)
            # 清空目前艦隊
            kcCommand.exec_single_command(player, place, 'clear')
            u._sleep(u._LAG)
            # 切換六個艦娘
            for i in xrange(6):
                if result[i] is not "":
                    nick_name = kcShipData.get_nick_name_by_ship_name(result[i])
                    print nick_name
                    if kcScripts.change_ship.run(player, 'c'+str(i+1), nick_name) is not False:
                        u._sleep(u._LAG)

    elif place == 'refill':
        fleet_cmds = ['f1', 'f2', 'f3', 'f4']
        if (command in fleet_cmds) and len(args) == 1:
            if args[0] == 'daily':
                kcScripts.refill_fleet_daily.run(command)
            elif args[0] == 'all':
                kcScripts.refill_fleet_all.run(command)
    else:
        u.unknown_command(command)
