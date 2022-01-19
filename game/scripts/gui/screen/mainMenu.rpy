init offset = -60

transform main_menu_transition:
    subpixel True
    on show:
        alpha 1.0
        linear 5.0 alpha 0

    on hide:
        alpha 0
        linear 5.0 alpha 1.0

label before_main_menu:
    $ renpy.music.play("rain.wav", channel="ambient1", loop=True, fadeout=2.0, fadein=4.0, relative_volume=0.1)
    $ renpy.music.play("Sad_Circus.mp3", channel="bg-music", loop=True, fadeout=2.0, fadein=4.0, relative_volume=0.3)

define in_menu = True
define menu_selection = None

label main_menu:
    #show screen mouse_pos(mousePos)
    show screen main_menu_bg
    show screen navigation(mousePos)
    show screen submenu_achievements

    while in_menu == True:
        pause
        #show screen main_menu
        #$ mouse = renpy.call_screen('main_menu', mousePos)
        #$ mouse = renpy.call_screen('navigation', mousePos)


#screen mouse_pos(mouse):

screen main_menu(mouse):
    #on "show" action With(Dissolve(1.0))
    #on "hide" action With(Dissolve(1.0))
    ## This ensures that any other menu screen is replaced.
    #tag menu

    text ">>> [menu_selection]"
    text ">>> [mouse[0]] : [mouse[1]]"
    mousearea:
        area (0, 0, 1.0, 1.0)
        hovered Function(getMousePos)

    use main_menu_bg
    use navigation(mouse)
 
init python:
    mousePos = [0, 0]

    def getMousePos():
        global mousePos
        x, y = pygame.mouse.get_pos()
        mousePos = [x, y]
        print "get mouse pos: " + str(x) + ":" + str(y)
        return [x, y]


#style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30
