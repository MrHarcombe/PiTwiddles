import RPi.GPIO as GPIO
import time

leds = [ 11, 13, 21 ]
switch = 26

GPIO.setmode(GPIO.BOARD)

GPIO.setup(leds,   GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

try:
  while True:
    while GPIO.input(switch) == 1:
      time.sleep(0.1)
    GPIO.output(leds, GPIO.HIGH)
    if GPIO.input(switch) == 1:
      GPIO.output(leds, GPIO.LOW)
finally:
  GPIO.cleanup()
