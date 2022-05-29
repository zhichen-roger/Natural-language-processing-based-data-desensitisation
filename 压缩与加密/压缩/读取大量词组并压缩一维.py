import gensim
import numpy as np
from sklearn.decomposition import PCA
def load_txt_vec(file, threshold=0, dtype='float'):	# 读取txt文件格式的word2vec词向量
    print('读取词向量文件中......')
    header = file.readline().split(' ')
    count = int(header[0]) if threshold <= 0 else min(threshold, int(header[0]))
    dim = int(header[1])
    words = []
    matrix = np.empty((count, dim), dtype=dtype)
    for i in range(count):
        word, vec = file.readline().split(' ', 1)
        words.append(word)
        matrix[i] = np.fromstring(vec, sep=' ', dtype=dtype)
    return (words, matrix)

if __name__ == '__main__':
    result=[]
    try:
        w2v_txt_file = open('newsblogbbs.vec', 'r', encoding='utf-8', errors='surrogateescape')  # txt格式的词向量文件
        words, vectors = load_txt_vec(w2v_txt_file)  # 载入txt文件格式的word2vec词向量
        for i in range(len(vectors)):
            result.append(vectors[i][:4])
        # for r in range(len(result)):
        #     print(result[r])
        #print(result)
        X = np.array(result)
        pca = PCA(n_components=1)  # 降到1维
        pca.fit(X)  # 训练
        newX = pca.fit_transform(X)  # 降维后的数据
        f1 = open("middleyas.txt", "w", encoding='utf-8')
        for index in range(len(newX)):
             print(newX[index][0])
             f1.write(str(words[index])+'\n'+str(newX[index][0]) + '\n')
        #print(result)
        f1.close()
    except ImportError as ex:
        print('Please install gensim, sklearn, numpy, matplotlib, and scipy to show embeddings.')
        print(ex)