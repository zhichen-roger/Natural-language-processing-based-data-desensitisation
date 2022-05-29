words=[]
wordsrange=[]
vectors=[]
vectorsrange=[]
# 词语打开字典并去掉换行符
with open("word.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除换行符
    result = ([x.strip() for x in lines if x.strip() != ''])
    # 将整理好字典提取成为全局字典
    for x in result:
        words.append(x)
# 向量打开字典并去掉换行符
with open("vector.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除换行符
    result = ([x.strip() for x in lines if x.strip() != ''])
    # 将整理好字典提取成为全局字典
    for x in result:
        vectors.append(float(x))
dict = {word:vector for word,vector in zip(words,vectors )}# dict={'张三': 90, '李四': 80, '王五': 70, '赵六': 60}
orderdict = sorted(dict.items(),key=lambda item:item[1],reverse=True)
for index in range(len(orderdict)):
    wordsrange.append(orderdict[index][0])
    vectorsrange.append(orderdict[index][1])
dictrange = {wordr:vectorr for wordr,vectorr in zip(wordsrange,vectorsrange )}
f3 = open("middlerange.txt", "w", encoding='utf-8')
for key, value in dictrange.items():
    print(key+" "+str(value))
    f3.write(key+" "+str(value) + '\n')
f3.close()

#添加到两份文件夹中
f1 = open("wordrange.txt", "w", encoding='utf-8')
for index in range(len(wordsrange)):
    f1.write(str(wordsrange[index]) + '\n')
print(len(wordsrange))
f1.close()

f2 = open("vectorrange.txt", "w", encoding='utf-8')
for index in range(len(vectorsrange)):
    f2.write(str(vectorsrange[index]) + '\n')
print(len(vectorsrange))
f2.close()

