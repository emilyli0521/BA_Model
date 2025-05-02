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
    fileNameSTR = "ba_raw_data_p80.txt"
    processed_content = preprocess(fileNameSTR)
    print(processed_content)
    
    numbered_content = [f"{idx + 1}. {match}" for idx, match in enumerate(processed_content)]

    with open("purged_num_{}".format(fileNameSTR), mode = "w", encoding = "utf-8") as g:
        g.write("\n".join(numbered_content))