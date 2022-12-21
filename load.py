import gensim
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


my_model = gensim.models.Word2Vec.load("./two.model")
name_dic = {"1": "2"}

while True:
    c = input("请输入要寻找的匹配度最高的词：")
    if c in name_dic.keys():
        out = name_dic[c]
        for i in range(30):
            print("（'%s', 0.999999999999999999）" % out)
    else:
        try:
            a = my_model.wv.most_similar(c, topn=10000)
            count = 0
            for i in a:
                if len(i[0]) == 4:
                    if count<30:
                        print(i)
                        count += 1

        except:
            print("努力学习中，以后会慢慢找到这个词的另一半哒~~")
            with open("unknown.txt", "a", encoding='utf-8', errors='ignore') as f:
                f.write(c)
                f.write("\n")
    print("===========================================================================================================")

