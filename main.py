############################################################################################
#                                TO DO LIST
#
#       Differentiate between spec types and give different health values accordingly
#       Update basic combat to include enemy actions
#               make enemies attacks automated
#
#       Give health a maximum value
#       Potential long term addition of status effects such as Damage Reduction and make it effect attacks etc.
#       separate classes from main and generally organize codebase
###########################################################################################


class Character:

    specialization = None
    name = None
    character_type = None
    current_abilities = []
    health = 30

    status_effects = {'Crowd-Control': {'CC-Status':  None, 'CC-Length': 0, 'CC-Type': None},
                      'Cast-Bar': {'Cast-Status': None, 'Cast-Length': 0, 'Cast-Info': {}, 'Cast-Target': (""*5)},
                      'Damage-Over-Time': {'Damage-Status':  None, 'Damage-Length': 0, 'Damage-Type': None,
                                           'Damage-Value': None},
                      'Healing-Over-Time': {'Healing-Status':  None, 'Healing-Length': 0, 'Healing-Type': None,
                                            'Healing-Value': None},
                      'Ability-Cooldowns': {'Ability-1': None, 'Ability-2': None, 'Ability-3': None}}

    char_dictionary = {'death knight': {"unholy": {"festering strike", "spread disease", "scourge strike"},
                                        "frost": {"obliterate", "remorseless winter", "breath of sindragosa"},
                                        "blood": {"death strike", "death and decay", "heart strike"}},
                       "demon hunter": {"vengeance": {"immolation aura", "metamorphosis", "soul cleave"},
                                        "havoc": {"chaos strike", "blade dance", "eye beam"}},
                       "druid": {"guardian": {"swipe", "maul", "frenzied regeneration"},
                                 "restoration": {"rejuvenation", "moonfire", "regrowth"},
                                 "balance": {"moonfire", "starfire", "starsurge"},
                                 "feral": {"swipe", "mangle", "rip"}},
                       "evoker": {"devastation": {"fire breath", "disintegrate", "azure strike"},
                                  "preservation": {"fire breath", "spiritbloom", "living flame"}},
                       "hunter": {"marksmanship": {"aimed shot", "multi-shot", "serpent sting"},
                                  "beast mastery": {"mongoose strike", "stampede", "snake bite"},
                                  "survival": {"explosive shot", "wildfire bomb", "sweeping spear"}},
                       "mage": {"frost": {"blizzard", "frost bolt", "frozen orb"},
                                "fire": {"fire blast", "fireball", "living bomb"},
                                "arcane": {"arcane missiles", "timewarp", "arcane explosion"}},
                       "monk": {"brewmaster": {"keg smash", "tiger palm", "fortifying brew"},
                                "windwalker": {"tiger palm", "spinning crane kick", "rising sun kick"},
                                "mistweaver": {"renewing mist", "vivify", "spinning crane kick"}},
                       "paladin": {"protection": {"consecration", "word of glory", "crusader strike"},
                                   "holy": {"holy shock", "flash of light", "crusader strike"},
                                   "retribution": {"crusader strike", "templar's verdict", "divine storm"}},
                       "priest": {"discipline": {"smite", "lesser heal", "power word: shield"},
                                  "holy": {"smite", "renew", "lesser heal"},
                                  "shadow": {"shadow word: pain", "smite", "mind blast"}},
                       "rogue": {"assassination": {"mutilate", "shiv", "envenom"},
                                 "subltey": {"sinister strike", "ambush", "eviscerate"},
                                 "outlaw": {"pistol shot", "dispatch", "ghostly strike"}},
                       "shaman": {"elemental": {"lightning bolt", "flame shock", "lava burst"},
                                  "restoration": {"lightning bolt", "riptide", "healing wave"},
                                  "enhancement": {"stormstrike", "lightning bolt", "earth shock"}},
                       "warrior": {"arms": {"mortal strike", "rend", "execute"},
                                   "fury": {"bloodthirst", "whirlwind", "rampage"},
                                   "protection": {"shield slam", "revenge", "ignore pain"}},
                       "warlock": {"affliction": {"curse of agony", "shadow bolt", "corruption"},
                                   "demonology": {"hand of guldan", "demonic skin", "shadowfury"},
                                   "destruction": {"chaos bolt", "incinerate", "immolate"}},
                       "basic-enemy": {"tank": {"basic attack"},
                                       "healer": {"basic heal"},
                                       "damage": {"basic strike"}}}

    def __init__(self, name):
        self.name = name

    def choose_class(self, npc=''):
        if npc:
            choice = npc
        else:
            choice = None
            while choice not in self.char_dictionary:
                choice = input("Please write the name of your preferred class,\nChoices: " +
                               ", ".join(
                                   c.capitalize() for c in self.char_dictionary.keys()) + "\nEnter Choice -> ").lower()
                if choice not in self.char_dictionary.keys():
                    print("You did not make an appropriate selection or it was misspelled.\n")
        self.character_type = choice

    def set_specialization(self, npc=''):
        if npc:
            self.specialization = npc
        else:
            choice = None
            while choice not in self.char_dictionary[self.character_type]:
                choice = input(
                    "Please write the name of your preferred specialization for " + self.character_type.capitalize() +
                    "\nYour choices are " + ", ".join(c.capitalize() for c in self.char_dictionary[self.character_type]) +
                    "\nEnter Choice ->").lower()
                if choice not in self.char_dictionary[self.character_type]:
                    print("You did not make an appropriate selection or it was misspelled.\n")
            self.specialization = choice
        self.set_abilities()

    def set_abilities(self):
        self.current_abilities = list(self.char_dictionary[self.character_type][self.specialization])

    def show_detailed_abilities(self):
        # parse_abilities(self.char_dictionary[self.character_type][self.specialization])
        print_abilities(self.current_abilities)

    def print_properties(self):
        print("\nYou are a " + self.specialization.capitalize() + " " + self.character_type.capitalize() +
              ". Your name is " + self.name + "\nYour current abilities are " +
              ", ".join(c.capitalize() for c in self.current_abilities) +
              ".\n\nHere is a more detailed explanation of each.\n")
        self.show_detailed_abilities()

    def print_status_effects(self):
        print("\nThe possible status effects on your character are:")
        for status in self.status_effects:
            print(status + " -> " + " ".join(self.status_effects[status]))
        print("\n")

    def update_character_status(self):
        if self.status_effects['Damage-Over-Time']['Damage-Status']:
            self.health -= self.status_effects['Damage-Over-Time']['Damage-Value']
            self.status_effects['Damage-Over-Time']['Damage-Length'] -= 1
            if self.status_effects['Damage-Over-Time']['Damage-Length'] <= 0:
                self.status_effects['Damage-Over-Time']['Damage-Status'] = None
                self.status_effects['Damage-Over-Time']['Damage-Type'] = None
                self.status_effects['Damage-Over-Time']['Damage-Length'] = 0
                self.status_effects['Damage-Over-Time']['Damage-Value'] = None
        if self.status_effects['Healing-Over-Time']['Healing-Status']:
            self.health += self.status_effects['Healing-Over-Time']['Healing-Value']
            self.status_effects['Healing-Over-Time']['Healing-Length'] -= 1
            if self.status_effects['Healing-Over-Time']['Healing-Length'] <= 0:
                self.status_effects['Healing-Over-Time']['Healing-Status'] = None
                self.status_effects['Healing-Over-Time']['Healing-Type'] = None
                self.status_effects['Healing-Over-Time']['Healing-Length'] = 0
                self.status_effects['Healing-Over-Time']['Healing-Value'] = None
        if self.status_effects['Crowd-Control']['CC-Status']:
            # interrupt spell cast if there was any upon being CC'd
            self.status_effects['Cast-Bar']['Cast-Status'] = None
            self.status_effects['Cast-Bar']['Cast-Length'] = 0
            self.status_effects['Cast-Bar']['Cast-Info'].clear()
            self.status_effects['Cast-Bar']['Cast-Target'] = (''*5)
            self.status_effects['Crowd-Control']['CC-Length'] -= 1
            if self.status_effects['Crowd-Control']['CC-Length'] <= 0:
                self.status_effects['Crowd-Control']['CC-Status'] = None
                self.status_effects['Crowd-Control']['CC-Length'] = 0
                self.status_effects['Crowd-Control']['CC-Type'] = None
        elif self.status_effects['Cast-Bar']['Cast-Status']:
            if self.status_effects['Cast-Bar']['Cast-Length'] == 1:
                character_self, target, allies, enemies, friend_or_foe = self.status_effects['Cast-Bar']['Cast-Target']
                if self.status_effects['Cast-Bar']['Cast-Info']['Primary Effect'] == 'Damage':
                    if self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Enemy-ST':
                        enemies[target].health -= self.status_effects['Cast-Bar']['Cast-Info']['Damage']
                    elif self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Enemy-AOE':
                        for enemy in enemies:
                            enemy.health -= self.status_effects['Cast-Bar']['Cast-Info']['Damage']

                if self.status_effects['Cast-Bar']['Cast-Info']['Primary Effect'] == 'Heal':
                    if self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Friendly-ST':
                        allies[target].health += self.status_effects['Cast-Bar']['Cast-Info']['Healing']
                    elif self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Friendly-AOE':
                        for ally in allies:
                            ally.health += self.status_effects['Cast-Bar']['Cast-Info']['Healing']
                    elif self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Self':
                        allies[character_self].health += self.status_effects['Cast-Bar']['Cast-Info']['Healing']

                if self.status_effects['Cast-Bar']['Cast-Info']['Primary Effect'] == 'Damage/Heal':
                    if self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Hybrid-ST':
                        if friend_or_foe:
                            enemies[target].health -= self.status_effects['Cast-Bar']['Cast-Info']['Damage']
                        else:
                            allies[target].health += self.status_effects['Cast-Bar']['Cast-Info']['Healing']
                    elif self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Hybrid-AOE':
                        for ally in allies:
                            ally.health += self.status_effects['Cast-Bar']['Cast-Info']['Healing']
                        for enemy in enemies:
                            enemy.health -= self.status_effects['Cast-Bar']['Cast-Info']['Damage']

                # need to fix/update CC when enemies are actually characters and not ints
                if self.status_effects['Cast-Bar']['Cast-Info']['Primary Effect'] == 'Damage/CC':
                    if self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Enemy-ST':
                        enemies[target].health -= self.status_effects['Cast-Bar']['Cast-Info']['Damage']
                    elif self.status_effects['Cast-Bar']['Cast-Info']['Target'] == 'Enemy-AOE':
                        for enemy in enemies:
                            enemy.health -= self.status_effects['Cast-Bar']['Cast-Info']['Damage']
                self.status_effects['Cast-Bar']['Cast-Status'] = None
                self.status_effects['Cast-Bar']['Cast-Length'] = 0
                self.status_effects['Cast-Bar']['Cast-Info'].clear()
                self.status_effects['Cast-Bar']['Cast-Target'] = (''*5)
            else:
                self.status_effects['Cast-Bar']['Cast-Length'] -= 1


def player_character_creation():
    name = input("Please enter your character's name: ")
    brand_new_character = Character(name)
    brand_new_character.choose_class()
    brand_new_character.set_specialization()
    brand_new_character.print_properties()
    brand_new_character.print_status_effects()
    return brand_new_character


def basic_enemy_creation(enemy_type):
    brand_new_character = Character('Basic Enemy')
    brand_new_character.choose_class('basic-enemy')
    brand_new_character.set_specialization(enemy_type)
    brand_new_character.print_properties()
    brand_new_character.print_status_effects()
    return brand_new_character


def print_abilities(*ability_tuple):
    for ability in ability_tuple[0]:
        print_ability_description(total_ability_dictionary[ability], "".join(ability).capitalize())


def print_ability_description(ability_dict, name):
    ability_string = name
    if ability_dict['Primary Effect'] == 'Damage':
        if ability_dict['Target'] == 'Enemy-ST':
            ability_string += " is a single target damage ability that does " + ability_dict['Damage'].__str__() +\
                              " damage"
        elif ability_dict['Target'] == 'Enemy-AOE':
            ability_string += " is an area of effect damage ability that does " + ability_dict['Damage'].__str__() +\
                              " damage"

    if ability_dict['Primary Effect'] == 'Heal':
        if ability_dict['Target'] == 'Friendly-ST':
            ability_string += " is a single target healing ability that does " + ability_dict['Healing'].__str__() +\
                              " healing"
        elif ability_dict['Target'] == 'Friendly-AOE':
            ability_string += " is an area of effect healing ability that does " + ability_dict['Healing'].__str__() +\
                              " healing"
        elif ability_dict['Target'] == 'Self':
            ability_string += " is a self healing ability that does " + ability_dict['Healing'].__str__() +\
                              " healing"

    if ability_dict['Primary Effect'] == 'Damage/Heal':
        if ability_dict['Target'] == 'Hybrid-ST':
            ability_string += " is a single target hybrid ability that does " + ability_dict['Healing'].__str__() +\
                              " healing and " + ability_dict['Damage'].__str__() + " damage"
        elif ability_dict['Target'] == 'Hybrid-AOE':
            ability_string += " is an area of effect hybrid ability that does " + ability_dict['Healing'].__str__() +\
                              " healing and " + ability_dict['Damage'].__str__() + " damage"

    if ability_dict['Primary Effect'] == 'Damage/CC':
        if ability_dict['Target'] == 'Enemy-ST':
            ability_string += " is a single target damage and crowd control ability that does " + \
                              ability_dict['Damage'].__str__() + " damage"
        elif ability_dict['Target'] == 'Enemy-AOE':
            ability_string += " is an area of effect damage and crowd control ability that does " + \
                              ability_dict['Damage'].__str__() + " damage"

    if ability_dict['Primary Effect'] == 'CC':
        if ability_dict['Target'] == 'Enemy-ST':
            ability_string += " is a single target crowd control ability"
        elif ability_dict['Target'] == 'Enemy-AOE':
            ability_string += " is an area of effect crowd control ability"

    if ability_dict['Duration']:
        if ability_dict['Duration'] > 1:
            ability_string += " with a duration of " + ability_dict['Duration'].__str__() + " turns,"
        else:
            ability_string += " with a duration of " + ability_dict['Duration'].__str__() + " turn,"
    else:
        ability_string += ","

    if not ability_dict['Cast Time']:
        ability_string += " it has no cast time "
    else:
        if ability_dict['Cast Time'] > 1:
            ability_string += " its cast time is " + ability_dict['Cast Time'].__str__() + " turns "
        else:
            ability_string += " its cast time is " + ability_dict['Cast Time'].__str__() + " turn "

    if not ability_dict['Cooldown']:
        ability_string += "and it has no cooldown."
    else:
        if ability_dict['Cooldown'] > 1:
            ability_string += "and its cooldown is " + ability_dict['Cooldown'].__str__() + " turns."
        else:
            ability_string += "and its cooldown is " + ability_dict['Cooldown'].__str__() + " turn."

    print(ability_string)


def combat_area(allies, enemies, team_size=3):
    print("*"*70)
    place = 0
    for i in range(team_size+1):
        print("*" + " "*68 + "*")
        if i < allies.__len__() and i < enemies.__len__():
            print("*" + " "*5 + allies[place].character_type.capitalize() + " "*(58-(len(allies[place].character_type) +
                  len(enemies[place].character_type))) + enemies[place].character_type.capitalize() + " "*5 + "*")
            print("*" + " "*2 + str(i+1) + "  " + allies[place].specialization.capitalize() + " " *
                  (58 - (len(allies[place].specialization) + len(enemies[place].specialization))) +
                  enemies[place].specialization.capitalize() + "  " + str(i+1) + " "*2 + "*")
            print("*" + " "*5 + '%2d' % allies[place].health + " "*54 + '%2d' % enemies[place].health + " "*5 + "*")
            place += 1
        elif i < allies.__len__():
            print("*" + " "*5 + allies[place].character_type.capitalize() + " "*(60-len(allies[place].character_type) +
                  len(enemies[place].charcter_type)) + " "*5 + "*")
            print("*" + " "*2 + str(i+1) + "  " + allies[place].specialization.capitalize() + " " *
                  (60 - len(allies[place].specialization)) + " " * 5 + "*")
            print("*" + " "*10 + '%2d' + " "*60 + "*" % allies[place].health)
            place += 1
        elif i < enemies.__len__():
            print("*" + " "*(63 - len(enemies[place].character_type)) + enemies[place].character_type.capitalize() +
                  " "*5 + "*")
            print("*" + " " * (63 - len(enemies[place].specialization)) + enemies[place].specialization.capitalize() +
                  "  " + str(i + 1) + " " * 2 + "*")
            print("*" + " "*61 + '%2d' % enemies[place].health + " "*5 + "*")
            place += 1
    print("*"*70 + '\n')


def basic_combat(player):
    enemy_list = [basic_enemy_creation('tank'), basic_enemy_creation('damage')]
    ally_list = [player]
    print("You have started Combat! Prepare yourself for battle.")

    combat = 1

    while combat:
        player.update_character_status()
        combat_area(ally_list, enemy_list)
        if death_checker(ally_list, enemy_list):
            print(death_checker(ally_list, enemy_list))
            break
        # start player turn

        if player.status_effects['Crowd-Control']['CC-Status']:
            print("Your character is crowd-controlled and can not cast right now.")
        else:
            for ability_cd in player.status_effects['Ability-Cooldowns']:
                if player.status_effects['Ability-Cooldowns'][ability_cd]:
                    print(ability_cd + " is on cooldown for " + player.status_effects['Ability-Cooldowns'][
                        ability_cd] + " turns.")

            choice = 0
            while not choice:
                print("Here is a list of your abilities:")
                for index, ability in enumerate(player.current_abilities):
                    print((index+1).__str__() + ": " + ability.capitalize())
                choice = int(input("Choose an ability by entering its number -> "))
                if choice not in range(1, player.current_abilities.__len__()+1):
                    choice = 0
                    print("You did not make a proper selection. Please choose an ability from the list that is not on "
                          "cooldown.\n")
                elif player.status_effects['Ability-Cooldowns']['Ability-'+choice.__str__()]:
                    choice = 0
                    print("You did not make a proper selection. Please choose an ability from the list that is not on "
                          "cooldown.\n")
            # choosing a target for single target abilities
            chosen_target = 0
            if total_ability_dictionary[player.current_abilities[choice-1]]['Target'] == 'Enemy-ST':
                print("Choose a target for your attack.")
                while not chosen_target:
                    chosen_target = int(input("Enter enemy number -> "))
                    if chosen_target not in range(1, enemy_list.__len__()+1):
                        chosen_target = 0
            if total_ability_dictionary[player.current_abilities[choice-1]]['Target'] == 'Friendly-ST':
                print("Choose a target for your heal.")
                for index, ally in enumerate(ally_list):
                    print("Ally " + (index+1).__str__() + " has " + ally.health.__str__() + " health left.")
                while not chosen_target:
                    chosen_target = int(input("Enter ally number -> "))
                    if chosen_target not in range(1, ally_list.__len__()+1):
                        chosen_target = 0
            f_o_f = 0
            if total_ability_dictionary[player.current_abilities[choice-1]]['Target'] == 'Hybrid-ST':
                f_o_f = int(input("With this hybrid ability you must first you must choose to attack or heal."
                                  " Press 0 to heal or 1 to attack -> "))
                if f_o_f:
                    print("Choose a target for your attack.")
                    for index, enemy in enumerate(enemy_list):
                        print("Enemy " + (index+1).__str__() + " has " + enemy.health.__str__() + " health left.")
                    while not chosen_target:
                        chosen_target = int(input("Enter enemy number -> "))
                        if chosen_target not in range(1, enemy_list.__len__()+1):
                            chosen_target = 0
                else:
                    print("Choose a target for your heal.")
                    for index, ally in enumerate(ally_list):
                        print("Ally " + (index+1).__str__() + " has " + ally.health.__str__() + " health left.")
                    while not chosen_target:
                        chosen_target = int(input("Enter ally number -> "))
                        if chosen_target not in range(1, ally_list.__len__()+1):
                            chosen_target = 0
            print("\n")
            perform_ability(total_ability_dictionary[player.current_abilities[choice-1]], 0, chosen_target-1,
                            ally_list, enemy_list, f_o_f)
        # end player turn

        if death_checker(ally_list, enemy_list):
            print(death_checker(ally_list, enemy_list))
            break


def death_checker(allies, enemies):
    ally_check = 0
    enemy_check = 0
    for ally in allies:
        if ally.health >= 1:
            ally_check = 1
    for enemy in enemies:
        if enemy.health >= 1:
            enemy_check = 1
    if enemy_check and ally_check:
        return 0
    elif ally_check:
        return "Well done! Your team has defeated all enemies and won the battle!"
    elif enemy_check:
        return "Damn! Your team has been defeated and lost the battle!"
    else:
        return "Well this is awkward. Both teams have been defeated and lost the battle!"


# self and target and numbers that represent their positions in allies[] and enemies[]
def perform_ability(ability_dict, character_self, target, allies, enemies, friend_or_foe):
    if ability_dict['Cast Time']:
        allies[character_self].status_effects['Cast-Bar']['Cast-Status'] = True
        allies[character_self].status_effects['Cast-Bar']['Cast-Length'] = ability_dict['Cast Time']
        allies[character_self].status_effects['Cast-Bar']['Cast-Info'] = ability_dict.copy()
        allies[character_self].status_effects['Cast-Bar']['Cast-Target'] = (character_self, target, allies,
                                                                            enemies, friend_or_foe)
    elif ability_dict['Primary Effect'] == 'Damage':
        if ability_dict['Target'] == 'Enemy-ST':
            enemies[target].health -= ability_dict['Damage']
        elif ability_dict['Target'] == 'Enemy-AOE':
            for enemy in enemies:
                enemy.health -= ability_dict['Damage']

    if ability_dict['Primary Effect'] == 'Heal':
        if ability_dict['Target'] == 'Friendly-ST':
            allies[target].health += ability_dict['Healing']
        elif ability_dict['Target'] == 'Friendly-AOE':
            for ally in allies:
                ally.health += ability_dict['Healing']
        elif ability_dict['Target'] == 'Self':
            allies[character_self].health += ability_dict['Healing']

    if ability_dict['Primary Effect'] == 'Damage/Heal':
        if ability_dict['Target'] == 'Hybrid-ST':
            if friend_or_foe:
                enemies[target].health -= ability_dict['Damage']
            else:
                allies[target].health += ability_dict['Healing']
        elif ability_dict['Target'] == 'Hybrid-AOE':
            for ally in allies:
                ally.health += ability_dict['Healing']
            for enemy in enemies:
                enemy.health -= ability_dict['Damage']

    if ability_dict['Primary Effect'] == 'Damage/CC':
        if ability_dict['Target'] == 'Enemy-ST':
            enemies[target].health -= ability_dict['Damage']
            enemies[target].status_effects['Crowd-Control']['CC-Status'] = True
            enemies[target].status_effects['Crowd-Control']['CC-Length'] = ability_dict['Duration']
        elif ability_dict['Target'] == 'Enemy-AOE':
            for enemy in enemies:
                enemy.health -= ability_dict['Damage']
                enemy.status_effects['Crowd-Control']['CC-Status'] = True
                enemy.status_effects['Crowd-Control']['CC-Length'] = ability_dict['Duration']

    if ability_dict['Primary Effect'] == 'CC':
        if ability_dict['Target'] == 'Enemy-ST':
            enemies[target].status_effects['Crowd-Control']['CC-Status'] = True
            enemies[target].status_effects['Crowd-Control']['CC-Length'] = ability_dict['Duration']
        elif ability_dict['Target'] == 'Enemy-AOE':
            for enemy in enemies:
                enemy.status_effects['Crowd-Control']['CC-Status'] = True
                enemy.status_effects['Crowd-Control']['CC-Length'] = ability_dict['Duration']


# t_a_d format "abilityname": {'Primary Effect': 'Damage/Heal/Hybrid/CC', 'Target': 'Enemy/Friendly/Hybrid-AOE/ST',
#  'Damage': None, 'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': None},

total_ability_dictionary = {
                      # death knight abilities
                      "festering strike ": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 6,
                                            'Healing': None, 'Duration': 4, 'Cooldown': 2, 'Cast Time': None},
                      "spread disease": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 5,
                                         'Healing': None, 'Duration': 3, 'Cooldown': 3, 'Cast Time': None},
                      "scourge strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                         'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "obliterate": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 12, 'Healing': None,
                                     'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "remorseless winter": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 4,
                                             'Healing': None, 'Duration': 2, 'Cooldown': 2, 'Cast Time': None},
                      "breath of sindragosa": {'Primary Effect': 'Damage/CC', 'Target': 'Enemy-AOE', 'Damage': 3,
                                               'Healing': None, 'Duration': 1, 'Cooldown': 3, 'Cast Time': None},
                      "death strike": {'Primary Effect': 'Damage/Heal', 'Target': 'Enemy-ST', 'Damage': 5,
                                       'Healing': 5, 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "death and decay": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 4,
                                          'Healing': None, 'Duration': 3, 'Cooldown': 3, 'Cast Time': None},
                      "heart strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 9, 'Healing': None,
                                       'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      # demon hunter abilities
                      "immolation aura": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 4,
                                          'Healing': None, 'Duration': 3, 'Cooldown': 4, 'Cast Time': None},
                      "metamorphosis": {'Primary Effect': 'Heal', 'Target': 'Self', 'Damage': None, 'Healing': 12,
                                        'Duration': None, 'Cooldown': 4, 'Cast Time': None},
                      "soul cleave": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 5, 'Healing': None,
                                      'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "chaos strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                                       'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "blade dance": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 6, 'Healing': None,
                                      'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      "eye beam": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 8, 'Healing': None,
                                   'Duration': None, 'Cooldown': 4, 'Cast Time': None},
                      # druid abilities
                      "swipe": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 5, 'Healing': None,
                                'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "maul": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                               'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "frenzied regeneration": {'Primary Effect': 'Heal', 'Target': 'Self', 'Damage': None,
                                                'Healing': 7, 'Duration': 3, 'Cooldown': 5, 'Cast Time': None},
                      "rejuvenation": {'Primary Effect': 'Damage', 'Target': 'Friendly-ST', 'Damage': None,
                                       'Healing': 6, 'Duration': 3, 'Cooldown': None, 'Cast Time': None},
                      "moonfire": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 6, 'Healing': None,
                                   'Duration': 3, 'Cooldown': None, 'Cast Time': None},
                      "starfire": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 10, 'Healing': None,
                                   'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "starsurge": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 9, 'Healing': None,
                                    'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "mangle": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                                 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "rip": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                              'Duration': 4, 'Cooldown': 3, 'Cast Time': None},
                      # evoker abilities
                      "fire breath": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 7, 'Healing': None,
                                      'Duration': 3, 'Cooldown': 4, 'Cast Time': 1},
                      "disintegrate": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 12, 'Healing': None,
                                       'Duration': None, 'Cooldown': 3, 'Cast Time': 1},
                      "azure strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 4, 'Healing': None,
                                       'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "spiritbloom": {'Primary Effect': 'Heal', 'Target': 'Friendly-AOE', 'Damage': None, 'Healing': 8,
                                      'Duration': None, 'Cooldown': 4, 'Cast Time': 1},
                      "living flame": {'Primary Effect': 'Damage/Heal', 'Target': 'Hybrid-ST', 'Damage': 6,
                                       'Healing': 6, 'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      # hunter abilities
                      "aimed shot": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 15, 'Healing': None,
                                     'Duration': None, 'Cooldown': 3, 'Cast Time': 2},
                      "multi-shot": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 6, 'Healing': None,
                                     'Duration': None, 'Cooldown': 1, 'Cast Time': None},
                      "serpent sting": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 4, 'Healing': None,
                                        'Duration': 3, 'Cooldown': 2, 'Cast Time': None},
                      "mongoose strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7,
                                          'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "stampede": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 7, 'Healing': None,
                                   'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "snake bite": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                     'Duration': 2, 'Cooldown': 3, 'Cast Time': None},
                      "explosive shot": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 9,
                                         'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "wildfire bomb": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 10,
                                        'Healing': None, 'Duration': None, 'Cooldown': 3, 'Cast Time': 1},
                      "sweeping spear": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 9,
                                         'Healing': None, 'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      # mage abilities
                      "blizzard": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 6, 'Healing': None,
                                   'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "frost bolt": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                                     'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "frozen orb ": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 6, 'Healing': None,
                                      'Duration': None, 'Cooldown': 3, 'Cast Time': 1},
                      "fire blast": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                                     'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "fireball": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 10, 'Healing': None,
                                   'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "living bomb": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 5, 'Healing': None,
                                      'Duration': 3, 'Cooldown': 4, 'Cast Time': None},
                      "arcane missiles": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 10,
                                          'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "timewarp": {'Primary Effect': 'CC', 'Target': 'Enemy-AOE', 'Damage': None, 'Healing': None,
                                   'Duration': 1, 'Cooldown': 5, 'Cast Time': 1},
                      "arcane explosion": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 6,
                                           'Healing': None, 'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      # monk abilities
                      "keg smash": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 3, 'Healing': None,
                                    'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "tiger palm": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 6, 'Healing': None,
                                     'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "fortifying brew": {'Primary Effect': 'Heal', 'Target': 'Self', 'Damage': None, 'Healing': 10,
                                          'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "spinning crane kick": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 4,
                                              'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "rising sun kick": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 11,
                                          'Healing': None, 'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      "renewing mist": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None, 'Healing': 3,
                                        'Duration': 4, 'Cooldown': 2, 'Cast Time': None},
                      "vivify": {'Primary Effect': 'Heal', 'Target': 'Friendly-AOE', 'Damage': None, 'Healing': 4,
                                 'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      # paladin abilities
                      "consecration": {'Primary Effect': 'Damage/Heal', 'Target': 'Hybrid-AOE', 'Damage': 2,
                                       'Healing': 2, 'Duration': 3, 'Cooldown': 3, 'Cast Time': None},
                      "word of glory": {'Primary Effect': 'Heal', 'Target': 'Self', 'Damage': None, 'Healing': 5,
                                        'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "crusader strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 6,
                                          'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "holy shock": {'Primary Effect': 'Damage/Heal', 'Target': 'Hybrid-ST', 'Damage': 7,
                                     'Healing': 7, 'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "flash of light": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None,
                                         'Healing': 9, 'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "templar's verdict": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 10,
                                            'Healing': None, 'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "divine storm": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 6, 'Healing': None,
                                       'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      # priest abilities
                      "smite": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                                'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "lesser heal": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None,
                                      'Healing': 12, 'Duration': None, 'Cooldown': None, 'Cast Time': 2},
                      "power word: shield": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None,
                                             'Healing': 7, 'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "renew": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None, 'Healing': 3,
                                'Duration': 4, 'Cooldown': None, 'Cast Time': None},
                      "shadow word: pain": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 5,
                                            'Healing': None, 'Duration': 4, 'Cooldown': 2, 'Cast Time': None},
                      "mind blast": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 13, 'Healing': None,
                                     'Duration': None, 'Cooldown': 3, 'Cast Time': 1},
                      # rogue abilities
                      "mutilate": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                   'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "shiv": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 4, 'Healing': None,
                               'Duration': 3, 'Cooldown': 1, 'Cast Time': None},
                      "envenom": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 13, 'Healing': None,
                                  'Duration': None, 'Cooldown': 4, 'Cast Time': None},
                      "sinister strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7,
                                          'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "ambush": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 9, 'Healing': None,
                                 'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "eviscerate": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 13, 'Healing': None,
                                     'Duration': None, 'Cooldown': 5, 'Cast Time': None},
                      "pistol shot": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                      'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "dispatch": {'Primary Effect': 'Damage/CC', 'Target': 'Enemy-ST', 'Damage': 9, 'Healing': None,
                                   'Duration': 1, 'Cooldown': 3, 'Cast Time': None},
                      "Ghostly Strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 9, 'Healing': None,
                                         'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      # shaman abilities
                      "lightning bolt": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                         'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "flame shock": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 2, 'Healing': None,
                                      'Duration': 4, 'Cooldown': 2, 'Cast Time': None},
                      "lava burst": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': None,
                                     'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "riptide": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None, 'Healing': 3,
                                  'Duration': 3, 'Cooldown': 2, 'Cast Time': None},
                      "healing wave": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': None, 'Healing': 6,
                                       'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "stormstrike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 5, 'Healing': None,
                                      'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      "earth shock": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 5, 'Healing': None,
                                      'Duration': None, 'Cooldown': 2, 'Cast Time': None},
                      # warrior abilities
                      "mortal strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 9, 'Healing': None,
                                        'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "rend": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 4, 'Healing': None,
                               'Duration': 3, 'Cooldown': 1, 'Cast Time': None},
                      "execute": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 14, 'Healing': None,
                                  'Duration': None, 'Cooldown': 7, 'Cast Time': None},
                      "bloodthirst": {'Primary Effect': 'Damage/Heal', 'Target': 'Enemy-ST', 'Damage': 8, 'Healing': 4,
                                      'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "whirlwind": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 5, 'Healing': None,
                                    'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      "rampage": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                  'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "shield slam": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 5, 'Healing': None,
                                      'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "revenge": {'Primary Effect': 'Damage/CC', 'Target': 'Enemy-ST', 'Damage': 5, 'Healing': None,
                                  'Duration': 1, 'Cooldown': 3, 'Cast Time': None},
                      "ignore pain": {'Primary Effect': 'Heal', 'Target': 'Self', 'Damage': None, 'Healing': 8,
                                      'Duration': None, 'Cooldown': 3, 'Cast Time': None},
                      # warlock abilities
                      "curse of agony": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 5, 'Healing': None,
                                         'Duration': 7, 'Cooldown': 3, 'Cast Time': 1},
                      "shadow bolt": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 7, 'Healing': None,
                                      'Duration': None, 'Cooldown': None, 'Cast Time': 1},
                      "corruption": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 3, 'Healing': None,
                                     'Duration': 5, 'Cooldown': None, 'Cast Time': None},
                      "fear": {'Primary Effect': 'CC', 'Target': 'Enemy-ST', 'Damage': None, 'Healing': None,
                               'Duration': 3, 'Cooldown': 1, 'Cast Time': 1},
                      "hand of guldan": {'Primary Effect': 'Damage', 'Target': 'Enemy-AOE', 'Damage': 2,
                                         'Healing': None, 'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "demonic skin": {'Primary Effect': 'Heal', 'Target': 'Self', 'Damage': None, 'Healing': 2,
                                       'Duration': 6, 'Cooldown': 6, 'Cast Time': None},
                      "shadowfury": {'Primary Effect': 'Damage/CC', 'Target': 'Enemy-AOE', 'Damage': 3, 'Healing': None,
                                     'Duration': 1, 'Cooldown': 3, 'Cast Time': 1},
                      "chaos bolt": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 13, 'Healing': None,
                                     'Duration': None, 'Cooldown': 3, 'Cast Time': 2},
                      "incinerate": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 4, 'Healing': None,
                                     'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "immolate": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 4, 'Healing': None,
                                   'Duration': 4, 'Cooldown': 2, 'Cast Time': 1},
                      # basic enemy abilities
                      "basic attack": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 5, 'Healing': None,
                                       'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "basic heal": {'Primary Effect': 'Heal', 'Target': 'Friendly-ST', 'Damage': 0, 'Healing': 5,
                                     'Duration': None, 'Cooldown': None, 'Cast Time': None},
                      "basic strike": {'Primary Effect': 'Damage', 'Target': 'Enemy-ST', 'Damage': 6, 'Healing': None,
                                       'Duration': None, 'Cooldown': None, 'Cast Time': None}
                      }


def t_a_d_primary_effect_check():
    ability_effect_list = []
    for ability in total_ability_dictionary:
        if total_ability_dictionary[ability]['Primary Effect'] not in ability_effect_list:
            ability_effect_list.append(total_ability_dictionary[ability]['Primary Effect'])
    print(ability_effect_list)


def t_a_d_target_check():
    ability_target_list = []
    for ability in total_ability_dictionary:
        if total_ability_dictionary[ability]['Target'] not in ability_target_list:
            ability_target_list.append(total_ability_dictionary[ability]['Target'])
    print(ability_target_list)


player_one = player_character_creation()
basic_combat(player_one)
