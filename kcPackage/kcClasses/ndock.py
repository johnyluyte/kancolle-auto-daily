# -*- coding: utf-8 -*-

# 修船廠資訊
class Ndock(object):
    def __init__(self, ndock_id, state, ship_id, complete_time, complete_time_str):
        self.ndock_id = ndock_id
        self.state = state
        self.ship_id = ship_id
        self.complete_time = complete_time
        self.complete_time_str = complete_time_str
    def print_info(self):
        print("第 " + str(self.ndock_id) + " 修船廠")
        print("狀態：" + str(self.state))
        print("船艦：" + str(self.ship_id))
        print("完成時間E：" + str(self.complete_time))
        print("完成時間H：" + str(self.complete_time_str))

