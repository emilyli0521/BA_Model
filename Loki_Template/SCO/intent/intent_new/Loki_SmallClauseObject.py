#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for SmallClauseObject

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
INTENT_NAME = "SmallClauseObject"

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_SmallClauseObject.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[SmallClauseObject] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)
    if utterance == "把作業本哭得沒有人能看得懂字跡":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            resultDICT["source"] = "reply"
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "把床單睡得主人不願再躺":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            resultDICT["source"] = "reply"
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "把床睡得沒人敢躺":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            resultDICT["source"] = "reply"
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "把毛衣哭得沒有人願意穿":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            resultDICT["source"] = "reply"
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    if utterance == "把玩具哭得同學都不敢摸。":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            resultDICT["source"] = "reply"
        else:
            # write your code here
            # resultDICT[key].append(value)
            pass

    return resultDICT