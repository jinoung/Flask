from bbs import app
from flask import g, Response, request, make_response, render_template
from datetime import datetime, date
import json


# JSON 데이터 파일 입출력
character = {
    "name" : "김진영",
    "age" : 52,
    "item" : ["파이선", "플라스크", "장고"],
    "kids" : ["김아진", "김아현", "김아현"],
    "wife" : ["장희정", "남규리", "손예진"]
}

@app.route('/jsondump')
def jsondump():
    with open('bbs/static/data.txt', 'w', encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii=False, indent='\t')
    return "JSON데이타 파일로 dump하기"

@app.route('/jsonload')
def jsonload():
    with open('bbs/static/data.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(type(character))
        print(character)
    return "JSON데이타 파일에서 loads하기"

# Request GET/POST와 POST데이터 파일로 입출력하기
# @app.route('/hello')
# def hellohtml():
#     return render_template("hello.html")
    
# @app.route('/method', methods=['GET', 'POST'])
# def hellomethod():
#     if request.method == 'GET':
#         #args_dict = request.args.to_dict()
#         #print(args_dict)
#         num = request.args["num"]
#         name = request.args.get("name")
#         return "GET으로 전달된 데이터({}, {})".format(num, name)
#     else:
#         num = request.form["num"]
#         name = request.form.get("name")
#         with open("bbs/static/save.txt", "w", encoding='utf-8') as f:
#             f.write("%s,%s" % (num, name))
#         return "POST로 전달된 데이터({}, {})".format(num, name)

# @app.route('/getinfo')
# def getinfo():
#     with open('bbs/static/save.txt', 'r', encoding='utf-8') as f:
#         student = f.read().split(',')
#     return '번호 : {}, 이름 : {}'.format(student[0], student[1])

#Hello world...    
@app.route("/")
def helloworld():
    return "Hello, World!!!"  

#<convert:variable_name> convert에는 string, int, float, path, uuid
@app.route("/hi/<name>")
def hi_name(name):
    return "Hi, {}!!!".format(name)    

@app.route("/input/<int:num>")
def hi_int(num):
    name = ''
    if num == 1:
        name = '아진'
    elif num == 2:
        name = '아현'      
    elif num == 3:
        name = '아림'
    return "Hello, {}".format(name)