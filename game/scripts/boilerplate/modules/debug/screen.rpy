init -10 python:
    class DebugAddon(object):
        def __init__(self, value, type='text', action=None):
            self.value = value
            self.type = type
            self.action = action

    class DebugClass(object):
        more = {}

        def __init__(self):
            config.periodic_callbacks.append(self.debug_screen_show)

            self.add('__label', "Label: [current_label]")
            self.add('__daytime', "Daytime: [daytime]", type='textbutton', action=self.changeDaytime)

        def debug_screen_show(self):
            if not renpy.show_screen('debug'):
                renpy.show_screen('debug')

        def changeDaytime(self):
            global daytime
            if (daytime == Daytime.morning):
                daytime = Daytime.evening
            if (daytime == Daytime.evening):
                daytime = Daytime.night
            if (daytime == Daytime.night):
                daytime = Daytime.morning

        def add(self, id, value, type='text', action=None):
            self.more[id] = DebugAddon(value, type, action)

        def remove(self, id):
            if self.more[id]:
                self.more[id] = None

    DEBUG = DebugClass()

default persistent.debug_opened = False

transform debug_hover:
    on idle:
        easein 0.2 xoffset 80
    on hover:
        easein 0.2 xoffset 0

screen debug_button():
    if persistent.debug_opened:
        button:
            style "debug_button"
            action SetVariable('persistent.debug_opened', not persistent.debug_opened)
            transclude
    else:
        button at debug_hover:
            style "debug_button"
            action SetVariable('persistent.debug_opened', not persistent.debug_opened)
            transclude

screen debug():
    zorder 500

    vbox:
        xanchor 1.0
        yanchor 0
        xpos 1.0
        xoffset -20
        ypos 20

        use debug_button:
            text "DEBUG" size (gui.text_size / 1.5)

        if persistent.debug_opened == True:
            frame:
                background "#99000090"

                vbox:
                    for id in DEBUG.more:
                        if DEBUG.more[id]:
                            if DEBUG.more[id].type == 'text':
                                text DEBUG.more[id].value:
                                    size gui.text_size / 2
                            elif DEBUG.more[id].type == 'textbutton':
                                textbutton DEBUG.more[id].value:
                                    xpos -7
                                    ysize gui.text_size / 2 + 2
                                    text_size gui.text_size / 2
                                    text_idle_color "#ffffff"
                                    text_hover_color "#e0e0e0"
                                    action DEBUG.more[id].action

style debug_button:
    xalign 1.0
    xanchor 1.0
    xsize 100
    padding (10, 10, 10, 10)
    background "#99000090"
