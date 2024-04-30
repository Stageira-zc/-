注：
在 Git Bash 下运行

curl -X POST  http://localhost:5000/books -d  '{"title": "1Q84", "author": "Haruki Murakami", "read": "true"}'   -H 'Content-Type: application/json'
curl -X POST http://localhost:5000/books  -H "Content-Type: application/json"
@REM 运行 Flask 服务端后，你可以在新的终端里测试 POST 路由：


