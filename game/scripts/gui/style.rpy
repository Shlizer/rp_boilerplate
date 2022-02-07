define gui.color_primary_light = '#c08650'
define gui.color_primary_dark = '#784a18'
define gui.color_primary_darker = '#402100'
define gui.color_primary_action = '#9b6328'

define gui.color_text_light = "#f5e5e5"
define gui.color_text = "#dbd0d0"

define gui.color_dark_1 = "#333333e7"
define gui.color_dark_2 = "#252525"

define gui.audio_btn_hover = "audio/sound/btn_hover.wav"
define gui.audio_btn_click = "audio/sound/btn_click.wav"


#################################################################
## BUTTONS
#################################################################
define gui.color_button_menu_idle = gui.color_dark_2
define gui.color_button_menu_hover = gui.color_primary_dark
define gui.color_button_menu_selected = gui.color_primary_light
define gui.color_button_menu_selected_hover = gui.color_primary_action
define gui.color_button_menu_text = "#838383"
define gui.color_button_menu_text_hover = gui.color_primary_darker

define gui.color_button_light_idle = gui.color_button_menu_idle + "50"
define gui.color_button_light_hover = gui.color_button_menu_idle
define gui.color_button_light_border = gui.color_button_menu_hover + "60"
define gui.color_button_light_border_hover = gui.color_button_menu_hover

define gui.color_button_light_selected = gui.color_button_menu_selected + "50"
define gui.color_button_light_selected_hover = gui.color_button_menu_selected
define gui.color_button_light_selected_border = gui.color_button_menu_selected_hover + "50"
define gui.color_button_light_selected_border_hover = gui.color_button_menu_selected_hover

init python:
    def getUIComposite(width, height, *args):
        compositeArgs = [(width, height)]

        for arg in args:
            compositeArgs.append((0,0))
            compositeArgs.append(AlphaMask(Solid(arg[0]), arg[1]))

        return Composite(*compositeArgs)

    def getUICompositeFrame(width, height, border, *args):
        return Frame(getUIComposite(width, height, *args), Borders(*border))

    def getUIBtnLight():
        return Composite(
            (40, 42),
            (0,0), AlphaMask(Solid(gui.color_button_light_bg), "images/btn_light_bg.png"),
            (0,0), AlphaMask(Solid(gui.color_button_light_border), "images/btn_light_border.png"),
        )
    def getUIBtnLightHover():
        return Composite(
            (40, 42),
            (0,0), AlphaMask(Solid(gui.color_button_light_bg), "images/btn_light_bg.png"),
            (0,0), AlphaMask(Solid(gui.color_button_light_border), "images/btn_light_border.png"),
        )
    def getUIBtnLightSelected():
        return Composite(
            (40, 42),
            (0,0), AlphaMask(Solid(gui.color_button_light_selected_bg), "images/btn_light_bg.png"),
            (0,0), AlphaMask(Solid(gui.color_button_light_selected_border), "images/btn_light_border.png"),
        )
    def getUIBtnLightSelectedHover():
        return Composite(
            (40, 42),
            (0,0), AlphaMask(Solid(gui.color_button_light_selected_bg), "images/btn_light_bg.png"),
            (0,0), AlphaMask(Solid(gui.color_button_light_selected_border), "images/btn_light_border.png"),
        )

style btn_basic is gui_button
style btn_menu is btn_basic
style btn_menu_selected is btn_basic
style btn_light is btn_basic
style btn_light_selected is btn_basic

style btn_basic:
    mouse "choice"
    hover_sound gui.audio_btn_hover
    activate_sound gui.audio_btn_click

style btn_menu:
    background getUICompositeFrame(32, 64, (31,31,3,3), (gui.color_button_menu_idle, "images/btn_menu_bg.png"))
    hover_background getUICompositeFrame(32, 64, (31,31,3,3), (gui.color_button_menu_hover, "images/btn_menu_bg.png"))
    selected_background getUICompositeFrame(32, 64, (31,31,3,3), (gui.color_button_menu_selected, "images/btn_menu_bg.png"))
    selected_hover_background getUICompositeFrame(32, 64, (31,31,3,3), (gui.color_button_menu_selected_hover, "images/btn_menu_bg.png"))
    xpos 0
    selected_xpos -60
    padding(50, 0, 40, 0)
    minimum (32, 61)
    xanchor 1.0
    xoffset 0

style btn_light_small:
    background getUICompositeFrame(20, 29, (9,9,9,9), (gui.color_button_light_idle, "images/btn_light_small_bg.png"), (gui.color_button_light_border, "images/btn_light_small_border.png"))
    hover_background getUICompositeFrame(20, 29, (9,9,9,9), (gui.color_button_light_hover, "images/btn_light_small_bg.png"), (gui.color_button_light_border_hover, "images/btn_light_small_border.png"))
    selected_background getUICompositeFrame(20, 29, (9,9,9,9), (gui.color_button_light_selected, "images/btn_light_small_bg.png"), (gui.color_button_light_selected_border, "images/btn_light_small_border.png"))
    selected_hover_background getUICompositeFrame(20, 29, (9,9,9,9), (gui.color_button_light_selected_hover, "images/btn_light_bg.png"), (gui.color_button_light_selected_border_hover, "images/btn_light_small_border.png"))
    padding (20, 10, 20, 10)
    minimum (20, 29)

style btn_light:
    background getUICompositeFrame(40, 42, (20,20,20,20), (gui.color_button_light_idle, "images/btn_light_bg.png"), (gui.color_button_light_border, "images/btn_light_border.png"))
    hover_background getUICompositeFrame(40, 42, (20,20,20,20), (gui.color_button_light_hover, "images/btn_light_bg.png"), (gui.color_button_light_border_hover, "images/btn_light_border.png"))
    selected_background getUICompositeFrame(40, 42, (20,20,20,20), (gui.color_button_light_selected, "images/btn_light_bg.png"), (gui.color_button_light_selected_border, "images/btn_light_border.png"))
    selected_hover_background getUICompositeFrame(40, 42, (20,20,20,20), (gui.color_button_light_selected_hover, "images/btn_light_bg.png"), (gui.color_button_light_selected_border_hover, "images/btn_light_border.png"))
    xpos 0
    selected_xpos -30
    padding (20, 10, 20, 10)
    minimum (40, 42)

style btn_menu_text is gui_button_text:
    color "#FF0000"



#################################################################
## CHECKBOX / RADIOBOX
#################################################################
style checkbox:
    background getUIComposite(32, 31, (gui.color_primary_darker, "images/checkbox_bg.png"), (gui.color_button_light_border, "images/checkbox_border.png"))
    hover_background getUIComposite(32, 31, (gui.color_primary_action, "images/checkbox_bg.png"), (gui.color_button_light_border_hover, "images/checkbox_border.png"))
    selected_background getUIComposite(32, 31, (gui.color_primary_dark, "images/checkbox_bg.png"), (gui.color_button_light_border, "images/checkbox_border.png"))
    selected_hover_background getUIComposite(32, 31, (gui.color_primary_action, "images/checkbox_bg.png"), (gui.color_button_light_border_hover, "images/checkbox_border.png"))
    xsize 32
    ysize 31


#################################################################
## PANELS
#################################################################
define gui.color_panel_bg = gui.color_dark_2 + "dd"
define gui.color_panel_border = gui.color_primary_action


init python:
    def getUIPanel():
        return Composite(
            (391, 406),
            (0,0), AlphaMask(Solid(gui.color_panel_bg), "images/panel_1_bg.png"),
            (0,0), AlphaMask(Solid(gui.color_panel_border), "images/panel_1_border.png"),
        )
    def getUIPanelFlip():
        return Composite(
            (391, 406),
            (0,0), AlphaMask(Solid(gui.color_panel_bg), "images/panel_1_flip_bg.png"),
            (0,0), AlphaMask(Solid(gui.color_panel_border), "images/panel_1_flip_border.png"),
        )


style panel:
    background Frame(getUIPanel(), 183, 180, 146, 174)
    padding (25, 25, 25, 25)
    minimum (391, 406)

style panel_flip:
    background Frame(getUIPanelFlip(), 183, 174, 146, 180)
    padding (25, 25, 25, 25)
    minimum (391, 406)


#################################################################
## TITLES
#################################################################
init python:
    def getUITitle():
        return Composite(
            (54, 61),
            (0,0), AlphaMask(Solid(gui.color_panel_border), "images/title_bg.png"),
        )


style title_text is gui_button_text


style title:
    background Frame(getUITitle(), 31, 31, 25, 25)
    padding (40, 0, 50, 0)
    minimum (54, 61)
style title_text:
    color gui.color_text
    size 30
