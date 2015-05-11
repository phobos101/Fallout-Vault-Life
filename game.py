__author__ = 'Robert Wilson - robwilson101@gmail.com'

def showInstructions():
    print ("Master of Avalon")
    print ("========")
    print ("Commands:")
    print ("'Go [direction]' e.g 'Go east'")
    print ("'Get [item]' e.g 'Get Sword")
    print ("'Map' to see where you can go")
    print ("'Inventory' to see your inventory")
    print ("'Sheet' to see your character sheet (HP, mana, etc)")
    print ("Other commands such as 'eat', 'drink', 'look' are also supported. Experiment!")

def showStatus():
    #prints out current status
    print ("\nYou are currently in the %r" % location[currentLocation]["name"])
    if "item" in location[currentLocation]:
        print ("You see a " + location[currentLocation]["item"]["name"])

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
    if len(inventory) > 0:
        print (str(inventory))
        #change this to printing each element in a normal string.
    else:
        print ("Your inventory is empty")
    print ("----------------------------------")

def showCharacter():
    print ("\n----------------------------------")
    print ("HP: %d/%d" % (currentHP, maxHP))
    print ("Gold: %d" % currentGold)
    print ("----------------------------------")

location = {
    1: {"name": "The Kings Road",
        "description": "Placeholder",
        "east": 2,
        "south": 3},

    2: {"name": "Cave - Upper area",
        "description": "Placeholder",
        "west": 1,
        "south": 4,
        "item": {"name": "sword",
                 "description": "A rusty sword"},
        },

    3: {"name": "The Black Horse Tavern",
        "description": "Placeholder",
        "north": 1,
        "item": {"name": "beer",
                 "description": "A foaming mug of ale"},
        },

    4: {"name": "Cave - Lower Area",
        "description": "Placeholder",
        "north": 2}

    }

currentLocation = 1
previewLocation = 0
inventory = []
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
        if "item" in location[currentLocation] and move[1] in location[currentLocation]["item"]["name"]:
            inventory += [move[1]]
            print ("You picked up the " + move[1] + "!")
            del location[currentLocation]["item"][move[1]]
        else:
            print("Cannot pickup " + move[1] + "!")
    elif move[0] == "map":
        showDirections()
    elif move[0] == "inventory":
        showInventory()
    elif move[0] == "sheet":
        showCharacter()
    elif move[0] == "instructions":
        showInstructions()
    elif move[0] == "quit" or move[0] == "exit":
        quit()
    else:
        print ("\nNot a valid move! Type 'instructions' to see valid moves.\n")