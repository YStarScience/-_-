#coding=utf-8
import jieba
import re
import json
import time
import ast
from collections import Counter
#[ [分词1],[分词2] ]
def Welf_Divide(welf_list):
    jieba.load_userdict('welf_word.txt')
    res=[]

    for i in welf_list:
        i=re.sub('五险一金补充|五险|一金','五险一金',i)
        res.append(jieba.cut(i))
    return res

#[ (词,词频),(词,词频) ]
def Count_Num(welf_list,welfare_num):
    jieba.load_userdict('welf_word.txt')
    text=''
    for i in welf_list:
        text=text+i
    text=re.sub('五险一金补充|五险|一金','五险一金',text)
    res=[]
    res=jieba.cut(text)

    return Counter(res).most_common(int(welfare_num))

def Divide():
    text=''
    with open('./福利.json','r',encoding='utf-8') as f:
        text=f.read()
        text=re.sub('},{','}-!-!-{',text)
    with open('./福利.json','w+',encoding='utf-8') as f:
        f.write(text)

    res=re.findall('{.*}',text)[0].split('-!-!-')
    welf_list=[]
    for i in res:
        #time.sleep(30)
        try:
            data=json.loads(i)
            welf_list.append(data['公司待遇特色'])
        except:
            pass
    return welf_list


def Welf_Re(welfare_num):
    welf_list = Divide()
    res = Count_Num(welf_list,welfare_num)

    return res

def Welf_Search(welfare_num):
    num=0
    data_list=[]
    res = Welf_Re(welfare_num)

    for i in res:
        num+=i[1]

    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    print(data_list)
    return data_list



