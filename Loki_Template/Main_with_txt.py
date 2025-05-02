#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import re
import sys


sys.path.append('/VDO')
sys.path.append('/SCS')
sys.path.append('/VIO')
sys.path.append('/SCO')

import VDO.VDO
import SCS.SCS
import VIO.VIO
import SCO.SCO

#logging.basicConfig(level=logging.DEBUG)

punctuationPat = re.compile("[,\.\?:;，。？：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？：；\n]+")
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
    
    return resultDICT_VDO, resultDICT_SCS, resultDICT_VIO, resultDICT_SCO


def save_results_to_file(result_str, inputSTR):
    file_name = "result_{}.txt".format(re.sub(r'[\\\/:*?"<>|]', "", inputSTR.split(".")[0])) # 清理文件名
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(result_str)


if __name__ == "__main__":
    runBOOL = True
    
    resultDICT_VDO = {}
    resultDICT_SCS = {}
    resultDICT_VIO = {}
    resultDICT_SCO = {}
    
    while runBOOL:
        inputSTR = input("請輸入一句含「把」的字句，或輸入 .txt 檔案，或按 Q 退出)：\n").strip()
        
        if inputSTR.upper() == "Q":
            runBOOL = False
            
        elif inputSTR.endswith('.txt'):
            try:
                with open(inputSTR, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    all_results = []
                    for idx, line in enumerate(lines, start=1):
                        line = line.strip()
                        if not line:  # Skip any empty lines
                            continue
                        resultDICT_VDO, resultDICT_SCS, resultDICT_VIO, resultDICT_SCO = getLokiResult(line)
                        resultSTR = ""
                        if resultDICT_VDO:
                            resultSTR = "是「把」字句，是 VDO 把字句。"
                        elif resultDICT_SCS:
                            resultSTR = "是「把」字句，是 SCS 把字句。"
                        elif resultDICT_VIO:
                            resultSTR = "是「把」字句，是 VIO 把字句。"
                        elif resultDICT_SCO:
                            resultSTR = "是「把」字句，是 SCO 把字句。"
                        else:
                            resultSTR = "不是「把」字句"
                        all_results.append(f"{idx}. {resultSTR}")
                    
                    file_name = "result_{}.txt".format(re.sub(r'[\\\/:*?"<>|]', "", inputSTR.split("/")[-1].split(".")[0])) # 清理文件名
                    with open(file_name, mode="w", encoding="utf-8") as g:
                        g.write("\n".join(all_results))
            
            except FileNotFoundError as e:
                print(f"檔案未找到。請重新輸入檔案路徑。 Error: {e}")
        else:
            # It's an input string
            resultDICT_VDO, resultDICT_SCS, resultDICT_VIO, resultDICT_SCO = getLokiResult(inputSTR)
            
            if any([resultDICT_VDO, resultDICT_SCS, resultDICT_VIO, resultDICT_SCO]):
                
                if resultDICT_VDO:
                    resultSTR = "是「把」字句，是 VDO 把字句。"
                    print(resultSTR)
                    save_results_to_file(resultSTR, inputSTR)

                elif resultDICT_SCS:
                    resultSTR = "是「把」字句，是 SCS 把字句。"
                    print(resultSTR)
                    save_results_to_file(resultSTR, inputSTR)

                elif resultDICT_VIO:
                    resultSTR = "是「把」字句，是 VIO 把字句。"
                    print(resultSTR)
                    save_results_to_file(resultSTR, inputSTR)

                elif resultDICT_SCO:
                    resultSTR = "是「把」字句，是 SCO 把字句。"
                    print(resultSTR)
                    save_results_to_file(resultSTR, inputSTR)

            else:
                resultSTR = "不是「把」字句"
                print(resultSTR)
                save_results_to_file(resultSTR, inputSTR)
