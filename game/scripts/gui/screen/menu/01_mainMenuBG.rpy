init offset = -60
   
transform main_menu_rain_animation:
    "images/main_menu/rain1.png"
    pause 0.05
    "images/main_menu/rain2.png"
    pause 0.05
    "images/main_menu/rain3.png"
    pause 0.05
    "images/main_menu/rain4.png"
    pause 0.05
    "images/main_menu/rain5.png"
    pause 0.05
    repeat
    
image main_menu_rain:
    contains main_menu_rain_animation

screen main_menu_bg():
    key "K_ESCAPE" action Function(print, 'K_ESCAPE')#Show('game_menu')
    frame:
        add "images/main_menu/bg.jpg" at float_with_mouse(22):
            xoffset -(2120 - X_RES)
            yoffset -(1280 - Y_RES)
        add "main_menu_rain" at float_with_mouse(22):
            xoffset -(2120 - X_RES)
            yoffset -(1280 - Y_RES)
        add "images/main_menu/fg.png" at float_with_mouse(16):
            xoffset -(2120 - X_RES)
            yoffset -(1280 - Y_RES)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30
