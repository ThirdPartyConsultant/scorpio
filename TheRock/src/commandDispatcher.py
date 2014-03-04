import RPi.GPIO as GPIO
import sys
import time

class CommandDispatcher:
    def __init__(self):
        self.executionDict = {'open_the_gate':'','turn_on_light':self._turn_on_light,'turn_off_light':self._turn_off_light,'turn_on_rely':self._turn_on_rely,'turn_off_rely':self._turn_off_rely}


    def isAction(self, action):
        return self.executionDict.has_key(action)

    def execute(self, action):
        try:
            self.executionDict[action]()
            return "done" + action
        except:
            return "somethine wrong", sys.exc_info()[0]
            
    def _turn_on_light(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, False)

    def _turn_off_light(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, True)

    def _turn_on_rely(self):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(24, GPIO.LOW)

    def _turn_off_rely(self):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(24, GPIO.HIGH)




#c = CommandDispatcher()
#c.execute('turn_on_light')
#time.sleep(5)
#c.execute('turn_off_light')

