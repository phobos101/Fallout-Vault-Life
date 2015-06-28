__author__ = 'Robert Wilson - robwilson101@gmail.com'
# Language = python3

import item_list, monster_list, location_list, random

def show_instructions():
    print("Master of Avalon")
    print("========")
    print("Commands:")
    print("'Go [direction]' - Travel to another area")
    print("'Get [item]' - Pickup an item")
    print("'Look' - Get information about your surroundings")
    print("'Fight [monster]' - Fight the monster")
    print("'Show Map' - See where you are and where uou can go")
    print("'Show Inventory' - Open your inventory")
    print("'Show Sheet' - See your character sheet (HP, mana, etc)")
    print("'Show Journal' - See your quest journal")
    print("Other commands are also supported. Experiment!\n")


def show_status():
    #prints out current status
    global iid, mid
    print("\n----------------------------------")
    print("You are currently in the %r" % location_list.location[current_location]['name'])
    print("----------------------------------")
    if 'iid' in location_list.location[current_location]:
        iid = location_list.location[current_location]['iid']
        print("You see a %s" % item_list.items[iid]['name'])
    else:
        print("You see no items in this area")
    if 'mid' in location_list.location[current_location]:
        mid  = location_list.location[current_location]['mid']
        print("You see a %s" % monster_list.monsters[mid]['name'])
    else:
        print("You see no monsters here")
    if "north" or "south" or "east" or "west" in location_list.location[current_location]:
        print("You see other areas nearby, maybe you should check your 'map'")
    print("----------------------------------\n")


def show_directions():
    print("\n----------------------------------")
    print("You are currently in the %r" % location_list.location[current_location]["name"])
    print("----------------------------------")
    if "north" in location_list.location[current_location]:
        preview_location = location_list.location[current_location]["north"]
        print("To the north is the %r" % location_list.location[preview_location]["name"])
    if "south" in location_list.location[current_location]:
        preview_location = location_list.location[current_location]["south"]
        print("To the south is the %r" % location_list.location[preview_location]["name"])
    if "east" in location_list.location[current_location]:
        preview_location = location_list.location[current_location]["east"]
        print("To the east is the %r" % location_list.location[preview_location]["name"])
    if "west" in location_list.location[current_location]:
        preview_location = location_list.location[current_location]["west"]
        print("To the west is the %r" % location_list.location[preview_location]["name"])
    print("----------------------------------\n")


def show_character():
    print("\n----------------------------------")
    print('''Defense:
        HP: %d/%d
        AC: %d (10 + armor value)
        armor: %s

    Offense:
        Attack: 1d%d
        Weapon: %s

    Progress:
        Level: %d
        XP: %d
        XP required for lvl %d: %d
        Kills: %d
    ''' % (current_hp, max_hp, inventory.ac, inventory.armor, inventory.attack, inventory.weapon, current_level,
           current_xp, (current_level+1), (1000 - current_xp), total_kills))
    print("----------------------------------\n")


def fight(monster):
        global current_hp, total_kills, current_gold, current_xp

        print("\nYou are fighting a %s!" % monster.name)
        print("Description: %s" % monster.description)
        while monster.hp > 0 and current_hp > 0:
            print("\n----------------------------------")
            print("%s HP: %d" % (monster.name, monster.hp))
            print("Your HP: %d" % current_hp)
            print("----------------------------------")
            print("What do you want to do?")
            print("'Attack' will attack the enemy.")
            print("'Counter' Attempt to counter the enemies attack.")
            print("'Flee' - Run away!")
            print("----------------------------------\n")
            fight_move = input(">").lower().split()

            if fight_move[0] == "attack":
                monster_damage = random.randint(1, monster.damage)
                player_attack = random.randint(1, 20)
                monster_attack = random.randint(1, 20)
                player_initiative = random.randint(1, 20)
                monster_initiative = random.randint(1, 20)
                print("\nYou roll initiative (d20): %d" % player_initiative)
                print("%s rolls initiative (d20): %d" % (monster.name, monster_initiative))
                if player_initiative >= monster_initiative:
                    print("You rolled a higher initiative!")
                    player_damage = random.randint(1, inventory.attack)
                    print("\nRolling to attack (1d20): %d vs. AC=%d" % (player_attack, monster.armor))
                    if player_attack >= monster.armor:
                        print("Hit!")
                        print("You swing with your %s for (1d%d): %d damage!" % (inventory.weapon,inventory.attack, player_damage))
                        monster.hp -= player_damage
                        if monster.hp < 1:
                            print("\nYou defeated the %s!" % monster.name)
                            current_xp += monster.xp
                            current_gold += monster.gold
                            total_kills += 1
                            print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                            return True
                        else:
                            print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monster_attack, inventory.ac))
                            if monster_attack >= inventory.ac:
                                print("Hit!")
                                print("The %s hits you  for (1d%d): %d damage"
                                      % (monster.name, monster.damage, monster_damage))
                                current_hp -= monster_damage
                                if current_hp < 1:
                                    print("\nYou have fallen in combat to the %s" % monster.name)
                                    break
                            else:
                                print("Miss!")
                    else:
                        print("Miss!")
                        print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monster_attack, inventory.ac))
                        if monster_attack >= inventory.ac:
                            print("Hit!")
                            print("The %s hits you for (1d%d): %d damage"
                                  % (monster.name, monster.damage, monster_damage))
                            current_hp -= monster_damage
                            if current_hp < 1:
                                print("\nYou have fallen in combat to the %s" % monster.name)
                                break
                        else:
                            print("Miss!")

                else:
                    print("The %s rolled a higher initiative!" % monster.name)
                    player_damage = random.randint(1, inventory.attack)
                    print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monster_attack, inventory.ac))
                    if monster_attack >= inventory.ac:
                        print("Hit!")
                        print("The %s hits you  for (1d%d): %d damage"
                              % (monster.name, monster.damage, monster_damage))
                        current_hp -= monster_damage
                        if current_hp < 1:
                            print("\nYou have fallen in combat to the %s" % monster.name)
                            break
                        else:
                            print("\nRolling to attack (1d20): %d vs. AC=%d" % (player_attack, monster.armor))
                            if player_attack >= monster.armor:
                                print("Hit!")
                                print("You swing with your %s for (1d%d): %d damage!" % (inventory.weapon, inventory.attack, player_damage))
                                monster.hp -= player_damage
                                if monster.hp < 1:
                                    print("\nYou defeated the %s!" % monster.name)
                                    current_xp += monster.xp
                                    current_gold += monster.gold
                                    total_kills += 1
                                    print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                    return True
                            else:
                                print("Miss!")
                    else:
                        print("Miss!")
                        print("\nRolling to attack (1d20): %d vs. AC=%d" % (player_attack, monster.armor))
                        if player_attack >= monster.armor:
                            print("Hit!")
                            print("You swing with your %s for (1d%d): %d damage!" % (inventory.weapon, inventory.attack, player_damage))
                            monster.hp -= player_damage
                            if monster.hp < 1:
                                print("\nYou defeated the %s!" % monster.name)
                                current_xp += monster.xp
                                current_gold += monster.gold
                                total_kills += 1
                                print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                return True
                        else:
                            print("Miss!")

            elif fight_move[0] == "flee":
                print("\nYou attempt to flee!")
                roll = random.randint(1, 20)
                print("You roll to escape (d20) DC=5 : %d" % roll)
                if roll >= 5:
                    print("\nYou 'tactically retreat' from the %s\n" % monster.name)
                    return False
                else:
                    print("\nYou fail to escape from the %s!\n" % monster.name)
                    print("\nThe %s hits you for %d damage" % (monster.name, monster.damage))
                    current_hp -= monster.damage
                    if current_hp < 1:
                        print("\nYou have fallen in combat to the %s" % monster.name)
                        break
            else:
                (print("\nNot a valid move! Type 'instructions' to see valid moves.\n"))


class Item(object):
    def __init__(self, name, type, damage, bonus, armor, cost, description, itemid):
        self.name = name
        self.type = type
        self.damage = damage
        self.bonus = bonus
        self.armor = armor
        self.cost = cost
        self.description = description
        self.itemid = itemid


class Monster(object):
    def __init__(self, name, hp, armor, damage, gold, xp, description, mid):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.gold = gold
        self.xp = xp
        self.description = description
        self.mid = mid


class Inventory(object):

    def __init__(self):
        self.items = {}
        self.armor = 'None'
        self.ac = 10
        self.attack = 4
        self.weapon = 'Fists'

    def add_item(self, item):
        self.items[item.itemid] = item
        if 'weapon' in item.type:
            self.weapon = item.name
            self.attack = item.damage
            print('\nNew Weapon: %s' % self.weapon)
            print('New Attack: %d' % self.attack)
        elif 'armor' in item.type:
            self.armor = item.name
            self.ac += item.armor
            print('New Armor: %s' % self.armor)
            print('New AC: %d' % self.ac)

    def drop_item(self, item):
        del self.items[item]

    def print_inventory(self):
        print("\n----------------------------------")
        print("Gold: %d" % current_gold)
        print("----------------------------------")
        if len(inventory.items) > 0:
            print('\t'.join(['Name', 'Type', 'Attack', 'Armor', 'Value', 'Description']))
            for item in self.items.values():
                print('\t'.join(
                [str(x) for x in [item.name, item.type, item.damage, item.armor, item.cost, item.description]]))
        else:
            print("Your inventory is empty")
        print("----------------------------------")


class Journal(object):
    def __init__(self):
        self.journal = {}

    def new_quest(self, quest):
        self.journal[quest.id] = quest

    def print_journal(self):
        print("\n----------------------------------")
        if len(journal.journal) > 0:
            print('\t'.join(['Name', 'Gold reward', 'XP reward', 'Description', 'Progress']))
            for quest in self.journal.values():
                print('\t'.join(
                    [str(x) for x in [quest.name, quest.gold, quest.xp, quest.description, quest.progress]]))
        else:
            print("Your journal is empty")
        print("----------------------------------\n")


# Initialize the inventory and journal
inventory = Inventory()
journal = Journal()

#Starts game by showing the instructions
show_instructions()

intro = True

# Declare main vars
current_location = 1
preview_location = 0
current_hp = 20
max_hp = 20
current_gold = 10
total_kills = 0
current_xp = 0
current_level = 1


# Game runs while player is alive
while current_hp > 0:
    if intro == True:
        show_status()
        intro = False

    move = input(">").lower().split()

    try:
        if move[0].lower() == "go":
            if move[1].lower() in location_list.location[current_location]:
                current_location = location_list.location[current_location][move[1]]
                show_status()
            else:
                print("\nYou cannot go that way\n")

        elif move[0].lower() == "get":
            if "iid" in location_list.location[current_location] and move[1].lower() in (item_list.items[iid]['name']).lower():
                inventory.add_item(Item(item_list.items[iid]['name'], item_list.items[iid]['type'],
                                        item_list.items[iid]['dmg'], item_list.items[iid]['bns'],
                                        item_list.items[iid]['arm'], item_list.items[iid]['val'],
                                        item_list.items[iid]['desc'], item_list.items[iid]['iid']))
                print("\n%s added to inventory!\n" % item_list.items[iid]['name'])
                del location_list.location[current_location]['iid']
            else:
                print("\nThere is no %s here!\n" % move[1])

        elif move[0].lower() == "fight":
            if current_location == 3:
                print("\nYou decide not to start a bar fight.\n")
            elif 'mid' in location_list.location[current_location] and move[1].lower() in (monster_list.monsters[mid]['name']).lower():
                if fight(Monster(monster_list.monsters[mid]['name'],monster_list.monsters[mid]['hp'],
                                              monster_list.monsters[mid]['arm'], monster_list.monsters[mid]['damage'],
                                              monster_list.monsters[mid]['gold'],monster_list.monsters[mid]['xp'],
                                              monster_list.monsters[mid]['desc'], monster_list.monsters[mid]['mid']))\
                        == True:
                    del location_list.location[current_location]['mid']
            else:
                print("\nThere is nothing to fight here\n")

        elif move[0].lower() == 'show':
            if move[1].lower() == 'map':
                show_directions()
            elif move[1].lower() == 'inventory' or move[1].lower() == 'inv':
                inventory.print_inventory()
            elif move[1].lower() == 'character' or move[1] == 'sheet' or move[1] == 'char':
                show_character()
            elif move[1].lower() == 'journal':
                journal.print_journal()
            elif move[1].lower() == 'instructions':
                show_instructions()
            else:
                print("Not a valid 'show' command")

        elif move[0].lower() == 'look':
            show_status()

        elif move[0].lower() == 'rest':
            if 'mid' in location_list.location[current_location]:
                print("\nYou cannot rest with enemies nearby!")
            else:
                print("\nYou rest for 8 hours...")
                current_hp = max_hp

        elif move[0].lower() == 'quit' or move[0].lower() == 'exit':
            quit(1)

        else:
            print("\nNot a valid move! Type 'instructions' to see valid moves.\n")
    except IndexError:
        print("\nNot a valid move! Type 'instructions' to see valid moves.\n")


print("\nGAME OVER")
quit(1)
