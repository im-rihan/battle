from classes.game import Person, Bcolors

magic = [{'name': 'Fire', 'cost': 10, 'damage': 60},
         {'name': 'Thunder', 'cost': 10, 'damage': 80},
         {'name': 'Blizzerd', 'cost': 10, 'damage': 90}, ]

player = Person(500, 40, 50, 30, magic)
enemy = Person(1000, 50, 45, 20, magic)

running = True
i = 0
while running:
    print('===================')
    player.choose_action()
    choice = input('Choose Actions :')
    index = int(choice)-1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You Attacked For ', dmg, 'Points Of Damage', enemy.get_hp())
