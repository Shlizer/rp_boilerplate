init -100 python:
    achievements = Achievements()
    achievements.register('welcome', 'Welcome!', 'Finish intro of the game.', 'welcome.png')
    achievements.register('existing', 'Err!', 'Only to receive error.', 'error.png', isHidden=True)
    achievements.register('existing', 'Err!', 'Only to receive error.', 'error.png', isHidden=True)
    achievements.register('second', 'Second!', 'Some second achievement.', 'second.png')
    achievements.register('third', 'Third!', 'Some third achievement.', 'third.png')
    achievements.register('progress', 'Progress', 'Achievement with progress', 'progress.png', amountMax = 100)
    achievements.register('progress2', 'Progress2', 'Another achievement with progress', 'progress.png', amount=5, amountMax = 100)
    achievements.register('forth', 'Forth!', 'Some forth achievement.', 'forth.png')
    achievements.register('secret', 'Secret!', 'This one is a secret.', 'secret.png', isSecret=True)

    achievements.init()
