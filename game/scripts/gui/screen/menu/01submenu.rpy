init offset = -70

init python:
    def hide_screens():
        for screen_name in submenu_screens:
            renpy.hide_screen('submenu_' + screen_name)

    def show_submenu(name):
        if renpy.get_screen('submenu_' + name) == None:
            hide_screens()
            renpy.show_screen('submenu_' + name)
        else:
            hide_screens()


define submenu_screens = [
    'achievements',
    'options',
    'about',
]


transform submenu_transition:
    align (0.4, 0.5)
    anchor (0.5, 0.5)

    on show:
        alpha 0
        linear 0.4 alpha 1

    on hide:
        linear 0.2 alpha 0


screen submenu(title, scroll=None, yinitial=0.0):
    button at submenu_transition:
        style "submenu_overlay"

        vbox:
            textbutton title style "submenu_title"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    vbox:
                        transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    transclude

            else:
                transclude


style submenu_overlay:
    background Solid("#333333e7")
    xpos 0.1
    ypos 0.1
    xsize 0.7
    ysize 0.7
    align (0.4, 0.5)
    anchor (0.5, 0.5)
    padding (20, 20, 20, 20)

style submenu_title is button:
    background Solid("#333333e7")
    xpos -20
    ypos -102
    padding(20, 20, 20, 20)

style submenu_title_text is text:
    font font_semibold
    color "#c08650"
    size 35
