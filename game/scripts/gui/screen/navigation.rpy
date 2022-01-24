## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init offset = -60

init python:
    class LoadMostRecent(Action):
        def __init__(self):
            self.slot = renpy.newest_slot()

        def __call__(self):
            renpy.load(self.slot)

        def get_sensitive(self):
            return self.slot is not None

define showMore = True

screen navigation():
    $ btnCounter = 0
    
    vbox at update_pos_26:
        style_prefix "nav"
        xoffset 1800
        yoffset 300
        yanchor 0.0
        yalign 0.5
        spacing 4

        if main_menu:

            if renpy.newest_slot() is not None:

                $ btnCounter = btnCounter + 1
                use navigation_button(_("Continue"), LoadMostRecent(), counter=btnCounter)

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Start"), Start(), counter=btnCounter)

        else:

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Save"), submenu='save', counter=btnCounter)

        $ btnCounter = btnCounter + 1
        use navigation_button(_("More/Less"), SetVariable('showMore', not showMore), counter=btnCounter)
        
        if showMore:
            $ btnCounter = btnCounter + 1
            use navigation_button(_("Load"), submenu='load', counter=btnCounter)
            
            $ btnCounter = btnCounter + 1
            use navigation_button(_("Options"), submenu='options', counter=btnCounter)

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Replays"), submenu='replays', counter=btnCounter)

        if not main_menu:

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Choices"), submenu='choices', counter=btnCounter)

        $ btnCounter = btnCounter + 1
        use navigation_button(_("Achievements"), submenu='achievements', counter=btnCounter)

        $ btnCounter = btnCounter + 1
        use navigation_button(_("Credits"), submenu='credits', counter=btnCounter)

        if not main_menu:

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Exit to menu"), MainMenu(), counter=btnCounter)

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            $ btnCounter = btnCounter + 1
            use navigation_button(_("Exit game"), Quit(confirm=not main_menu), counter=btnCounter)

transform navButton(counter = 0):
    on idle:
        easein 0.7 xpos 0
    on hover:
        easein 0.3 xpos -60

transform navButtonSelected():
    on idle:
        easein 0.7 xpos -60
    on hover:
        easein 0.3 xpos -60


screen navigation_button(label, action = NullAction, submenu = None, counter = 0):
    #on "show" action Function(print, "SHOW " + label)
    button:# at (navButton(counter) if action == NullAction and submenu != None else navButtonSelected():
        xanchor 1.0
        xoffset 0

        if submenu == None or submenu != submenu_opened:
            at navButton(counter)
            style "nav_button"
            text label
        else:
            at navButtonSelected()
            style "nav_button_opened"
            text label style "nav_text_opened"

        mouse "choice"
        hover_sound gui.audio_btn_hover
        activate_sound gui.audio_btn_click

        if action == NullAction and submenu != None:
            action [Function(show_submenu, submenu)]# at btn_selection(transition_data[0], transition_data[1])
        else:
            action action


style nav_button is gui_button
style nav_text is gui_button_text
style nav_button_opened is nav_button
style nav_text_opened is gui_button_text

style nav_button:
    xsize 300
    ysize 61
    xpos 0
    padding(50, 0, 40, 0)
    background Frame("images/button_menu_idle.png", Borders(31,31,3,3))
    hover_background Frame("images/button_menu_hover.png", Borders(31,31,3,3))

style nav_text:
    color gui.color_menu_buttons_text
    hover_color gui.color_menu_buttons_text_hover
    size 30

style nav_button_opened:
    #xsize 6 5
    #xoffset -280
    xpos -60
    padding(30, 0, 40, 0)
    background Frame("images/button_menu_hover.png", Borders(31,31,3,3))
    hover_background Frame("images/button_menu_opened_hover.png", Borders(31,31,3,3))

style nav_text_opened:
    xpos 20
    color gui.color_menu_buttons_text_hover
    hover_color gui.color_menu_buttons_text_hover
    size 30
