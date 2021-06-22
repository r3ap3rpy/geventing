from gevent import monkey; monkey.patch_all()
import gevent
import subprocess

commands = [
    "systeminfo",
    "ipconfig",
]

def asyncommands(command):
    print(f"Performing command: {command}")
    stdout, stderr = subprocess.Popen(command)
    print(f"stdout: {stdout.decode()}")

result = [gevent.spawn(asyncommands,command) for command in commands]

gevent.wait(result)