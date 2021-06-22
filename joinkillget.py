from gevent import Greenlet
from gevent import sleep
g = Greenlet(sleep, 5)
print("Starting sleep!")
g.start()
print("Killing immediately!")
g.kill(Exception("You shall not live!"))
print(g.dead)