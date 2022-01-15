init python:
    #achievements_worker_started = False

    def phone_worker():
        global phone

        if phone.opened and not renpy.get_screen('phone_opened'):
            #achievements_worker_started = True
            renpy.show_screen('phone_opened')
            renpy.restart_interaction()
        elif not phone.opened and renpy.get_screen('phone_opened'):
            renpy.hide_screen('phone_opened')
            renpy.restart_interaction()

    config.periodic_callbacks.append(phone_worker)
