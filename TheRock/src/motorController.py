import RPi.GPIO as GPIO
import sys
import time

class MotorController:
    def __init__(self):
        self.executionDict = {'turn_right':self._turn_right, 'turn_left':self._turn_left,'stop':self._stop, 'forward':self._forward, 'backward':self._backward}

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)

    def isAction(self, action):
        return self.executionDict.has_key(action)

    def execute(self, action):
        try:
            self.executionDict[action]()
            return "done" + action
        except:
            return "somethine wrong" , sys.exc_info()[0]

    def _forward(self):
        print "do forward"
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        print "after set.."
        self.right_forward()
        self.left_forward()

    def _stop(self):
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)

    def left_forward(self):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)

    def left_backward(self):
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)

    def right_forward(self):
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)

    def right_backward(self):
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)


    def _turn_left(self):
        self.right_forward()
        self.left_backward()

    def _turn_right(self):
        self.left_forward()
        self.right_backward()



    def _backward(self):
        self.right_backward()
        self.left_backward()


