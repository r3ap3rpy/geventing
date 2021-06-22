from gevent import monkey
import gevent
monkey.patch_all()
import requests


urls = [
    'https://www.google.com/',
    'https://www.apple.com/',
    'https://www.python.org/'
]

def response(url):
    print(f"Working on url: {url}")
    print(f"Response: {requests.get(url = url)}")

jobs = [gevent.spawn(response, _url) for _url in urls]

gevent.wait(jobs)