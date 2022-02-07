screen submenu_options_graphics():
    on "show" action [
        SetVariable('submenu_options_selected', 'graphics'),
        Hide('submenu_options_audio'),
        Hide('submenu_options_gameplay'),
    ]
    on "hide" action [
        #SetVariable('submenu_options_selected', ''),
    ]

    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.07 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.55
            ysize 0.68
 
            vbox:
                xoffset 30
                yoffset 30
                spacing 10
            
                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Resolution") style "section_title"
                        textbutton _("480p") style "section_button" action Preference("display", 0.446875)
                        textbutton _("720p") style "section_button" action Preference("display", 0.6666666666666667)
                        textbutton _("1080p") style "section_button" action Preference("display", 1.0)
                        textbutton _("1440p") style "section_button" action Preference("display", 2.0)
                        textbutton _("Fullscreen") style "section_button" action Preference("display", "fullscreen")
                
                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Framerate") style "section_title"
                        textbutton _("Default") style "section_button" action Preference("gl framerate", None)
                        textbutton _("25") style "section_button" action Preference("gl framerate", 25)
                        textbutton _("60") style "section_button" action Preference("gl framerate", 60)
                        textbutton _("120") style "section_button" action Preference("gl framerate", 120)
                        textbutton _("144") style "section_button" action Preference("gl framerate", 144)
            
                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("System cursor") style "section_title"
                        button style "checkbox" action Preference("system cursor", "toggle") yalign 0.5
                
                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Animations") style "section_title"
                        button style "checkbox" action NullAction() yalign 0.5


screen submenu_options_audio():
    on "show" action [
        SetVariable('submenu_options_selected', 'audio'),
        Hide('submenu_options_graphics'),
        Hide('submenu_options_gameplay'),
    ]
    on "hide" action [
        #SetVariable('submenu_options_selected', ''),
    ]
    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.07 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.55
            ysize 0.68

            vbox:
                xoffset 30
                yoffset 30
                spacing 10
            
                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Music vol") style "section_title"
                        bar value Preference("music volume") yalign 0.5

                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Sound vol.") style "section_title"
                        bar value Preference("sound volume") yalign 0.5

                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Ambient vol.") style "section_title"
                        bar value Preference("mixer ambient volume") yalign 0.5

                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Voice vol.") style "section_title"
                        bar value Preference("voice volume") yalign 0.5

                frame style "section":
                    hbox:
                        spacing 10
                        textbutton _("Mute All") style "section_title"
                        button style "checkbox" action Preference("all mute", "toggle") yalign 0.5
                

screen submenu_options_gameplay():
    on "show" action [
        SetVariable('submenu_options_selected', 'gameplay'),
        Hide('submenu_options_graphics'),
        Hide('submenu_options_audio'),
    ]
    on "hide" action [
        #SetVariable('submenu_options_selected', ''),
    ]
    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.07 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.55
            ysize 0.68


style section is btn_light:
    xsize 0.92

style section_title is gui_button:
    padding (8, 8, 8, 8)
    xsize 210
style section_title_text is gui_label:
    color gui.color_text_light
    font font_semibold
    size 28

style section_button is btn_basic:
    padding (12, 8, 12, 8)
    idle_background gui.color_primary_darker
    hover_background gui.color_primary_action
    selected_background gui.color_primary_dark
    selected_hover_background gui.color_primary_action
style section_button_text is gui_button_text:
    idle_color gui.color_text
    hover_color gui.color_text + "90"
    selected_color gui.color_text_light
    selected_hover_color gui.color_text_light + "90"
    font font_regular
    selected_font font_semibold
    size 28
    

$'''
    vbox:
        hbox:
            #vbox:
            #    style_prefix "radio"
            #    label _("Rollback Side")
            #    textbutton _("Disable") action Preference("rollback side", "disable")
            #    textbutton _("Left") action Preference("rollback side", "left")
            #    textbutton _("Right") action Preference("rollback side", "right")

            #vbox:
            #    style_prefix "check"
            #    label _("Skip")
            #    textbutton _("Unseen Text") action Preference("skip", "toggle")
            #    textbutton _("After Choices") action Preference("after choices", "toggle")
            #    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Auto-Forward Time")

                bar value Preference("auto-forward time")
    '''