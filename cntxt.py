from gevent import Greenlet

def inside():
    print(f"Using context manager!")
    return 99

with Greenlet.spawn(inside) as g:
    print(f"Entered context manager!")

print(g.get(block = False))

# functions can be made asynchronous by passing the f(block = False)