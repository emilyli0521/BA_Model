#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import re
import sys
import os


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

# input/output pass:

BASE_INPUT_DIR  = r"C:\Users\Emily\Desktop\BA_Model\preprocessing\data"
BASE_OUTPUT_DIR = r"C:\Users\Emily\Desktop\BA_Model\Loki_Template\CKIP Verified Results"


def _bucket_dir_from_filename(fname: str) -> str:
    """
    從檔名抓頁碼 pN，決定要放到 p1-10、p11-20... 之類的資料夾
    找不到頁碼時預設 p1-10
    """
    m = re.search(r"p(\d+)", fname.lower())
    if not m:
        start = 1
    else:
        p = int(m.group(1))
        start = ((p - 1) // 10) * 10 + 1
    end = start + 9
    return f"p{start}-{end}"

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
                # === NEW: 若使用者只輸入檔名，從預設資料夾找；若輸入完整路徑則直接用 ===
                inpath = inputSTR
                if not os.path.isabs(inpath):
                    inpath = os.path.join(BASE_INPUT_DIR, inputSTR)

                with open(inpath, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    all_results = []
                    for idx, line in enumerate(lines, start=1):
                        line = line.strip()
                        if not line:
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

                    # === NEW: 依檔名決定分桶資料夾，並寫到 CKIP Verified Results\pX-Y\ ===
                    stem = os.path.splitext(os.path.basename(inpath))[0]
                    bucket = _bucket_dir_from_filename(stem)
                    outdir = os.path.join(BASE_OUTPUT_DIR, bucket)
                    os.makedirs(outdir, exist_ok=True)
                    
                    safe_stem = re.sub(r'[\\/:*?"<>|]', '', stem)  # 先清理檔名
                    outfile = os.path.join(outdir, f"result_{safe_stem}.txt")

                    with open(outfile, mode="w", encoding="utf-8") as g:
                        g.write("\n".join(all_results))

                    print(f"共處理 {len(all_results)} 句。已輸出到：{outfile}")

            except FileNotFoundError as e:
                print(f"檔案未找到。請確認是否放在 {BASE_INPUT_DIR} 或提供正確路徑。\nError: {e}")

        else:
            
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
