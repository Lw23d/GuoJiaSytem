from pymysql import *

#创建数据库连接
conn=connect(host='localhost',user='root',password='Lyb15260072876',database='project',port=3306)
#创建游标
cursor=conn.cursor()

#写入数据
def querys(sql,params):
    params=tuple(params)
    cursor.execute(sql,params)
    conn.commit()
