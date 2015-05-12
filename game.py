__author__ = 'Robert Wilson - robwilson101@gmail.com'
# Language = python3

import random

def showInstructions():
    print("Master of Avalon")
    print("========")
    print("Commands:")
    print("'Go [direction]' e.g 'Go east'")
    print("'Get [item]' e.g 'Get Sword")
    print("'Map' - See where you are and where uou can go")
    print("'Look' - Get information about your surroundings")
    print("'Fight' - Fight the monster")
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
        inventory.print_items()
    else:
        print("Your inventory is empty")
    print("----------------------------------\n")

def showJournal():
    print("\n----------------------------------")
    if len(journal.journal) > 0:
        journal.print_items()
    else:
        print("Your journal is empty")
    print("----------------------------------\n")


def showCharacter():
    print("\n----------------------------------")
    print("HP: %d/%d" % (currentHP, maxHP))
    print("Mana: %d/%d" % (currentMana, maxMana) )
    print("Gold: %d" % currentGold)
    print("XP: %d" % currentXP)
    print("XP required for lvl %d: %d " % ((currentLvl + 1), (1000 - currentXP)))
    print("Kills: %d" % totalKills)
    print("----------------------------------\n")


class Item(object):
    def __init__(self, name, attack, armor, cost, quantity, description, iid):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.cost = cost
        self.quantity = quantity
        self.description = description
        self.iid = iid


class Monster(object):
    def __init__(self, name, hp, armor, attack, gold, xp, description, mid):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.gold = gold
        self.xp = xp
        self.description = description
        self.mid = mid


class Quest(object):
    def __init__(self, name, gold, xp, description, qid, progress):
        self.name = name
        self.gold = gold
        self.xp = xp
        self.description = description
        self.qid = qid
        self.progress = progress


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        del self.items[item]

    def print_items(self):
        print('\t'.join(['Name', 'DMG', 'AMR', 'VAL', 'QTY', 'DESC']))
        for item in self.items.values():
            print('\t'.join(
                [str(x) for x in [item.name, item.attack, item.armor, item.cost, item.quantity, item.description]]))


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
        journal.new_quest(Quest('Alerics Medallion', 10, 50, 'I must find and retrieve Alerics medallion', 1,
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
                playerInitiative = random.randint(1, 20)
                monsterInitiative = random.randint(1, 20)
                print("\nYou roll initiative (d20): %d" % playerInitiative)
                print("%s rolls initiative (d20): %d" % (monster.name, monsterInitiative))
                if playerInitiative >= monsterInitiative:
                    print("You rolled a higher initiative!")
                    if "sword" in inventory.items:
                        print("\nYou swing with your sword for 5 damage!")
                        monster.hp -= 5
                    else:
                        print("\nYou swing with you fist for 1 damage!")
                        monster.hp -= 1
                    if monster.hp < 1:
                        print("\nYou defeated the %s!" % monster.name)
                        currentXP += monster.xp
                        currentGold += monster.gold
                        totalKills += 1
                        print("\nYou gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))
                    else:
                        print("\nThe %s hits you back for %d damage" % (monster.name, monster.attack))
                        currentHP -= monster.attack
                        if currentHP < 1:
                            print("\nYou have fallen in combat to the %s" % monster.name)

                else:
                    print("The %s rolled a higher initiative!" % monster.name)
                    print("\nThe %s hits you for %d damage" % (monster.name, monster.attack))
                    currentHP -= monster.attack
                    if currentHP < 1:
                        print("\nYou have fallen in combat to the %s" % monster.name)
                        break
                    if "sword" in inventory.items:
                        print("\nYou swing with your sword for 5 damage!")
                        monster.hp -= 5
                    else:
                        print("\nYou swing with you fist for 1 damage!")
                        monster.hp -= 1
                    if monster.hp < 1:
                        print("\nYou defeated the %s!" % monster.name)
                        currentXP += monster.xp
                        currentGold += monster.gold
                        totalKills += 1
                        print("\nYou gained %d XP and looted %d gold!\n" % (monster.xp, monster.gold))

            elif fightMove[0] == "flee":
                print("\nYou attempt to flee!")
                roll = random.randint(1, 20)
                print("You roll to escape (d20) DC=5 : %d" % roll)
                if roll >= 5:
                    print("\nYou 'tactically retreat' from the %s\n" % monster.name)
                    break
                else:
                    print("\nYou fail to escape from the %s!\n" % monster.name)
                    print("\nThe %s hits you for %d damage" % (monster.name, monster.attack))
                    currentHP -= monster.attack
                    if currentHP < 1:
                        print("\nYou have fallen in combat to the %s" % monster.name)

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

inventory = Inventory()
showInstructions()
journal = Journal()

intro = True

currentLocation = 1
previewLocation = 0
currentHP = 10
maxHP = 10
currentGold = 10
currentMana = 10
maxMana = 10
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
            else:
                print("\nYou cannot go that way\n")

        elif move[0] == "get":
            if "iid" in location[currentLocation] and move[1] in location[currentLocation]["item"]:
                if move[1] == "sword":
                    if location[currentLocation]["iid"] == 1:
                        inventory.add_item(Item('sword', 5, 1, 10, 1, 'A rusty looking sword', 1))
                    else:
                        print("\nYou managed to pickup a magical vorpal sword, but it then disappears\n")
                        break
                if move[1] == "beer":
                    inventory.add_item(Item('beer', 1, 0, 1, 1, 'A foaming mug of ale', 100))
                print("\nYou picked up the " + move[1] + "!\n")
                del location[currentLocation]["item"]
            else:
                print("\nThere is no" + move[1] + " here!\n")

        elif move[0] == "fight":
            if currentLocation == 3:
                print("\nYou decide not to start a bar fight.\n")
            elif "mid" in location[currentLocation]:
                if location[currentLocation]["mid"] == 1:
                    fight(Monster('goblin', 10, 1, 3, 10, 10, 'A weak looking goblin.', 1))
                    del location[currentLocation]["monster"]
                    inventory.add_item(Item('Alerics Medallion', 0, 0, 20, 1, 'A shiny medallion with the icon of Pelor embossed onto it. It belomgs to Aleric.', 50))
                    print("\n[+] You found Alerics medallion!\n")
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
                    inventory.remove_item('beer')
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