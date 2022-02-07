init -900 python:
    class MouseTooltip(renpy.Displayable):
        x = 0
        y = 0

        def __init__(self, **kwargs):
            super(renpy.Displayable, self).__init__(**kwargs)
            self.text = Text("")
            self.textsize = 14
            self.textcolor = Color("#FFF")
            self.padding = 12
            self.bold = False
            self.backgroundcolor = Color("#7777") # use something like #0007 for real VN
            self.x = 10
            self.y = 30

        def event(self, ev, x, y, st):
            import pygame
            # ignore all events except MOUSEMOTION
            # not sure whether events like MOUSEBUTTONDOWN update the position too and should therefore be added here?!
            if ev.type != pygame.MOUSEMOTION:
                return None
            self.x = x
            self.y = y
            tooltip = GetTooltip()
            if tooltip:
                self.text = Text(tooltip, size=self.textsize, color=self.textcolor, xpos=self.padding, ypos=self.padding, bold=self.bold)
                renpy.redraw(self, 0)
            elif self.text.text != [""]: # avoid unnecessary redraw calls
                self.text = Text("") # if there is no tooltip clear the text just once
                renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            # avoid to render an empty rectangle when the text got cleared
            if self.text.text != [""]:
                w, h = self.text.size()
                render = renpy.Render(w, h)

                # if tooltip is close to the top or right side make sure it stays on the screen
                x = self.x + self.padding
                if x > config.screen_width - w - self.padding:
                    x = config.screen_width - w - self.padding
                
                y = self.y-h-self.padding*2 # -h to place text above cursor
                if y < 0:
                    y = 0


                # fixed = transparent background rectangle
                fixed = Fixed(self.backgroundcolor, xpos=-self.padding, xsize=int(w)+self.padding*2, ysize=int(h)+self.padding*2, zorder=900)
                fixed.add(self.text)
                render.place(fixed, x+20, y+50)
                return render
            return renpy.Render(1, 1)

define mouseTooltip = MouseTooltip()
