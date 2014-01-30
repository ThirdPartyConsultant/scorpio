import sys
import time

class ApiHandler:
    def __init__(self):
        self.executionDict = {'service':'','workday':self._turn_on_light,'target':self._turn_off_light}


    def isAction(self, action):
        return self.executionDict.has_key(action)

    def execute(self, action):
        try:
            self.executionDict[action]()
            return "done"
        except:
            return "somethine wrong", sys.exc_info()[0]
            
    def _turn_on_light(self):
        return "XX"

    def _turn_off_light(self):
        return "OO"


#c = CommandDispatcher()
#c.execute('turn_on_light')
#time.sleep(5)
#c.execute('turn_off_light')

