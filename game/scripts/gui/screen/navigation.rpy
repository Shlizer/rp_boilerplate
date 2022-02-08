## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init offset = -60

init python:
    class menuButtonAction(Action):
        def __init__(self, submenu):
            self.submenu = submenu

        def __call__(self):
            NullAction()

        def get_selected(self):
            return self.submenu and submenu_opened == self.submenu

    class menuContinueButtonAction(Action):
        def __init__(self):
            self.slot = renpy.newest_slot()

        def __call__(self):
            renpy.load(self.slot)

        def get_sensitive(self):
            return self.slot is not None

define showMore = True

screen navigation():
    $ btnCounter = 0
    
    vbox at float_with_mouse(26):
        style_prefix "nav"
        xoffset 1800
        yoffset 300
        yanchor 0.0
        yalign 0.5
        spacing 4

        if main_menu:

            if renpy.newest_slot() is not None:

                $ btnCounter = btnCounter + 1
                use navigation_button(_("Continue"), menuContinueButtonAction(), counter=btnCounter)

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Start"), submenu='chapters', counter=btnCounter)

        else:

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Save"), submenu='save', counter=btnCounter)

        $ btnCounter = btnCounter + 1
        use navigation_button(_("Load"), submenu='load', counter=btnCounter)
        
        $ btnCounter = btnCounter + 1
        use navigation_button(_("Options"), submenu='options', counter=btnCounter)

        $ btnCounter = btnCounter + 1
        use navigation_button(_("Extras"), submenu='extras', counter=btnCounter)

###
        #$ btnCounter = btnCounter + 1
        #use navigation_button(_("Replays"), submenu='replays', counter=btnCounter)

        #if not main_menu:

        #    $ btnCounter = btnCounter + 1
        #    use navigation_button(_("Choices"), submenu='choices', counter=btnCounter)

        #$ btnCounter = btnCounter + 1
        #use navigation_button(_("Achievements"), submenu='achievements', counter=btnCounter)

        #$ btnCounter = btnCounter + 1
        #use navigation_button(_("Credits"), submenu='credits', counter=btnCounter)

###

        if not main_menu:

            $ btnCounter = btnCounter + 1
            use navigation_button(_("Exit to menu"), MainMenu(), counter=btnCounter)

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            $ btnCounter = btnCounter + 1
            use navigation_button(_("Exit game"), Quit(confirm=not main_menu), counter=btnCounter)

transform navButton(counter = 0):
    #xpos 300 + (counter * 30)
    on idle:
        easein 0.7 xpos 0
    on hover:
        easein 0.3 xpos -60

transform navButtonSelected(counter = 0):
    #xpos 300 + (counter * 30)
    on idle:
        easein 0.7 xpos -60
    on hover:
        easein 0.3 xpos -70

screen navigation_button(label, action = NullAction, submenu = None, counter = 0):
    button:
        if (submenu_opened == submenu and submenu != None):
            at navButtonSelected(counter)
        else:
            at navButton(counter)
        text label

        if action == NullAction and submenu != None:
            action [menuButtonAction(submenu), Function(show_submenu, submenu)]
        else:
            action action


style nav_button is btn_menu
style nav_text is btn_menu_text

style nav_button:
    xsize 300
    ysize 61
    xpos 0
