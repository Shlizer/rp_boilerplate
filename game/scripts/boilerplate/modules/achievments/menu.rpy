init offset = -60

screen achievement_menu():
    tag menu

    default _trophy_hover = None
    $ counter = achievements.getCount()

    use game_menu(_("Achievements") + " | {:01d}/{}".format(counter[0], counter[1]), scroll="viewport"):
        style_prefix "achievements"

        frame:
            background None
            padding (20, 20, 20, 20)
            align (0.0, 0.0)
            ysize 1080

            vpgrid:
                cols 2
                spacing 10

                ## Granted or in progress achievements
                for trophy in achievements.getGrantedOrInProgress():
                    button:
                        if _trophy_hover == trophy.id:
                            if trophy.finished:
                                background Solid('#08c')
                            else:
                                background Solid('#757575')
                        else:
                            if trophy.finished:
                                background Solid('#08A')
                            else:
                                background Solid('#6b6b6b')

                        hovered [SetLocalVariable('_trophy_hover', trophy.id), With(Dissolve(0.1))]
                        unhovered [SetLocalVariable('_trophy_hover', None), With(Dissolve(0.1))]
                        action [Function(achievements.revoke, trophy.id)]

                        hbox:
                            yalign 0.5
                            xysize (100, 100)
                            #add trophy.icon size (100, 100) yalign 0.5

                            null width 20

                            vbox:
                                spacing 0
                                yfill False
                                
                                if trophy.amountMax > 0:
                                    $ _trophy_name = trophy.name + ' (' + str(trophy.amount or 0) + '/' + str(trophy.amountMax) + ')'
                                else:
                                    $ _trophy_name = trophy.name

                                text _trophy_name style 'achievements_label' color '#000'
                                text trophy.description color '#000'

                                if trophy.finished:
                                    text getTime(trophy.finishDate) color '#000'

                ## Locked achievements
                for trophy in achievements.getLocked():

                    button:
                        hovered [SetLocalVariable('_trophy_hover', trophy.id), With(Dissolve(0.1))]
                        unhovered [SetLocalVariable('_trophy_hover', None), With(Dissolve(0.1))]
                        action [Function(achievements.grant, trophy.id)]

                        hbox:
                            yalign 0.5
                            xysize (100, 100)
                            ## This will display a locked icon.
                            #add 'gui/images/achievements/_locked.png' size (100, 100) yalign 0.5

                            null width 20

                            vbox:
                                spacing 0
                                yfill False

                                if not trophy.isSecret:
                                    text trophy.name style 'achievements_label' color '#FFF3'
                                    text trophy.description color '#FFF3'
                                else:
                                    text _('Hidden Achievement') style 'achievements_label' color '#FFF3'

style victory_message_text:
    color "#000"
    size 20

transform achievement_appear:
    subpixel True
    on show:
        yoffset -160.0 alpha 1.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset 0.0

    on hide:
        yoffset 0.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset -160.0
        alpha 0.0


style achievements_vbox is vbox
style achievements_text is text
style achievements_button is frame

style achievements_vbox:
    minimum (330, 100)
    maximum (360, 100)
    spacing 2
    yfill False

style achievements_label:
    size 26
    outlines [(1, '#00000022', 0, 1)]
    yalign 0.5

style achievements_text:
    size 16
    yalign 0.5

style achievements_locked_text:
    antialias True
    color "#555555"
    size 16

style achievements_button:
    background Solid('#444444')
    minimum (500, 140)
    align (0.5, 0.5)
    padding (15, 15, 15, 15)