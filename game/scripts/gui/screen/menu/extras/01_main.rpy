init python:
    def check_submenu_extras_autoopen():
        global submenu_extras_selected
        if submenu_extras_selected != '':
            renpy.show_screen('submenu_extras_' + submenu_extras_selected)

define submenu_extras_selected = ''

screen submenu_extras():
    on "show" action [
        Function(check_submenu_extras_autoopen),
        Show('submenu_extras_buttons'),
    ]
    on "hide" action [
        SetVariable('submenu_extras_selected', ''),
        Hide('submenu_extras_buttons'),
    ]
    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel"
            xoffset (0.02 * X_RES)
            yoffset (0.09 * Y_RES)
            xsize 0.72
            ysize 0.82

            textbutton _("Extras") style "title":
                xoffset 50
                yoffset -60
