init python:
    def check_submenu_options_autoopen():
        global submenu_options_selected
        if submenu_options_selected != '':
            renpy.show_screen('submenu_options_' + submenu_options_selected)

define submenu_options_selected = 'audio'

screen submenu_options():
    on "show" action [
        Function(check_submenu_options_autoopen),
        Show('submenu_options_buttons'),
    ]
    on "hide" action [
        SetVariable('submenu_options_selected', ''),
        Hide('submenu_options_buttons'),
    ]

    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel"
            xoffset (0.02 * X_RES)
            yoffset (0.09 * Y_RES)
            xsize 0.72
            ysize 0.82

            textbutton _("Options") style "title":
                xoffset 50
                yoffset -60
