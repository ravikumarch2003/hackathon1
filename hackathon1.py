import sys
import time
import socket
import json
import urllib2
import usb.core
import usb.util
import platform

def prep_usb():
    global dev
    global dev_type
    dev=usb.core.find(idVendor=0x2123, idProduct=0x1010)
    
    try:
 	dev.detach_kernel_driver(0)
    except Exception, e:
	pass
    dev.set_configuration()
    if dev is None:
	dev=usb.core.find(idVendor=0x0a81, idProduct=0x0701)
    	if dev is None:
	   raise ValueError('Attached device not found by Rpi')
        else:
	   dev_type="Original"
    else:
        dev_type="Thunder"
    print "Finished prepping Up"
    print dev_type


def turnLeft():
    if "Thunder" == dev_type:
        dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, 0x04, 0x00,0x00,0x00,0x00,0x00,0x00])
    elif "Original" == dev_type:
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [0x04])
    print "Turning Left"

def turnRight():
    if "Thunder" == dev_type:
        dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, 0x08, 0x00,0x00,0x00,0x00,0x00,0x00])
    elif "Original" == dev_type:
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [0x08])

def turnUp():
    if "Thunder" == dev_type:
        dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, 0x02, 0x00,0x00,0x00,0x00,0x00,0x00])
    elif "Original" == dev_type:
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [0x02])

def turnDown():
    if "Thunder" == dev_type:
        dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, 0x01, 0x00,0x00,0x00,0x00,0x00,0x00])
    elif "Original" == dev_type:
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [0x01])

def launchMissile():
    cnt=1
    while cnt<5:
	    if "Thunder" == dev_type:
	        dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, 0x10, 0x00,0x00,0x00,0x00,0x00,0x00])
	    elif "Original" == dev_type:
		dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [0x10])
            cnt=cnt+1

def abortMissile():
    if "Thunder" == dev_type:
	dev.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, 0x20, 0x00,0x00,0x00,0x00,0x00,0x00])
    elif "Original" == dev_type:
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, [0x20])
            


prep_usb()
turnLeft()
time.sleep(5)
turnRight()
time.sleep(5)
turnDown()
time.sleep(2)
turnUp()
time.sleep(2)

launchMissile()




	
   