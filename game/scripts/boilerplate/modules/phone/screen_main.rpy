screen phone_main:
    zorder 350

    ########################################
    # Cellphone icon
    ########################################
    imagebutton:
        auto "images/phone/icon_%s.png"
        yalign 1.0
        xpos 30
        yoffset -30
        action [
            SetVariable('config.rollback_enabled', phone.opened),
            Function(phone.toggle),
            With(Dissolve(0.2))
        ]

    text "phone opened: " + str(phone.opened)
