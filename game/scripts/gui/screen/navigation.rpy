## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init offset = -60

transform navButton:
    transform_anchor True
    xanchor 1.0
    on idle:
        easein 0.2 xsize 300
    on hover:
        easein 0.2 xsize 330

screen navigation(mouse = [0,0]):
    vbox:
        style_prefix "navigation"

        xpos 0.95
        yalign 0.5
        
        spacing 0

        if main_menu:

            button at navButton:
                text _("Start")
                mouse "choice"
                action Start()
                hover_sound "audio/sound/btn_hover.wav"
                activate_sound "audio/sound/btn_click.wav"

        else:

            button at navButton:
                text _("Save")
                mouse "choice"
                action ShowMenu("save")
                hover_sound "audio/sound/btn_hover.wav"
                activate_sound "audio/sound/btn_click.wav"

        button at navButton:
            text _("Load")
            mouse "choice"
            action SetVariable('menu_selection', 'load')#ShowMenu("load")
            hover_sound "audio/sound/btn_hover.wav"
            activate_sound "audio/sound/btn_click.wav"

        button at navButton:
            text _("Options")
            mouse "choice"
            action Function(show_submenu, 'options')
            hover_sound "audio/sound/btn_hover.wav"
            activate_sound "audio/sound/btn_click.wav"

        button at navButton:
            text _("Achievements")
            mouse "choice"
            action Function(show_submenu, 'achievements')
            hover_sound "audio/sound/btn_hover.wav"
            activate_sound "audio/sound/btn_click.wav"

        if _in_replay:

            button at navButton:
                text _("End Replay")
                mouse "choice"
                action EndReplay(confirm=True)
                hover_sound "audio/sound/btn_hover.wav"
                activate_sound "audio/sound/btn_click.wav"

        elif not main_menu:

            button at navButton:
                text _("Main Menu")
                mouse "choice"
                action MainMenu()
                hover_sound "audio/sound/btn_hover.wav"
                activate_sound "audio/sound/btn_click.wav"

        button at navButton:
            text _("About")
            mouse "choice"
            action Function(show_submenu, 'about')
            hover_sound "audio/sound/btn_hover.wav"
            activate_sound "audio/sound/btn_click.wav"

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            button at navButton:
                text _("Quit")
                mouse "choice"
                action Quit(confirm=not main_menu)
                hover_sound "audio/sound/btn_hover.wav"
                activate_sound "audio/sound/btn_click.wav"


style navigation_button is gui_button
style navigation_text is gui_button_text

style navigation_button:
    #size_group "navigation"
    xsize 300
    padding(40, 20, 40, 20)
    background Solid("#45454570")
    hover_background Solid("#be6f2670")

style navigation_text:
    color "#999999"
    hover_color "#c29d6670"
    size 30
