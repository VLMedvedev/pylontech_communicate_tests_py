#!/usr/bin/env python3

# -*- coding:utf-8 -*-
#import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600,timeout=1) #receive data once every 0.01S 
print(ser.portstr)

ser.flushInput()

data = ""
print("You can always receive data, press Ctrl + C to exit")
while 1: 
    while ser.inWaiting() > 0:
        data = ser.readline()
    if data != "":
        print(data)
        data = ""
