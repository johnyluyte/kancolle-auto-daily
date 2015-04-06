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


python 加上偵測按鍵、按左即選則左（進擊）、按右即選擇右（側退）
一個新的 js 左邊或下面加上 wiki 、加上潛艇艦娘圖案、陳菊？


## 腳本

1. 半夜自動遠征，自動補給，自動出發  (自動點選執行任務?)

2. 自動修復(在修復畫面不停檢查是否有空的港口，有的話就檢查是否有待維修的船，自動維修)

3. 手動選擇地圖後，自動戰鬥(自動選陣行、自動不追擊、自動撤退?)



簡易腳本
- 遠征
- 每日任務 15 次補給

需要 API
- 遠征 ＋ 清晨自動解每日每週遠征任務
- 自動排隊修理船

需要圖像辨識
- 練等級 1-5

需要 API + 圖像辨識
- 練等級 ＋ 自動解每日戰鬥任務



## 考察：

火力、雷裝、對空、裝甲

如果只有雷裝成長，完全不用考慮培養到改，因為雜魚驅逐艦就可加強雷裝惹


--要培養、改完再餵食--

五十鈴
0,1,0,1
1,1,4,2  Lv12

最上
2,1,0,2
2,1,3,2 lv10


--不培養，直接餵食的--

千歳、千代田
0,0,1,2
0,0,2,2 lv10 也可能會失敗，不如直接餵
0,2,1,2 lv12

大井、北上
0,1,0,1
0,4,0,1 lv10


## TODO：

右邊那個 js 要產生黑色海苔遮住提督姓名

一個 新的 js 去監控 http header 並且 filter 我們要的 response

根據 response 內容去做邏輯判斷，將要執行的動作透過圖片顯示在畫面左上角 （例如進攻或側退，是否需要維修等等）

python 不停的截圖看畫面左上角，當偵測到圖片後，分析該圖片的意思，並且點擊“clear image” 清空圖片，告訴 js 說我看到了

python 再根據該圖片的內容，做 js 要求的動作


但是上面的方法很難傳送 json，可以的話還是想要傳送 json

但是礙於 mac 網路不固定，沒有一個固定的 IP

可能需要藉由一個中繼的 proxy server 來跟 js 溝通，明明就在同一台電腦，卻不能互相溝通 ＱＱ

另一個要注意的是，hostmonster 的是 shared host，可能不能自己擁有一個 port 長駐

一個方法是 js, php 跟 python 有一個共同 sync 的變數 next_pkg_no，由 python 統一 sync 其他兩者

pyhton 不斷跟 php request 這個 json 封包，而 js 則是監聽 http header，聽到我們要的封包後，將 next_pkg_no 塞進去封包並傳給 php

php 此時就能回應 python 的要求，pyhton 得到封包後，解析並決定下一步要幹麻


看起來有點複雜？要不要嘗試 hostmonster 以外的選擇？用 amazon ec2 說不定就有固定 ip ?


弄半天，發現好像不能單純用 js 去抓到 chrome 所有接收的 http response 有 XSS 的問題，

仔細想想也是，如果有個常駐的 js 能抓到我瀏覽器的所有 response，好像安全性也令人擔憂

所以最後改從 chrome dev tool 抓 response，複製到 clipboard，再從 clipboard 抓進 python 分析



去找到 api_id 對照船 或是 sortid 的表格


從回到主畫面的 port json 就可以得到所有船艦資訊，所以理論上可以知道“哪個艦娘”在哪個頁面的哪個位置。


用 alias 的方式將 python ensei15.py 改成好玩的名稱
例如
poi~
那珂ちゃんのファンをやめます   (那珂ちゃん遠征)
how do you turn this on
5566 cannot die


用相同的概念來做一個 那珂ちゃん 自動解體互動
cchien:~/git/kancolle-auto-daily $ 那珂ちゃん
那珂1：艦隊のアイドル那珂ちゃんでーす、よっろしく
那珂2：艦隊のアイドル那珂ちゃんでーす、よっろしく
那珂3：艦隊のアイドル那珂ちゃんでーす、よっろしく
raw_input:
那珂ちゃんのファンをやめます
赤城：わかりました
那珂：やめて
解體


不小心關掉 kancolle 視窗後，用 ctrl+shift+t 開啟，不會受區域限制！？ 不用 ＶＰＮ

難道是因為 ctrl+shift+t 是從 cache 開的關係？

用英文再寫一篇！？

這篇充分說明了會英文與日文的重要

我對 javascript 和 pyhton 都沒有很熟
遇到不懂的地方，上 stackOverflow 或丟 google 查，馬上就可以找到相關資訊
想要哪些 module 或 library，也是馬上上網查，到處找國外網站的資料
安裝 module 遇到問題時，也是上網查

英文不好的話，不要說寫出什麼功能，根本第一步就卡死了，

日文在這次的研究中也很重要
我一開始算是被學長拉進來玩這遊戲的，老實說不太清楚遊戲規則在幹麻
但花了一天閱讀日版的 wiki 後，可以說是對遊戲十分了解
了解遊戲規則後再解讀 API 時更能得心應手
也因為會日文的關係，上網可以找到前人的一些資訊，應證自己的 API 解讀是否正確
http://masarakki.gitbooks.io/c86-kancolle-api/content/intro.html
最後，我覺得很關鍵的一點就是
由於這是日本人寫的遊戲，很多 url, method, variable, json key/value 都是以羅馬拼音的方式命名
例如補給 羅馬拼音就是 hokyu
Request URL:http://125.6.189.103/kcsapi/api_req_hokyu/charge
所以我看到上面這樣的 url ，就知道這是補給的 API call
不會日文的人就無法理解

另外例如船艦的 json 如下（以吹雪作為例子）
"api_taik": 15,  = 耐久，耐久的羅馬拼音為 taikyu
"api_kaih": 40,  = 迴避，迴避的羅馬拼音為 kaihi
"api_houg": 10,  = 火力，在遊戲中，火力影響砲撃威力，砲擊的羅馬拼音為 hougeki
"api_raig": 27,  = 雷裝，在遊戲中，雷裝影響水雷雷擊威力，雷擊的羅馬拼音為 raigeki
"api_tyku": 10,  = 對空，對空的羅馬拼音為 taiku，變形 tyku
"api_tais": 20,  = 對潛，對潛的羅馬拼音為 taisei
因為會日文的關係，這些變數對我而言一眼就了解
不會日文的恐怕還要建立表格來對照


最後當然就是需要一點資工的基礎，跟一顆努力不懈的好奇心啦。
時間、穩定的網路、VPN 等等



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
