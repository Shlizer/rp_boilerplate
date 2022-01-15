init -150 python:
    import time

    def Noop():
        pass
    
    ########################################
    # Phone main class
    ########################################
    class Phone(NoRollback):
        opened = False
        wallpaper_current = 0
        wallpaper_max = 5
        wallpaper = Solid("#aaaaaa")
        apps = {}

        def __init__(self):
            self.changeWallpaper()
            self.opened = persistent.phone_opened #for testing

        def changeWallpaper(self):
            if self.wallpaper_current >= 5:
                self.wallpaper_current = 1
            else:
                self.wallpaper_current += 1

            self.wallpaper = Image("images/phone/wallpapers/" + str(self.wallpaper_current) + ".jpg")

        def open(self):
            self.opened = True
            persistent.phone_opened = self.opened #for testing

        def close(self):
            self.opened = False
            persistent.phone_opened = self.opened #for testing

        def toggle(self):
            self.close() if self.opened else self.open()

        def addApp(self, app):
            if self.apps.get(app.name):
                toast("App with name " + app.name + " already exists")
            else:
                self.apps[app.name] = app

        def removeApp(self, name):
            if not self.apps.get(name):
                toast("App with name " + app.name + " doesn't exist")
            else:
                self.apps[app.name] = None

        def getApps(self):
            list = []
            
            for name in self.apps:
                list.append(self.apps[name])
            
            list.sort(key=lambda x: x.order)
            return list

    ########################################
    # Phone app class
    ########################################
    class PhoneApp(NoRollback):
        name = None
        icon = None
        active = False
        order = 100
        action = Noop

        def __init__(self, name, action=Noop, icon=None, active=False, order=100):
            self.name = name
            self.action = action
            self.icon = icon
            self.active = active
            self.order = order

    phone = Phone()
