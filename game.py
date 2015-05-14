__author__ = 'Robert Wilson - robwilson101@gmail.com'
# Language = python3

import random

def showInstructions():
    print("Master of Avalon")
    print("========")
    print("Commands:")
    print("'Go [direction]' - Travel to another area")
    print("'Get [item]' - Pickup an item")
    print("'Map' - See where you are and where uou can go")
    print("'Look' - Get information about your surroundings")
    print("'Fight [monster]' - Fight the monster")
    print("'Inventory' - Open your inventory")
    print("'Sheet' - See your character sheet (HP, mana, etc)")
    print("'Journal' - See your quest journal")
    print("Other commands are also supported. Experiment!\n")


def showStatus():
    #prints out current status
    print("\n----------------------------------")
    print("You are currently in the %r" % location[currentLocation]["name"])
    print("----------------------------------")
    if "item" in location[currentLocation]:
        print("You see a %s" % location[currentLocation]["item"])
    else:
        print("You see no items in this area")
    if "monster" in location[currentLocation]:
        print("You see a %s" % location[currentLocation]["monster"])
    else:
        print("You see no monsters here")
    if "north" or "south" or "east" or "west" in location[currentLocation]:
        print("You see other areas nearby, maybe you should check your 'map'")
    print("----------------------------------\n")


def showDirections():
    print("\n----------------------------------")
    print("You are currently in the %r" % location[currentLocation]["name"])
    print("----------------------------------")
    if "north" in location[currentLocation]:
        previewLocation = location[currentLocation]["north"]
        print("To the north is the %r" % location[previewLocation]["name"])
    if "south" in location[currentLocation]:
        previewLocation = location[currentLocation]["south"]
        print("To the south is the %r" % location[previewLocation]["name"])
    if "east" in location[currentLocation]:
        previewLocation = location[currentLocation]["east"]
        print("To the east is the %r" % location[previewLocation]["name"])
    if "west" in location[currentLocation]:
        previewLocation = location[currentLocation]["west"]
        print("To the west is the %r" % location[previewLocation]["name"])
    print("----------------------------------\n")


def showInventory():
    print("\n----------------------------------")
    if len(inventory.items) > 0:
        inventory.print_inventory()
    else:
        print("Your inventory is empty")
    print("----------------------------------")
    if len(inventory.equipped) > 0:
        inventory.print_equipped()
    else:
        print("Nothing equipped")
    print("----------------------------------\n")


def showJournal():
    print("\n----------------------------------")
    if len(journal.journal) > 0:
        journal.print_journal()
    else:
        print("Your journal is empty")
    print("----------------------------------\n")


def showCharacter():
    print("\n----------------------------------")
    print("HP: %d/%d" % (currentHP, maxHP))
    print("AC: %d" % ac)
    #print("Mana: %d/%d" % (currentMana, maxMana) )
    print("Gold: %d" % currentGold)
    print("XP: %d" % currentXP)
    print("XP required for lvl %d: %d " % ((currentLvl + 1), (1000 - currentXP)))
    print("Kills: %d" % totalKills)
    print("----------------------------------\n")


class Item(object):
    def __init__(self, name, damage, bonus, armor, cost, description, itemid):
        self.name = name
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


class Quest(object):
    def __init__(self, name, gold, xp, description, progress):
        self.name = name
        self.gold = gold
        self.xp = xp
        self.description = description
        self.progress = progress


class Inventory(object):
    def __init__(self):
        self.items = {}
        self.equipped = {}

    def add_item(self, item):
        self.items[item.itemid] = item

    def drop_item(self, item):
        del self.items[item]

    def equip_item(self, item):
        self.equipped[item.itemid] = item
        del self.items[item]

    def unequip_item(self, item):
        self.items[item.itemid] = item
        del self.equipped[item]

    def print_inventory(self):
        print('\t'.join(['Name', 'Damage', 'AC', 'Value', 'Description']))
        for item in self.items.values():
            print('\t'.join(
                [str(x) for x in [item.name, item.damage, item.armor, item.cost, item.description]]))

    def print_equipped(self):
        print("Weapon: %s" % self.equipped.values(self.item.name))


class Journal(object):
    def __init__(self):
        self.journal = {}

    def new_quest(self, quest):
        self.journal[quest.id] = quest

    def print_journal(self):
        print('\t'.join(['Name', 'Gold reward', 'XP reward', 'Description', 'Progress']))
        for quest in self.journal.values():
            print('\t'.join(
                [str(x) for x in [quest.name, quest.gold, quest.xp, quest.description, quest.progress]]))


def doquest(quest):
    if quest == 1:
        print("\n----------------------------------")
        print("Quest 1 - Alerics Medallion")
        print("----------------------------------\n")
        journal.new_quest(Quest('Alerics Medallion', 10, 50, 'I must find and retrieve Alerics medallion',
                                'Started'))
        print("")


def fight(monster):
        global currentHP
        global totalKills
        global currentXP
        global currentGold
        print("\nYou are fighting a %s!" % monster.name)
        print("Description: %s" % monster.description)
        while monster.hp > 0 and currentHP > 0:
            print("\n----------------------------------")
            print("%s HP: %d" % (monster.name, monster.hp))
            print("Your HP: %d" % currentHP)
            print("----------------------------------")
            print("What do you want to do?")
            print("'Attack' will attack the enemy.")
            print("'Counter' Attempt to counter the enemies attack.")
            print("'Flee' - Run away!")
            print("----------------------------------\n")
            fightMove = input(">").lower().split()

            if fightMove[0] == "attack":
                playerdamage = random.randint(1, 4)
                monsterdamage = random.randint(1, monster.damage)
                playerattack = random.randint(1, 20)
                monsterattack = random.randint(1, 20)
                playerInitiative = random.randint(1, 20)
                monsterInitiative = random.randint(1, 20)
                print("\nYou roll initiative (d20): %d" % playerInitiative)
                print("%s rolls initiative (d20): %d" % (monster.name, monsterInitiative))
                if playerInitiative >= monsterInitiative:
                    print("You rolled a higher initiative!")
                    if any(range(99)) in inventory.items:
                        playerdamage = random.randint(1, 6)
                        print("\nRolling to attack (1d20): %d vs. AC=%d" % (playerattack, monster.armor))
                        if playerattack >= monster.armor:
                            print("Hit!")
                            print("You swing with your sword for (1d4): %d damage!" % playerdamage)
                            monster.hp -= playerdamage
                            if monster.hp < 1:
                                print("\nYou defeated the %s!" % monster.name)
                                currentXP += monster.xp
                                currentGold += monster.gold
                                totalKills += 1
                                print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                return True
                            else:
                                print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monsterattack, ac))
                                if monsterattack >= ac:
                                    print("Hit!")
                                    print("The %s hits you  for (1d%d): %d damage"
                                          % (monster.name, monster.damage, monsterdamage))
                                    currentHP -= monsterdamage
                                    if currentHP < 1:
                                        print("\nYou have fallen in combat to the %s" % monster.name)
                                        break
                                else:
                                    print("Miss!")
                        else:
                            print("Miss!")
                            print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monsterattack, ac))
                            if monsterattack >= ac:
                                print("Hit!")
                                print("The %s hits you for (1d%d): %d damage"
                                      % (monster.name, monster.damage, monsterdamage))
                                currentHP -= monsterdamage
                                if currentHP < 1:
                                    print("\nYou have fallen in combat to the %s" % monster.name)
                                    break
                            else:
                                print("Miss!")
                    else:
                        print("\nRolling to attack (1d20): %d vs. AC=%d" % (playerattack, monster.armor))
                        if playerattack >= monster.armor:
                            print("Hit!")
                            print("You swing with your fist for (1d4): %d damage!" % playerdamage)
                            monster.hp -= playerdamage
                            if monster.hp < 1:
                                print("\nYou defeated the %s!" % monster.name)
                                currentXP += monster.xp
                                currentGold += monster.gold
                                totalKills += 1
                                print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                return True
                            else:
                                print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monsterattack, ac))
                                if monsterattack >= ac:
                                    print("Hit!")
                                    print("The %s hits you for (1d%d): %d damage"
                                          % (monster.name, monster.damage, monsterdamage))
                                    currentHP -= monsterdamage
                                    if currentHP < 1:
                                        print("\nYou have fallen in combat to the %s" % monster.name)
                                        break
                                else:
                                    print("Miss!")
                        else:
                            print("Miss!")
                            print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monsterattack, ac))
                            if monsterattack >= ac:
                                print("Hit!")
                                print("The %s hits you for (1d%d): %d damage"
                                      % (monster.name, monster.damage, monsterdamage))
                                currentHP -= monsterdamage
                                if currentHP < 1:
                                    print("\nYou have fallen in combat to the %s" % monster.name)
                                    break
                            else:
                                print("Miss!")

                else:
                    print("The %s rolled a higher initiative!" % monster.name)
                    if any(range(99)) in inventory.items:
                        playerdamage = random.randint(1, 6)
                        print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monsterattack, ac))
                        if monsterattack >= ac:
                            print("Hit!")
                            print("The %s hits you  for (1d%d): %d damage"
                                  % (monster.name, monster.damage, monsterdamage))
                            currentHP -= monsterdamage
                            if currentHP < 1:
                                print("\nYou have fallen in combat to the %s" % monster.name)
                                break
                            else:
                                print("\nRolling to attack (1d20): %d vs. AC=%d" % (playerattack, monster.armor))
                                if playerattack >= monster.armor:
                                    print("Hit!")
                                    print("You swing with your sword for (1d6): %d damage!" % playerdamage)
                                    monster.hp -= playerdamage
                                    if monster.hp < 1:
                                        print("\nYou defeated the %s!" % monster.name)
                                        currentXP += monster.xp
                                        currentGold += monster.gold
                                        totalKills += 1
                                        print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                        return True
                                else:
                                    print("Miss!")
                        else:
                            print("Miss!")
                            print("\nRolling to attack (1d20): %d vs. AC=%d" % (playerattack, monster.armor))
                            if playerattack >= monster.armor:
                                print("Hit!")
                                print("You swing with your sword for (1d6): %d damage!" % playerdamage)
                                monster.hp -= playerdamage
                                if monster.hp < 1:
                                    print("\nYou defeated the %s!" % monster.name)
                                    currentXP += monster.xp
                                    currentGold += monster.gold
                                    totalKills += 1
                                    print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                    return True
                            else:
                                print("Miss!")
                    else:
                        print("\nThe %s rolls to attack (1d20): %d vs. AC=%d" % (monster.name, monsterattack, ac))
                        if monsterattack >= ac:
                            print("Hit!")
                            print("The %s hits you  for (1d%d): %d damage"
                                  % (monster.name, monster.damage, monsterdamage))
                            currentHP -= monsterdamage
                            if currentHP < 1:
                                print("\nYou have fallen in combat to the %s" % monster.name)
                                break
                            else:
                                print("\nRolling to attack (1d20): %d vs. AC=%d" % (playerattack, monster.armor))
                                if playerattack >= monster.armor:
                                    print("Hit!")
                                    print("You swing with your fist for (1d4): %d damage!" % playerdamage)
                                    monster.hp -= playerdamage
                                    if monster.hp < 1:
                                        print("\nYou defeated the %s!" % monster.name)
                                        currentXP += monster.xp
                                        currentGold += monster.gold
                                        totalKills += 1
                                        print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                        return True
                                else:
                                    print("Miss!")
                        else:
                            print("Miss!")
                            print("\nRolling to attack (1d20): %d vs. AC=%d" % (playerattack, monster.armor))
                            if playerattack >= monster.armor:
                                print("Hit!")
                                print("You swing with your fist for (1d4): %d damage!" % playerdamage)
                                monster.hp -= playerdamage
                                if monster.hp < 1:
                                    print("\nYou defeated the %s!" % monster.name)
                                    currentXP += monster.xp
                                    currentGold += monster.gold
                                    totalKills += 1
                                    print("You gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                                    return True

            elif fightMove[0] == "flee":
                print("\nYou attempt to flee!")
                roll = random.randint(1, 20)
                print("You roll to escape (d20) DC=5 : %d" % roll)
                if roll >= 5:
                    print("\nYou 'tactically retreat' from the %s\n" % monster.name)
                    return False
                else:
                    print("\nYou fail to escape from the %s!\n" % monster.name)
                    print("\nThe %s hits you for %d damage" % (monster.name, monster.damage))
                    currentHP -= monster.damage
                    if currentHP < 1:
                        print("\nYou have fallen in combat to the %s" % monster.name)
                        break
            else:
                (print("\nNot a valid move! Type 'instructions' to see valid moves.\n"))

location = {
    1: {"name": "The Kings Road",
        "description": "Placeholder",
        "east": 2,
        "south": 3},

    2: {"name": "Cave - Upper area",
        "description": "Placeholder",
        "west": 1,
        "south": 4,
        "item": "sword",
        "iid": 1},

    3: {"name": "The Black Horse Tavern",
        "description": "Placeholder",
        "north": 1,
        "south": 5,
        "item": "beer",
        "iid": 100},

    4: {"name": "Cave - Lower Area",
        "description": "Placeholder",
        "north": 2,
        "monster": "goblin",
        "mid": 1},

    5: {"name": "The Black Horse Tavern - Backroom",
        "description": "Placeholder",
        "north": 3,
        "qid": 1}
}

all_items = {
    1: {"name": "Sword", "dmg": 6, "bns": 0, "arm": 0, "val": 10, "desc": "A rusty looking sword", "iid": 1},
    2: {"name": "Sword", "dmg": 8, "bns": 0, "arm": 0, "val": 30, "desc": "A standard iron sword", "iid": 2},
    3: {"name": "Sword", "dmg": 8, "bns": 1, "arm": 0, "val": 100, "desc": "This sword hums with mysterious energy",
        "iid": 3},
    100: {"name": "Beer", "bns": 0, "desc": "A foaming mug of ale", "dmg": 1, "arm": 0, "val": 1, "iid": 100},
    1000: {"name": 'Alerics Medallion', "dmg": 0, "bns": 0, "arm": 1, "val": 50, "desc":
           'A shiny medallion with the icon of Pelor embossed onto it. It belongs to Aleric.', "iid": 1000}
    }

all_monsters = {
    1: {"name": "Goblin", "hp": 10, "arm": 10, "damage": 3, "gold": 10, "xp": 10, "desc": "A weak looking goblin",
        "mid": 1},
    2: {"name": "Goblin", "hp": 15, "arm": 12, "damage": 6, "gold": 13, "xp": 20, "desc": "A goblin", "mid": 2}
    }

inventory = Inventory()
showInstructions()
journal = Journal()

intro = True

currentLocation = 1
previewLocation = 0
currentHP = 20
maxHP = 20
ac = 10
currentGold = 10
#currentMana = 10
#maxMana = 10
totalKills = 0
currentXP = 0
currentLvl = 1

while currentHP > 0:
    if intro == True:
        showStatus()
        intro = False

    move = input(">").lower().split()

    try:
        if move[0] == "go":
            if move[1] in location[currentLocation]:
                currentLocation = location[currentLocation][move[1]]
                showStatus()
                if "qid" in location[currentLocation]:
                    #Need to figure out how to populate journal with quest based on the quest ID!
                    #doquest(Quest())
                    print("")
            else:
                print("\nYou cannot go that way\n")

        elif move[0] == "get":
            if "iid" in location[currentLocation] and move[1] in location[currentLocation]["item"]:
                iid = location[currentLocation]["iid"]
                inventory.add_item(Item(all_items[iid]["name"], all_items[iid]["dmg"], all_items[iid]["bns"],
                                        all_items[iid]["arm"], all_items[iid]["val"], all_items[iid]["desc"],
                                        all_items[iid]["iid"]))
                print("\n%s added to inventory!\n" % all_items[iid]["name"])
                del location[currentLocation]["item"]
            else:
                print("\nThere is no %s here!\n" % move[1])

        elif move[0] == "fight":
            if currentLocation == 3:
                print("\nYou decide not to start a bar fight.\n")
            elif "mid" in location[currentLocation] and move[1] in location[currentLocation]["monster"]:
                mid = location[currentLocation]["mid"]
                if fight(Monster(all_monsters[mid]["name"],all_monsters[mid]["hp"], all_monsters[mid]["arm"],
                              all_monsters[mid]["damage"], all_monsters[mid]["gold"],all_monsters[mid]["xp"],
                              all_monsters[mid]["desc"], all_monsters[mid]["mid"])) == True:
                    del location[currentLocation]["monster"]
                    if mid == 1:
                        del all_monsters[1]

                if 1 not in all_monsters.keys():
                    inventory.add_item(Item('Alerics Medallion', 0, 0, 0, 50,
                                            'A shiny medallion with the icon of Pelor embossed onto it.'
                                            ' It belongs to Aleric.', 1000))
                    print("[+] You found Alerics medallion!\n")
            else:
                print("\nThere is nothing to fight here\n")

        elif move[0] == "map":
            showDirections()

        elif move[0] == "inventory":
            showInventory()

        elif move[0] == "sheet":
            showCharacter()

        elif move[0] == "journal":
            showJournal()

        elif move[0] == "instructions":
            showInstructions()

        elif move[0] == "look":
            showStatus()

        elif move[0] == "drink":
            if move[1] in inventory.items:
                if move[1] == "beer":
                    print("\nYou drink the foaming mug of ale!")
                    inventory.drop_item('beer')
                if move[1] == "sword":
                    print("\nYou swallow the sword, congratulations you succeeded in killing yourself!\n")
                    currentHP = 0
            else:
                print("\nYou don't have a %r to drink!" % move[1])

        elif move[0] == "quit" or move[0] == "exit":
            quit(1)

        else:
            print("\nNot a valid move! Type 'instructions' to see valid moves.\n")
    except IndexError:
        print("\nNot a valid move! Type 'instructions' to see valid moves.\n")


print("\nGAME OVER")
quit(1)

"""
elif move[0] == "equip":
    print(inventory.items)
    if 1 in inventory.items.keys():
        inventory.equip_item()
        print("Success")
    else:
        print("Failed")"""