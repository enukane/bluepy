import os
import socket
import json
import sys

SOCKNAME = "/tmp/ble.sock"

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
try:
    sock.connect(SOCKNAME)
except socket.error, msg:
    print msg
    sys.exit(1)

json_str = sock.recv(4096)
data = json.loads(json_str)

print data
