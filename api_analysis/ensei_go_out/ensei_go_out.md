
點選出擊

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcs/scenes/SallyMain.swf?version=2.3.3
Request Method:GET
Status Code:200 OK (from cache)
```

點選遠征

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_get_member/mission
Request Method:POST
Status Code:200 OK
```

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":[{"api_mission_id":1,"api_state":2},{"api_mission_id":2,"api_state":2},{"api_mission_id":3,"api_state":2},{"api_mission_id":4,"api_state":2},{"api_mission_id":5,"api_state":2},{"api_mission_id":6,"api_state":2},{"api_mission_id":7,"api_state":2},{"api_mission_id":8,"api_state":2},{"api_mission_id":9,"api_state":2},{"api_mission_id":10,"api_state":2},{"api_mission_id":11,"api_state":2},{"api_mission_id":12,"api_state":2},{"api_mission_id":13,"api_state":2},{"api_mission_id":14,"api_state":2},{"api_mission_id":15,"api_state":2},{"api_mission_id":16,"api_state":2},{"api_mission_id":17,"api_state":0},{"api_mission_id":32,"api_state":0}]}
```

參見 response1.md

- **api_mission_id** 就是遠征任務的 id
- **api_state** 0 代表尚未達成過，1 代表目前正在進行，2 代表已達成過現在沒在進行



選取遠征 1-1，點選遠征開始

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_req_mission/start
Request Method:POST
Status Code:200 OK
```

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_complatetime":1427985550385,"api_complatetime_str":"2015-04-02 23:39:10"}}
```
```
{
  "api_result": 1,
  "api_result_msg": "成功",
  "api_data": {
    "api_complatetime": 1427985550385,
    "api_complatetime_str": "2015-04-02 23:39:10"
  }
}
```

- **api_complete_time** 是以 Epoch 型態表示的遠征完成時間
- **api_complete_time_str** 上述 Epoch 轉成人類好讀的格式，注意時區是 JST，也就是 GMT +9




接著自動送出下面這個

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_get_member/deck
Request Method:POST
Status Code:200 OK
```

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":[{"api_member_id":12130401,"api_id":1,"api_name":"\u7b2c1\u8266\u968a","api_name_id":"","api_mission":[0,0,0,0],"api_flagship":"0","api_ship":[79,132,59,101,18,182]},{"api_member_id":12130401,"api_id":2,"api_name":"\u7b2c2\u8266\u968a","api_name_id":"","api_mission":[1,1,1427985550385,0],"api_flagship":"0","api_ship":[12,25,7,83,128,172]},{"api_member_id":12130401,"api_id":3,"api_name":"\u7b2c3\u8266\u968a","api_name_id":"","api_mission":[0,0,0,0],"api_flagship":"0","api_ship":[5,49,4,66,16,13]}]}
```


取得目前艦隊資料的 API call

參見 response2

- **api_member_id** 提督 ID(記得拿掉)
- **api_id** 第幾個艦隊
- **api_name** 艦隊名稱
- **api_name_id** 不知道，待研究
- **api_mission** 此艦隊目前在進行哪個任務
  - 第一個值，我猜應該是遠征第一個頁面?
  - 第二個值，我猜應該是該頁面的第幾個任務？
  - 第三個值，遠征任務完成時間 Epoch
  - 第四個值，不知道待研究
- **api_flagship** 第幾艘船是旗艦，我覺得除非遊戲規則更改，否則這個變數應該不會更改，應該 obsolete 掉
- **api_ship** 這支艦隊是由那些船艦所組成，那些船艦的數值是"此帳號的第幾隻艦娘"(在其他 API 中，多被稱作_ **api_id**)

舉例來說

"api_ship": [
  1,
  2,
  3,
  4,
  10,
  150
]

代表這隻艦隊是由你開始遊戲以來
得到的第 1 隻艦娘、第 2 隻、第 3 隻、第 4 隻、第 10 隻跟第 110 隻艦娘所組成

注意 **api_id** 這個數值是固定且不會改變的

舉例來說，你目前有 4 隻艦娘，抓到的下一隻的 **api_id** 就是 5，再抓到下一隻就是 6

如果你將 **api_id** 為 5 的艦娘給解體，則 6 的依然是 6，不會更改

抓到下一隻的 **api_id** 會是 7

也就是說**api_id** 為 5 的艦娘就此從缺了。

這個機制可以保證每個艦娘都有一個獨特的 **api_id**，

即使有兩個名稱、等級、裝備、所有屬性都相同的艦娘，我們依然可以由 **api_id** 來分辨兩者。





遠征 1-2

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_req_mission/start
Request Method:POST
Status Code:200 OK
```

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_complatetime":1427985950395,"api_complatetime_str":"2015-04-02 23:45:50"}}
```

接著自動送出下面這個


```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_get_member/deck
Request Method:POST
Status Code:200 OK
```

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":[{"api_member_id":12130401,"api_id":1,"api_name":"\u7b2c1\u8266\u968a","api_name_id":"","api_mission":[0,0,0,0],"api_flagship":"0","api_ship":[79,132,59,101,18,182]},{"api_member_id":12130401,"api_id":2,"api_name":"\u7b2c2\u8266\u968a","api_name_id":"","api_mission":[1,1,1427985550385,0],"api_flagship":"0","api_ship":[12,25,7,83,128,172]},{"api_member_id":12130401,"api_id":3,"api_name":"\u7b2c3\u8266\u968a","api_name_id":"","api_mission":[1,3,1427985950395,0],"api_flagship":"0","api_ship":[5,49,4,66,16,13]}]}
```


參考 response 3



