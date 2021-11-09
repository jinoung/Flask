from bbs import app
from flask import g, Response, request, make_response, render_template
from datetime import datetime, date



@app.route('/reqenv')
def reqenv():
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
        'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
        'PATH_INFO: %(PATH_INFO) s <br>'
        'QUERY_STRING: %(QUERY_STRING) s <br>'
        'SERVER_NAME: %(SERVER_NAME) s <br>'
        'SERVER_PORT: %(SERVER_PORT) s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
        'wsgi.version: %(wsgi.version) s <br>'
        'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
        'wsgi.input: %(wsgi.input) s <br>'
        'wsgi.errors: %(wsgi.errors) s <br>'
        'wsgi.multithread: %(wsgi.multithread) s <br>'
        'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
        'wsgi.run_once: %(wsgi.run_once) s') % request.environ


#@app.route('/lo', subdomain='g') #g.local.com/lo
#def helloworld_local():
#    return "Hello, Local.com!!!"

# def ymd(fmt):
#     def trans(date_str):
#         return datetime.strptime(date_str, fmt)
#     return trans

# @app.route('/dt')
# def dt():
#     datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d')) #2nd는 default값
#     return "우리나라 시간 형식 : " + str(datestr)

# @app.route('/reqp')
# def req_parameter():
    #key값 q를 알고 있을 경우, key:value가 dict형식으로 전달됨...
    #value = request.args.get('q') 
    #return "q=%s" % str(value)

    #args_dict = request.args.to_dict()
    #return args_dict

    #value가 여러개인 key값을 알고 있을 경우 list로 받는다...
    # list = request.args.getlist('q')
    # return str(list)

# @app.route("/res1")
# def res2():
#     custom_res = Response("Custom response...", 200, {'test' : 'ttt', 'test2' : 'hhh'}) #test는 header에 전달됨
#     return make_response(custom_res)

#WSGI(WebServer Gateway Interface) : 뭘 말하고 싶은걸까? 펑션을 넘겨주는 식으로 WSGI가 구현되었다??
# @app.route('/test_wsgi')
# def wsgi_test():
#     def application(environ, start_response):
#         body = 'The request method was %s' % environ['REQUEST_METHOD']
#         headers = [('Content-type', 'text/plain'),
#                    ('Content-length', str(len(body)))]
#         start_response('200 OK', headers)
#         return [body]
#     return make_response(application) #인자가 스트링이면 html, 지금처럼 펑션(주소)이면 plain

#client가 요청한 정보를 request하기 전/후처리...적절한 활용방안은?
# @app.before_request 
# def before_request():
#     g.str = "영어"
#     g.user = "jinoung"

#전역변수 g에 대해서..
# @app.route("/g")
# def helloworld2():
#     return "Hello, World3!!! g.user = " + getattr(g, 'user', None) #3rd 인자는 default값