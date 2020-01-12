def getText():
    txt = open("hamlet.txt", "r").read()     # 打开文本文件hamlet.txt
    txt = txt.lower()    # 将所有字符串转换为小写字符
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':    # 将标点字符替换为空字符
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1    # word的对应值，若字典中不存在word，返回0
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10} {1:>5}".format(word, count))
