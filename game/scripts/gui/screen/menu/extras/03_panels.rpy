screen submenu_extras_replays():
    on "show" action [
        SetVariable('submenu_extras_selected', 'replays'),
        Hide('submenu_extras_choices'),
        Hide('submenu_extras_achievements'),
        Hide('submenu_extras_credits'),
    ]

    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.06 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.50
            ysize 0.68
 
            vbox:
                xoffset 30
                yoffset 30
                spacing 10
            
                frame style "section":
                    text "TBD"


screen submenu_extras_choices():
    on "show" action [
        SetVariable('submenu_extras_selected', 'choices'),
        Hide('submenu_extras_replays'),
        Hide('submenu_extras_achievements'),
        Hide('submenu_extras_credits'),
    ]
    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.06 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.50
            ysize 0.68

            vbox:
                xoffset 30
                yoffset 30
                spacing 10
            
                frame style "section":
                    text "TBD"


screen submenu_extras_achievements():
    on "show" action [
        SetVariable('submenu_extras_selected', 'achievements'),
        Hide('submenu_extras_replays'),
        Hide('submenu_extras_choices'),
        Hide('submenu_extras_credits'),
    ]
    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.06 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.50
            ysize 0.68

            vbox:
                xoffset 30
                yoffset 30
                spacing 10
            
                frame style "section":
                    text "TBD"


screen submenu_extras_credits():
    on "show" action [
        SetVariable('submenu_extras_selected', 'credits'),
        Hide('submenu_extras_replays'),
        Hide('submenu_extras_choices'),
        Hide('submenu_extras_achievements'),
    ]
    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.06 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.50
            ysize 0.68
            
            vbox:
                xoffset 30
                yoffset 30
                spacing 10
            
                frame style "section":
                    text "TBD"

