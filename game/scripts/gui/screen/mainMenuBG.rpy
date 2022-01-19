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
    frame:
        add TrackCursor("images/main_menu/bg.jpg", 22):
            xalign 0.85
            yalign 0.8
        add TrackCursor("main_menu_rain", 22) at center
        add TrackCursor("images/main_menu/fg.png", 16) at center

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
