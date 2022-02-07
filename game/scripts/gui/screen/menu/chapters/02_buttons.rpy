init python:
    def getChapterCount():
        count = 0
        
        while True and count < 100:
            if not renpy.has_screen('submenu_chapter_' + str(count + 1)):
                break;
            count += 1
        return count
    
    class menuChaptersButtonAction(Action):
        def __init__(self, section):
            self.section = section

        def __call__(self):
            NullAction()

        def get_selected(self):
            return submenu_chapter_selected == self.section


screen submenu_chapters_buttons():
    on "show" action [
        Function(getChapterCount)
    ]
    on "hide" action [
        Hide('submenu_chapters_graphics'),
        Hide('submenu_chapters_audio'),
        Hide('submenu_chapters_gameplay'),
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

                for chapter in range(getChapterCount()):
                    textbutton _("Graphics"):
                        style "btn_options_selection"
                        action [Show('submenu_chapters_graphics'), menuChaptersButtonAction('graphics')]
                    text str(chapter)

                textbutton _("Graphics"):
                    style "btn_options_selection"
                    action [Show('submenu_chapters_graphics'), menuChaptersButtonAction('graphics')]
                textbutton _("Audio"):
                    style "btn_options_selection"
                    action [Show('submenu_chapters_audio'), menuChaptersButtonAction('audio')]
                textbutton _("Gameplay"):
                    style "btn_options_selection"
                    action [Show('submenu_chapters_gameplay'), menuChaptersButtonAction('gameplay')]


style btn_options_selection is btn_light:
    xsize 180


screen submenu_chapter_1:
    textbutton "Chapter 1"

screen submenu_chapter_2:
    textbutton "Chapter 2"

screen submenu_chapter_3:
    textbutton "Chapter 3"

screen submenu_chapter_4:
    textbutton "Chapter 4"

screen submenu_chapter_5:
    textbutton "Chapter 5"