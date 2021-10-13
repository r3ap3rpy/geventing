from gevent import Greenlet
from gevent import sleep

g = Greenlet(sleep, 5)
print(f"Starting sleep!")
g.start()
print(f"Killing immediately!")
g.kill(Exception("You shall not live!"))
print(f"is dead: {g.dead}")