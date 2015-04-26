# Kancolle Auto daily


## 目標：

自動執行“艦隊收集”每日任務

但是直接分析 API 發 quest 會被抓
且造成 server 負擔，影響其他玩家

(放入 官方 twitter)

https://github.com/masarakki/IJN48
BANされたよ!

上面那篇文章作者是 2014年1月 寫的，所以有些 API 已經完全不一樣了
舉例來說，我已經攔截不到戰鬥過程的 JSON，導致無法分析是否該突入夜戰，或是該撤退
這項 API 的更改應該就是為了防止自動練功的程式。



## 現有程式調查 survey

在 github 搜尋 kancolle 可以找到一堆 open source 的艦これ相關程式，為了避免重造輪子，先針對這些開源程式做研究。

程式大致可以分成下列幾種：

### 1. Database 型態

https://github.com/ponkotuy/MyFleetGirls
https://myfleet.moe/
https://github.com/sirobot/kancolle


### 2. 協助 proxy，cache 等

艦これ封鎖日本海外 IP，故海外玩家大部分必須經由 VPN 啟動基本連線。(連上後遊戲本身不會鎖IP，故連上後就可以切斷 VPN)

proxy 類程式可以讓玩家不須連上 VPN，或是提供代連的服務

瀏覽器在開啟艦これ時，需要從伺服器拿到並初始化一些資料，有時候某些步驟是多餘的，cache 類程式檢查使用者端瀏覽器是否已經有相關 cache，加快遊戲讀取速度。


### 3. 自動系列(外掛)

https://github.com/methane/kancolle-tools/blob/master/autorepair.py
自動維修，解析 API 後直接發封包給 server 要求維修。
最後更新 26 Oct 2013

https://github.com/tesseract2048/kancolle-warden/blob/master/client_simulator.py
自動遠征、戰鬥、維修等等，解析 API 後直接發封包給 server 要求。
最後更新 19 Feb 2014

https://github.com/niyuna/kancolle_echor/blob/master/kancolle_echor.py
跟上面一樣，自動遠征、戰鬥、維修等等，解析 API 後直接發封包給 server 要求。
最後更新 7 Jun 2014

https://github.com/amylase/kancolle-auto
用圖形辨識的方式自動重複遠征-完成-補給-遠征..
這個用到的 sikuli 就是我需要的!?


為什麼一開始不用 sikuli? 因為 OSX 10.10.x 不能用

如何安裝 sikuli
你可以去
http://doc.sikuli.org/index.html
http://www.sikuli.org/download.html
http://www.sikulix.com/
https://github.com/sikuli/sikuli
https://github.com/RaiMan/SikuliX-2014
https://github.com/RaiMan/SikuliX2
https://launchpad.net/sikuli/+download
找到瘋掉，最後只發現這些都 does not work on OSX 10.10.x

所以如果你跟我一樣是 OSX 10.10.x，請直接參考

https://bugs.launchpad.net/sikuli/+bug/1362011
參考這篇文章最後三篇

或直接看這篇的下面
https://bugs.launchpad.net/sikuli/+bug/1362011/comments/10

為了怕文章不見，這裡先備份(引用)

1. 下載 "The only file needed to download:" 那個檔案
2. 放到 download/nightly
3. control + 右鍵，開啟未受信任的檔案
4. 依照自己的需求勾選 Pack，我選擇 pack 1，並勾選 Jython 跟 JRuby
5. 按下 setup
6. 出現問確定，按下 yes
7. 開始下載各 package
8. 開始 creating jars
9. 出現 Hallo from Sikulix.texstSetup. Python Scripting SikuliX seems to be working!
10. download/nightly 資料夾內的東西可以刪掉嗎

If you have OSX Mavericks or later, go to the http://nightly.sikuli.de/ page (the nightly builds page), ignore everything but the part that reads:

"The only file needed to download:
sikulixsetup-1.1.0 (store and run in an empty folder)"

... and download that sikulixsetup file.

Put this in its own folder, call the folder "Sikuli".

Run the setup file. Choose option 1, add the jruby option. Install and wait for downloading and installing to do their thing.

You should get the "Hallo from Sikulix.texstSetup. Python Scripting SikuliX seems to be working!" message (maybe two of these).

You can now move the Sikuli folder containing the app, the "Downloads" folder and the setup file to the standard /Applications/ folder. You can delete both the "Downloads" folder in the Sikuli folder and the original setup jar file.

It's probably a good idea to make a new folder called "Scripts" and keep all your sikuli script files in there. It is a personal preference (some might like that to be in ~/Documents/, for example), but I like having this in the Sikuli folder so that everything is located within a simple hierarchy.


直接用 command line 執行：
/Applications/SikuliX.app/run -r ~/myScript.sikuli

即使是在 terminal ，SikuliX 也要花 6~8 秒才能啟動並執行 script，相對來說很慢

不過我們是用在戰鬥途中，就還好！？ 反正 kancolle 進入戰鬥畫面前也有一段空閒時間

Q:
https://answers.launchpad.net/sikuli/+question/249084
A:
仕様です



### 4. 輔助型、提供資訊

艦これ預設的 UI 實在是很爛，所以很多玩家開發出介面型工具，讓遊戲資訊能更簡潔明瞭的顯示出來，讓玩家掌握

http://grabacr.net/kancolleviewer
最強的艦これ專用瀏覽器，可惜 Windows 限定

https://github.com/otiai10/kanColleWidget
實用的 chrome extension 外掛

https://github.com/KanColleTool/KanColleTool
跟 kancolleviewer 很像，




## 待研究：


https://github.com/rhenium/kancolle_helper
這個是怎麼純用 chrome extension 就抓到見娘資料的?
是用 cookie?  以前遊戲有用 cookie存?

https://github.com/amylase/kancolle-auto
用圖形辨識的方式自動重複遠征-完成-補給-遠征..
這個用到的 sikuli 就是我需要的!?

1. Cookie

詳情可以到 dev tool -> Resource 研究
幾乎所有 js 都附有註解，包含部分付款資訊的 js

2. API

官方更新 API 後就無法使用，上面 github 內許多自動執行的已經無法運作了 (API 不同?)

官方假設刻意修改部分 server 端 API，並同時更新 client 端 flash，

但 server 端仍保留向下相容接受舊的 API，並偷偷記錄那些玩家還在使用舊的 API，就可抓出那些玩家使用外掛..

3.



## 步驟

1. 用尺量螢幕長寬，以及要點擊之按鈕的位置，找出兩者相對比例後，推算出要丟給 pymouse 的座標
2. 上述方法可以有效抓到大致位置，但要更精確的話，需要能夠確實“看見 pymouse 點擊的位置”
3. 使用 realplayer 錄影，試圖抓取 pymouse 點擊之位置，但是 realplayer 似乎只抓得到“人工控制滑鼠點擊”，而抓不到 pymouse 點擊
4. 寫一個 javascript 程式，該程式可將指定的網頁頁面覆蓋上滿滿的方格，當方格被滑鼠點擊時，會印出自己的座標，利用此小程式找到 WYSWYG 的 pymosuse 對應座標
5. 但是 event.clientX, event.clientY 會受到視窗相對位置影響，也就是說，我們要避免捲動到螢幕 -> removeSection()
6. 連線不穩定，大約半小時就會跳出一次 page error 的 javascript confirm 問說要不要重新讀取，但是即使出現這個 error，遊戲依然可以正常繼續下去，不重新讀取也不會有任何影響，因此對我們來說，這個 error 除了擾人以外，沒有任何意義。 -> ignorePrompt()
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

我們想要得到 dmm server 回傳的 http response，因為裡面含有的 JSON 資訊可以讓程式了解該做什麼

http://stackoverflow.com/questions/220231/accessing-the-web-pages-http-headers-in-javascript
js 似乎無法直接取得 chrome 收到的所有 http response

改變戰略，用 chrome developer tool 的 network，下 filter 後來抓 JSON
用 pyUserInput 控制滑鼠鍵盤，取得 json

在 filter 欄位加入 -method:GET 可過濾掉我們不要的資訊
錯！！ 還是無法過濾掉 gadget/ 這種資訊！

或是在 filter 欄位直接輸入 port | deck | ndeck | questlist 等等


http://www.macdrifter.com/2011/12/python-and-the-mac-clipboard.html
http://pastebin.com/4MjuSkW3
然後參考這篇文章，用 python 從 clipboard 取得剛剛複製的 JSON 資訊

會遇到 unicode 編碼問題
http://stackoverflow.com/questions/11544541/python-ascii-and-unicode-decode-error
http://stackoverflow.com/questions/16058065/how-can-i-convert-strings-like-u5c0f-u738b-u5b50-u003a-u6c49-u6cd5-u82f1-u5bf9


寫成 command line 模式

接下來就是程式架構，盡量用 OOP 的方式撰寫，把不同功能的 module 區分清楚

之後就可以將不同的 "macro" 寫成不同的腳本，直接在統一個 command line 模式下呼叫

# http://www51.atpages.jp/kancollev/kcplayer.php?c=37v28&vol=0.2
用 audacity 剪輯語音與 UC



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

--UC--

摩耶
如月中破


## TODO：

然後在 Python 裡面 parse JSON，規則參考 艦これ　API/JSON 分析那篇 (自己寫)

API 的分析請見下篇文章



去找到 api_id 對照船 或是 sortid 的表格
從回到主畫面的 port json 就可以得到所有船艦資訊，所以理論上可以知道“哪個艦娘”在哪個頁面的哪個位置。

這邊有些有趣的 data
https://www.snip2code.com/Snippet/32881/Kankore-Slot-Item-Data

需要一個 api_sortno(艦娘圖鑑的號碼) 與 艦娘名稱 的對應表格

到 http://wikiwiki.jp/kancolle/?%B4%CF%C1%A5

透過 excel + sublime text 簡易處理，產生一個 python 的 [圖鑑號碼-艦娘名稱] 對照 list

github 公開 excel 與 python


7. 每次都要貼上很麻煩，用成 greasemonkey 或是 chrome extension?




## 腳本

1. 半夜自動遠征，自動補給，自動出發  (自動點選執行任務?)

2. 自動修復(在修復畫面不停檢查是否有空的港口，有的話就檢查是否有待維修的船，自動維修)

3. 手動選擇地圖後，自動戰鬥(自動選陣行、自動不追擊、自動撤退?)


在 shell 輸入 data ndock, data deck1, data decks, data isuzu 時，要能顯示
在 data 那邊，加入一下各航空母艦艦載量，加入一下改的等級?
在編成時，輸入 c1 akagi 可以自動幫我換好艦娘(
  - 要先確認並過濾重複的艦娘，找到正確的(own_id 最小)
  - 找到在第幾頁，並自動選取(從 q 或 w 然後 asdf 這樣選)
延續上面的，只是這次可以在編成畫面輸入 cf loli 就全員換成第六驅逐艦隊，cf main 就換成 main force
當然也可以透過 fleet 來顯示目前所有預設的艦隊，然後輸入 fleet loli 來看詳細
自動檢查"接下來的行程" (有哪些船艦快修好了，有哪些遠征快回來了，有哪些船艦快造好了 等等)
自動在進入 port, ndock, factory 時檢查 api  (dev tool 記得要縮到只剩一個，filter 位置會改變，要記下來)


簡易腳本
- 遠征
- 每日任務 15 次補給

需要 API
- 遠征 ＋ 清晨自動解每日每週遠征任務
- 自動排隊修理船
- 自動檢查任務進度

需要圖像辨識
- 練等級 1-5
http://akankorebiyori.blog.fc2.com/blog-entry-121.html

需要 API + 圖像辨識
- 練等級 ＋ 自動解每日戰鬥任務



## TODO：

家具背景記得換一換再錄影

要印出 output, log 檔案，每個 log 都要以時間日期 stamp 開頭
當錯誤跳出時備份截圖
要能藉由圖片偵測“遊戲的畫面”在螢幕個位置，並自動調整 pymouse 應點擊的位置

用 alias 的方式將 python ensei15.py 改成好玩的名稱
例如
poi~
那珂ちゃんのファンをやめます   (那珂ちゃん遠征)
how do you turn this on
5566 cannot die

聲音可以從這裡下載
http://www51.atpages.jp/kancollev/kcplayer.php?f=0&c=37v1

用這個來拆除那珂ちゃん
http://www51.atpages.jp/kancollev/kcplayer.php?c=37v13

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

最後當然就是需要一點資工的基礎，跟一顆努力不懈的好奇心。
時間、穩定的網路、VPN 等等

邊學習 python 邊完成的練習

3/25 開始玩
3/28 開始寫外掛
coursera 的 programming for everybody
coursera 的 Interactive python programming I
coursera 的 Interactive python programming II
Learn Python the Hard Way
還有大量的 StackOverflow


怎麼解決 iTaiwan 每四小時斷線的問題→要輸入 iTaiwan 密碼→還要重新連結 VPN→重新連上 kancolle?
用 4G 網路


## License

This project is licensed under the terms of the [MIT license](http://opensource.org/licenses/MIT).

Please note that this project is built with materials from the following parties:

-[PyUserInput](https://github.com/SavinaRoja/PyUserInput)
-[py 辨識圖片](http://programmingcomputervision.com/)

Please also refer to their Licenses for further information.
