import os
import gensim
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import os.path
import sys
from gensim.corpora import WikiCorpus


inp = "./语料库/4.txt"

program = os.path.basename("训练模型")
logger = logging.getLogger(program)

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
# logger.info("running %s" % ' '.join(sys.argv))
model = Word2Vec(LineSentence(inp), size=200, window=20, min_count=1, iter=1000, hs=1, sg=0,
                 workers=multiprocessing.cpu_count())
#
model.save('two.model')

# my_model = gensim.models.Word2Vec.load("./first.model")

# a = my_model.wv.most_similar("pass", topn=1)
# print(len(a[0]))
# print(a[0])
#
# print(len(a[0][0]))
# print()
# print(a)