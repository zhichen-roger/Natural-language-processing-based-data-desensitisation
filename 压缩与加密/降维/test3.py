import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import gensim
import matplotlib as mpl

# 若要显示中文字体则取消注释下面两行
# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定中文字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def plot_with_labels(low_dim_embs, labels, filename):   # 绘制词向量图
    assert low_dim_embs.shape[0] >= len(labels), 'More labels than embeddings'
    print('绘制词向量中......')
    plt.figure(figsize=(10, 10))  # in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)	# 画点，对应low_dim_embs中每个词向量
        plt.annotate(label,	# 显示每个点对应哪个单词
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.savefig(filename)
    plt.show()

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

def load_bin_vec(frame):	# 读取bin文件格式的word2vec词向量,读取速度较慢，请耐心等待
    print('读取词向量文件中......')
    k = 0
    word_vecs = []
    words = []
    model = gensim.models.KeyedVectors.load_word2vec_format(frame, binary=True)
    vec_vocab = model.vocab
    for word in vec_vocab:
        embedding = model[word]
        word_vecs.append(embedding)
        words.append(word)
        k += 1
        if k % 10000 == 0:
            print("load_bin_vec %d" % k)
    return words, word_vecs

if __name__ == '__main__':
    try:
        # 若要载入txt文件格式的word2vec词向量，则执行下面这两行
        w2v_txt_file = open('v7_EN.vec', 'r',encoding='utf-8', errors='surrogateescape')	# txt格式的词向量文件
        words, vectors = load_txt_vec(w2v_txt_file)	# 载入txt文件格式的word2vec词向量
        # 若要载入bin文件格式的word2vec词向量，则执行下面这两行，并注释上面两行
        # w2v_bin_file = 'GoogleNews-vectors-negative300.bin'	# bin格式的词向量文件
        # words, vectors = load_bin_vec(w2v_bin_file)	# 载入bin文件格式的word2vec词向量
        tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000, method='exact')
        plot_only = 100	# 限定画点（词向量）的个数，只画词向量文件的前plot_only个词向量
        low_dim_embs = tsne.fit_transform(vectors[:plot_only]) # 需要显示的词向量，一般比原有词向量文件中的词向量个数少，不然点太多，显示效果不好
        labels = [words[i] for i in range(plot_only)] # 要显示的点对应的单词列表
        plot_with_labels(low_dim_embs, labels, 'w2v.png')

    except ImportError as ex:
        print('Please install gensim, sklearn, numpy, matplotlib, and scipy to show embeddings.')
        print(ex)

