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
import re
from ArticutAPI import ArticutAPI
from pprint import pprint

articut = ArticutAPI.Articut(username="a0930591669@gmail.com", apikey="abi4k2-YpjE4b+lhJyM5N1gg%UM#iGn")

LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
DEBUG = True
CHATBOT_MODE = False

USERNAME = "a0930591669@gmail.com"
LOKI_KEY = "KPW&jm%H^mXc#4Ob1KWONpeZjKSC^3h"

      
userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print(f"[ERROR] userDefinedDICT => {e}")

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_VerbDirectObject.json"), encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] responseDICT => {e}")

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

skipVerbLIST = ["做", "著", "圍", "作", "成", "植", "伸", "入", "準", "理", "近", "列", "同", "歸", "串", "向", "比", "凋", "至", "換", "營", "得", "退", "叫", "來", "發", "消", "保", "視", "減", "勞", "諸", "傳", "改", "當", "變", "為", "交"]
    

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    if utterance == "得先把這問題說一說":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "說一說"
            subSTR = re.sub("[<>/]", "", args[1])
            parsedResult = articut.parse(subSTR)
            resultDICT["parsed"] = parsedResult
                        
            if parsedResult.get("result_pos", [])[1] in skipVerbLIST:
                pass

    if utterance == "應該把別人做的作品拿出來看一看":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            subSTR = re.sub("[<>/]", "", args[1])
            resultDICT = articut.parse(subSTR)
            verbLIST = articut.getVerbStemLIST(resultDICT)
            resultDICT["parsed"] = parsedResult
            if verbLIST[0][-1][-1] in skipVerbLIST:
                pass
            else:
                resultDICT

    if utterance == "把一個原本非常重要的「鄉土」定義問題懸而不論，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "懸而不論"
            pass

    if utterance == "把光圈由５﹒６往８﹒０逐漸縮小，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "縮小"
            pass

    if utterance == "把問題都丟給委員幫忙解決。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "解決"
            pass

    if utterance == "把圖畫書和純繪畫做了巧妙的結合，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "結合"
            pass


    if utterance == "把彌補國安基金虧損以「經濟發展」項目編列，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "編列"
            pass

    if utterance == "把滿是蜘蛛絲的祖宗牌位拿出來看，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "看"
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
            resultDICT["action"] = "平分"
            pass

    if utterance == "把這些存心與行動與週遭的人分享，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "分享"
            pass

    if utterance == "把選舉投票通知書透過里長發放給":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "發放"
            pass

    if utterance == "會把他踹好幾腳。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "踹"
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
            resultDICT["action"] = "驅趕"
            pass

    if utterance == "把這些勞動規約標準統一化。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "統一化"
            pass

    if utterance == "把他一推":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "推他"
            pass

    if utterance == "把他們從無所事事的環境裡拯救出來":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "拯救他"
            pass

    if utterance == "把你刻在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "刻你在"
            pass

    if utterance == "把全部的文章都修改了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "修改"
            pass

    if utterance == "把初夜留待結婚之後":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            subSTR = re.sub("[<>/]", "", args[1])
            resultDICT = articut.parse(subSTR)
            verbLIST = articut.getVerbStemLIST(resultDICT)
            resultDICT["parsed"] = parsedResult
            if verbLIST[0][-1][-1] in skipVerbLIST:
                pass
            else:
                resultDICT               

    if utterance == "把國民黨和民進黨都罵光了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "罵光"
            pass

    if utterance == "把我那老一套耳提面命，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "耳提面命"
            pass

    if utterance == "把開會摘要連同圖文並茂的曲線圖或表格即時存檔":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "存檔"
            pass

    if utterance == "把你罵了一頓":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "罵了你"
            pass

    if utterance == "把複雜晦暗的現代社會以純化的方式來表現":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "表現"
            pass

    if utterance == "把他看三遍了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "看三遍了"
            pass

    if utterance == "把部分的勞工法令從五人以下企業排除適用":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "排除適用"
            pass
       
    if utterance == "把一幅畫賣給了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "賣給"
            pass

    if utterance == "把和道奇在外卡戰的差距拉開到":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "拉開"
            pass

    if utterance == "把國內所跳的舞介紹到":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "介紹"
            pass

    if utterance == "把牛隊先發投手「阿甘」蔡仲南打退場":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "打退場"
            pass

    if utterance == "把蚊蟲驅趕至":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "驅趕至"
            pass

    if utterance == "把近萬個汽車格改":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "改"
            pass

    if utterance == "把錢直接留在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "留"
            pass

    if utterance == "把十塊錢給":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "給"
            pass

    if utterance == "把那些書刊「粉身碎骨」":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "粉身碎骨"
            pass

    if utterance == "把主角換掉":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "換掉"
            pass

    if utterance == "把功課做完了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "做完了"
            pass

    if utterance == "把商店轉型":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "轉型"
            pass

    if utterance == "把寶貴揹著":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "揹著"
            pass

    if utterance == "把功課準備好":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "準備好"
            pass

    if utterance == "把寧靜大美人載走了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "載走了"
            pass

    if utterance == "把東西遞交":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "遞交"
            pass

    if utterance == "把結婚照外賣的興致大減":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "大減"
            pass

    if utterance == "把頭搖一搖":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "搖一搖"
            pass

    
    return resultDICT

