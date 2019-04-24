# @Time      : 2019.04.18
# @Author    : kawa Yeung
# @Licence   : MIT
# @function  : database tests


from db.utils import conn


if __name__=="__main__":
    sql = "select * from test_conn"
    cur = conn.cursor()
    r = cur.execute(sql)
    r = cur.fetchall()
    print(r)
    cur.close()
    conn.close()
