define achievements_toast_wait = 2.5

transform achievement_appear:
    subpixel True
    on show:
        yoffset -110
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset 0.0

    on hide:
        yoffset 0.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset -110.0

screen achievements_toast:
    zorder 500

    if len(achievements.toAdd):
        button at achievement_appear:
            background "#82919690"
            xsize 270
            ysize 100
            xpos 10
            ypos 10
            text achievements.toAdd[0].name

            timer achievements_toast_wait action [
                Hide('achievements_toast'),
                Show('achievements_toast_waiter'),
            ]

screen achievements_toast_waiter:
    timer 0.4 action [
        Function(achievements.popShown),
        Hide('achievements_toast_waiter'),
        SetVariable('achievements_worker_started', False)
    ]
