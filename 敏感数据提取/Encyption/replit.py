from docx import Document
import  re
import os
osfile = []
dir = r"D:\pythonProjectEncryption\Encyption"
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.split('.')[1] == 'txt' and file != 'yiyuan.txt':
            osfile.append(file)

for indexFile in range(len(osfile)):
    splitTxtSpace=[]
    txtcontext=[]
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
                txtcontext.append(splitTxtSpace[index3]+'。')
        for index4 in range(len(txtcontext)):
            print(txtcontext[index4])

        f2 = open('../resulttxt/' + 'result_' + osfile[indexFile].split('.')[0] + ".txt", "w", encoding='utf-8')
        for line in range(len(txtcontext)):
            f2.write(txtcontext[line] + '\n')
        print('example' + osfile[indexFile].split('.')[0] + ".txt" + "保存成功")
        f2.close()
        print("okB")