from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# 后端与数据库链接
import pymysql

# 创建数据库连接
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='332412',
#     database='book'
# )
# cursor = conn.cursor()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# @app.route('/books',methods=['GET'])
# def all_books():
#     return jsonify({
#         'status':'success',
#         'books':BOOKS,
#
#     })
# 更新路由以处理添加新书的Post请求
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added'



    else:
        response_object['books'] = BOOKS

        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='332412',
            database='book'
        )
        cursor = conn.cursor()


        cursor.execute('TRUNCATE TABLE book_backup')
        cursor.execute('INSERT INTO book_backup SELECT * FROM books;')
        cursor.execute('TRUNCATE TABLE books')
        for book in BOOKS:
            sql_title = "INSERT INTO books(title,author,is_read) VALUES (%s,%s,%s)"
            cursor.execute(sql_title, (book['title'], book['author'], book['read']))

        conn.commit()
        cursor.close()
        conn.close()
    return jsonify(response_object)


#
@app.route('/books/<books_id>', methods=['PUT', 'DELETE'])
def single_book(books_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(books_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(books_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


# @app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
# def single_book(book_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book updated!'
#     if request.method == 'DELETE':
#         remove_book(book_id)
#         response_object['message'] = 'Book removed!'
#     return jsonify(response_object)


if __name__ == '__main__':
    app.run()
