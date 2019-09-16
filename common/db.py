# coding:utf-8
#heboqiang
import pymysql


# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host='115.28.108.130',
                           port=3306,
                           user='test',
                           passwd='123456',  # passwd 不是 password
                           db='api_test',
                           charset='utf8')  # 如果查询有中文，需要指定测试集编码

    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    conn.commit()
    result = cur.fetchone()  # 获取所有查询结果
    print(result)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果


# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接0 

# 封装常用数据库操作
def check_user(user,name):
    # 注意sql中''号嵌套的问题
    sql = "select * from user =  '{}' where name = '{}'".format(user).format(name)
    result = query_db(sql)
    return True if result else False


def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql)


def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    change_db(sql)


