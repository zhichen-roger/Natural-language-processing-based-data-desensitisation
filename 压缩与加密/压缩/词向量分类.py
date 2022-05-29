word = []
vector = []
Dict = []
num = 0
# 打开字典并去掉换行符
with open("middleyas.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除换行符
    result = ([x.strip() for x in lines if x.strip() != ''])
    #print(result)
    for x in result:
        Dict.append(x)
    # 将整理好字典提取成为全局字典
    for k in range(len(Dict) - int(len(Dict) % 2)):
        if num == 1:
            vector.append(Dict[k])
        else:
            num = 0
            word.append(Dict[k])
        num += 1
    #添加到两份文件夹中
    f1 = open("word.txt", "w", encoding='utf-8')
    for index in range(len(word)):
        f1.write(str(word[index]) + '\n')
    print(len(word))
    f1.close()

    f2 = open("vector.txt", "w", encoding='utf-8')
    for index in range(len(vector)):
        f2.write(str(vector[index]) + '\n')
    print(len(vector))
    f2.close()






