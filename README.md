### Welcome

This is the supporting material for my course on [**gevent**](https://www.gevent.org/intro.html).

Gevent is a coroutine -based Python networking library that uses greenlet to provide a high-level synchronous API on top of the libev or libuv event loop.

In order to reproduce the example the following steps need to be done.
Install at least Python3.7 on your computer.
Perform the following steps.

``` bash
python -m pip install virtualenv
virtualenv g
.\g\scripts\activate
pip install gevent requests
```

Usefull [**tutorial**](http://sdiehl.github.io/gevent-tutorial/) in general.

Another usefull [**tutorial**](https://greenlet.readthedocs.io/en/latest/) about greenlets!

Here are the official [examples](https://www.gevent.org/examples/) you can use to practice.