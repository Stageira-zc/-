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
# 字典的基本操作

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {

        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {

        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]
# print(book['title'], '\t',book['author'], '\t',book['read'], '\t')
# 备份表的内容
# cursor.execute('TRUNCATE TABLE book_backup')
# cursor.execute('SELECT * INTO book_backup FROM books;')
# 清空当前表

# 更新表格内容
cursor.execute('TRUNCATE TABLE book_backup')
cursor.execute('INSERT INTO book_backup SELECT * FROM books;')
cursor.execute('TRUNCATE TABLE books')
for book in BOOKS:
    sql_title = "INSERT INTO books(title,author,is_read) VALUES (%s,%s,%s)"
    cursor.execute(sql_title, (book['title'], book['author'], book['read']))

conn.commit()
cursor.close()
conn.close()
