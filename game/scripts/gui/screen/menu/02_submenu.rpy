init offset = -70

init python:
    def hide_screens():
        for screen_name in submenu_screens:
            renpy.hide_screen('submenu_' + screen_name)

    def check_submenu():
        global submenu_opened
        screen_name = 'submenu_' + str(submenu_opened)

        if submenu_opened != None and renpy.has_screen(screen_name) and not renpy.get_screen(screen_name):
            show_submenu(submenu_opened)

    def show_submenu(name = ''):
        global submenu_opened

        if name == '':
            return
        if not renpy.has_screen('submenu_' + str(name)):
            print "screen submenu_" + str(name) + " not found!"
            return
        
        if renpy.get_screen('submenu_' + name) == None:
            print ">>> open submenu_" + str(name)
            submenu_opened = name
            hide_screens()
            renpy.show_screen('submenu_' + name)
        else:
            submenu_opened = None
            hide_screens()

define submenu_opened = ''
#define submenu_opened = 'achievements'

define submenu_screens = [
    'start',
    'save',
    'load',
    'options',
    'achievements',
    'about',
]


transform submenu_transition:
    on show:
        alpha 0
        linear 0.4 alpha 1

    on hide:
        linear 0.2 alpha 0

screen submenu(title, scroll=None, yinitial=0.0):
    style_prefix "submenu"

    button at submenu_transition:

        frame at update_pos_26:
            textbutton title style "submenu_title"

            vbox:
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

style submenu_button is empty
style submenu_frame is empty
style submenu_title is button
style submenu_title_text is text

style submenu_frame:
    background gui.color_panel_bg
    xoffset (0.02 * X_RES)
    yoffset (0.2 * Y_RES)
    xsize 0.72
    ysize 0.72
    padding (20, 20, 20, 20)

style submenu_title:
    background gui.color_panel_bg
    xpos -20
    ypos -103
    padding(20, 20, 20, 20)

style submenu_title_text:
    font font_semibold
    color gui.color_panel_title_color
    size 35
