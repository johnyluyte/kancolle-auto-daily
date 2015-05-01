# -*- coding: utf-8 -*-
import kcUtility as u
import kcShipData
import kcCommand

import kcScripts.change_ship
import kcScripts.refill_fleet_daily
import kcScripts.refill_fleet_all
import kcScripts.factory_build
import kcScripts.factory_uc
import kcScripts.auto_repair


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
                    if kcScripts.change_ship.run(player, 'c'+str(i+1), nick_name) is not False:
                        u._sleep(u._LAG)

    elif place == 'refill':
        fleet_cmds = ['f1', 'f2', 'f3', 'f4']
        if (command in fleet_cmds) and len(args) == 1:
            # "f1 dialy"
            if args[0] == 'daily':
                kcScripts.refill_fleet_daily.run(player, command)
            # "f1 all"
            elif args[0] == 'all':
                kcScripts.refill_fleet_all.run(command)

    elif place == 'factory':
        build_cmds = ['dock1', 'dock2']
        if command in build_cmds:
            # "dock1 uc"
            if len(args) == 1 and args[0] == 'uc':
                kcScripts.factory_uc.run(command)
            # "dock1 shimakaze"
            elif len(args) == 1:
                if args[0] == 'shimakaze' or args[0] == 's':
                    kcScripts.factory_build.run( command, (250,30,200,30) )
                elif args[0] == 'kuubou' or args[0] == 'k':
                    kcScripts.factory_build.run( command, (300,30,400,300) )
            # "dock2 250 30 200 30"
            elif len(args) == 4:
                kcScripts.factory_build.run( command, args )
        elif command == 'kaihatu':
            # "kaihatu plane"
            if len(args) == 1:
                # http://wikiwiki.jp/kancolle/?%B3%AB%C8%AF%A5%EC%A5%B7%A5%D4
                if args[0] == 'plane' or args[0] == 'p':
                    kcScripts.factory_build.run( command, (20,60,10,110) )
                elif args[0] == 'sonar' or args[0] == 's':
                    kcScripts.factory_build.run( command, (10,10,10,20) )
                elif args[0] == 'bakurai' or args[0] == 'b':
                    kcScripts.factory_build.run( command, (10,30,10,10) )
                elif args[0] == 'sb':
                    kcScripts.factory_build.run( command, (10,30,10,31) )
            # "kaihatu 20 50 10 110"
            elif len(args) == 4:
                kcScripts.factory_build.run( command, args )
        elif command == 'build' and args[0] == 'uc':
            kcScripts.factory_uc.run(command)

    elif place == 'auto':
        if command == 'repair':
            kcScripts.auto_repair.run(player)

    else:
        u.unknown_command(command)
