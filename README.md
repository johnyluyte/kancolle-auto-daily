# Kancolle Auto daily


## 目標：

自動執行“艦隊收集”每日任務


## 步驟

1. 用尺量螢幕長寬，以及要點擊之按鈕的位置，找出兩者相對比例後，推算出要丟給 pymouse 的座標
2. 上述方法可以有效抓到大致位置，但要更精確的話，需要能夠確實“看見 pymouse 點擊的位置”
3. 使用 realplayer 錄影，試圖抓取 pymouse 點擊之位置，但是 realplayer 似乎只抓得到“人工控制滑鼠點擊”，而抓不到 pymouse 點擊
4. 寫一個 javascript 程式，該程式可將指定的網頁頁面覆蓋上滿滿的方格，當方格被滑鼠點擊時，會印出自己的座標，利用此小程式找到 WYSWYG 的 pymosuse 對應座標 (有點大費周章？根本不用 squares？ 直接用一個大方塊印出滑鼠點擊時滑鼠的 xposition 就好了？)


javascript 程式要能控制 square opacty, font-color, background color, attributes after clicked, etc.



## TODO：

要印出 output, log 檔案，每個 log 都要以時間日期 stamp 開頭
當錯誤跳出時備份截圖
要能藉由圖片偵測“遊戲的畫面”在螢幕個位置，並自動調整 pymouse 應點擊的位置


## License

This project is licensed under the terms of the [MIT license](http://opensource.org/licenses/MIT).

Please note that this project is built with materials from the following parties:

-[PyUserInput](https://github.com/SavinaRoja/PyUserInput)
-[py 辨識圖片](http://programmingcomputervision.com/)

Please also refer to their Licenses for further information.
