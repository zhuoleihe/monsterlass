import random

class Base:
    # This initializes new instances of the class with the following values
    def __init__(self, name, species, hp=10, atk=2):  # Note the default values set for hp and attack
        self.name = name
        # the species of the object -- 'monster' or 'player'
        self.species = species
        self.hp = hp
        self.atk_damage = atk

    def isDeath(self):
        if self.hp <= 0:
            if self.species == 'player':
                print('{} {} has fainted. Do you want to continue?'.format(self.species, self.name))
            else:
                print('{} {} has been defeated! Do you wish to continue?'.format(self.species, self.name))
        else:
            print('{} {} is still alive'.format(self.species, self.name))

    def attack(self, enemy, name, hit, max_damage):  # This method combines all the methods together into one call
        hit_roll = random.randint(0, 100)
        print('{} {} hit roll is {}'.format(self.species, self.name, hit_roll))  # Prints out the value that was randomly rolled

        if hit >= hit_roll:
            print('{} {} used {} successfully'.format(self.species, self.name, name))
            enemy.dmgTaken(self.dmgDealt(max_damage))
        else:
            print(self.name, 'used', name, 'and failed')

    def dmgTaken(self, dmg):  # This function reduces the hp of the unit based on the dmg parameter
        self.hp = self.hp - dmg
        print('{} {} took {} points of damage!'.format(self.species, self.name, dmg))
        print('{} {} has {} hit points left.'.format(self.species, self.name, self.hp))
        self.isDeath()

    def dmgDealt(self, max_damage):
        dmg = random.randint(self.atk_damage, max_damage)
        return dmg

monsters = {'a': {'name': 'Kaito', 'hp': 15, 'atk': 3, 'move1': 'tackle', 'move2': 'string shot', 'move3': 'headbutt'},
                'b': {'name': 'Ai', 'hp': 35, 'atk': 3, 'move1': 'tackle', 'move2': 'bite', 'move3': 'headbutt'},
                'c': {'name': 'Harley', 'hp': 50, 'atk': 3, 'move1': 'tackle', 'move2': 'quick attack', 'move3': 'headbutt'}}

move_list = {'tackle': {'hit_rate': 60, 'power': 10},
             'string shot': {'hit_rate': 90, 'power': 5},
             'headbutt': {'hit_rate': 50, 'power': 20},
             'bite': {'hit_rate': 80, 'power': 10},
             'quick attack': {'hit_rate': 90, 'power': 15}}
  #choose a monster
n = 'a'

player = Base('Conan', 'player')

    # Creates the instances that defines the monster, note that the name is pulled from the dictionary index 'n'
monster = Base(monsters[n]['Kaito'], 'monster')

monster.hp = monsters[n]['hp']
monster.atk_damage = monsters[n]['atk']

def atk_seq(name, hit, power):
    player.attack(monster, name, hit, power)
    move_choice = ['move1', 'move2', 'move3']
    move_select = random.choice(move_choice)
    monster.attack(player, monsters[n][move_select], move_list[monsters[n][move_select]]['hit_rate'],
                       move_list[monsters[n][move_select]]['power'])

atk_seq('Thundershock', 90, 10)
