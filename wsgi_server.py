from gevent.pywsgi import WSGIServer

def application(env, start_response):
    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"<b>Hello World</b>"]

    if env['PATH_INFO'] == '/users':
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"<b>The list of users!</b>"]
    start_response('404 Not Found', [('Content-Type','text/html')])
    return [b"<h1>Not Found</h1>"]

print(f"Serving on port 8080")
WSGIServer(('127.0.0.1',8080), application).serve_forever()