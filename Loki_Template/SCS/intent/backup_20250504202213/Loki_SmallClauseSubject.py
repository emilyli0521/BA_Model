#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for SmallClauseSubject

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
from ArticutAPI import Articut

articut = Articut(username="a0930591669@gmail.com", apikey="abi4k2-YpjE4b+lhJyM5N1gg%UM#iGn")

LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
DEBUG = True
CHATBOT_MODE = False

USERNAME = "a0930591669@gmail.com"
LOKI_KEY = "KPW&jm%H^mXc#4Ob1KWONpeZjKSC^3h"


userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_SmallClauseSubject.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[SmallClauseSubject] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

skipVerbLIST = ["讓", "趕", "貪", "寄", "拿", "丟", "罵", "載", "達", "完", "買", "抱", "鬆", "哭", "燒", "揹", "摔", "哭", "笑"]

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
                
    if utterance == "把人身去換金錢，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "去換"
            pass


    if utterance == "把名片改成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "改成"
            pass


    if utterance == "把技藝傳給":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "傳給"
            pass
 

    if utterance == "把六百多人的研發部門遷往":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "遷往"
            pass


    if utterance == "把A調整為B":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "調整為"
            pass
 

    if utterance == "把功勞歸於":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "歸於"
            pass


    if utterance == "把南京中山陵、玄武湖的景點也串在一起":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "串"
            pass


    if utterance == "把屋子保持得很乾爽":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "保持得"
            pass


    if utterance == "把張三視為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "視為"
            pass


    if utterance == "把日產量減產五十萬桶。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "減產"
            pass


    if utterance == "把王五醉得":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "醉得"
            pass


    if utterance == "把目光轉向":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "轉向"
            pass


    if utterance == "把大地裝扮成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "裝扮成"
            pass


    if utterance == "把她殺了哥哥。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "殺了"
            pass


    if utterance == "把當地以老古石堆砌成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "堆砌成"
            pass


    if utterance == "把你當做":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "當做"
            pass
 

    if utterance == "把他醉倒了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "醉倒"
            pass


    if utterance == "把一心待他好的鄰家女袁詠儀視如敝屣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "視如敝屣"
            pass


    if utterance == "把他退學":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "退學"
            pass
 
                
    if utterance == "把大把的雜物碎片撒得":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "撒得"
            pass


    if utterance == "把它包紮得":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "包紮得"
            pass


    if utterance == "把美學研究和文化研究有機地結為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "結為"
            pass


    if utterance == "把真正的美善陷於":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "陷於"
            pass

    if utterance == "把什麼問題都攪在":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "攪在"
            pass 

    if utterance == "把作品編號的勞動製造條件公諸":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "公諸"
            pass 

    if utterance == "把咱家那位夜間部同學公諸於世":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "公諸於世"
            pass  

    if utterance == "把案情導向":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "導向"
            pass 

    if utterance == "把這種經驗稱之為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "稱之為"
            pass 
                
    if utterance == "把中央和地方增減數目相抵":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "相抵"
            pass 
                
    if utterance == "把燈對準":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "對準"
            pass 

    if utterance == "把精神病患者裝上":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "裝上"
            pass 

    if utterance == "把火箭送入":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "送入"
            pass 

    if utterance == "把整個住宅劃分成":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "劃分成"
            pass   

    if utterance == "把泡湯商機從家裏拉至":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "拉至"
            pass

    if utterance == "把他們結合成為":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "結合成為"
            pass

    if utterance == "把獎座一分為三，":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "分為"
            pass

    if utterance == "把劍鞘上鑲著":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["action"] = "鑲著"
            pass  

    return resultDICT