#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import logging
import json
import re
from pprint import pprint
import sys


sys.path.append('/VDO')
sys.path.append('/SCS')
sys.path.append('/VIO')
sys.path.append('/SCO')

import VDO.VDO
import SCS.SCS
import VIO.VIO
import SCO.SCO

##logging.basicConfig(level=logging.DEBUG)

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";","."]
    
    resultDICT_VDO = VDO.VDO.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_SCS = SCS.SCS.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_VIO = VIO.VIO.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_SCO = SCO.SCO.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    
    logging.debug("Loki Result VDO => {}".format(resultDICT_VDO))
    logging.debug("Loki Result SCS => {}".format(resultDICT_SCS))
    logging.debug("Loki Result VIO => {}".format(resultDICT_VIO))
    logging.debug("Loki Result SCO => {}".format(resultDICT_SCO))
    
        
    return resultDICT_VDO,resultDICT_SCS,resultDICT_VIO,resultDICT_SCO



if __name__ == "__main__":
    while True:
        inputSTR = input("請輸入任何有「把」的句子 \n")
        resultDICT_VDO, resultDICT_SCS, resultDICT_VIO, resultDICT_SCO = getLokiResult(inputSTR)
        

        if any([resultDICT_VDO, resultDICT_SCS, resultDICT_VIO, resultDICT_SCO]):
            if resultDICT_VDO:
                print("是「把」字句，是 VDO 把字句。")

            elif resultDICT_SCS:
                print("是「把」字句，是 SCS 把字句。")

            elif resultDICT_VIO:
                print("是「把」字句，是 VIO 把字句。")

            elif resultDICT_SCO:
                print("是「把」字句，是 SCO 把字句。")

        else:
            print("不是「把」字句")
            
        

