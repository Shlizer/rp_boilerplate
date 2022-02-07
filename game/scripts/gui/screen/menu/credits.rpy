## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

init offset = -60

screen submenu_credits():
    on "show" action [
        Show('submenu_credits_frame'),
    ]
    on "hide" action [
        Hide('submenu_credits_frame'),
    ]

    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel"
            xoffset (0.02 * X_RES)
            yoffset (0.09 * Y_RES)
            xsize 0.72
            ysize 0.82

            textbutton _("Credits") style "title":
                xoffset 50
                yoffset -60

screen submenu_credits_frame():
    button at submenu_panel_transition(yPos=-300):
        frame at float_with_mouse(26):
            style "btn_options_selection"
            xoffset (0.07 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.62
            ysize 0.72
            
            viewport:
                yinitial 0.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    label "[config.name!t]"
                    text _("Version [config.version!t]\n")

                    ## gui.about is usually set in options.rpy.
                    if gui.about:
                        text "[gui.about!t]\n"

                    text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


