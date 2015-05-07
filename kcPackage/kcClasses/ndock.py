# -*- coding: utf-8 -*-
import time
import kcShipData
import kcUtility as u

# 修船廠資訊
class Ndock(object):
    current_time = None

    def __init__(self, ndock_id, state, ship_local_id, complete_time, complete_time_str):
        self.ndock_id = ndock_id
        self.state = state
        self.ship_local_id = ship_local_id
        if complete_time is not 0:
            self.complete_time = int(str(complete_time)[:-3])
            # 1430398364561
            # 1430398364 即到"秒"，後面三個是秒以下，可省略
        else:
            self.complete_time = 0
        self.complete_time_str = complete_time_str

    def update_current_time(self):
        self.current_time = int(str(time.time()).split('.')[0])

    """
    def print_info(self, player):
        print("第 " + str(self.ndock_id) + " 修船廠")

        ndock_state = {0:'閒置', 1:'維修中'}
        print("狀態：" + ndock_state.get(self.state, 'Error'))

        name = kcShipData.get_name_by_local_id(player, self.ship_id)
        name = u.append_color(name, 'yellow')
        print("船艦：" + name)

        self.update_current_time()
        seconds_left = 0
        if self.complete_time is not 0:
            seconds_left = self.complete_time - self.current_time

        # 從 7615 秒 轉成 02:06:55 格式
        hour = int(seconds_left // 3600) # 先 cast 成 int，以免整除時出現 1.0 等
        minute = int(seconds_left % 3600 // 60)
        second = int(seconds_left % 60)

        msg  = ' ( {:0>2s}:{:0>2s}:{:0>2s} )'.format(str(hour), str(minute), str(second))

        print("完成時間 Epoch：" + str(self.complete_time))
        print("剩餘時間(秒)：" + str(seconds_left) + u.append_color(msg, 'yellow'))
        print("完成時間(日本時間)：" + str(self.complete_time_str))
    """

    def get_info(self, player):
        ndock_state = {0:'閒置', 1:'維修中'}

        name = kcShipData.get_name_by_local_id(player, self.ship_local_id)

        self.update_current_time()
        seconds_left = 0
        if self.complete_time is not 0:
            seconds_left = self.complete_time - self.current_time

        # 從 7615 秒 轉成 02:06:55 格式
        hour = int(seconds_left // 3600) # 先 cast 成 int，以免整除時出現 1.0 等
        minute = int(seconds_left % 3600 // 60)
        second = int(seconds_left % 60)

        count_down  = '({:0>2s}:{:0>2s}:{:0>2s})'.format(str(hour), str(minute), str(second))

        info = dict()
        info['ndock_id']        = self.ndock_id
        info['state']           = ndock_state.get(self.state, 'Error')
        info['ship_local_id']   = self.ship_local_id
        info['name_count_down'] = u.append_color(name + count_down, 'yellow')
        info['seconds_left']    = seconds_left
        return info
