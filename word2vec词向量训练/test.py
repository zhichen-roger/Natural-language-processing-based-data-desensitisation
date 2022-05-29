from gensim.models import Word2Vec

zh_wiki_word2vec_model = Word2Vec.load('wiki.model')

testwords = ['孩子', '数学', '学术', '白痴', '篮球']
for i in range(5):
    res = zh_wiki_word2vec_model.wv.most_similar(testwords[i])
    print(testwords[i])
    print(res)