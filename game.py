__author__ = 'Robert Wilson - robwilson101@gmail.com'

def showInstructions():
    print ("RPG Game")
    print ("========")
    print ("Commands:")
    print ("'Go [direction]' e.g 'Go east'")
    print ("'Get [item]' e.g 'Get Sword")
    print ("'Map' to see where you can go")
    print ("'Inventory' to see your inventory")

def showStatus():
    #prints out current status
    print ("\nYou are currently in the %r" % rooms[currentRoom]["name"])
    if "item" in rooms[currentRoom]:
        print ("You see a " + rooms[currentRoom]["item"])

def showDirections():
    print ("\n----------------------------------")
    if "north" in rooms[currentRoom]:
        previewRoom = rooms[currentRoom]["north"]
        print ("To the north is the " + rooms[previewRoom]["name"])
    if "south" in rooms[currentRoom]:
        previewRoom = rooms[currentRoom]["south"]
        print ("To the south is the " + rooms[previewRoom]["name"])
    if "east" in rooms[currentRoom]:
        previewRoom = rooms[currentRoom]["east"]
        print ("To the east is the " + rooms[previewRoom]["name"])
    if "west" in rooms[currentRoom]:
        previewRoom = rooms[currentRoom]["west"]
        print ("To the west is the " + rooms[previewRoom]["name"])
    print ("----------------------------------")

def showInventory():
    print ("\n----------------------------------")
    if len(inventory) > 0:
        print (str(inventory))
    else:
        print ("Your inventory is empty")
    print ("----------------------------------")

rooms = {
    1 : { "name" : "Road",
          "east" : 2,
          "south" : 3 },

    2 : { "name" : "Cave - Upper area",
          "west" : 1,
          "south" : 4,
          "item" : "sword" },

    3 : { "name" : "Tavern",
          "north" : 1,
          "item" : "beer" },

    4 : { "name" : "Cave - Area area",
          "north" : 2 }
    }

currentRoom = 1
previewRoom = 0
inventory = []
showInstructions()

while True:
    showStatus()

    move = raw_input(">").lower().split()

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom] [move[1]]
        else:
            print ("You cannot go that way")
    elif move[0] == "get":
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            inventory += [move[1]]
            print ("You picked up the " + move[1] + "!")
            del rooms[currentRoom]["item"]
        else:
            print("Cannot pickup " + move[1] + "!")
    elif move[0] == "map":
        showDirections()
    elif move[0] == "inventory":
        showInventory()
    elif move[0] == "quit" or move[0] == "exit":
        quit()
    else:
        print ("\nNot a valid move!\n")
        showInstructions()