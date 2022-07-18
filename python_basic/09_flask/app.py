#Django는 프레임워크라서 스프링느낌, flask는 가벼운 테스트느낌 (약간 JSP같은느낌 )
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/') #호출할때 동작할 함수
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return 'user 호출!!'

@app.route('/user/<username>/<int:age>')  #url뒤에 값을 넣어 보내기: 매개변수 선언에서 받아서 써야함. int 안써주면 기본은 string으로 받아짐
def user_1(username, age):
    return f'{username}고객님의 나이는 {age+1}살 입니다.'

#get방식으로 request활용해서 받아오기
@app.route('/customer') #get방식으로 /customer?user=ahra&age=22 이런식으로 주소창에 써주면 됨.
def customer():
    print('name:', request.args.get('user'))
    print('age:', request.args.get('age'))
    return "customer 호출"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("form_input.html")
    else: #post방식일 때 
        #return f"로그인: {request.form['username']} {request.form['password']}"
        return render_template("form_result.html", result=request.form)

@app.route('/fileupload', methods=['GET', 'POST'])
def fileupload():
    if request.method == 'GET':
        return render_template('fileupload.html')
    else:
        f = request.files['file']
        path = os.path.dirname(__file__)+ '/upload/' + f.filename
        print(path)
        f.save(path)
        return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

