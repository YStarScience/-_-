def Money_Int(result_list):#[(),()]
    res=[]
    for i in range(len(result_list)):
        money=0
        # print(result_list[i][2])
        # print(type(result_list[i][2]))
        if len(result_list[i][2].split('万/月'))==2 or len(result_list[i][2].split('万以上/月'))==2 :
            try:
                money=(int(float(result_list[i][2].split('万/月')[0])*10000*12))
            except:
                money=(int(float(result_list[i][2].split('万以上/月')[0])*10000))
        elif len(result_list[i][2].split('万/年'))==2 or len(result_list[i][2].split('万以上/年'))==2:
            try:
                money=(int(float(result_list[i][2].split('万/年')[0])*10000))
            except:
                money=(int(float(result_list[i][2].split('万以上/年')[0])*10000))
        elif len(result_list[i][2].split('千/月')) == 2 or len(result_list[i][2].split('千以上/月')) == 2:
            try:
                money=(int(float(result_list[i][2].split('千/月')[0]) * 1000 * 12))
            except:
                money=(int(float(result_list[i][2].split('千以上/月')[0]) * 10000))
        elif len(result_list[i][2].split('千/年')) == 2 or  len(result_list[i][2].split('千以上/月')) == 2:
            try:
                money=(int(float(result_list[i][2].split('千/年')[0]) * 1000))
            except:
                money=(int(float(result_list[i][2].split('千以上/年')[0])*10000))
        elif len(result_list[i][2].split('元/天')) ==2:
            money=(int(float(result_list[i][2].split('元/天')[0])*30*12))
        elif len(result_list[i][2].split('元/小时')) == 2:
            money = (int(float(result_list[i][2].split('元/小时')[0]) *24 * 30 * 12))
        res.append((result_list[i][0],money))

    return sorted(res,key=lambda money:money[1],reverse=True)
