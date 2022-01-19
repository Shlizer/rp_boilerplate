init -100 python:
    renpy.music.register_channel("bg-music", "music", loop=True, file_prefix="audio/music/")
    renpy.music.register_channel("ambient1", "music", loop=True, file_prefix="audio/sound/")
    renpy.music.register_channel("btn-sfx", "sfx", loop=True, file_prefix="audio/sound/")
