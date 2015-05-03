# -*- coding: utf-8 -*-
import kcUtility as u

"""
定義各個畫面名稱

-上方-
戰績: senseki
友軍:
圖鑑:
道具:
模樣:
任務: quest
課金:

-主要-
主畫面/回主畫面: port
編成: hensei
補給: refill
改裝: kaisou
入渠: ndock
工廠: factory
出擊: fight
"""
# 定義各個按鈕的位置


# 遊戲主畫面

"""
cmd 的第一個 hash key 是目前所在的場景名稱(general 代表所有頁面)
cmd 的第二個 hash key 是目前所在的場景可執行的指令
因此，可以用 cmd[目前所在頁面].keys() 來取得目前場景可執行的所有指令

cmd 的 value 是個 tuple 其格式如下

type 0 滑鼠點擊乙次：                           (msg, type=0, pos1)
type 1 滑鼠點擊乙次(會切換場景)：               (msg, type=1, pos1)
type 2 一系列的滑鼠點擊：                       (msg, type=2, count, func, pos1, sleep1, pos2, sleep2 ..)
type 3 滑鼠點擊乙次，有 callback：              (msg, type=3, pos1, func)
type 4 滑鼠點擊乙次(會切換場景)，有 callback：  (msg, type=4, pos1, func)


@msg    - (str) 顯示的訊息
@type   - (int) 指令種類
      0   滑鼠點擊乙次
      1   滑鼠點擊乙次(會切換場景)
      2   一系列的滑鼠點擊
@count  - (int) 滑鼠點擊的次數，當 type == 2 時才有效
@func   - (str) callback function name，以 None 代表無
@pos1   - (int list[2]) 滑鼠點擊的座標 [x, y]
@sleep1 - (int) pos1 點擊完成後，休息幾秒
(以下 optional)
@pos2   - 同 pos1
@sleep2 - 同 sleep1
@pos3   - 同 pos1
@sleep3 - 同 sleep1

"""


def exec_single_command(player, place ,command, sleep=0):
    cmd_msg  = cmd[place][command][0]
    cmd_type = cmd[place][command][1]
    cmd_pos  = cmd[place][command][2]

    # type 0 滑鼠點擊乙次：
    if cmd_type == 0:
        u.get_focus_game()
        if not cmd_msg.strip() == "":
            u.uprint(cmd_msg)
        u.click_and_wait(cmd_pos, sleep)
        u.get_focus_terminal()
    # type 1 滑鼠點擊乙次(會切換場景)：
    elif cmd_type == 1:
        u.get_focus_game()
        u.uprint(cmd_msg)
        u.click_and_wait(cmd_pos, sleep)
        u.set_place(player, command)
        u.get_focus_terminal()
        """
    # type 2 一系列的滑鼠點擊：
    elif cmd_type == 2:
        pass
    # type 3 滑鼠點擊乙次，有 callback：
    elif cmd_type == 3:
        pass
    # type 4 滑鼠點擊乙次(會切換場景)，有 callback：
    elif cmd_type == 4:
        pass
        """
    else:
        u.unknown_command(command)


def get_place_of_command(command):
    """
    @ command : (string) 使用者輸入的字串的第一個 word
    @ return  : (string)   該指令所在的位置("general", "hensei", "refill", "ndock", ..)
                (bool)     如果該指令不合法，回傳 False
    """
    result = None
    # 這些 if elif 的順序也代表了搜尋的順序
    if command in cmd[u.get_place()].keys():
        result = u.get_place()
    elif command in cmd['general'].keys():
        result = 'general'
    return result


def get_current_available_cmds():
    return cmd['general'].keys() + cmd[u.get_place()].keys()



cmd = dict()

cmd['general'] = dict()
cmd['general']['ok']        = ("なのです", 0, (400,500))
cmd['general']['c']         = ("キャンセル", 0, (116,550))



# 在主要的那五個畫面之間移動時，只需用左邊那些按鈕即可
cmd['shared_menu'] = dict()
cmd['shared_menu']['port']        = ("母港へ移動しました", 1, (79,160))
cmd['shared_menu']['hensei']      = ("編成画面へ移動しました", 1, (29,252))
cmd['shared_menu']['refill']      = ("補給画面へ移動しました", 1, (29,303))
cmd['shared_menu']['kaisou']      = ("改装画面へ移動しました", 1, (23,358))
cmd['shared_menu']['ndock']       = ("入渠画面へ移動しました", 1, (23,410))
cmd['shared_menu']['factory']     = ("工廠画面へ移動しました", 1, (25,458))
cmd['shared_menu']['senseki']     = ("戦績画面へ移動しました", 1, (163,155))
cmd['shared_menu']['quest']       = ("任務画面へ移動しました", 1, (556,152))

cmd['shared_page'] = dict()
# 改變船隻排列的依據
cmd['shared_page']['sort']        = ("ソートルールを変更しました", 0, (775,212))
# 跳到第一頁 或 最後一頁
cmd['shared_page']['q']           = ("first page を選択しました", 0, (440,557))
cmd['shared_page']['w']           = ("last page を選択しました", 0, (716,554))
# 跳到下一頁 或 上一頁
cmd['shared_page']['a']           = ("ページを変更しました", 0, (517,552))
cmd['shared_page']['s']           = ("ページを変更しました", 0, (549,551))
cmd['shared_page']['d']           = ("ページを変更しました", 0, (584,551))
cmd['shared_page']['f']           = ("ページを変更しました", 0, (619,551))
cmd['shared_page']['g']           = ("ページを変更しました", 0, (641,551))
# 選擇目前頁面第 N 個船
cmd['shared_page']['1']           = ("一番目の艦娘を選択しました", 0, (495,240))
cmd['shared_page']['2']           = ("二番目の艦娘を選択しました", 0, (497,267))
cmd['shared_page']['3']           = ("三番目の艦娘を選択しました", 0, (497,298))
cmd['shared_page']['4']           = ("四番目の艦娘を選択しました", 0, (500,334))
cmd['shared_page']['5']           = ("五番目の艦娘を選択しました", 0, (499,363))
cmd['shared_page']['6']           = ("六番目の艦娘を選択しました", 0, (499,394))
cmd['shared_page']['7']           = ("七番目の艦娘を選択しました", 0, (498,429))
cmd['shared_page']['8']           = ("八番目の艦娘を選択しました", 0, (498,453))
cmd['shared_page']['9']           = ("九番目の艦娘を選択しました", 0, (496,484))
cmd['shared_page']['0']           = ("十番目の艦娘を選択しました", 0, (497,511))


cmd['port'] = dict()
cmd['port']['port']         = (cmd['shared_menu']['port'][0], 1, cmd['shared_menu']['port'][2])
cmd['port']['hensei']       = (cmd['shared_menu']['hensei'][0], 1, (202,238))
cmd['port']['refill']       = (cmd['shared_menu']['refill'][0], 1, (80,315))
cmd['port']['kaisou']       = (cmd['shared_menu']['kaisou'][0], 1, (318,315))
cmd['port']['ndock']        = (cmd['shared_menu']['ndock'][0], 1, (127,462))
cmd['port']['factory']      = (cmd['shared_menu']['factory'][0], 1, (275,462))
cmd['port']['senseki']      = (cmd['shared_menu']['senseki'][0], 1, cmd['shared_menu']['senseki'][2])
cmd['port']['quest']        = (cmd['shared_menu']['quest'][0], 1, cmd['shared_menu']['quest'][2])
cmd['port']['fight']        = ("出撃画面へ移動しました", 1, (207,363), "play_voice_('戦いは避けたいですね')")  # 出擊
cmd['port']['toggle']       = ("GUI を表示/非表示したのです", 0, cmd['shared_menu']['port'][2])
cmd['port']['pat']          = ("あぁ〜", 0, (658,446))




# 補給
cmd['refill'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['refill'][key] = value
cmd['refill']['f1']         = ("第一艦隊を選択しました", 0, (150,223))
cmd['refill']['f2']         = ("第二艦隊を選択しました", 0, (179,220))
cmd['refill']['f3']         = ("第三艦隊を選択しました", 0, (206,221))
cmd['refill']['f4']         = ("第四艦隊を選択しました", 0, (241,220))
cmd['refill']['f5']         = ("編成されていない艦娘たちを選択しました", 0, (268,220))
cmd['refill']['all']        = ("全艦隊を選択/解除", 0, (121,223))
cmd['refill']['1']          = ("一番目の艦娘を選択しました", 0, (161,268))
cmd['refill']['2']          = ("二番目の艦娘を選択しました", 0, (165,316))
cmd['refill']['3']          = ("三番目の艦娘を選択しました", 0, (158,366))
cmd['refill']['4']          = ("四番目の艦娘を選択しました", 0, (160,419))
cmd['refill']['5']          = ("五番目の艦娘を選択しました", 0, (160,471))
cmd['refill']['6']          = ("六番目の艦娘を選択しました", 0, (162,517))
cmd['refill']['q']          = ("first page を選択しました", 0, (218,551))
cmd['refill']['w']          = ("last page を選択しました", 0, (498,551))
cmd['refill']['a']          = ("ページを変更しました", 0, (298,552))
cmd['refill']['s']          = ("ページを変更しました", 0, (332,548))
cmd['refill']['d']          = ("ページを変更しました", 0, (363,548))
cmd['refill']['f']          = ("ページを変更しました", 0, (395,549))
cmd['refill']['g']          = ("ページを変更しました", 0, (426,549))
cmd['refill']['oil']        = ("燃料のみ補給しました", 0, (641,540))
cmd['refill']['bullet']     = ("弾薬のみ補給しました", 0, (775,534))
cmd['refill']['matome']     = ("燃料と弾薬まとめて補給しました", 0, (703,543))


# 編成
cmd['hensei'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['hensei'][key] = value
for key, value in cmd['shared_page'].items():
    cmd['hensei'][key] = value
# 因為有 はずす 選項的關係，所以有些按鈕要做些微調
cmd['hensei']['hazusu']     = ("艦娘をはずしました", 0 , (431,234))
cmd['hensei']['1']          = (cmd['shared_page']['1'][0], 0 , (469,266))
cmd['hensei']['2']          = (cmd['shared_page']['2'][0], 0 , (471,293))
cmd['hensei']['3']          = (cmd['shared_page']['3'][0], 0 , (464,325))
cmd['hensei']['q']          = (cmd['shared_page']['q'][0], 0 , (435,550))
cmd['hensei']['w']          = (cmd['shared_page']['w'][0], 0 , (716,546))
cmd['hensei']['yes']        = ("変更完了です", 0 , (716,546))
cmd['hensei']['y']          = cmd['hensei']['yes']
cmd['hensei']['hai']        = cmd['hensei']['yes']
# change fleets 艦隊
cmd['hensei']['f1']         = (cmd['refill']['f1'][0], 0, (139,223))
cmd['hensei']['f2']         = (cmd['refill']['f2'][0], 0, (166,222))
cmd['hensei']['f3']         = (cmd['refill']['f3'][0], 0, (198,221))
cmd['hensei']['f4']         = (cmd['refill']['f4'][0], 0, (226,222))
# 解除旗艦以外的編列
cmd['hensei']['clear']      = ("伴随艦一括解除したのです", 0, (423,217))
# watch status 船隻狀態
cmd['hensei']['s1']         = ("旗艦の詳細です", 0, (329,314))
cmd['hensei']['s2']         = ("二番目の艦娘の詳細です", 0, (668,317))
cmd['hensei']['s3']         = ("三番目の艦娘の詳細です", 0, (328,429))
cmd['hensei']['s4']         = ("四番目の艦娘の詳細です", 0, (672,432))
cmd['hensei']['s5']         = ("五番目の艦娘の詳細です", 0, (327,537))
cmd['hensei']['s6']         = ("六番目の艦娘の詳細です", 0, (673,540))
# change ship 切換船隻
cmd['hensei']['c1']         = ("旗艦を変更します", 0, (413,317))
cmd['hensei']['c2']         = ("二番目の艦娘を変更します", 0, (757,311))
cmd['hensei']['c3']         = ("三番目の艦娘を変更します", 0, (411,431))
cmd['hensei']['c4']         = ("四番目の艦娘を変更します", 0, (751,430))
cmd['hensei']['c5']         = ("五番目の艦娘を変更します", 0, (410,540))
cmd['hensei']['c6']         = ("六番目の艦娘を変更します", 0, (752,538))
# Lock
cmd['hensei']['lock1']         = ("一番目の艦娘のロックを変更したのです", 0, (762,265))
cmd['hensei']['lock2']         = ("二番目の艦娘のロックを変更したのです", 0, (761,296))
cmd['hensei']['lock3']         = ("三番目の艦娘のロックを変更したのです", 0, (762,324))
cmd['hensei']['lock4']         = ("四番目の艦娘のロックを変更したのです", 0, (758,356))
cmd['hensei']['lock5']         = ("五番目の艦娘のロックを変更したのです", 0, (759,382))
cmd['hensei']['lock6']         = ("六番目の艦娘のロックを変更したのです", 0, (759,407))
cmd['hensei']['lock7']         = ("七番目の艦娘のロックを変更したのです", 0, (757,437))
cmd['hensei']['lock8']         = ("八番目の艦娘のロックを変更したのです", 0, (760,460))
cmd['hensei']['lock9']         = ("九番目の艦娘のロックを変更したのです", 0, (757,488))
cmd['hensei']['lock0']         = ("十番目の艦娘のロックを変更したのです", 0, (759,516))


# 改裝
cmd['kaisou'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['kaisou'][key] = value
cmd['kaisou']['f1']         = (cmd['refill']['f1'][0], 0, (144,212))
cmd['kaisou']['f2']         = (cmd['refill']['f2'][0], 0, (175,216))
cmd['kaisou']['f3']         = (cmd['refill']['f3'][0], 0, (201,208))
cmd['kaisou']['f4']         = (cmd['refill']['f4'][0], 0, (235,211))
cmd['kaisou']['f5']         = (cmd['refill']['f5'][0], 0, (264,211))
# 選擇第一二三四艦隊的六個人
cmd['kaisou']['q']          = (cmd['shared_page']['1'][0], 0, (206,263))
cmd['kaisou']['w']          = (cmd['shared_page']['2'][0], 0, (207,314))
cmd['kaisou']['e']          = (cmd['shared_page']['3'][0], 0, (209,367))
cmd['kaisou']['r']          = (cmd['shared_page']['4'][0], 0, (209,426))
cmd['kaisou']['t']          = (cmd['shared_page']['5'][0], 0, (205,479))
cmd['kaisou']['y']          = (cmd['shared_page']['6'][0], 0, (207,528))
# 切換下方的頁面
cmd['kaisou']['a']          = (cmd['shared_page']['a'][0], 0, (180,548))
cmd['kaisou']['s']          = (cmd['shared_page']['s'][0], 0, (210,545))
cmd['kaisou']['d']          = (cmd['shared_page']['d'][0], 0, (246,539))
# 選擇沒編列艦隊的人
cmd['kaisou']['1']          = (cmd['shared_page']['1'][0], 0, (211,251))
cmd['kaisou']['2']          = (cmd['shared_page']['2'][0], 0, (210,282))
cmd['kaisou']['3']          = (cmd['shared_page']['3'][0], 0, (205,316))
cmd['kaisou']['4']          = (cmd['shared_page']['4'][0], 0, (205,336))
cmd['kaisou']['5']          = (cmd['shared_page']['5'][0], 0, (207,368))
cmd['kaisou']['6']          = (cmd['shared_page']['6'][0], 0, (205,399))
cmd['kaisou']['7']          = (cmd['shared_page']['7'][0], 0, (203,429))
cmd['kaisou']['8']          = (cmd['shared_page']['8'][0], 0, (206,453))
cmd['kaisou']['9']          = (cmd['shared_page']['9'][0], 0, (209,484))
cmd['kaisou']['0']          = (cmd['shared_page']['0'][0], 0, (205,509))
# 拋棄裝備
cmd['kaisou']['clear1']     = ("装備を外したのです", 0, (547,275))
cmd['kaisou']['clear2']     = ("装備を外したのです", 0, (326,329))
cmd['kaisou']['clear3']     = ("装備を外したのです", 0, (325,362))
cmd['kaisou']['clear4']     = ("装備を外したのです", 0, (327,394))
# 合成
cmd['kaisou']['gousei']     = ("近代化改修をします", 0, (613,533))
cmd['kaisou']['c']          = (cmd['general']['c'][0], 0, (550,539))



# 入渠
cmd['ndock'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['ndock'][key] = value
for key, value in cmd['shared_page'].items():
    cmd['ndock'][key] = value
cmd['ndock']['dock1']       = ("一番目のドックを選択しました", 0, (249,268))
cmd['ndock']['dock2']       = ("二番目のドックを選択しました", 0, (246,342))
cmd['ndock']['dock1item']   = ("一番目のドックでアイテムを使用しますか", 0, (754,250))
cmd['ndock']['dock2item']   = ("二番目のドックでアイテムを使用しますか", 0, (758,336))
cmd['ndock']['repair']      = ("いますぐ修理しますか？", 0, (690,535))
cmd['ndock']['hai']         = ("はい、なのです", 0, (503,498))
cmd['ndock']['iie']         = ("いいえ、キャンセルします", 0, (312,494))


# 工廠
cmd['factory'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['factory'][key] = value
cmd['factory']['dock1']     = (cmd['ndock']['dock1'][0], 0, (614,280))
cmd['factory']['dock2']     = (cmd['ndock']['dock2'][0], 0, (622,360))
cmd['factory']['dock1item'] = (cmd['ndock']['dock1item'][0], 0, (744,288))
cmd['factory']['dock2item'] = (cmd['ndock']['dock1item'][0], 0, (758,336))
cmd['factory']['kaitai']    = ("解体されるのは悲しいことです", 0, (234,347))
cmd['factory']['kaihatu']   = ("新しい装備を開発します", 0, (214,431))
cmd['factory']['haiki']     = ("古い装備を廃棄します", 0, (223,509))
cmd['factory']['sort']      = (cmd['shared_page']['sort'][0], 0, (586,211))
cmd['factory']['destory']   = ("Hastala Vista, Baby!", 0, (699,533))
cmd['factory']['hai']       = (cmd['ndock']['hai'][0], 0, (486,483))
cmd['factory']['iie']       = (cmd['ndock']['iie'][0], 0, (318,485))
# 建造與開發的材料 oil, bullet, steel, aluminum
cmd['factory']['oil+1']        = ("", 0, (362,254))
cmd['factory']['oil-1']        = ("", 0, (364,322))
cmd['factory']['oil+10']       = ("", 0, (491,237))
cmd['factory']['oil-10']       = ("", 0, (438,239))
cmd['factory']['oil+100']      = ("", 0, (490,265))
cmd['factory']['oil-100']      = ("", 0, (438,263))
cmd['factory']['bullet+1']     = ("", 0, (361,383))
cmd['factory']['bullet-1']     = ("", 0, (361,452))
cmd['factory']['bullet+10']    = ("", 0, (491,366))
cmd['factory']['bullet-10']    = ("", 0, (438,367))
cmd['factory']['bullet+100']   = ("", 0, (491,393))
cmd['factory']['bullet-100']   = ("", 0, (439,392))
cmd['factory']['steel+1']      = ("", 0, (589,254))
cmd['factory']['steel-1']      = ("", 0, (592,319))
cmd['factory']['steel+10']     = ("", 0, (718,238))
cmd['factory']['steel-10']     = ("", 0, (666,238))
cmd['factory']['steel+100']    = ("", 0, (719,263))
cmd['factory']['steel-100']    = ("", 0, (667,264))
cmd['factory']['aluminum+1']   = ("", 0, (591,384))
cmd['factory']['aluminum-1']   = ("", 0, (593,450))
cmd['factory']['aluminum+10']  = ("", 0, (720,365))
cmd['factory']['aluminum-10']  = ("", 0, (665,365))
cmd['factory']['aluminum+100'] = ("", 0, (721,393))
cmd['factory']['aluminum-100'] = ("", 0, (669,395))
cmd['factory']['build']        = ("建造開始、なのです", 0, (711,537))

# 拆解與廢棄時的選單
cmd['factory']['q']         = (cmd['shared_page']['q'][0], 0, (218,550))
cmd['factory']['w']         = (cmd['shared_page']['w'][0], 0, (497,552))
cmd['factory']['a']         = (cmd['shared_page']['a'][0], 0, (297,549))
cmd['factory']['s']         = (cmd['shared_page']['s'][0], 0, (332,552))
cmd['factory']['d']         = (cmd['shared_page']['d'][0], 0, (364,551))
cmd['factory']['f']         = (cmd['shared_page']['f'][0], 0, (395,551))
cmd['factory']['g']         = (cmd['shared_page']['q'][0], 0, (422,553))
cmd['factory']['1']         = (cmd['shared_page']['1'][0], 0, (294,237))
cmd['factory']['2']         = (cmd['shared_page']['2'][0], 0, (296,266))
cmd['factory']['3']         = (cmd['shared_page']['3'][0], 0, (297,297))
cmd['factory']['4']         = (cmd['shared_page']['4'][0], 0, (296,333))
cmd['factory']['5']         = (cmd['shared_page']['5'][0], 0, (296,362))
cmd['factory']['6']         = (cmd['shared_page']['6'][0], 0, (296,395))
cmd['factory']['7']         = (cmd['shared_page']['7'][0], 0, (295,424))
cmd['factory']['8']         = (cmd['shared_page']['8'][0], 0, (296,454))
cmd['factory']['9']         = (cmd['shared_page']['9'][0], 0, (294,482))
cmd['factory']['0']         = (cmd['shared_page']['0'][0], 0, (295,518))


# 任務一覽第 N 頁按鈕位置
cmd['quest'] = dict()
cmd['quest']['port'] = cmd['shared_menu']['port']
cmd['quest']['senseki'] = cmd['shared_menu']['senseki']
cmd['quest']['q']           = (cmd['shared_page']['q'][0], 0, (264,562))
cmd['quest']['w']           = (cmd['shared_page']['w'][0], 0, (654,562))
cmd['quest']['a']           = (cmd['shared_page']['a'][0], 0, (355,563))
cmd['quest']['s']           = (cmd['shared_page']['s'][0], 0, (406,564))
cmd['quest']['d']           = (cmd['shared_page']['d'][0], 0, (455,563))
cmd['quest']['f']           = (cmd['shared_page']['f'][0], 0, (514,563))
cmd['quest']['g']           = (cmd['shared_page']['g'][0], 0, (563,561))
cmd['quest']['1']           = ("一番目の任務を選択しました", 0, (739,243))
cmd['quest']['2']           = ("二番目の任務を選択しました", 0, (739,307))
cmd['quest']['3']           = ("三番目の任務を選択しました", 0, (739,376))
cmd['quest']['4']           = ("四番目の任務を選択しました", 0, (743,443))
cmd['quest']['5']           = ("五番目の任務を選択しました", 0, (746,519))

# 戦績
cmd['senseki'] = dict()
cmd['senseki']['port']      = cmd['shared_menu']['port']
cmd['senseki']['quest']     = cmd['shared_menu']['quest']
cmd['senseki']['info']      = ("情報ページを選択したのです", 0, (61,250))
cmd['senseki']['ranking']   = ("ランキングページを選択したのです", 0, (61,290))


# 出擊畫面
cmd['fight'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['fight'][key] = value
cmd['fight']['pve']         = ("出撃をします！", 1, (232,330))
cmd['fight']['pvp']         = ("演習をします！", 1, (463,331))
cmd['fight']['pvt']         = ("遠征をします！", 1, (682,330))

# 出擊
cmd['pve'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['pve'][key] = value
cmd['pve']['pvp']         = (cmd['fight']['pvp'][0], 1, (668,223))
cmd['pve']['pvt']         = (cmd['fight']['pvt'][0], 1, (744,222))
cmd['pve']['a']           = ("鎮守府海域を選択したのです", 0, (160,551))
cmd['pve']['s']           = ("南西諸島海域を選択したのです", 0, (234,550))
cmd['pve']['d']           = ("北方海域を選択したのです", 0, (310,547))
cmd['pve']['f']           = ("西方海域を選択したのです", 0, (380,549))
cmd['pve']['g']           = ("南方海域を選択したのです", 0, (452,538))
cmd['pve']['h']           = ("中部海域を選択したのです", 0, (530,546))
cmd['pve']['w']           = ("Extra Operation を挑戦してみます", 0, (727,375))
cmd['pve']['q']           = ("一般海域へ戻ったのです", 0, (144,378))
cmd['pve']['1']           = ("一番目の海域を選択したのです", 0, (166,284))
cmd['pve']['2']           = ("二番目の海域を選択したのです", 0, (511,280))
cmd['pve']['3']           = ("三番目の海域を選択したのです", 0, (172,412))
cmd['pve']['4']           = ("四番目の海域を選択したのです", 0, (504,415))
cmd['pve']['f1']          = (cmd['refill']['f1'][0], 0, (366,222))
cmd['pve']['f2']          = (cmd['refill']['f2'][0], 0, (394,215))
cmd['pve']['f3']          = (cmd['refill']['f3'][0], 0, (429,220))
cmd['pve']['f4']          = (cmd['refill']['f4'][0], 0, (455,215))
cmd['pve']['hai']         = (cmd['ndock']['hai'][0], 0, (729,545))
cmd['pve']['yes']         = cmd['pve']['hai']
cmd['pve']['y'  ]         = cmd['pve']['hai']
cmd['pve']['tatakau']     = ("出撃開始、全力で参ります！", 1, (637,545))

# 演習
cmd['pvp'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['pvp'][key] = value
cmd['pvp']['pve']         = (cmd['fight']['pve'][0], 1, (585,223))
cmd['pvp']['pvt']         = (cmd['fight']['pvt'][0], 1, (755,226))
cmd['pvp']['1']           = ("一番目の演習相手を選択したのです", 0, (290,292))
cmd['pvp']['2']           = ("二番目の演習相手を選択したのです", 0, (284,352))
cmd['pvp']['3']           = ("三番目の演習相手を選択したのです", 0, (284,403))
cmd['pvp']['4']           = ("四番目の演習相手を選択したのです", 0, (277,462))
cmd['pvp']['5']           = ("五番目の演習相手を選択したのです", 0, (276,514))
cmd['pvp']['f1']          = (cmd['refill']['f1'][0], 0, (190,191))
cmd['pvp']['f2']          = (cmd['refill']['f2'][0], 0, (223,190))
cmd['pvp']['f3']          = (cmd['refill']['f3'][0], 0, (256,188))
cmd['pvp']['f4']          = (cmd['refill']['f4'][0], 0, (283,190))
cmd['pvp']['c']           = (cmd['general']['c'][0], 0, (754,129))
cmd['pvp']['idomu']       = ("演習を挑む、艦隊を選んでください", 0, (243,504))
cmd['pvp']['tatakau']     = ("演習開始、全力で参ります！", 1, (474,529))


# 遠征
cmd['pvt'] = dict()
for key, value in cmd['shared_menu'].items():
    cmd['pvt'][key] = value
cmd['pvt']['pve']         = (cmd['fight']['pve'][0], 1, (362,211))
cmd['pvt']['pvp']         = (cmd['fight']['pvp'][0], 1, (439,212))
cmd['pvt']['a']           = ("鎮守府海域を選択したのです", 0, (143,532))
cmd['pvt']['s']           = ("南西諸島海域を選択したのです", 0, (202,536))
cmd['pvt']['d']           = ("北方海域を選択したのです", 0, (260,534))
cmd['pvt']['f']           = ("西方海域を選択したのです", 0, (309,534))
cmd['pvt']['g']           = ("南方海域を選択したのです", 0, (369,535))
cmd['pvt']['hai']         = (cmd['ndock']['hai'][0], 0, (687,539))
cmd['pvt']['yes']         = cmd['pvt']['hai']
cmd['pvt']['y']           = cmd['pvt']['hai']
cmd['pvt']['f2']          = (cmd['refill']['f2'][0], 0, (397,215))
cmd['pvt']['f3']          = (cmd['refill']['f3'][0], 0, (426,216))
cmd['pvt']['f4']          = (cmd['refill']['f4'][0], 0, (457,215))
cmd['pvt']['1']           = ("一番目の遠征任務を選択したのです", 0, (232,271))
cmd['pvt']['2']           = ("二番目の遠征任務を選択したのです", 0, (236,311))
cmd['pvt']['3']           = ("三番目の遠征任務を選択したのです", 0, (228,335))
cmd['pvt']['4']           = ("四番目の遠征任務を選択したのです", 0, (229,368))
cmd['pvt']['5']           = ("五番目の遠征任務を選択したのです", 0, (230,391))
cmd['pvt']['6']           = ("六番目の遠征任務を選択したのです", 0, (230,424))
cmd['pvt']['7']           = ("七番目の遠征任務を選択したのです", 0, (227,451))
cmd['pvt']['8']           = ("八番目の遠征任務を選択したのです", 0, (227,482))


cmd['tatakau'] = dict()
cmd['tatakau']['l']         = ("左を選択したのです", 0, (300,350))
cmd['tatakau']['r']         = ("右を選択したのです", 0, (517,343))
cmd['tatakau']['1']         = ("陣形 - 単縦陣(水雷特化)", 0, (452,279))
cmd['tatakau']['2']         = ("陣形 - 複縦陣(命中特化)", 0, (572,279))
cmd['tatakau']['3']         = ("陣形 - 輪形陣(防御重視)", 0, (694,282))
cmd['tatakau']['4']         = ("陣形 - 梯形陣", 0, (516,446))
cmd['tatakau']['5']         = ("陣形 - 単横陣(対潜特化)", 0, (648,441))

