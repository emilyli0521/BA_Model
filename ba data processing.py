#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def preprocess(fileName):

    with open(fileName, mode= "r", encoding ="utf-8") as f:
        content = f.read()
    content = content.replace("\n", "").replace("\t", "")
    content = content.replace("more", "")

    pattern = r"把[^，。？！；：]*[，。？！；：]"
    matched_sentences = re.findall(pattern, processed_content)

    return matched_sentences



if __name__ == "__main__":
    fileNameSTR = "ba raw data.txt"
    processed_content = preprocess(fileNameSTR)
    print(processed_content)
    #for match in processed_content:
        #print(match)
    with open("purged_{}".format(fileNameSTR), mode = "w", encoding = "utf-8") as g:
        g.write("\n".join(processed_content))