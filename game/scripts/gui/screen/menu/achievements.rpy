screen submenu_achievements():
    default trophy_hover = None
    $ counter = achievements.getCount()

    use submenu(_("Achievements")):
        vpgrid:
            cols 2
            spacing 10

            ## Granted or in progress achievements
            for trophy in achievements.getGrantedOrInProgress():
                button:
                    if trophy_hover == trophy.id:
                        if trophy.finished:
                            background Solid('#08c')
                        else:
                            background Solid('#757575')
                    else:
                        if trophy.finished:
                            background Solid('#08A')
                        else:
                            background Solid('#6b6b6b')

                    hovered [SetLocalVariable('trophy_hover', trophy.id), With(Dissolve(0.1))]
                    unhovered [SetLocalVariable('trophy_hover', None), With(Dissolve(0.1))]
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
                        hovered [SetLocalVariable('trophy_hover', trophy.id), With(Dissolve(0.1))]
                        unhovered [SetLocalVariable('trophy_hover', None), With(Dissolve(0.1))]
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

