import pymysql
def Db_Connect(host,user,passwd,db,port,charset):
    con = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset)
    cur = con.cursor()
    return cur