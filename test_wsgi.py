from wsgiref.simple_server import make_server
#from cgi import parse_qs,escape
from urllib.parse import parse_qs


def form(env):
    cl = int(env.get('CONTENT_LENGTH','0'))
    d = env['wsgi.input'].read(cl)
    d_d = parse_qs(d)
    print(d_d)
    return [d_d.get(b'a',b'1')[0]]
route = {
    'form': form
}
#env словарь всех переменных
def app(env,resp_start):

    resp_start('200 OK', [('Content-Type', 'text/html')])
    qs = env.get('QUERY_STRING', '')
    qs_d = parse_qs(qs)

    path = env.get('PATH_INFO','/')[1:]
    print(path)
    parts = path.split('/')
    print(parts)
    if len(parts) >0 and parts[0]:
        fn = route.get(parts[0])
        if fn is not None:
            res =fn(env)
    else:
        with open('html.html','r') as f:
            res=[(f.read()%(qs_d.get('a'),)).encode('UTF-8')]
    print(res)
    return res



    """
    resp_start('200 OK',[('Content-Type','text/html')])
    buf = [('%s:%s<br/>'%(k,v)).encode('UTF-8') for k,v in env.items()]
    return buf"""


serv = make_server('localhost',8080,app)
serv.serve_forever()
