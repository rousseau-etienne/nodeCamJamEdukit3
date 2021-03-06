#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# wii_remote_1.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
# adapted to commande camJam Edukit3
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1101
#
# Author : Matt Hawkins
# Date   : 30/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid
import time
import urllib
import os

#import RPi.GPIO as io

#io.setmode(io.BCM)
#pins = (2,3,4,17)
#for i in pins:
#  io.setup(i,io.OUT)

button_delay = 0.1


print('Press 1 + 2 on your Wii Remote now ...')
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print("Error opening wiimote connection")
  quit()

wii.rumble = 1
time.sleep(0.5)
wii.rumble = 0
print('Wii Remote connected...\n')
print('Press some buttons!\n')
print('Press PLUS and MINUS together to disconnect and quit.\n')

wii.rpt_mode = cwiid.RPT_BTN

#continueProgramm = 1

while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print('\nClosing connection ...')
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    os.system("shutdown now")
    quit()
    #wii.close()
    #continueProgramm = 0

  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print('Left pressed')
    urllib.urlopen("http://localhost:8080/backward").read()
    time.sleep(button_delay)
    #io.output(2, True)

  if(buttons & cwiid.BTN_RIGHT):
    print('Right pressed')
    urllib.urlopen("http://localhost:8080/forward").read()
    time.sleep(button_delay)
    #io.output(3, True)

  if (buttons & cwiid.BTN_UP):
    print('Up pressed')
    urllib.urlopen("http://localhost:8080/left").read()
    time.sleep(button_delay)
    #io.output(4, True)

  if (buttons & cwiid.BTN_DOWN):
    print('Down pressed')
    urllib.urlopen("http://localhost:8080/right").read()
    time.sleep(button_delay)
    #io.output(17, True)

  if (buttons & cwiid.BTN_1):
    print('Button 1 pressed')
    urllib.urlopen("http://localhost:8080/slow").read()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print('Button 2 pressed')
    urllib.urlopen("http://localhost:8080/fast").read()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    print('Button A pressed')
    time.sleep(button_delay)
    #for i in pins:
      #io.output(i, False)

  if (buttons & cwiid.BTN_B):
    print('Button B pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    print('Home Button pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print('Minus Button pressed')
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print('Plus Button pressed')
    time.sleep(button_delay)
