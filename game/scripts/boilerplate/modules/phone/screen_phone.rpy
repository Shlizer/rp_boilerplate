init python:
    def getPhoneBG():
        return Composite(
            #(550, 1056),
            (452, 970),
            (0,0), phone.wallpaper,
            (0,0), Solid("#000000bb", xsize=452, ysize=37),
            (0,900), Solid("#000000bb", xsize=452, ysize=70),
        )

define phone_toggle_time = 0.2

transform phone_backdrop_toggle:
    subpixel True
    on show:
        alpha 0
        linear phone_toggle_time alpha 1.0

    on hide:
        alpha 1.0
        linear phone_toggle_time alpha 0

transform phone_toggle:
    subpixel True
    on show:
        zoom 0.1
        linear phone_toggle_time zoom 1.0

    on hide:
        zoom 1.0
        linear phone_toggle_time zoom 0

default app_hover = None

screen phone_opened:
    zorder 350

    ########################################
    # Backdrop
    ########################################
    frame at phone_backdrop_toggle:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        background None

        imagebutton:
            idle Solid("#00000080")
            xpos 0
            ypos 0
            xsize X_RES
            ysize Y_RES
            action [
                SetVariable('config.rollback_enabled', phone.opened),
                Function(phone.toggle),
                With(Dissolve(0.2))
            ]

    ########################################
    # Phone view
    ########################################
    frame at phone_toggle:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
        yanchor 0.5
        background None

        # phone wallpaper
        image getPhoneBG():
            xsize 452
            ysize 970
            xalign 0.5
            yalign 0.5
            xanchor 0.5
            yanchor 0.5

        # phone background
        image "images/phone/bg.png":
            xalign 0.5
            yalign 0.5
            xanchor 0.5
            yanchor 0.5

        # phone content
        frame:
            background None
            xsize 442
            ysize 850
            xalign 0.5
            yalign 0.5
            xanchor 0.5
            yanchor 0.5
            yoffset -15

            vpgrid:
                cols 3
                spacing 10
                area (0, 0, 432, 825)
                mousewheel True
                draggable True

                if len(phone.getApps()) > 18:
                    scrollbars "vertical"

                side_xalign 0.5

                for app in phone.getApps():
                    button:
                        xysize (128, 128)
                        align (0.5, 0.5)
                        padding (15, 15, 15, 15)

                        if not app.active:
                            background Solid('#444')
                        elif app_hover == app.name:
                            background Solid('#08c')
                        else:
                            background Solid('#08A')

                        hovered [SetLocalVariable('app_hover', app.name), With(Dissolve(0.1))]
                        unhovered [SetLocalVariable('app_hover', None), With(Dissolve(0.1))]

                        if app.active:
                            tooltip app.name
                            action app.action
                        else:
                            action NullAction()

        # phone bot icons
        frame:
            background None
            xsize 340
            ysize 50
            xalign 0.5
            yalign 0.5
            xanchor 0.5
            yanchor 0.5
            yoffset 440

            hbox:
                xsize 340
                ysize 50
                imagebutton auto "images/phone/icon_1_%s.png" xalign 0.0 yalign 0.5 action NullAction()
                imagebutton auto "images/phone/icon_2_%s.png" xalign 0.5 yalign 0.5 action NullAction()
                imagebutton auto "images/phone/icon_3_%s.png" xalign 1.0 yalign 0.5 action NullAction()

    add mouseTooltip
