label start:
    jump test_choice

label test_choice:
    menu:
        "Achievements":
            jump achievements
        "Debug":
            jump test_debug
        "Exit":
            return

label achievements:
    menu:
        "Open menu":
            $ renpy.call_screen("achievement_menu")
            jump achievements
        "Add one":
            $ achievements.grant('welcome')
            jump achievements
        "Add more":
            $ achievements.grant('welcome')
            $ achievements.grant('second')
            $ achievements.grant('third')
            jump achievements
        "Add 15 to progress achievement":
            $ achievements.grant('progress', 15)
            jump achievements
        "Clear achievements":
            $ achievements.revokeAll()
            jump achievements
        "Back":
            jump test_choice

label test_debug:
    $ debug_mc_name = 'unknown'
    "This part is about debug panel. It can be opened and closed by clicking button on the right top corner and it's state is saved after closing app."
    "Currently it shows only default options, but it can be dynamically expanded with extra lines. Now, I'll add MC name variable to track there."
    $ DEBUG.add('mc_name', "MC: [debug_mc_name]")

    "OK, it should be already visible in opened panel. This time I'll try to change it to different value."
    $ debug_mc_name = 'Johnny'

    "Did it change? It should. Now I'll remove it and go back to menu of this preview."
    $ DEBUG.remove('mc_name')

    jump test_choice
