import pymysql


# 创建数据库连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='332412',
    database='book'
)
try:
    # 测试连接状态
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        if result and result[0] == 1:
            print("pymysql数据库连接成功！")
        else:
            print("pymysql数据库连接失败！")

except Exception as e:
    print("pymysql数据库连接异常：", e)

finally:
    # 关闭数据库连接
    conn.close()
