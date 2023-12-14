from db_operations import db_query



def insert_sql(parm):
    sql = " insert into soft (soft) values (QUOTE("+parm+")) "
    con_mysql(sql)

def check_sql(parm):
    sql = " select num1 from soft where soft = QUOTE('"+parm+"')  "
    return con_mysql_result(sql)


def insert_ip(parm, parm1, parm2):
    sql = " insert into ip (id, ip, domain) values ( "+parm+" , '"+parm1+"', '"+parm2+"') "
    return con_mysql(sql)

def con_mysql_result(sql):
    ConMysql = db_query('mysql', '127.0.0.1', 3306, 'root', '123456', 'softlist')
    db_query.con_ok(ConMysql)
    return db_query.con_res(ConMysql, sql)

def con_mysql(sql):
    # 连接oracle获得oa的数据
    ConMysql = db_query('mysql', '127.0.0.1', 3306, 'root', '123456', 'softlist')
    db_query.con_ok(ConMysql)
    db_query.con_exe(ConMysql, sql)