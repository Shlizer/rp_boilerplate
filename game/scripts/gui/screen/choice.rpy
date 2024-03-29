## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##

screen choice(items):
    style_prefix "choice"
    default choice_hover = None

    vbox:
        for i in range(len(items)):
            button:
                hovered [SetLocalVariable('choice_hover', i), With(Dissolve(0.1))]
                unhovered [SetLocalVariable('choice_hover', None), With(Dissolve(0.1))]
                action items[i].action

                hover_sound "audio/sound/btn_hover.wav"
                activate_sound "audio/sound/btn_click.wav"

                if (choice_hover == i):
                    background Frame("images/gui/choice_box_hover.png", 2, 2, 2, 2, Tile=True)
                    text items[i].caption color "#eeeeee"
                else:
                    background Frame("images/gui/choice_box_idle.png", 2, 2, 2, 2, Tile=True)
                    text items[i].caption

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
