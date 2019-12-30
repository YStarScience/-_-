import jieba
import db_connect
import re
import time
from gensim import corpora,models,similarities
size0=200
size1=100
size2=50
yy=200
yy1=250
def Resume(place,major,text):
    if text!='':
        cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
        sql = "select distinct title,company,least_money,most_money,keyword,info from job where keyword like '%" + major + "%' or info like '%" + major + "%' or title like '%" + major + "%'  and place_province like '%" + place +"%' or place_city like '%" + place +"%' limit 100"

        cur.execute(sql)
        #resume是添加交集功能，
        data = cur.fetchall()

        doc_test=text
        #print(doc0,doc1,doc_test)
        all_doc_chara=[]
        all_doc=[]
        try:
            for i in data:
                all_doc.append(i[0]+'-!-!-'+i[1]+'-!-!-'+i[2]+'-!-!-'+i[3]+'-!-!-'+i[4].split(' ')[5])
                all_doc_chara.append("".join(re.sub(',|!|\?','',i[0].upper()))+"".join(re.sub(',|!|\?| ',' ',i[5].upper())))
        except:
            pass


        all_doc_list=[]
        for doc in all_doc_chara:
            doc_list=[word for word in jieba.cut(doc)]
            all_doc_list.append(doc_list)

        #print(all_doc_list)#原文本的分词列表
        doc_test_list=[word for word in jieba.cut(doc_test)]

        #print(doc_test_list)#测试文本的分词列表
        dictionary=corpora.Dictionary(all_doc_list)
        #print(dictionary.keys())#原文本的字典键
        #print(dictionary.token2id)#原文本键键名对应
        corpus=[dictionary.doc2bow(doc) for doc in all_doc_list]
        #print(corpus)#原文本键和出现次数[[(),()],[(),()]]
        doc_test_vec=dictionary.doc2bow(doc_test_list)
        #print(doc_test_vec)
        tfidf=models.TfidfModel(corpus)#不同的转化需要不同的参数，在TF-IDF转化中，训练的过程就是简单的遍历训练语料库(corpus)，然后计算文档中每个特征的频率。
        #找到有特征性的词作为区分的标准，tf计算是局部的，idf计算是全局的
        #tf-idf算法是创建在这样一个假设之上的：对区别文档最有意义的词语应该是那些在文档中出现频率高，而在整个文档集合的其他文档中出现频率少的词语
        #但是在本质上idf是一种试图抑制噪声的加权，并且单纯地认为文本频率小的单词就越重要，文本频率大的单词就越无用，显然这并不是完全正确的。idf的简单结构并不能有效地反映单词的重要程度和特征词的分布情况，使其无法很好地完成对权值调整的功能，所以tf-idf法的精度并不是很高。
        index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=len(dictionary.keys()))

        sim=index[tfidf[doc_test_vec]]
        # print(sim)
        res=sorted(enumerate(sim),key=lambda item:-item[1])
        res_list=[]
        child_res_dict={}
        child_res_dict['node']=[]
        child_res_dict['link']=[]
        print(res)
        # print(len(res))
        if len(res) <= 5:
            cou_num = 1
            for i in range(0,len(res)):

                if res[i][1] > 0.005:
                    node_dict1 = {'name': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                  'value': '%.2f' % (res[i][1] * 1000), 'x': (cou_num + 1) * 10, 'y': 200,
                                  'symbolSize': size1,
                                  'label': {'normal': {'position': 'inside', 'fontSize': 10, 'color': '#FF6633'}},
                                  "draggable": "true"}

                    node_dict2 = {'name': '序号:' + str(i) + ',职位名:' + all_doc[res[i][0]].split('-!-!-')[0] + ',工资区间:' + \
                                          all_doc[res[i][0]].split('-!-!-')[2] + '-' + \
                                          all_doc[res[i][0]].split('-!-!-')[3],
                                  'value': '%.2f' % (res[i][1] * 1000), 'x': (cou_num + 1) * 10, 'y': 200,
                                  'symbolSize': size2,
                                  'label': {'normal': {'position': 'inside', 'fontSize': 10, 'color': '#FF6633'}},
                                  "draggable": "true"}

                    # node_dict3 = {'name': '序号:' + str(i) + ',关键词:' + all_doc[res[i][0]].split('-!-!-')[4],
                    #               'value': '%.2f' % (res[i][1] * 1000), 'x': (cou_num + 1) * 10, 'y': 200,
                    #               'symbolSize': size2,
                    #               'label': {'normal': {'position': 'inside', 'fontSize': 10, 'color': '#FF6633'}},
                    #               "draggable": "true"}
                    cou_num += 3

                    child_res_dict['node'].append(node_dict1)
                    child_res_dict['node'].append(node_dict2)
                    # child_res_dict['node'].append(node_dict3)

                    link_dict1 = {'source': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                  'target': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                  'name': '', 'value': '', 'label': '',
                                  'lineStyle': {"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}}
                    link_dict2 = {'source': '序号:' + str(i) + ',职位名:' + all_doc[res[i][0]].split('-!-!-')[0] + ',工资区间:' + \
                                            all_doc[res[i][0]].split('-!-!-')[2] + '-' + \
                                            all_doc[res[i][0]].split('-!-!-')[3],
                                  'target': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                  'name': '', 'value': '', 'label': '',
                                  'lineStyle': {"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}}
                    # link_dict3 = {'source': '序号:' + str(i) + ',关键词:' + all_doc[res[i][0]].split('-!-!-')[4],
                    #               'target': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                    #               'name': '', 'value': '', 'label': '',
                    #               'lineStyle': {"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}}

                    child_res_dict['link'].append(link_dict1)
                    child_res_dict['link'].append(link_dict2)
                    # child_res_dict['link'].append(link_dict3)

            child_res_dict['node'].append({'name': '分析结果', 'value': '', 'x': 10, 'y': 200, 'symbolSize': size0,
                                           'label': {'normal': {'position': 'inside', 'fontSize': 14, 'color': '#FF6633'}},
                                           "draggable": "true"})
            copy_list = child_res_dict['link'].copy()
            for j in range(0, len(copy_list), 3):
                child_res_dict['link'].append({'source': copy_list[j]['source'],
                                               'target': child_res_dict['node'][len(child_res_dict['node']) - 1]['name'],
                                               'name': '', 'value': '', 'label': '', 'lineStyle': {
                        "normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}})
            res_list.append(child_res_dict)
        else:
            cou_num = 1
            for i in range(0,8):

                if res[i][1] > 0.005:
                    node_dict1 = {'name': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                      'value': '%.2f' % (res[i][1] * 1000), 'x': (cou_num+1)*10, 'y': 200,
                                      'symbolSize': size1,
                                      'label': {'normal': {'position': 'inside', 'fontSize': 10, 'color': '#FF6633'}},
                                      "draggable": "true"}

                    node_dict2 = {'name': '序号:' + str(i) + ',职位名:' + all_doc[res[i][0]].split('-!-!-')[0] + ',工资区间:' + \
                                         all_doc[res[i][0]].split('-!-!-')[2] + '-' + \
                                         all_doc[res[i][0]].split('-!-!-')[3],
                                      'value': '%.2f' % (res[i][1] * 1000), 'x': (cou_num + 1) * 10, 'y': 200,
                                      'symbolSize': size2,
                                      'label': {'normal': {'position': 'inside', 'fontSize': 10, 'color': '#FF6633'}},
                                      "draggable": "true"}


                    # node_dict3 = {'name': '序号:' + str(i) + ',关键词:' + all_doc[res[i][0]].split('-!-!-')[4],
                    #                   'value': '%.2f' % (res[i][1] * 1000), 'x': (cou_num + 1) * 10, 'y': 200,
                    #                   'symbolSize': size2,
                    #                   'label': {'normal': {'position': 'inside', 'fontSize': 10, 'color': '#FF6633'}},
                    #                   "draggable": "true"}
                    cou_num += 3

                    child_res_dict['node'].append(node_dict1)
                    child_res_dict['node'].append(node_dict2)
                    # child_res_dict['node'].append(node_dict3)




                    link_dict1 = {'source':'序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                        'target': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                        'name': '', 'value': '', 'label': '','lineStyle':{"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}}
                    link_dict2 = {'source': '序号:' + str(i) + ',职位名:' + all_doc[res[i][0]].split('-!-!-')[0] + ',工资区间:' + \
                                         all_doc[res[i][0]].split('-!-!-')[2] + '-' + \
                                         all_doc[res[i][0]].split('-!-!-')[3],
                                          'target': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                          'name': '', 'value': '', 'label': '','lineStyle':{"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}}
                    link_dict3 = {'source': '序号:' + str(i) + ',关键词:' + all_doc[res[i][0]].split('-!-!-')[4],
                                          'target': '序号:' + str(i) + ',公司名:' + all_doc[res[i][0]].split('-!-!-')[1],
                                          'name': '', 'value': '', 'label': '','lineStyle':{"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}}



                    child_res_dict['link'].append(link_dict1)
                    child_res_dict['link'].append(link_dict2)
                    child_res_dict['link'].append(link_dict3)

            child_res_dict['node'].append({'name': '分析结果', 'value': '', 'x': 10, 'y': 200, 'symbolSize': size0,
                                           'label': {'normal': {'position': 'inside', 'fontSize': 14, 'color': '#FF6633'}},
                                           "draggable": "true"})
            copy_list = child_res_dict['link'].copy()
            for j in range(0, len(copy_list), 3):
                child_res_dict['link'].append({'source': copy_list[j]['source'],
                                               'target': child_res_dict['node'][len(child_res_dict['node']) - 1]['name'],
                                               'name': '', 'value': '', 'label': '','lineStyle':{"normal": {"width": 2.0, "curveness": 0.2, "color": '#FF6633'}}})
            res_list.append(child_res_dict)



        return res_list
    else:
        return []



