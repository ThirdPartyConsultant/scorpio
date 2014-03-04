
import RPi.GPIO as GPIO
import time


pin = 25


GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
#print dir(GPIO)
#GPIO.output(pin, )

