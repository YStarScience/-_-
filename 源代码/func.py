'''
企业对大数据要求最迫切的前十名招聘职位
大数据职位需求量最高的前10名城市
大数据职位需求量最高的前10大行业（如互联网、金融、电子商务等）
计算机相关专业技能需求前10名。
计算机专业薪水最高的前10名招聘职位
企业对哪类大数据人才需求最为迫切（大数据分析师、大数据架构师等等）
'''
#coding=utf-8
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
import gensim_search
import welf_search
import db_connect
import money_int
import money_least
import money_most
import resume

app = Flask(__name__)
CORS(app)
@app.route('/zhuanye/<var>',methods=['POST','GET'])
def to_zhuanye_page(var):
    return render_template('/zhuanye/'+var)
@app.route('/xuqiu/<var>',methods=['POST','GET'])
def to_xuqiu_page(var):
    return render_template('/xuqiu/'+var)
@app.route('/salary/<var>',methods=['POST','GET'])
def to_salary_page(var):
    return render_template('/salary/'+var)
@app.route('/<var>',methods=['POST','GET'])
def to_new_page(var):
    return render_template(var)
@app.route('/articles/<var>', methods=['POST', 'GET'])
def to_articles_page(var):
    return render_template('/articles/' + var)
###########################################################
#职位名，薪水
@app.route('/zhuanye/ruanjiankaifa',methods=['GET','POST'])
def query_major_rk():
    sql='SELECT TITLE,COUNT(TITLE),MOST_MONEY\
        from job\
        where info like "%软件开发%"\
        group by title having count(*) > 0\
        ORDER BY COUNT(title) DESC\
        LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)

    data_list = []
    res = list(cur.fetchall())
    res_sorted_by_money=money_int.Money_Int(res)
    for i in range(len(res_sorted_by_money)):
        data_list.append({'name': res_sorted_by_money[i][0], 'value': (int(res_sorted_by_money[i][1]/1000/12))})
    print(jsonify(data_list))
    return jsonify(data_list)
@app.route('/zhuanye/ruanjianceshi',methods=['GET','POST'])
def query_major_rc():

    sql='SELECT TITLE,COUNT(TITLE),MOST_MONEY\
        from job\
        where info like "%软件测试%"\
        group by title having count(*) > 0 \
        ORDER BY COUNT(title) DESC\
        LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    res_sorted_by_money = money_int.Money_Int(res)
    for i in range(len(res_sorted_by_money)):
        data_list.append({'name': res_sorted_by_money[i][0], 'value':(int(res_sorted_by_money[i][1] / 1000 / 12))})
    print(jsonify(data_list))
    return jsonify(data_list)


@app.route('/zhuanye/wangluoanquan',methods=['GET','POST'])
def query_major_wa():

    sql='SELECT TITLE,COUNT(TITLE),MOST_MONEY\
        from job\
        where info like "%网络安全%"\
        group by title having count(*) > 0\
        ORDER BY COUNT(title) DESC\
        LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    res_sorted_by_money = money_int.Money_Int(res)
    for i in range(len(res_sorted_by_money)):
        data_list.append({'name': res_sorted_by_money[i][0], 'value': (int(res_sorted_by_money[i][1] / 1000 / 12))})
    print(jsonify(data_list))
    return jsonify(data_list)


@app.route('/zhuanye/dianzishangwu',methods=['GET','POST'])
def query_major_ds():

    sql ='SELECT TITLE,COUNT(TITLE),MOST_MONEY\
        from job\
        where info like "%电子商务%"\
        group by title having count(*) > 0\
        ORDER BY COUNT(title) DESC\
        LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    res_sorted_by_money = money_int.Money_Int(res)
    for i in range(len(res_sorted_by_money)):
        data_list.append({'name': res_sorted_by_money[i][0], 'value': (int(res_sorted_by_money[i][1] / 1000 / 12))})
    print(jsonify(data_list))
    return jsonify(data_list)


@app.route('/zhuanye/tongxinyuanli',methods=['GET','POST'])
def query_major_tx():

    sql ='SELECT TITLE,COUNT(TITLE),MOST_MONEY\
            from job\
            where info like "%通信原理%" and title like "%通信%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    res_sorted_by_money = money_int.Money_Int(res)
    for i in range(len(res_sorted_by_money)):
        data_list.append({'name': res_sorted_by_money[i][0], 'value': (int(res_sorted_by_money[i][1] / 1000 / 12))})
    print(jsonify(data_list))
    return jsonify(data_list)


@app.route('/zhuanye/duomeitijishu',methods=['GET','POST'])
def query_major_dmt():

    sql = 'SELECT TITLE,COUNT(TITLE),MOST_MONEY\
            from job\
            where info like "%多媒体技术%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    res_sorted_by_money = money_int.Money_Int(res)
    for i in range(len(res_sorted_by_money)):
        data_list.append({'name': res_sorted_by_money[i][0], 'value': (int(res_sorted_by_money[i][1] / 1000 / 12))})
    print(jsonify(data_list))
    return jsonify(data_list)




###########################################################
#职位名，需求量百分比
@app.route('/xuqiu/ruanjiankaifa',methods=['GET','POST'])
def query_demand_rk():

    sql = 'SELECT TITLE,COUNT(TITLE)\
            from job\
            where info like "%软件开发%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)


@app.route('/xuqiu/ruanjianceshi',methods=['GET','POST'])
def query_demand_rc():
    sql =  'SELECT TITLE,COUNT(TITLE)\
            from job\
            where title like "%测试%"\
            group by title having count(*) > 0 \
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)


@app.route('/xuqiu/wangluoanquan',methods=['GET','POST'])
def query_demand_wa():
    sql = 'SELECT TITLE,COUNT(TITLE)\
            from job\
            where info like "%网络安全%" or title like "%网络"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)


@app.route('/xuqiu/dianzishangwu',methods=['GET','POST'])
def query_demand_ds():
    sql = 'SELECT TITLE,COUNT(TITLE)\
            from job\
            where info like "%电子商务%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
                '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)


@app.route('/xuqiu/tongxinyuanli',methods=['GET','POST'])
def query_demand_tx():
    sql = 'SELECT TITLE,COUNT(TITLE)\
            from job\
            where info like "%通信原理%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)



@app.route('/xuqiu/duomeitijishu',methods=['GET','POST'])
def query_demand_dmt():
    sql = 'SELECT TITLE,COUNT(TITLE)\
            from job\
            where info like "%多媒体%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)





#########################################################
#职位名，需求量
@app.route('/position',methods=['GET','POST'])
def query_position():
    sql =  'SELECT title,COUNT(title) as titlenum\
            FROM job\
            WHERE info LIKE "%大数据%"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict={}
    data_dict['names']=[]
    data_dict['values']=[]
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_dict['names'].append(res[i][0])
    for i in range(len(res)):
        data_dict['values'].append(int((res[i][1])))
    # print(data_dict)
    return jsonify(data_dict)



#########################################################
#城市名，需求量
@app.route('/city',methods=['GET','POST'])
def query_city():
    sql = 'SELECT place_province,count(place_province) as num\
            FROM job\
            WHERE info LIKE "%大数据%"\
            group by place_province having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
    '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list = []
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name': res[i][0], 'value': int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)



#########################################################
#专业名，需求量
@app.route('/talents',methods=['GET','POST'])
def query_talents():
    sql = 'SELECT title,COUNT(title) as titlenum\
            FROM job\
            WHERE info LIKE "%大数据%" and title LIKE "%师"\
            group by title having count(*) > 0\
            ORDER BY COUNT(title) DESC\
            LIMIT 10\
        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    data_dict['names'] = []
    data_dict['values'] = []
    data_dict['extra']=[]
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_dict['names'].append({"name": res[i][0]})
        data_dict['extra'].append(res[i][0])
    for i in range(len(res)):
        data_dict['values'].append(int((res[i][1])))
    # print(data_dict)
    return jsonify(data_dict)

#########################################################
#职位名，百分比
@app.route('/welfare',methods=['GET','POST'])
def query_welfare():
    if request.method=='POST':
        welfare_num=request.form.get('welfare_num')

    elif request.method=='GET':
        welfare_num = request.args.get('welfare_num')
    print(jsonify(welf_search.Welf_Search(welfare_num)))
    return jsonify({'data':(welf_search.Welf_Search(welfare_num))})



#########################################################
#地区，最低，最高，
@app.route('/salary/beijing',methods=['GET','POST'])
def query_salary_bj():
    sql = 'SELECT  place_city,least_money,most_money\
                FROM job\
                WHERE place_province="北京" AND place_city!="北京"\
                    '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same=[]

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1=[]
    res_fi2=[]

    for i in res_sorted_by_least:
            if i["地区名"] not in is_not_same:
                is_not_same.append(i["地区名"])
                res_fi1.append({"地区名":i["地区名"],"最低工资":i["最低工资"]})
    is_not_same=[]
    for i in res_sorted_by_most:
            if i["地区名"] not in is_not_same:
                is_not_same.append(i["地区名"])
                res_fi2.append({"地区名":i["地区名"],"最高工资":i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"]=res_fi2[i]["最高工资"]
    #{'numsh':[最高],'numsl':[最低],'names':[名称]}
    data_dict['numsh']=[]
    data_dict['numsl']=[]
    data_dict['names']=[]
    for i in range(len(res_fi1)):

        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    data_dict['names'].remove('昌平区')
    del data_dict['numsh'][5]
    del data_dict['numsl'][5]
    print(data_dict)

    return jsonify(data_dict)


@app.route('/salary/chongqing',methods=['GET','POST'])
def query_salary_cq():
    sql = 'SELECT DISTINCT place_city,least_money,most_money\
                 FROM job\
                 WHERE place_province="重庆" AND place_city!="重庆"\
                     '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)

@app.route('/salary/fujian',methods=['GET','POST'])
def query_salary_fj():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="福建" AND place_city!="福建"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)



@app.route('/salary/hebei',methods=['GET','POST'])
def query_salary_hb():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="河北" AND place_city!="河北"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)


#没数据
@app.route('/salary/hunan',methods=['GET','POST'])
def query_salary_hn():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="湖南" AND place_city!="湖南"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)


#没数据
@app.route('/salary/jiangsu',methods=['GET','POST'])
def query_salary_js():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="江苏" AND place_city!="江苏"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)


#？
@app.route('/salary/shandong',methods=['GET','POST'])
def query_salary_sd():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="山东" AND place_city!="山东"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)


#？
@app.route('/salary/shanghai',methods=['GET','POST'])
def query_salary_sh():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="上海" AND place_city!="上海"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)


#？
@app.route('/salary/zhejiang',methods=['GET','POST'])
def query_salary_zj():
    sql = 'SELECT  place_city,least_money,most_money\
                    FROM job\
                    WHERE place_province="浙江" AND place_city!="浙江"\
                        '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_dict = {}
    res = list(cur.fetchall())
    is_not_same = []

    res_sorted_by_least = money_least.Money_Least(res)
    res_sorted_by_most = money_most.Money_Most(res)

    res_fi1 = []
    res_fi2 = []

    for i in res_sorted_by_least:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi1.append({"地区名": i["地区名"], "最低工资": i["最低工资"]})
    is_not_same = []
    for i in res_sorted_by_most:
        if i["地区名"] not in is_not_same:
            is_not_same.append(i["地区名"])
            res_fi2.append({"地区名": i["地区名"], "最高工资": i["最高工资"]})

    for i in range(len(res_fi1)):
        res_fi1[i]["最高工资"] = res_fi2[i]["最高工资"]

    data_dict['numsh'] = []
    data_dict['numsl'] = []
    data_dict['names'] = []
    for i in range(len(res_fi1)):
        data_dict['numsh'].append(res_fi1[i]['最高工资'])
        data_dict['numsl'].append(res_fi1[i]['最低工资'])
        data_dict['names'].append(res_fi1[i]['地区名'])
    # print(data_dict)
    return jsonify(data_dict)


#####################################################
#省，需求量
@app.route('/location',methods=['GET','POST'])
def query_location():
    sql = 'SELECT DISTINCT place_province,count(place_province)\
             FROM job\
             group by place_province having count(*) > 0\
            '
    cur = db_connect.Db_Connect(host='localhost', user='root', passwd='1234', db='51job', port=3306, charset='utf8')
    cur.execute(sql)
    data_list=[]
    res = list(cur.fetchall())
    num = 0
    for i in range(len(res)):
        num += res[i][1]
    for i in range(len(res)):
        data_list.append({'name':res[i][0],'value':int((res[i][1]))})
    # print(data_dict)
    return jsonify(data_list)
#####################################################

#职业名&具体信息，匹配度
@app.route('/resume/',methods=['GET','POST'])
def query_keyword():
    if request.method=='POST':
        select1 = request.form.get('select1')
        select2 = request.form.get('select2')
        textArea1=request.form.get('textArea1')

    elif request.method=='GET':
        select1 = request.args.get('select1')
        select2 = request.args.get('select2')
        textArea1=request.args.get('textArea1')
    print(select1,select2,textArea1)
    res=resume.Resume(select1,select2,textArea1)


    return jsonify(res)

#简历，正则，词云
if __name__=='__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()

