__author__ = 'Robert Wilson - robwilson101@gmail.com'

import random


def showInstructions():
    print ("Master of Avalon")
    print ("========")
    print ("Commands:")
    print ("'Go [direction]' e.g 'Go east'")
    print ("'Get [item]' e.g 'Get Sword")
    print ("'Map' to see where you can go")
    print ("'Fight' to fight the monster")
    print ("'Inventory' to see your inventory")
    print ("'Sheet' to see your character sheet (HP, mana, etc)")
    print ("Other commands such as 'eat', 'drink', 'look' are also supported. Experiment!")


def showStatus():
    #prints out current status
    print ("\nYou are currently in the %r" % location[currentLocation]["name"])
    if "item" in location[currentLocation]:
        print ("You see a " + location[currentLocation]["item"])
    if "monster" in location[currentLocation]:
        print("You see a " + location[currentLocation]["monster"])


def showDirections():
    print ("\n----------------------------------")
    if "north" in location[currentLocation]:
        previewLocation = location[currentLocation]["north"]
        print ("To the north is the " + location[previewLocation]["name"])
    if "south" in location[currentLocation]:
        previewLocation = location[currentLocation]["south"]
        print ("To the south is the " + location[previewLocation]["name"])
    if "east" in location[currentLocation]:
        previewLocation = location[currentLocation]["east"]
        print ("To the east is the " + location[previewLocation]["name"])
    if "west" in location[currentLocation]:
        previewLocation = location[currentLocation]["west"]
        print ("To the west is the " + location[previewLocation]["name"])
    print ("----------------------------------")


def showInventory():
    print ("\n----------------------------------")
    #if len(inventory) > 0:
    inventory.print_items()
    #else:
        #print ("Your inventory is empty")
    print ("----------------------------------")


def showCharacter():
    print ("\n----------------------------------")
    print ("HP: %d/%d" % (currentHP, maxHP))
    print ("Gold: %d" % currentGold)
    print ("----------------------------------")


class Item(object):
    def __init__(self, name, attack, armor, cost, quantity, description):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.cost = cost
        self.quantity = quantity
        self.description = description


class Monster(object):
    def __init__(self, name, hp, armor, attack, gold, description):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.gold = gold
        self.description = description


class Inventory(object):
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        del self.items[item]

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Arm', 'Val', 'Qty' 'Desc']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.cost, item.quantity, item.description]]))


class Fight(object):
    def __init__(self):
        self.monsters = {}

    def fight_monster(self, monster):
        self.monsters[monster.name] = monster
        print ("\nYou are fighting a %s" % monster.name)
        playerInitiative = random.randint(1,20)
        monsterInitiative = random.randint(1,20)
        if playerInitiative >= monsterInitiative:
            if "sword" in inventory.items:
                print ("\nYou swing with your sword for 5 damage!")
            else:
                print ("\nYou swing with you fist for 1 damage!")
        else:
            print("The %s hits you for %d damage" % (monster.name, monster.attack))


location = {
    1: {"name": "The Kings Road",
        "description": "Placeholder",
        "east": 2,
        "south": 3},

    2: {"name": "Cave - Upper area",
        "description": "Placeholder",
        "west": 1,
        "south": 4,
        "item": "sword"},

    3: {"name": "The Black Horse Tavern",
        "description": "Placeholder",
        "north": 1,
        "item": "beer"},

    4: {"name": "Cave - Lower Area",
        "description": "Placeholder",
        "north": 2,
        "monster": "goblin"}
    }

currentLocation = 1
previewLocation = 0
inventory = Inventory()
monster = Fight()
showInstructions()
currentHP = 10
maxHP = 10
currentGold = 10

while True:
    showStatus()

    move = raw_input(">").lower().split()

    if move[0] == "go":
        if move[1] in location[currentLocation]:
            currentLocation = location[currentLocation][move[1]]
        else:
            print ("You cannot go that way")
    elif move[0] == "get":
        if "item" in location[currentLocation] and move[1] in location[currentLocation]["item"]:
            if move[1] == "sword":
                inventory.add_item(Item('sword', 5, 1, 10, 1, 'A rusty looking sword'))
            if move[1] == "beer":
                inventory.add_item(Item('beer', 1, 0, 1, 1, 'A foaming mug of ale'))
            print ("You picked up the " + move[1] + "!")
            del location[currentLocation]["item"]
        else:
            print("Cannot pickup " + move[1] + "!")
    elif move[0] == "fight":
        if currentLocation == 3:
            print "You decide not to start a bar fight."
        elif "monster" in location[currentLocation]:
            monster.fight_monster(Monster('goblin', 10, 1, 3, 10, 'A weak looking goblin.'))
        else:
            print ("There is nothing to fight here")
    elif move[0] == "map":
        showDirections()
    elif move[0] == "inventory":
        showInventory()
    elif move[0] == "sheet":
        showCharacter()
    elif move[0] == "instructions":
        showInstructions()
    elif move[0] == "drink":
        if move[1] == "beer":
            print "You drink the foaming mug of ale!"
            inventory.remove_item('beer')
        if move[1] == "sword":
            print "You attempt to swallow the sword. You die."
            quit(1)
    elif move[0] == "quit" or move[0] == "exit":
        quit(1)
    else:
        print ("\nNot a valid move! Type 'instructions' to see valid moves.\n")