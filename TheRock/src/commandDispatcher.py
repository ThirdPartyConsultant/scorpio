import RPi.GPIO as GPIO
import sys
import time

class CommandDispatcher:
    def __init__(self):
        self.executionDict = {'open_the_gate':'','turn_on_light':self._turn_on_light,'turn_off_light':self._turn_off_light}


    def isAction(self, action):
        return self.executionDict.has_key(action)

    def execute(self, action):
        try:
            self.executionDict[action]()
            return "done"
        except:
            return "somethine wrong", sys.exc_info()[0]
            
    def _turn_on_light(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, False)

    def _turn_off_light(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, True)


#c = CommandDispatcher()
#c.execute('turn_on_light')
#time.sleep(5)
#c.execute('turn_off_light')

