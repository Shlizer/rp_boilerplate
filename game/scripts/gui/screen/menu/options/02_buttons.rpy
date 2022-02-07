init python:
    class menuOptionsButtonAction(Action):
        def __init__(self, section):
            self.section = section

        def __call__(self):
            NullAction()

        def get_selected(self):
            return submenu_options_selected == self.section


screen submenu_options_buttons():
    on "hide" action [
        Hide('submenu_options_graphics'),
        Hide('submenu_options_audio'),
        Hide('submenu_options_gameplay'),
    ]

    button at submenu_panel_transition(xPos=300):
        frame at float_with_mouse(26):
            style "empty"
            xoffset (0.02 * X_RES)
            yoffset (0.09 * Y_RES)
            xsize 0.72
            ysize 0.82

            vbox:
                xalign 0.98
                yalign 0.5
                spacing 5

                textbutton _("Graphics"):
                    style "btn_options_selection"
                    action [Show('submenu_options_graphics'), menuOptionsButtonAction('graphics')]
                textbutton _("Audio"):
                    style "btn_options_selection"
                    action [Show('submenu_options_audio'), menuOptionsButtonAction('audio')]
                textbutton _("Gameplay"):
                    style "btn_options_selection"
                    action [Show('submenu_options_gameplay'), menuOptionsButtonAction('gameplay')]


style btn_options_selection is btn_light:
    xsize 180
