init -900 python:
    ToastType = enum(success='success', info='info', warning='warning', error='error')

    def toast(message, title=None, type=ToastType.error):
        print message
