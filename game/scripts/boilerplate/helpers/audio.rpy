init -100 python:
    renpy.music.register_channel("music", "music", loop=True, file_prefix="audio/music/")
    renpy.music.register_channel("ambient", "ambient", loop=True, file_prefix="audio/sound/")
    renpy.music.register_channel("btn-sfx", "sfx", loop=True, file_prefix="audio/sound/")
