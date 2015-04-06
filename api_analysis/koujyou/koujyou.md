

工廠


```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcs/sound/kcicwowutxbvgh/1.mp3?version=5
Request Method:GET
Status Code:200 OK (from cache)
```

建造完成等級一的 霧島

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_req_kousyou/getship
Request Method:POST
Status Code:200 OK
```

回傳的 json

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_id":213,"api_ship_id":85,"api_kdock":[{"api_member_id":12130401,"api_id":1,"api_state":0,"api_created_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0,"api_item5":1},{"api_member_id":12130401,"api_id":2,"api_state":0,"api_created_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0,"api_item5":1},{"api_member_id":12130401,"api_id":3,"api_state":-1,"api_created_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0,"api_item5":0},{"api_member_id":12130401,"api_id":4,"api_state":-1,"api_created_ship_id":0,"api_complete_time":0,"api_complete_time_str":"0","api_item1":0,"api_item2":0,"api_item3":0,"api_item4":0,"api_item5":0}],"api_ship":{"api_id":213,"api_sortno":24,"api_ship_id":85,"api_lv":1,"api_exp":[0,100,0],"api_nowhp":63,"api_maxhp":63,"api_leng":3,"api_slot":[317,318,319,-1,-1],"api_onslot":[3,3,3,0,0],"api_kyouka":[0,0,0,0,0],"api_backs":5,"api_fuel":80,"api_bull":110,"api_slotnum":3,"api_ndock_time":0,"api_ndock_item":[0,0],"api_srate":0,"api_cond":40,"api_karyoku":[80,89],"api_raisou":[0,0],"api_taiku":[30,69],"api_soukou":[52,69],"api_kaihi":[31,59],"api_taisen":[0,0],"api_sakuteki":[13,39],"api_lucky":[10,49],"api_locked":0,"api_locked_equip":0},"api_slotitem":[{"api_id":317,"api_slotitem_id":7},{"api_id":318,"api_slotitem_id":11},{"api_id":319,"api_slotitem_id":37}]}}
```

排版過後參見 response1.md



這部分還有待研究，但是一開始的地方應該跟 港口 很像 api_item5 應該就是建造資材

後面則是造好的船艦的資訊


- **api_id** 造好的這隻艦娘是此帳號的第幾隻艦娘
- **api_ship_id** 造好的這隻艦娘在 server 端的 ID，注意這個 ID 跟艦娘在圖鑑的 ID 不一樣！
- **api_kdock** 各個造船廠渠道的資訊
  - **api_member_id** 提督 ID(記得拿掉)
  - **api_id** 第幾個造船廠，總共 1~4 個造船廠
  - **api_state** 1 代表此造船廠正在建造船艦、0 代表閒置，-1 代表未開放(需課金開放)
  - **api_complete_time** 是以 Epoch 型態表示的造船完成時間
  - **api_complete_time_str** 是將上述 Epoch 轉成人類好讀的格式的造船完成時間，注意時區是 JST，也就是 GMT +9
- **api_slotitem** 造好的這隻艦娘的目前裝備，部分裝備清單可參考[這裡](https://www.snip2code.com/Snippet/32881/Kankore-Slot-Item-Data)(資料可能有點舊)



