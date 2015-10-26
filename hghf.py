import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

try:
        GPIO.output(20,0)
        GPIO.output(21,1)

        while True:
                while (GPIO.input(16) == 1):
                        time.sleep(0.1)

                GPIO.output(20,1)
                GPIO.output(21,0)

                while (GPIO.input(16) == 0):
                        time.sleep(0.1)

                while (GPIO.input(16) == 1):
                        time.sleep(0.1)

                GPIO.output(20,0)
                GPIO.output(21,1)

                while (GPIO.input(16) == 0):
                        time.sleep(0.1)
finally:
        GPIO.cleanup()
