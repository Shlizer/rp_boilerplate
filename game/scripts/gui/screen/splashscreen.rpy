#define config.end_splash_transition = Dissolve(2.0)

label splashscreen:
    #$ renpy.music.play("rain.wav", channel="ambient1", loop=True, tight=True, if_changed=True, fadeout=2.0, fadein=4.0, relative_volume=0.1)
    # $ renpy.music.play("Sad_Circus.mp3", channel="bg-music", loop=True, fadeout=2.0, fadein=4.0, relative_volume=0.5)
return
