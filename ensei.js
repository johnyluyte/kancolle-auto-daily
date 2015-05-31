// ==UserScript==
// @name         ensei
// @namespace    http://chunnorris.cc/
// @version      0.1
// @description  Remove ensei IDs I am not interested in
// @author       cchien
// @match        http://wikiwiki.jp/kancolle/?%B1%F3%C0%AC
// @grant        none
// ==/UserScript==

$('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></' + 'script>').appendTo(document.body);

function clear3(){
    $('#body p').remove();
    $('#note').remove();
    $('#footer').remove();
}

function clear2(){
    var b = $('#body').find('#h2_content_1_9').nextAll();
    var len = b.length;
    for(var i=0;i<len;i++){
        b[i].remove();
    }
    $('#body').find('#h2_content_1_9').remove();
}

function clear1(){
    var a = $('#body').children();
    // console.log(a);
    for(var i=0;i<32;i++){
        a[i].remove();
    }
}


ignore_mission = [
    '練習航海',
    '観艦式予行',
    '観艦式',
    '強行偵察任務',
    '包囲陸戦隊撤収作戦',
    '艦隊決戦援護作戦',
    '敵地偵察作戦',
    '艦隊演習',
    '航空戦艦運用演習',
    '通商破壊作戦',
    '敵母港空襲作戦',
    '潜水艦通商破壊作戦',
    '西方海域封鎖作戦',
    '潜水艦派遣演習',
    '潜水艦派遣作戦',
    '海外艦との接触',
    '遠洋練習航海',
    '遠洋潜水艦作戦',
    '対潜警戒任務',
    '鼠輸送作戦',
    '東京急行',        // LV 50
    '東京急行（弐）',   // LV 65
    '東京急行(弐)'   // LV 65
    ];

function main($ie5){
    var $a = $ie5.contents().find('a');
    for(var i=0;i<$a.length;i++){
        // console.log($a.eq(i).text());
        $target = $a.eq(i)
        for(var k=0;k<ignore_mission.length;k++){
            if($target.text() == ignore_mission[k]){
                // console.log($target.parent().parent());
                $target.parent().parent().remove();
                break;
            }
        }
    }
}

$(function(){
    clear1();
    clear2();
    clear3();
    // main();

    var $ie5_list = $(".ie5");
    for(var i=0;i<$ie5_list.length;i++){
        main($ie5_list.eq(i));
    }

});
