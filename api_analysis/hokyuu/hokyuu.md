補給

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_req_hokyu/charge
Request Method:POST
Status Code:200 OK
```

收到 response

```
svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_ship":[{"api_id":205,"api_fuel":40,"api_bull":65,"api_onslot":[2,2,2,0,0]},{"api_id":132,"api_fuel":15,"api_bull":20,"api_onslot":[0,0,0,0,0]},{"api_id":59,"api_fuel":25,"api_bull":25,"api_onslot":[1,1,0,0,0]},{"api_id":101,"api_fuel":40,"api_bull":65,"api_onslot":[2,2,2,0,0]},{"api_id":18,"api_fuel":25,"api_bull":30,"api_onslot":[1,1,1,0,0]},{"api_id":182,"api_fuel":10,"api_bull":20,"api_onslot":[0,0,0,0,0]}],"api_material":[2989,6063,3181,5524],"api_use_bou":0}}
```

排版過後參見 response1.md




經過多次實驗與推斷，

**api_id** 這隻艦娘是此帳號的第幾隻艦娘，

例如你登入遊戲時選的那隻起始腳色的 api_id 就會是

```
"api_id": 1,
```

- **-api_fuel** 艦娘(目前?/消耗?)的燃料，每類型好像都不一樣，不是觀察重點故不研究
- **api_bull** 艦娘(目前?/消耗?)彈藥量，每類型好像都不一樣，不是觀察重點故不研究
- **api_onslot** 艦娘裝備，不影響我們腳本，故不研究
- **api_material** 提督目前總資源(燃料、彈藥、鋼材、機材)


