init python:
    achievements_worker_started = False

    def achievements_worker():
        global achievements
        global achievements_worker_started

        if len(achievements.toAdd) and not achievements_worker_started and not renpy.get_screen('achievements_toast'):
            achievements_worker_started = True
            renpy.show_screen('achievements_toast')
            renpy.restart_interaction()

    config.periodic_callbacks.append(achievements_worker)
