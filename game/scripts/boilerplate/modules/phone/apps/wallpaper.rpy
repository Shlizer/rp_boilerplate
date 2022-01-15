init -140 python:
    app = PhoneApp('wallpaper', action=[phone.changeWallpaper, With(Dissolve(0.3))], order=10, active=True)
    phone.addApp(app)
