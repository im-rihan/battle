from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

# Creating Some Black Magic
fire = Spell('Fire', 10, 100, 'Black')
thunder = Spell('Thunder', 10, 100, 'Black')
blizzard = Spell('Blizzard', 10, 100, 'Black')
quack = Spell('Quack', 20, 200, 'Black')
meteor = Spell('Meteor', 14, 140, 'Black')

# Creating Some White Magic
cure = Spell('Cure', 12, 120, 'White')
cura = Spell('Cura', 18, 180, 'White')

# Creating Some Items
potion = Item('Potion', 'potion', 'heals 50 hp', 50)
hipotion = Item('Hi-Potion', 'potion', 'heals 100 hp', 100)
superpotion = Item('Super-Potion', 'potion', 'heals 500 hp', 500)
elixer = Item('Elixer', 'elixer',
              'fully recover hp/mp of one party member', 9999)
hielixer = Item('Hi-Elixer', 'elixer',
                'fully recover partys member hp/mp', 9999)
grenade = Item('Grenade', 'grenade', 'deals 500 damage', 500)

# Instantiate People
player_spells = [fire, thunder, blizzard, quack, meteor, cure, cura]
player_item = [{'item': potion, 'quantity': 5}, {
    'item': hipotion, 'quantity': 5}, {'item': superpotion, 'quantity': 10},
    {'item': elixer, 'quantity': 15}, {'item': hielixer, 'quantity': 20},
    {'item': grenade, 'quantity': 3}]

player = Person(400, 40, 50, 30, player_spells, player_item)
enemy = Person(400, 50, 45, 20, [], [])

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
        print('You Attacked For ', dmg, 'player hp is', enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        choice_magic = int(input('Choose Magic :'))-1

        if choice_magic == -1:
            continue

        spell = player.magic[choice_magic]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL+'\n not enough MP' + Bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == 'White':
            player.heal(magic_dmg)
            print(Bcolors.OKBLUE + '\n' + spell.name + ' heals for ',
                  str(magic_dmg), 'Hp ' + Bcolors.ENDC)
        elif spell.type == 'Black':
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + '\n' + spell.name + ' deals',
                  str(magic_dmg), 'Points Of Damage' + Bcolors.ENDC)
    elif index == 2:
        player.choose_items()
        choice_item = int(input('Choose Item :'))-1
        if choice_item == -1:
            continue

        item = player.items[choice_item]['item']
        if player.items[choice_item]['quantity'] == 0:
            print(Bcolors.FAIL + '\n' + 'None Left ' + Bcolors.ENDC)
            continue
        player.items[choice_item]['quantity'] -= 1

        if item.type == 'potion':
            print(Bcolors.OKBLUE + '\n' + item.name + ' heals for',
                  str(item.prop), 'hp' + Bcolors.ENDC)
        elif item.type == 'elixer':
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(Bcolors.WARNING + '\n' + item.name +
                  'fully restored hp/mp' + Bcolors.ENDC)
        elif item.type == 'attack':
            enemy.take_damage(item.prop)
            print(Bcolors.FAIL + '\n' + item.name + 'deals ',
                  str(item.prop) + 'points of Damage'+Bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy deals for', enemy_dmg,
          ' damage. Player hp is', player.get_hp())

    print('===============')

    print('Enemy Hp', Bcolors.FAIL +
          str(enemy.get_hp())+'/'+str(enemy.get_max_hp())+Bcolors.ENDC)
    print('Your Hp', Bcolors.OKBLUE +
          str(player.get_hp())+'/'+str(player.get_max_hp())+Bcolors.ENDC + '\n')
    print('your Mp', Bcolors.OKGREEN + str(player.get_mp()) +
          '/'+str(player.get_max_mp())+Bcolors.ENDC)
    print('Enemy Mp', Bcolors.WARNING + str(enemy.get_mp()) +
          '/'+str(enemy.get_max_mp())+Bcolors.ENDC + '\n')

    if enemy.get_hp() == 0:
        print(Bcolors.OKBLUE + 'You Win ' + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + 'You Lost ' + Bcolors.ENDC)
        running = False
