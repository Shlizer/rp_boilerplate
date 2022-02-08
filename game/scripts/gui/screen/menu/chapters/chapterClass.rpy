init python:
    class Chapters():
        registered = {}

        def register(self, name, description, image = None, count = None):
            count = count or (len(self.registered) + 1)
            #if renpy.has_screen('submenu_chapter_' + str(count)):
            self.registered[count] = Chapter(count, name, description, image)
            #else:
            #    toast("Cannot register chapter '"+str(name)+"': no screen.")

        def get(self):
            return self.registered.items()

    class Chapter():
        def __init__(self, count, name, description, image = None):
            self.count = count
            self.name = name
            self.description = description
            self.image = image

    class menuChaptersButtonAction(Action):
        #def __init__(self, chapterNumber):
        #    self.chapterNumber = chapterNumber

        #def __call__(self):
        #    NullAction()

        def get_selected(self):
            global submenu_chapter_selected
            return submenu_chapter_selected == self.number

            
        def __init__(self, number, selected):
            self.number = number
            self.selected = selected

        def __call__(self):
            NullAction()

        #def get_selected(self):
        #    return selected

        def get_sensitive(self):
            return renpy.has_screen('submenu_chapter_' + str(self.number))


    chapters = Chapters()
    chapters.register('first', '')
    chapters.register('secont', '')
    chapters.register('third', '')
    chapters.register('ff', '')
    chapters.register('hfdgshfds', '')
    chapters.register('thirtrest5rshfsd', '')
    chapters.register('with error', '', count = 15)

    for k,v in chapters.get():
        print k

    '''
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

                    for number, data in chapters.get():
                        textbutton _("Chapter %d") % data.count:
                            style "btn_chapters_selection"
                            action [Show('submenu_chapter_' + str(data.count)), menuChaptersButtonAction(data.count)]
    '''
