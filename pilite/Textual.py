#!/usr/bin/env python

import serial, time, sys

s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/ttyAMA0"

try:
    s.open()
except serial.SerialException as e:
    sys.stderr.write("could not open port %r: %s\n" % (s.port, e))
    sys.exit(1)

s.write(bytes("$$$ALL,OFF\r", "UTF-8"))
time.sleep(0.5)
while True:
    name = input("Enter Your Name: ", )
    s.write(bytes("Hello " + name, "UTF-8"))
    time.sleep(5)
