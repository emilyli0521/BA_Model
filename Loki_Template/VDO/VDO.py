#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 4.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from copy import deepcopy
from glob import glob
from importlib import import_module
from pathlib import Path
from requests import post
from requests import codes
import json
import math
import os
import re

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CWD_PATH = str(Path.cwd())

lokiIntentDICT = {}
for modulePath in glob("{}/intent/Loki_*.py".format(BASE_PATH)):
    moduleNameSTR = Path(modulePath).stem[5:]
    modulePathSTR = modulePath.replace(CWD_PATH, "").replace(".py", "").replace("/", ".").replace("\\", ".")[1:]
    globals()[moduleNameSTR] = import_module(modulePathSTR)
    lokiIntentDICT[moduleNameSTR] = globals()[moduleNameSTR]

LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
try:
    accountInfo = json.load(open(os.path.join(BASE_PATH, "account.info"), encoding="utf-8"))
    USERNAME = accountInfo["username"]
    LOKI_KEY = accountInfo["loki_key"]
except Exception as e:
    print("[ERROR] AccountInfo => {}".format(str(e)))
    USERNAME = ""
    LOKI_KEY = ""

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    if "word_count_balance" in result:
                        self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[], refDICT={}):
    resultDICT = deepcopy(refDICT)
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            lokiResultDICT = {k: [] for k in refDICT}
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                if lokiRst.getIntent(index, resultIndex) in lokiIntentDICT:
                    lokiResultDICT = lokiIntentDICT[lokiRst.getIntent(index, resultIndex)].getResult(
                        key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex),
                        lokiResultDICT, refDICT, pattern=lokiRst.getPattern(index, resultIndex))

            # save lokiResultDICT to resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                if type(resultDICT[k]) != list:
                    resultDICT[k] = [resultDICT[k]] if resultDICT[k] else []
                if type(lokiResultDICT[k]) == list:
                    resultDICT[k].extend(lokiResultDICT[k])
                else:
                    resultDICT[k].append(lokiResultDICT[k])
    else:
        resultDICT["msg"] = lokiRst.getMessage()
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[], refDICT={}):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content
        refDICT       DICT           參考內容

    output
        resultDICT    DICT           合併 runLoki() 的結果

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    resultDICT = deepcopy(refDICT)
    if resultDICT is None:
        resultDICT = {}

    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST=filterLIST, refDICT=resultDICT)
            if "msg" in resultDICT:
                break

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # VerbDirectObject
##    print("[TEST] VerbDirectObject")
    inputLIST = ['把軟底改為','把他換下場。','把俄羅斯視為','把錢拿回來，','把他的身體塗成','把他看三遍了。','把便宜佔盡了。','把她殺了哥哥。','把我帶往何處？','把牠們全都救回','把那座墓哭垮了','把錢交給選民，','想要把這個獎獻給','把啤酒不停地喝。','把它登子去典當，','把所有產業都留在','把爭議點講清楚。','把稅繳進了台北市','把賺到的錢匯回，','把赤壁之戰擴大成','把錢提出去也要管','會把他踹好幾腳。','得先把這問題說一說','把債權人大量灌水，','把四個經營區調整為','把四周的景象都映入','把它粗略區分為二，','把洋基隊打者三振得','把越南新娘娶回台北','把身上所有金飾藏在','把這影集看了五次。','把這種〝情〞再賦予','把錢拿到大陸投資，','把錢直接留在國外，','把「命運共同體」掛在','把一百零八種煩惱視為','把李登輝鬥垮、鬥臭。','把林女腳鐐戒具解開，','把相關資料影印帶來，','把競選Ｔ恤放在車上，','把雙胞女兒放在樹下，','把問題扯到丁懋時身上？','把棘手的政治爭議擱置？','把自己的生活方式推廣到','把「西洋梨」身材完全展露','把人物的情感全部調動起來','把六百多人的研發部門遷往','把相關附屬設施納入評估，','把自己最愛惜的兒子賣去，','把色情在一個月內趕出轄區','把這一龐雜的書體系統化，','要把正確的知識告訴她們。','把作品特色淋漓盡致的發揮，','把問題都丟給委員幫忙解決。','把所有的可能疑慮包括在內。','把所有的可能發展涵蓋在內。','把所有的石板棺都搶救下來，','把這四部電影找來好好欣賞。','把「九二共識」和「一中」視為','把「火」和「濕氣」徹底清除，','把國內所跳的舞介紹到外地去。','把這二堆龐雜的教科書系統化，','希望把人民生活品質水準提升到。','希望把這杯飲料與所有朋友分享。','想要把這個禮物與所有台中人共享','應該把別人做的作品拿出來看一看','把選舉投票通知書透過里長發放給','想要把這個獎獻給他的太太和兒子。','把光圈由５﹒６往８﹒０逐漸縮小，','把圖畫書和純繪畫做了巧妙的結合，','把滿是蜘蛛絲的祖宗牌位拿出來看，','把這些存心與行動與週遭的人分享，','把總冠軍的1000萬元獎金給大家平分，','把傳統廟會元素以當代藝術形式呈現，','把國家情勢導引成退化、退步的政府，','把一個堅倔強又脆弱細緻的女人深深刻劃','把一個堅倔強又脆弱細緻的女人深深刻劃在','把對象內在的或外在的那份美充分挖掘出來，','把彌補國安基金虧損以「經濟發展」項目編列，','把七十年代曖昧不清的「鄉土」觀念明確的重定為','把一個原本非常重要的「鄉土」定義問題懸而不論，','把勞工自由選擇適用哪一個制度改成透過勞資協商，','把未來二十年、三十年、甚至一百年的問題拿到現在解決，','把當地以老古石堆砌成抗風的「蜂巢田」方式引進作品裡。','把真、善、美圈選為三類最高級的價值判斷就已經開始了。','把這張錯漏候選人號次的公報拿到他的競選總部提出檢舉，']
    testLoki(inputLIST, ['VerbDirectObject'])
##    print("")


if __name__ == "__main__":
    inputSTR = "我把錢拿回家"
    filterLIST = ["VerbDirectObject"]
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]

    resultDICT_VDO = execLoki(inputSTR, filterLIST=filterLIST, splitLIST=splitLIST)
    if "VerbDirectObject" in resultDICT_VDO:
        for entry in resultDICT_VDO["VerbDirectObject"]:
            print(f"[VerbDirectObject] {entry['text']} ===> {entry['result']}")
    else:
        print("没有找到 VerbDirectObject 结果")    


##    # 測試所有意圖
##    testIntent()
##
##    # 測試其它句子
##    filterLIST = []
##    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
##    # 設定參考資料
##    refDICT = { # value 必須為 list
##        #"key": []
##    }
##    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, refDICT=refDICT)                      # output => {"key": ["今天天氣"]}
##    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT) # output => {"key": ["今天天氣", "後天氣象"]}
##    resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST=filterLIST, refDICT=refDICT)                # output => {"key": ["今天天氣", "後天氣象"]}