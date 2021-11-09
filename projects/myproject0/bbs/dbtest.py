from flask import Flask, request, render_template
from bbs import dbdb, app

@app.route('/dbinit')
def dbinit():
    dbdb.create_table()
    return 'DB student table 생성'

@app.route('/dbtest')
def dbtest():
    return render_template('hello.html')

@app.route('/method', methods=['GET', 'POST'])
def dbmethod():
    if request.method == 'GET':
        return 'GET 으로 전송한다'
    else:
        num = request.form["num"]
        name = request.form["name"]
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/dbgetinfo')        
def dbgetinfo():
    info = dbdb.select_all() #[(num, name), (num, name)...]
    return render_template("dbtest.html", data=info)