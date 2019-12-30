#encoding=utf-8
import re
import jieba
import numpy as np
from gensim.models import word2vec
import up_and_low
import os
import db_connect
def Gensim_Search(text_url,keyword):
    if os.path.exists(text_url):
        pass
    else:
        text=''
        cur=db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
        sql='select keyword from job'
        cur.execute(sql)

        for i in (cur.fetchall()):
            text=text+str(i[0])
        with open(text_url,'w+',encoding='utf-8') as f:
            f.write(text)
    up_and_low.Up_And_Low(text_url)
    sentences=word2vec.Text8Corpus(text_url)
    model=word2vec.Word2Vec(sentences, size=200)
    model.save('./textmodel.model')
    try:
        most_similar_word=model.most_similar(keyword.upper())
        return most_similar_word
    except:
        return None
    #y2=model.similarity(u"网络", u"设计")
    #print(y2)
    #for i in model.most_similar(u"Flash设计师"):
    # print(i[0],i[1])



Gensim_Search('./福利.json','设计')
