import gevent
from gevent.greenlet import Greenlet

class MyGreenLet(gevent.Greenlet):
    def __init__(self, seconds):
        Greenlet.__init__(self)
        self.seconds = seconds
    def _run(self):
        gevent.sleep(self.seconds)
    def __str__(self):
        return f'MyGreenLet({self.seconds})'

        