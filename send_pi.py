#!/usr/bin/env python3

# -*- coding:utf-8 -*-
#import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600,timeout=1) 
#ser = serial.Serial("/dev/ttyAMA0",9600,timeout=1) 
print(ser.portstr)

command = "96\r\n"
print("send:", command )
len = ser.write(command.encode('utf-8'))    
print("len = ",len)

print("You can always send data, press Ctrl + C to exit")
while True:
#     strInput = input("enter some words:\r\n")
#     ser.write(strInput.encode())
    ser.write(command.encode('utf-8'))
    time.sleep(0.5)
    print("send:", command )

ser.flush()



