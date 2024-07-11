with open("./corpus.txt", mode= "w", encoding = "utf-8") as i:
    i.write("Hello")

with open("./corpus.txt", mode= "r", encoding ="utf-8") as f:
   contents = f.read()
   print(contents)