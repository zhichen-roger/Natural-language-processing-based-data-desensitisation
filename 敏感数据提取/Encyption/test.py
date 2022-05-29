import re
from stanfordcorenlp import StanfordCoreNLP
import os

# 读取医院名
Hospital=[]
with open("./yiyuan.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除换行符
    result = ([x.strip() for x in lines if x.strip() != ''])
    # 将整理好字典提取成为全局字典
    for x in result:
        Hospital.append(x)

nlp = StanfordCoreNLP('D:\stanford\stanford-corenlp-latest\stanford-corenlp-full-2021-01-09', lang='zh')
osfile = []
dir = r"..\Encyption"
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.split('.')[1] == 'txt' and file != 'yiyuan.txt':
            osfile.append(file)

for indexFile in range(len(osfile)):
    splitTxtSpace=[]
    example=[]
    with open('../Encyption/' + osfile[indexFile], "r", encoding="utf-8") as f:
        lines = f.readlines()
        resultTxt = ([x.strip() for x in lines if x.strip() != ''])
        for index1 in range(len(resultTxt)):
            splitTxt = resultTxt[index1].split('。')
            for index2 in range(len(splitTxt)):
                splitTxtSpace.append(splitTxt[index2].strip())
        splitTxtSpace = [i for i in splitTxtSpace if (len(str(i)) != 0)]
        for index3 in range(len(splitTxtSpace)):
            if splitTxtSpace[index3] !='':
                example.append(splitTxtSpace[index3]+'。')
        for index in range(len(example)):
            Location=[]

            # 数字
            pattern1 = "(13\d{7,11}|14[5|7]\d{6,10}|15\d{7,11}|166\d{6,10}|17[3|6|7]\d{6,10}|18\d{7,11})"
            phone_list1 = re.compile(pattern1)
            p = phone_list1.findall(example[index])
            for iNum in range(len(p)):
                print('电话: ',p[iNum])
                example[index] = example[index].replace(p[iNum], '****')

            print(example[index])


