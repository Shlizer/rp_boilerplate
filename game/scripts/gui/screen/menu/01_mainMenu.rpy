init offset = -60

transform main_menu_transition:
    subpixel True
    on show:
        alpha 1.0
        linear 5.0 alpha 0

    on hide:
        alpha 0
        linear 5.0 alpha 1.0

init -70 python:
    def playMainMenuAudio():
        if renpy.music.get_playing('ambient') == None:
            print 'play rain'
            renpy.music.play("rain.wav", channel="ambient", loop=True, fadeout=2.0, fadein=4.0, relative_volume=0.1)
        if renpy.music.get_playing('music') == None:
            renpy.music.play("Sad_Circus.mp3", channel="music", loop=True, fadeout=2.0, fadein=4.0, relative_volume=0.3)

label before_main_menu:
    $ playMainMenuAudio()

define config.layers = [ 'master', 'transient', 'threeD_text', 'screens', 'overlay' ]
define e_3d = Character("Eileen3D", show_layer="threeD_text")

transform text_rotate_3d(time=1.5):
    matrixanchor (0.5,0.5)
    matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,0)
    linear time matrixtransform RotateMatrix(0,180,0) * OffsetMatrix(0,0,0)
    linear time matrixtransform RotateMatrix(0,360,0) * OffsetMatrix(0,0,0)
    matrixtransform RotateMatrix(0,0,0) * OffsetMatrix(0,0,0)
    repeat



transform ttt():
    #contains:
    subpixel True
    perspective True
    xpos 150
    zpos -1079
    matrixanchor (0.5,0.5)
    matrixtransform RotateMatrix(0,10,0)# * OffsetMatrix(-10, 0, 0)

    contains:
        #perspective True
        #matrixanchor (0.5,0.5)
        offset (-110, -110)
        matrixtransform OffsetMatrix(100, -300, 0)

screen test():
    zorder 100
    frame:
        xalign 0.5
        yalign 0.5

        # text "asfasdfasf" at text_rotate_3d():
        #     xalign 0.5
        #     yalign 0.5
        
        button at text_rotate_3d():
            style "btn"
            text _("Start")
            action Function(show_submenu, 'load')
            hover_sound gui.audio_btn_hover
            activate_sound gui.audio_btn_click


$'''
'' '
label main_menu:
    #camera screens:
    #    perspective True

    #show screen mouse_pos(mousePos)
    show screen main_menu_bg()
    
    show screen navigation()
    #show screen submenu_achievements()
    # show screen test()

    while True:
        pause
$' ''
'''

init python:
    def check_submenu_autoopen():
        global submenu_opened
        if submenu_opened != '':
            show_submenu(submenu_opened)


screen main_menu():
    on "show" action Function(check_submenu_autoopen)
    #key "K_ESCAPE" action Show('game_main_menu')
    #$ print renpy.has_label("game_menu")
    #show screen mouse_pos(mousePos)
    use main_menu_bg()
    use navigation()

    #use submenu_achievements()

style btn:
    padding(40, 20, 40, 20)
    #background gui.color_menu_buttons_bg
    #hover_background gui.color_menu_buttons_bg_hover