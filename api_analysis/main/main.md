
主畫面

```
Remote Address:125.6.189.103:80
Request URL:http://125.6.189.103/kcsapi/api_port/port
Request Method:POST
Status Code:200 OK
```

參見 response1


- **api_material**
  - **api_id 1~4** 分別是 燃料、彈藥、鋼鐵、機材 的數量
  - **api_id 5~8** 分別是 高速建造、高速修復、建造資材、改修資材的數量
- **api_deck_port** 跟 遠征 API 那篇一樣，參考那篇即可
- **api_ndock** 跟 ndeck修復 API　那篇一樣，參考那篇即可
- **api_basic** 包含了提督ID、名稱、等級、經驗值、最大可擁有船艦數、裝備數、擁有的家具、造船渠道、維修渠道、遠征勝敗場、出征勝敗場、演習勝敗場、徽章數量等等，那些會顯示在戰績表示頁面的資訊。
- **api_log** 主畫面下方按下"表示"按鈕時會跑出來的資訊(艦隊最新消息)。
- **api_p_bgm_id** 背景音樂的 ID
- **api_ship** 所有你所擁有的艦娘的資訊，這段資料很長也很重要，我們提出來另外研究，如下


參見 response1_api_ship


如果你都有 follow 剛剛的文章的話，會發現這個跟剛剛 工廠 API 的 **api_ship** 格式一模一樣

沒錯，所以參考工廠那邊即可

不對，應該是工廠要參考這裡才對 XD


- **api_id** 這艘船是此帳號的"第幾隻艦娘"
舉例來說，遊戲開始時如果你選了電()
- **api_sortno** 這個才是這隻艦娘在圖鑑上的 ID，要注意的是，有些艦娘改造之後(ex: 電改) 沒有獨自的圖鑑，則此數值依然會更改，通常是跳到 3XX

例如
*電(いなづま)*的圖鑑是：074
http://wikiwiki.jp/kancolle/?%C5%C5
*電改*是：337
而圖鑑頁面 337 是空的
http://wikiwiki.jp/kancolle/?%B4%CF%CC%BC%A5%AB%A1%BC%A5%C9%B0%EC%CD%F7

- **api_lv** 目前等級
- **api_exp** 目前經驗、下一級所需經驗
- **api_nowhp** 目前血量(耐久度)
- **api_maxhp** 最大血量
- **api_slot** 目前裝備，-1 代表未開放
- **api_kyouka** 已強化的數值
- **api_backs** 可搭載艦上機的數量
- **api_fuel** 燃料量
- **api_bull** 彈藥量
- **api_slotnum** 可用之裝備欄位
- **api_cond** 疲勞值
- **api_karyoku** 火力（かりょく），這邊開始以日文羅馬拼音命名變數
- **api_raisou** 雷装（らいそう）
- **api_taiku** 対空（たいくう）
- **api_soukou** 装甲（そうこう）
- **api_kaihi** 回避（かいひ）
- **api_taisen** 対潜（たいせん）
- **api_sakuteki** 索敵（さくてき）
- **api_lucky** 運（lucky），靠杯為什麼運氣就是用英文 XD





