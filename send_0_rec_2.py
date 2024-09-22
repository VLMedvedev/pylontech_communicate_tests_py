#!/usr/bin/env python3

# -*- coding:utf-8 -*-
#import RPi.GPIO as GPIO
import serial
import time


port1 = '/dev/ttyAMA0'
port2 = '/dev/ttyAMA2'
baud = 9600
ser1 = serial.Serial(port1, baud, timeout=0)
print("connected to: " + ser1.portstr)
ser2 = serial.Serial(port2, baud, timeout=0)
print("connected to: " + ser2.portstr)

#ser.flushInput()
#ser.flushOutput()
command = "hello seengreat!\r\n"
print("send:", command )
len = ser1.write(command.encode('utf-8'))
print("len = ",len)

data = ""
print("You can always receive data, press Ctrl + C to exit")
while True:
    time.sleep(0.5)
    while ser2.inWaiting() > 0:
        data = ser2.read(ser2.inWaiting())
        #data = ser2.readline()
    #data = ser2.read()
    if data != "":
        print("recive", data)
        data = ""

    ser1.write(command.encode('utf-8'))
    print("send:", command)

ser1.close()
ser2.close()
