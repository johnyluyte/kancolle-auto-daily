# Kancolle Auto daily


## 目標：

自動執行“艦隊收集”每日任務


## 步驟

1. 用尺量螢幕長寬，以及要點擊之按鈕的位置，找出兩者相對比例後，推算出要丟給 pymouse 的座標
2. 上述方法可以有效抓到大致位置，但要更精確的話，需要能夠確實“看見 pymouse 點擊的位置”
3. 使用 realplayer 錄影，試圖抓取 pymouse 點擊之位置，但是 realplayer 似乎只抓得到“人工控制滑鼠點擊”，而抓不到 pymouse 點擊
4. 寫一個 javascript 程式，該程式可將指定的網頁頁面覆蓋上滿滿的方格，當方格被滑鼠點擊時，會印出自己的座標，利用此小程式找到 WYSWYG 的 pymosuse 對應座標
5. 但是 event.clientX, event.clientY 會受到視窗相對位置影響，也就是說，我們要避免捲動到螢幕 -> removeSection()
6. 連線不穩定，大約半小時就會跳出一次 page error 的 javascript confirm 問說要不要重新讀取，但是即使出現這個 error，遊戲依然可以正常繼續下去，不重新讀取也不會有任何影響，因此對我們來說，這個 error 除了擾人以外，沒有任何意義。 -> ignorePrompt()
7. 每次都要貼上很麻煩，用成 greasemonkey 或是 chrome extension?



## 腳本

1. 半夜自動遠征，自動補給，自動出發  (自動點選執行任務?)

2. 自動修復(在修復畫面不停檢查是否有空的港口，有的話就檢查是否有待維修的船，自動維修)

3. 手動選擇地圖後，自動戰鬥(自動選陣行、自動不追擊、自動撤退?)


## TODO：

怎麼解決 iTaiwan 每四小時斷線的問題→要輸入 iTaiwan 密碼→還要重新連結 VPN→重新連上 kancolle?
用 4G 網路

要印出 output, log 檔案，每個 log 都要以時間日期 stamp 開頭
當錯誤跳出時備份截圖
要能藉由圖片偵測“遊戲的畫面”在螢幕個位置，並自動調整 pymouse 應點擊的位置


## License

This project is licensed under the terms of the [MIT license](http://opensource.org/licenses/MIT).

Please note that this project is built with materials from the following parties:

-[PyUserInput](https://github.com/SavinaRoja/PyUserInput)
-[py 辨識圖片](http://programmingcomputervision.com/)

Please also refer to their Licenses for further information.
