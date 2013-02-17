
import RPi.GPIO as GPIO
import sys
import time

sw = 7 # pin7 is the switch...
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sw, GPIO.IN)
input_value = GPIO.input(sw) 

cnt = 0
while True:
    time.sleep(0.1)
    input_value = GPIO.input(sw) 
    print(str(cnt)+"input is %s" % input_value)
    cnt += 1
    if cnt == 100:
        break
