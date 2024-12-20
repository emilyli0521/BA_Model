#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for VerbDirectObject

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_VerbDirectObject.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[VerbDirectObject] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "希望把人民生活品質水準提升到。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "提升"
            pass

    if utterance == "希望把這杯飲料與所有朋友分享。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "分享"
            pass

    if utterance == "得先把這問題說一說":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "說一說"
            pass

    if utterance == "想要把這個獎獻給":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "獻給"
            pass

    if utterance == "想要把這個獎獻給他的太太和兒子。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "獻給"
            pass

    if utterance == "想要把這個禮物與所有台中人共享":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "共享"
            pass

    if utterance == "應該把別人做的作品拿出來看一看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "看一看"
            pass

    if utterance == "把「九二共識」和「一中」視為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "視為"
            pass

    if utterance == "把「命運共同體」掛在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "掛在"
            pass

    if utterance == "把「火」和「濕氣」徹底清除，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "清除"
            pass

    if utterance == "把「西洋梨」身材完全展露":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "展露"
            pass

    if utterance == "把一個原本非常重要的「鄉土」定義問題懸而不論，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "懸而不論"
            pass

    if utterance == "把一個堅倔強又脆弱細緻的女人深深刻劃":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "深深刻劃"
            pass

    if utterance == "把一個堅倔強又脆弱細緻的女人深深刻劃在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "深深刻劃在"
            pass

    if utterance == "把一百零八種煩惱視為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "視為"
            pass

    if utterance == "把七十年代曖昧不清的「鄉土」觀念明確的重定為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "重定為"
            pass

    if utterance == "把人物的情感全部調動起來":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "調動起來"
            pass

    if utterance == "把他換下場。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "換下場"
            pass

    if utterance == "把他看三遍了。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "看三遍"
            pass

    if utterance == "把作品特色淋漓盡致的發揮，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "發揮"
            pass

    if utterance == "把便宜佔盡了。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "佔盡"
            pass

    if utterance == "把俄羅斯視為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "視為"
            pass

    if utterance == "把傳統廟會元素以當代藝術形式呈現，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "呈現"
            pass

    if utterance == "把債權人大量灌水，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "灌水"
            pass

    if utterance == "把光圈由５﹒６往８﹒０逐漸縮小，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "縮小"
            pass

    if utterance == "把問題扯到丁懋時身上？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "扯"
            pass

    if utterance == "把問題都丟給委員幫忙解決。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "解決"
            pass

    if utterance == "把啤酒不停地喝。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "喝"
            pass

    if utterance == "把四個經營區調整為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "調整"
            pass

    if utterance == "把四周的景象都映入":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "映入"
            pass

    if utterance == "把國內所跳的舞介紹到外地去。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "介紹"
            pass

    if utterance == "把圖畫書和純繪畫做了巧妙的結合，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "結合"
            pass

    if utterance == "把她殺了哥哥。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "殺了"
            pass

    if utterance == "把它登子去典當，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "典當"
            pass

    if utterance == "把它粗略區分為二，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "區分"
            pass

    if utterance == "把對象內在的或外在的那份美充分挖掘出來，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "挖掘"
            pass

    if utterance == "把彌補國安基金虧損以「經濟發展」項目編列，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "編列"
            pass

    if utterance == "把我帶往何處？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "帶往"
            pass

    if utterance == "把所有產業都留在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "留"
            pass

    if utterance == "把所有的可能疑慮包括在內。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "包括"
            pass

    if utterance == "把所有的可能發展涵蓋在內。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "涵蓋"
            pass

    if utterance == "把所有的石板棺都搶救下來，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "搶救"
            pass

    if utterance == "把未來二十年、三十年、甚至一百年的問題拿到現在解決，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "解決"
            pass

    if utterance == "把李登輝鬥垮、鬥臭。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "鬥垮、鬥臭"
            pass

    if utterance == "把林女腳鐐戒具解開，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "解開"
            pass

    if utterance == "把棘手的政治爭議擱置？":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "擱置"
            pass

    if utterance == "把洋基隊打者三振得":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "三振"
            pass

    if utterance == "把滿是蜘蛛絲的祖宗牌位拿出來看，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "看"
            pass

    if utterance == "把爭議點講清楚。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "講清楚"
            pass

    if utterance == "把牠們全都救回":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "救回"
            pass

    if utterance == "把相關資料影印帶來，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "帶來"
            pass

    if utterance == "把相關附屬設施納入評估，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "評估"
            pass

    if utterance == "把真、善、美圈選為三類最高級的價值判斷就已經開始了。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "圈選"
            pass

    if utterance == "把稅繳進了台北市":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "繳"
            pass

    if utterance == "把競選Ｔ恤放在車上，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "放"
            pass

    if utterance == "把總冠軍的1000萬元獎金給大家平分，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "評分"
            pass

    if utterance == "把自己最愛惜的兒子賣去，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "賣去"
            pass

    if utterance == "把自己的生活方式推廣到":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "推廣"
            pass

    if utterance == "把色情在一個月內趕出轄區":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "趕出"
            pass

    if utterance == "把賺到的錢匯回，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "匯回"
            pass

    if utterance == "把越南新娘娶回台北":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "娶回"
            pass

    if utterance == "把身上所有金飾藏在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "藏"
            pass

    if utterance == "把這一龐雜的書體系統化，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "系統化"
            pass

    if utterance == "把這二堆龐雜的教科書系統化，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "系統化"
            pass

    if utterance == "把這些存心與行動與週遭的人分享，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "分享"
            pass

    if utterance == "把這四部電影找來好好欣賞。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "找"
            pass

    if utterance == "把這張錯漏候選人號次的公報拿到他的競選總部提出檢舉，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "拿"
            pass

    if utterance == "把這影集看了五次。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "看"
            pass

    if utterance == "把這種〝情〞再賦予":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "賦予"
            pass

    if utterance == "把選舉投票通知書透過里長發放給":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "發放"
            pass

    if utterance == "把那座墓哭垮了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "哭垮"
            pass

    if utterance == "把錢交給選民，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "交"
            pass

    if utterance == "把錢拿到大陸投資，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "拿"
            pass

    if utterance == "把錢拿回來，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            
        else:
            resultDICT["action"] = "拿"
            pass

    if utterance == "把錢提出去也要管":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "管"
            pass

    if utterance == "把錢直接留在國外，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "留"
            pass

    if utterance == "把雙胞女兒放在樹下，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "放"
            pass

    if utterance == "會把他踹好幾腳。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "踹"
            pass

    if utterance == "把小王殺了女友":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "殺了"
            pass

    if utterance == "把約翰殺了父親":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "殺了"
            pass

    if utterance == "把臉一板":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "板著臉"
            pass

    if utterance == "把你打了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "打了"
            pass

    if utterance == "把你打了一頓":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "打了"
            pass

    if utterance == "把墓碑哭垮了":
        if CHATBOT_MODE:
            
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "哭垮了"
            pass

    if utterance == "把瑪莉打了一頓":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "打了"
            pass

    if utterance == "把入冬的台北粧點成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "粧點"
            pass

    if utterance == "把一幅畫賣給了老闆":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "賣給"
            pass

    if utterance == "把國家情勢導引成退化、退步的政府，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "導引"
            pass

    if utterance == "把蚊蟲驅趕至門口":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "把這些勞動規約標準統一化。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "要把正確的知識告訴她們。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "告訴"
            pass
        
    return resultDICT
