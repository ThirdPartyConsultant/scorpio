
import RPi.GPIO as GPIO

import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def stop():
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def left_forward():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)

def left_backward():
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)

def right_forward():
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)

def right_backward():
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)


def left_turn():
    right_forward()
    left_backward()

def right_turn():
    left_forward()
    right_backward()


def forward():
    right_forward()
    left_forward()

def backward():
    right_backward()
    left_backward()

forward()
time.sleep(3)
backward()
time.sleep(3)
left_turn()
time.sleep(3)
right_turn()
time.sleep(3)
stop()


GPIO.cleanup()

