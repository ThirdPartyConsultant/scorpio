
class CommandDispatcher:
    def __init__(self):
        self.executionDict = {'open_the_gate':'','turn_on_light':''}


    def isAction(self, action):
        return self.executionDict.has_key(action)


