import re
from pymysql import *


def get_conn():
    conn = connect(host="192.168.173.100",
                    port=3306,
                    user="root",
                    passwd="12345678",
                    database="db1",
                    charset="utf8")

    return conn


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def test_get_values():
    conn = get_conn()
    cursor = conn.cursor()

    sql = "select * from test1"

    cursor.execute(sql)

    for line in cursor.fetchall():
        print(line)
    conn.commit()

    close_conn(conn, cursor)


def test_add_values():
    conn = get_conn()
    cursor = conn.cursor()

    for num in range(0, 1000000, 10000):
        for a in range(num, num + 10000):
            sql = "insert into test1(name, age) values ('b', %d)" % a
            cursor.execute(sql)
        conn.commit()

    close_conn(conn, cursor)


if __name__ == "__main__":
    test_add_values()
    test_get_values()