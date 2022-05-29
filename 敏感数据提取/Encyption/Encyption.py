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

nlp = StanfordCoreNLP('..\stanford\stanford-corenlp-latest\stanford-corenlp-full-2021-01-09', lang='zh')
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
            #splitTxt = resultTxt[index1].split('。')
            splitTxt = resultTxt[index1].split('#')
            for index2 in range(len(splitTxt)):
                splitTxtSpace.append(splitTxt[index2].strip())
        splitTxtSpace = [i for i in splitTxtSpace if (len(str(i)) != 0)]
        for index3 in range(len(splitTxtSpace)):
            if splitTxtSpace[index3] !='':
                #example.append(splitTxtSpace[index3]+'。')
                example.append(splitTxtSpace[index3])
        ### 脱敏
        for index in range(len(example)):
            Location=[]
            # 医院机构
            for yy in range(len(Hospital)):
                if example[index].find(Hospital[yy])!=-1:
                    print('医院名: '+Hospital[yy])
                    example[index]=example[index].replace(Hospital[yy], '****')
            # 姓名
            for iname in range(0, len(nlp.ner(example[index]))):
                if nlp.ner(example[index])[iname][1] == 'PERSON':
                    namestring = nlp.ner(example[index])[iname][0]
                    print('人名: ' + namestring)
                    example[index] = example[index].replace(namestring, '****')
            # 数字
            pattern1 = "(13\d{7,11}|14[5|7]\d{6,10}|15\d{7,11}|166\d{6,10}|17[3|6|7]\d{6,10}|18\d{7,11})"
            phone_list1 = re.compile(pattern1)
            p = phone_list1.findall(example[index])
            # p = re.match(phone_list1, example[index])
            # if p:
            for iNum in range(len(p)):
                print('手机号: ', p[iNum])
                example[index] = example[index].replace(p[iNum], '****')
            # 身份证号
            pattern2 = r"1[1,2,4,5]\d{13,17}x|1[1,2,4,5]\d{13,17}X|1[1,2,4,5]\d{14,18}|[2,3,4,5,6]\d{14,18}X|[2,3,4,5,6]\d{14,18}x|[2,3,4,5,6]\d{15,19}"
            # 字符串形式的正则表达式
            id_list1 = re.compile(pattern2)
            id = id_list1.findall(example[index])
            # 获取字符串
            for iId in range(len(id)):
                print('身份证号: ', id[iId])
                example[index] = example[index].replace(id[iId], '****')
            # 地点
            for i in range(0, len(nlp.ner(example[index]))):
                if nlp.ner(example[index])[i][1] == 'FACILITY':
                    Location.append(nlp.ner(example[index])[i][0])
                if nlp.ner(example[index])[i][1] == 'STATE_OR_PROVINCE' or nlp.ner(example[index])[i][1] == 'CITY' or nlp.ner(example[index])[i][1] == 'GPE' or nlp.ner(example[index])[i][1] == 'LOCATION':
                    Location.append(nlp.ner(example[index])[i][0])
            for iloction in range(len(Location)):
                print('地点: ',Location[iloction])
                example[index] = example[index].replace(Location[iloction], '****')
            f2 = open('../resulttxt/' + 'result_' + osfile[indexFile].split('.')[0] + ".txt", "w", encoding='utf-8')
            for line in range(len(example)):
                f2.write(example[line] + '\n')
            print('example' + osfile[indexFile].split('.')[0] + ".txt" + "保存成功")
            f2.close()
            print("okB")