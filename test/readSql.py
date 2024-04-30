import json

import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='332412',
    database='book'
)

cursor = conn.cursor()
cursor.execute("select * from user")
json_data = '{"name": "jzc", "age": 30}'
json_str = json.dumps(json_data)

sql1 = "insert into user(json) values ({})".format(json_str)
# INSERT INTO user (json) VALUES ('{"name": "jzc", "age": 30}')

cursor.execute(sql1)
conn.commit()
cursor.close()
conn.close()

'''
json_data ='{"name": "jzc", "age": 30}'
json_str = json.dumps(json_data)

sql1 = "insert into user(json) values ('{}')".format(json_str)
INSERT INTO user (json) VALUES ('{"name": "jzc", "age": 30}')
sql1 = "INSERT INTO user (json) VALUES (json_str)" 为什么不行

在这个语句中，json_str 是一个 Python 变量名，它包含一个 JSON 格式的字符串。然而，在 SQL 语句中，json_str 是一个字符串字面量，而不是一个变量名。
因此，如果您执行这个语句，实际上会将字符串字面量 'json_str' 插入到 json 列中，而不是变量 json_str 中包含的 JSON 数据。

为了解决这个问题，您需要使用字符串格式化，将 json_str 变量的值插入到 SQL 语句中，而不是将字符串字面量 'json_str' 插入到 SQL 语句中。例如，您可以使用以下代码：



json_data = '{"name": "jzc", "age": 30}'
json_str = json.dumps(json_data)

sql1 = "INSERT INTO user (json) VALUES ('{}')".format(json_str)
在这个语句中，{} 表示一个占位符，它会被格式化字符串的 format() 方法替换为 json_str 变量的值。
因此，如果 json_str 的值为 {"name": "jzc", "age": 30}，则格式化后的 SQL 语句将变为：


INSERT INTO user (json) VALUES ('{"name": "jzc", "age": 30}')
在这个 SQL 语句中，json_str 变量的值被插入到 VALUES 子句中的引号中，形成了一个字符串字面量，这个字符串字面量包含了 json_str 变量中的 JSON 数据。

'''
