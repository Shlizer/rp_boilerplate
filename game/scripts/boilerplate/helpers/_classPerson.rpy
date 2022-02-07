init -100 python:
    def getMaxExp(level):
        return exp_base + (exp_base * (level - 1))

    class Person(object):
        level = None
        exp = None
        max_exp = None
        id = None
        name = None
        callName = None
        color = None
        pin = False

        def __init__(self, id, name, callName = None, color = None, pin = False, level = 1, exp = 0):
            self.id = id
            self.color = color
            self.level = level
            self.exp = exp
            self.max_exp = getMaxExp(level)
            self.setName(name, callName)
            self.pin = pin

        def setName(self, name, callName = None):
            self.name = name
            self.callName = callName or self.callName

        def addExp(self, exp):
            max = getMaxExp(self.level)

            if (self.exp + exp >= max):
                self.level += 1
                self.addExp(exp - max)
            else:
                self.exp += exp


