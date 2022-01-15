init -60 python:
    def image_daytime(st, at, path):
        return im.Scale(path % daytime, X_RES, Y_RES), 0.1
