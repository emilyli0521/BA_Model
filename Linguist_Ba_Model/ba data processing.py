#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
def preprocess(fileName):
    with open("ba raw data.txt", mode= "r", encoding ="utf-8") as f:
        content = f.read()
        content = content.replace("\n", "").replace("\t", "")
        content = content.replace("more", "")       
    return content
pattern = r"把[^，。？！；：]*[，。？！；：]"
processed_content = preprocess("ba raw data.txt")
matched_sentences = re.findall(pattern, processed_content)
for match in matched_sentences:
    print(match)
with open("purged_ba raw data.txt".format("ba raw data.txt"), mode = "w", encoding = "utf-8") as g:
    for sentence in matched_sentences:        
            g.write(sentence + '\n')
               
