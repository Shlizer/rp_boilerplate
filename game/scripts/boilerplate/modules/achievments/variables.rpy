init -100 python:
    achievements = Achievements()
    achievements.register('buy', 'Whale!', 'Buy and launch this game.', 'buy')
    achievements.register('secret1', 'Secret 1', 'This one is a secret.', 'secret', isSecret=True)
    achievements.register('secret2', 'Secret 2', 'This one is a secret.', 'secret', isSecret=True)


    achievements.register('second', 'Second!', 'Some second achievement.', 'second')
    achievements.register('third', 'Third!', 'Some third achievement.', 'third')
    achievements.register('progress', 'Progress', 'Achievement with progress', 'progress', amountMax = 100)
    achievements.register('progress2', 'Progress2', 'Another achievement with progress', 'progress', amount=5, amountMax = 100)
    achievements.register('finish', 'Atta boy!', 'Finish game at least once.', 'finish')

    achievements.register('second2', 'Second!', 'Some second achievement.', 'second')
    achievements.register('third2', 'Third!', 'Some third achievement.', 'third')
    achievements.register('progress3', 'Progress', 'Achievement with progress', 'progress', amountMax = 100)
    achievements.register('progress4', 'Progress2', 'Another achievement with progress', 'progress', amount=5, amountMax = 100)
    achievements.register('finish2', 'Atta boy!', 'Finish game at least once.', 'finish')

    #achievements.register('second3', 'Second!', 'Some second achievement.', 'second')
    #achievements.register('third3', 'Third!', 'Some third achievement.', 'third')
    #achievements.register('progress5', 'Progress', 'Achievement with progress', 'progress', amountMax = 100)
    #achievements.register('progress6', 'Progress2', 'Another achievement with progress', 'progress', amount=5, amountMax = 100)
    #achievements.register('finish3', 'Atta boy!', 'Finish game at least once.', 'finish')

    achievements.register('secret3', 'Secret 3', 'This one is a secret.', 'secret', isSecret=True)
    achievements.register('secret4', 'Secret 4', 'This one is a secret.', 'secret', isSecret=True)

    achievements.init()
