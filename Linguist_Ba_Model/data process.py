'''
content =f.read()
   print(content)
   '''
'''
with open("../test2.txt", mode = "w", encoding = "utf-8") as g:
   content = g.write("早安")
   print(content)
   '''
def preprocess(fileName):
    with open("{}.txt".format(fileName), mode = "r", encoding = "utf-8") as f:
        content = f.read()
        content = content.replace("\n", "").replace("\t", "")
        content = content.split("moremore")
        content = '\n'.join(content)
        content = content.replace("more", "")
            
    with open("{}_purged.txt".format(fileName), mode = "w", encoding = "utf-8") as g:
       g.write(content)


preprocess("../test2")