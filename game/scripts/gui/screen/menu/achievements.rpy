screen submenu_achievements():
    default trophy_hover = None
    $ counter = achievements.getCount()
    style_prefix "achievements"

    use submenu(_("Achievements") + " {:01d}/{}".format(counter[0], counter[1])):
        frame:
            background '#ff0000da'
            padding (0,0,0,0)
            xsize 1.0
            ysize 1.0

            vpgrid:
                cols 4
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True
                scrollbars "vertical"

                ## Granted or in progress achievements
                use achievement_list(achievements.getGrantedOrInProgress())
                
                ## Locked achievements
                use achievement_list(achievements.getLocked())

transform achievement_button_hover:
    on idle:
        easeout 0.3 alpha 0.7

    on hover:
        easeout 0.3 alpha 1.0

screen achievement_list(list, active=False):
    default trophy_hover = None
    style_prefix "achievements_list"

    for trophy in list:
        button at achievement_button_hover:
            #style "achievement_list_btn"

            if trophy_hover == trophy.id:
                background Solid('#08c' if trophy.finished else '#757575')
            else:
                background Solid('#08A' if trophy.finished else '#6b6b6b')
             
            hovered [SetLocalVariable('trophy_hover', trophy.id), With(Dissolve(0.1))]
            unhovered [SetLocalVariable('trophy_hover', None), With(Dissolve(0.1))]
            action [Function(achievements.revoke if trophy.finished else achievements.grant, trophy.id)]

            hbox:
                yalign 0.5
                spacing 0

                $ trophy_icon = trophy.icon if (trophy.finished or not trophy.isSecret) else"images/achievements/__locked.png"
                
                ## This will display a locked icon if it should be hidden.
                add trophy_icon:
                    size (120, 120)
                    xalign 0.0
                    yalign 0.5

                null width 20

$'''
                vbox:
                    spacing 0
                    yfill False

                    #if not trophy.isSecret:
                    #    text trophy.name style 'achievements_label' color '#FFF3'
                    #    text trophy.description color '#FFF3'
                    #else:
                    #    text _('Hidden Achievement') style 'achievements_label' color '#FFF3'
                    
                    if trophy.amountMax > 0:
                        $ _trophy_name = trophy.name + ' (' + str(trophy.amount or 0) + '/' + str(trophy.amountMax) + ')'
                    else:
                        $ _trophy_name = trophy.name

                    text _trophy_name style 'achievements_label' color '#000'
                    text trophy.description color '#000'

                    if trophy.finished:
                        text getTime(trophy.finishDate) color '#000'
'''

style achievements_vpgrid is vpgrid
style achievements_vpgrid_scrollbar is gui_vscrollbar

style achievements_vpgrid:
    xsize 1.0
    ysize 1.0
    spacing 20

style achievements_vpgrid_scrollbar:
    size 1
    thumb Solid('#ffff0080')
    left_gutter 20
    right_gutter 20

style achievements_list_button is button:
    minimum (311, 150)
    maximum (311, 150)
    padding (10, 10, 10, 10)
