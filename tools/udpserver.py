#!/usr/bin/env python
# Muestra por STDOUT lo recibido en el puerto 3000

import socket
from datetime import datetime


UDP_IP = "::"
UDP_PORT = 3000

sock = socket.socket(socket.AF_INET6, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print datetime.now(), ", ", data
