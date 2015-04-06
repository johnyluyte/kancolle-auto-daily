
港口
熊野 在第二個港口 剩下 24:30 秒左右修復

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_get_member/ndock
Request Method:POST
Status Code:200 OK
```

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":[{"api_member_id":12130401,"api_id":1,"api_state":0,"api_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0},{"api_member_id":12130401,"api_id":2,"api_state":1,"api_ship_id":118,"api_complete_time":1427963491374,"api_complete_time_str":"2015-04-02 17:31:31","api_item1":37,"api_item2":0,"api_item3":69,"api_item4":0},{"api_member_id":12130401,"api_id":3,"api_state":-1,"api_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0},{"api_member_id":12130401,"api_id":4,"api_state":-1,"api_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0}]}
```


排版過後參見 response1.md


回傳的是 ndock

維修頁面的 json 整體而言與工廠的 json 類似

- - -

- **api_member_id** 提督 ID(記得拿掉)
- **api_id** 第幾個維修廠，總共 1~4 個維修廠
- **api_state** 1 代表此維修廠正在維修船艦、0 代表閒置，-1 代表未開放(需課金開放)
- **api_ship_id** 正在維修的這隻艦娘在 server 端的 ID，注意這個 ID 跟艦娘在圖鑑的 ID 不一樣！
- **api_complete_time** 是以 Epoch 型態表示的造船完成時間
- **api_complete_time_str** 是將上述 Epoch 轉成人類好讀的格式的造船完成時間，注意時區是 JST，也就是 GMT +9
- **api_item1 ~ 4** 應該是維修時使用的鋼材、燃料等等(待驗證)

