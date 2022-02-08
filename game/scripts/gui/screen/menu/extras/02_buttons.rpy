init python:
    class menuExtrasButtonAction(Action):
        def __init__(self, section):
            self.section = section

        def __call__(self):
            NullAction()

        def get_selected(self):
            return submenu_extras_selected == self.section

screen submenu_extras_buttons():
    on "hide" action [
        Hide('submenu_extras_replays'),
        Hide('submenu_extras_choices'),
        Hide('submenu_extras_achievements'),
        Hide('submenu_extras_credits'),
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

                textbutton _("Replays"):
                    style "btn_extras_selection"
                    action [Show('submenu_extras_replays'), menuExtrasButtonAction('replays')]
                textbutton _("Choices"):
                    style "btn_extras_selection"
                    action [Show('submenu_extras_choices'), menuExtrasButtonAction('choices')]
                textbutton _("Achievements"):
                    style "btn_extras_selection"
                    action [Show('submenu_extras_achievements'), menuExtrasButtonAction('achievements')]
                textbutton _("Credits"):
                    style "btn_extras_selection"
                    action [Show('submenu_extras_credits'), menuExtrasButtonAction('credits')]


style btn_extras_selection is btn_light:
    xsize 270
style btn_extras_selection_text is btn_light_text
