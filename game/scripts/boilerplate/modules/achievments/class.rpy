init -150 python:
    import time

    ########################################
    # Single trophy (achievement) class; only for storing data - not logic
    # - amount: tuple of current and max values
    # - isHidden: this achievement won't show on achievement list
    # - isSecret: this one will show on list, but it's title and description are hidden until granted
    ########################################
    class Trophy(object):
        def __init__(self, id, name, description, icon, amount=None, amountMax=None, isHidden=False, isSecret=False):
            self.id = id
            self.name = name
            self.description = description
            self.icon = icon
            self.amount = amount
            self.amountMax = amountMax
            self.isHidden = isHidden
            self.isSecret = isSecret
            self.finished = False
            self.finishDate = None

        def add(self, amount):
            self.amount = min((self.amount or 0) + amount, self.amountMax)
            return self.amount >= self.amountMax

        def sub(self, amount):
            if amount > 0:
                self.amount = max(0, (self.amount or 0) - amount)
                self.reset()
            return self.amount == 0

        def finish(self, withDate = None):
            self.finished = True
            self.finishDate = withDate or time.time()

        def reset(self):
            self.amount = None
            self.finished = False
            self.finishDate = None

    def savePersistent(id, finishDate=None, amount=None):
        if not persistent.achievements:
            persistent.achievements = {}

        if finishDate or amount:
            persistent.achievements[id] = {}
            persistent.achievements[id]['amount'] = amount
            persistent.achievements[id]['finishDate'] = finishDate
        else:
            persistent.achievements[id] = None


    ########################################
    # Main achievement class to handle all registered and granted achievements
    ########################################
    class Achievements(NoRollback):
        registered = {}
        toAdd = []
        
        def init(self):
            if persistent.achievements:
                for id in persistent.achievements:
                    if persistent.achievements[id]:
                        if self.registered[id]:
                            self.registered[id].amount = persistent.achievements[id]['amount'] or None
                            if persistent.achievements[id]['finishDate']:
                                self.registered[id].finish(persistent.achievements[id]['finishDate'])
                        else:
                            toast("Get state from persistent: there's no achievement registered for ID " + id)

        def register(self, id, name, description, icon, amount=None, amountMax=None, isHidden=False, isSecret=False):
            if self.registered.get(id) == None:
                self.registered[id] = Trophy(id, name, description, icon=icon, amount=amount, amountMax=amountMax, isHidden=isHidden, isSecret=isSecret)
            else:
                toast("Achievement with given ID already exists: " + id)

        def grant(self, id, amount=None):
            trophy = self.registered.get(id)

            if trophy != None:
                if trophy.finished == False:
                    if amount:
                        if not trophy.add(amount):
                            return savePersistent(trophy.id, amount=trophy.amount)
                        
                    trophy.finish()
                    savePersistent(trophy.id, trophy.finishDate, trophy.amount)
                    self.toAdd.append(trophy)
                else:
                    toast("Achievement with ID '" + id + "' is already finished")
            else:
                toast("Achievement with given ID (" + id + ") wasn't registered")

        def revoke(self, id, amount=None):
            trophy = self.registered.get(id)

            if trophy != None:
                if amount:
                    if trophy.sub(amount):
                        savePersistent(trophy.id)
                    else:
                        savePersistent(trophy.id, amount=trophy.amount)
                else:
                    trophy.reset()
                    savePersistent(trophy.id)
            else:
                toast("Achievement with given ID (" + id + ") wasn't registered")

        def revokeAll(self):
            for id in self.registered:
                if self.registered[id].finished == True or self.registered[id].amount > 0:
                    self.revoke(id)

        def getCount(self):
            all = 0
            granted = 0

            for id in self.registered:
                if self.registered[id].finished:
                    all += 1
                    granted += 1
                elif not self.registered[id].isHidden:
                    all += 1

            return (granted, all)

        def getGrantedOrInProgress(self):
            list = []

            for id in self.registered:
                if not self.registered[id].isHidden and (self.registered[id].finished or self.registered[id].amount > 0):
                    list.append(self.registered[id])

            list.sort(key=lambda x: (x.finishDate, not x.amount), reverse=True)
            return list

        def getLocked(self):
            list = []

            for id in self.registered:
                if not self.registered[id].isHidden and not self.registered[id].finished and not self.registered[id].amount:
                    list.append(self.registered[id])

            list.sort(key=lambda x: x.isSecret)
            return list

        def popShown(self):
            if len(self.toAdd):
                self.toAdd.pop(0)
