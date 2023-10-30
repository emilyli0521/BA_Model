#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def preprocess(fileName):
    with open("ba raw data.txt", mode= "r", encoding ="utf-8") as f:
        content = f.read()
        content = content.replace("\n", "").replace("\t", "")
        content = content.split("moremore")
        content = '\n'.join(content)
        content = content.replace("more", "")
        content = content.replace("\n", "")
        content = content.replace("。", "。\n")
        print(content)    

        with open("purged_ba raw data.txt".format(fileName), mode = "w", encoding = "utf-8") as g:
            g.write(content)

preprocess("ba raw data.txt")