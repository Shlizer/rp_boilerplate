init -100 python:
    class RoamEventInterface(object):
        def canGo(self, label, isRoom = False):
            return True
        def inRoom(self, label, backTo):
            renpy.call(backTo, self)
