from flask import Flask

app = Flask(__name__)
app.debug = True
#app.config['SERVER_NAME'] = 'locla.com:5000' #hosts파일에 등록되어 있어야...
import bbs.seniorcoding
import bbs.wings2pc
import bbs.dbtest