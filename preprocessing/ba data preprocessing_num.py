#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def preprocess(fileName):

    with open(fileName, mode= "r", encoding ="utf-8") as f:
        content = f.read()
    content = content.replace("\n", "").replace("\t", "")
    content = content.replace("more", "")

    pattern = r"[一二三四五六七八九]?[這那]?把[^，。？！；：]*[，。？！；：]"
    matched_sentences = re.findall(pattern, content)

    return matched_sentences



if __name__ == "__main__":
    # 絕對路徑設定
    input_file = r"C:\Users\Emily\Desktop\BA_Model\preprocessing\data\ba_raw_data_p108.txt"
    output_file = r"C:\Users\Emily\Desktop\BA_Model\preprocessing\data\purged_num_ba_raw_data_p108.txt"

    processed_content = preprocess(input_file)

    # 加上編號
    numbered_content = [f"{idx + 1}. {match}" for idx, match in enumerate(processed_content)]

    # 螢幕輸出
    print(f"共找到 {len(numbered_content)} 句符合的句子。")
    print("\n".join(numbered_content[:10]))  

    # 存檔
    with open(output_file, mode="w", encoding="utf-8") as g:
        g.write("\n".join(numbered_content))

    print(f"處理後的結果已儲存到：{output_file}")