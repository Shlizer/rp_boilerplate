
screen submenu_chapters_buttons():
    #on "hide" action [ 
        #Hide('submenu_chapter')
        #Hide('submenu_chapter_' + str(number))
    #]
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

                for number, data in chapters.get():
                    textbutton _("Chapter %d") % data.count:
                        style "btn_chapters_selection"

                        action [
                            menuChaptersButtonAction(data.count, submenu_chapter_selected == data.count),
                            #Hide('submenu_chapter_' + str(submenu_chapter_selected)),
                            Show('submenu_chapter_' + str(data.count))
                        ]

style btn_chapters_selection is btn_light:
    xsize 270
style btn_chapters_selection_text is btn_light_text

screen submenu_chapter(number = 9):
    on "show" action [
        SetVariable('submenu_chapter_selected', number),
    ]

    button at submenu_panel_transition(xPos=-300):
        frame at float_with_mouse(26):
            style "panel_flip"
            xoffset (0.06 * X_RES)
            yoffset (0.14 * Y_RES)
            xsize 0.50
            ysize 0.68
            textbutton "----Chapter " + str(number)

screen submenu_chapter_1:
    on "show" action [ Function(hide_submenu_chapters, 1) ]
    use submenu_chapter(1)

screen submenu_chapter_2:
    on "show" action [ Function(hide_submenu_chapters, 2) ]
    #on "hide" action [ Hide('submenu_chapter_2') ]
    use submenu_chapter(2)

screen submenu_chapter_3:
    on "show" action [ Function(hide_submenu_chapters, 3) ]
    #on "hide" action [ Hide('submenu_chapter_3') ]
    use submenu_chapter(3)

screen submenu_chapter_4:
    on "show" action [ Function(hide_submenu_chapters, 4) ]
    #on "hide" action [ Hide('submenu_chapter_4') ]
    use submenu_chapter(4)

#screen submenu_chapter_5:
#    use submenu_chapter(5)
