from gevent import monkey
import gevent
monkey.patch_all()
import requests

urls = [
    'http://127.0.0.1:8080/',
    'http://127.0.0.1:8080/notfound',
    'http://127.0.0.1:8080/users'
]

def response(url):
    print(f"Working on url: {url}")
    print(f"Response: {requests.get(url = url).text}")

jobs = [ gevent.spawn(response, url) for url in urls ]

gevent.wait(jobs)