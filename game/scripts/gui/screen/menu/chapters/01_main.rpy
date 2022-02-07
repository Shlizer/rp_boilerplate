init python:
    def check_submenu_chapters_autoopen():
        global submenu_chapter_selected
        if submenu_chapter_selected != '':
            renpy.show_screen('submenu_chapters_' + submenu_chapter_selected)

define submenu_chapter_selected = ''

screen submenu_chapters():
    on "show" action [
        Function(check_submenu_chapters_autoopen),
        Show('submenu_chapters_buttons'),
    ]
    on "hide" action [
        SetVariable('submenu_chapter_selected', ''),
        Hide('submenu_chapters_buttons'),
    ]

    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel"
            xoffset (0.02 * X_RES)
            yoffset (0.09 * Y_RES)
            xsize 0.72
            ysize 0.82

            textbutton _("Select chapter") style "title":
                xoffset 50
                yoffset -60
