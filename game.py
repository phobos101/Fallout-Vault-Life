__author__ = 'Robert Wilson - robwilson101@gmail.com'
# Language = python3

import item_list, monster_list, location_list, player, random

def show_instructions():
    print("Fallout")
    print("========")
    print("Commands:")
    print("'Go [direction]' - Travel to another area")
    print("'Get [item]' - Pickup an item")
    print("'Look' - Get information about your surroundings")
    print("'Fight [monster]' - Fight the monster")
    print("'Show Map' - See where you are and where you can go")
    print("'Show Inventory' - Open your inventory")
    print("'Show Sheet' - See your character sheet (HP, caps, etc)")
    print("'Show Journal' - See your quest journal")
    print("Other commands are also supported. Experiment!\n")


def show_status():
    #prints out current status
    global iid, mid
    print("\n----------------------------------")
    print("You are currently in %r" % location_list.location[current_location]['name'])
    print("----------------------------------")
    print(location_list.location[current_location]["description"])
    print("\n----------------------------------")

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
        print("You see other areas nearby")
    print("----------------------------------\n")


def show_directions():
    print("\n----------------------------------")
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


def fight(monster):
        print("\nYou are fighting a %s!" % monster.name)
        print(monster.description)
        while monster.hp > 0 and player.current_hp > 0:
            print("\n----------------------------------")
            print("%s HP: %d" % (monster.name, monster.hp))
            print("Your HP: %d" % player.current_hp)
            print("----------------------------------")
            print("What do you want to do?")
            print("'Attack' will attack the enemy.")
            print("'Flee' - Run away!")
            print("----------------------------------\n")
            fight_move = input(">").lower().split()

            if fight_move[0] == "attack":
                player_attack = random.randint(1, 20) + ((player.l * 2) + (player.a * 4) + (player.l * 2))
                monster_attack = 100 - ((player.l * 4) + (player.a * 4) + (random.randint(1, 20)))
                player_initiative = 10 + player.l + player.a
                monster_initiative = random.randint(1, 30)
                if player_initiative >= monster_initiative:
                    print("\nYou move to attack the %s (%d%%)" % (monster.name, player_attack))
                    roll = random.randint(1, 100)
                    if player_attack >= roll:
                        print("Hit!")
                        player_damage = random.randint(1, player.inventory.attack) + player.inventory.bonus
                        print("You deal %d damage with your %s. The enemy resists %d damage."
                              % (player_damage, player.inventory.weapon, monster.armor))
                        total_damage = player_damage - monster.armor
                        if total_damage > 0:
                            monster.hp -= (total_damage)
                            if monster.hp < 1:
                                print("\nYou defeated the %s!" % monster.name)
                                player.current_xp += monster.xp
                                player.current_caps += monster.gold
                                player.total_kills += 1
                                print("You gained %d XP and looted %d caps!\n" % (monster.xp, monster.gold))
                                return True

                        print("\nThe %s moves to attack (%d%%)" % (monster.name, monster_attack))
                        roll = random.randint(1, 100)
                        if monster_attack >= roll:
                            print("Hit!")
                            monster_damage = random.randint(1, monster.damage)
                            print("The %s hits you for %d damage. You resist %d damage."
                                  % (monster.name, monster_damage, player.inventory.dr))
                            total_damage = monster_damage - player.inventory.dr
                            if total_damage > 0:
                                player.current_hp -= (total_damage)
                                if player.current_hp < 1:
                                    print("\nYou have fallen in combat to the %s" % monster.name)
                                    break
                        else:
                            print("Miss!")
                    else:
                        print("Miss!")
                        print("\nThe %s moves to attack (%d%%)" % (monster.name, monster_attack))
                        roll = random.randint(1, 100)
                        if monster_attack >= roll:
                            print("Hit!")
                            monster_damage = random.randint(1, monster.damage)
                            print("The %s hits you for %d damage. You resist %d damage."
                                  % (monster.name, monster_damage, player.inventory.dr))
                            total_damage = monster_damage - player.inventory.dr
                            if total_damage > 0:
                                player.current_hp -= (total_damage)
                                if player.current_hp < 1:
                                    print("\nYou have fallen in combat to the %s" % monster.name)
                                    break
                        else:
                            print("Miss!")

                else:
                    print("\nThe %s moves to attack (%d%%)" % (monster.name, monster_attack))
                    roll = random.randint(1, 100)
                    if monster_attack >= roll:
                        print("Hit!")
                        monster_damage = random.randint(1, monster.damage)
                        print("The %s hits you for %d damage. You resist %d damage."
                              % (monster.name, monster_damage, player.inventory.dr))
                        total_damage = monster_damage - player.inventory.dr
                        if total_damage > 0:
                            player.current_hp -= (total_damage)
                            if player.current_hp < 1:
                                print("\nYou have fallen in combat to the %s" % monster.name)
                                break

                        print("\nYou move to attack the %s (%d%%)" % (monster.name, player_attack))
                        roll = random.randint(1, 100)
                        if player_attack >= roll:
                            print("Hit!")
                            player_damage = random.randint(1, player.inventory.attack)
                            print("You deal %d damage with your %s. The enemy resists %d damage."
                                  % (player_damage, player.inventory.weapon, monster.armor))
                            total_damage = player_damage - monster.armor
                            if total_damage > 0:
                                monster.hp -= (total_damage)
                                if monster.hp < 1:
                                    print("\nYou defeated the %s!" % monster.name)
                                    player.current_xp += monster.xp
                                    player.current_caps += monster.gold
                                    player.total_kills += 1
                                    print("You gained %d XP and looted %d caps!\n" % (monster.xp, monster.gold))
                                    return True
                        else:
                            print("Miss!")

                    else:
                        print("Miss!")
                        print("\nYou move to attack the %s (%d%%)" % (monster.name, player_attack))
                        roll = random.randint(1, 100)
                        if player_attack >= roll:
                            print("Hit!")
                            player_damage = random.randint(1, player.inventory.attack)
                            print("You deal %d damage with your %s. The enemy resists %d damage."
                                  % (player_damage, player.inventory.weapon, monster.armor))
                            total_damage = player_damage - monster.armor
                            if total_damage > 0:
                                monster.hp -= (total_damage)
                                if monster.hp < 1:
                                    print("\nYou defeated the %s!" % monster.name)
                                    player.current_xp += monster.xp
                                    player.current_caps += monster.gold
                                    player.total_kills += 1
                                    print("You gained %d XP and looted %d caps!\n" % (monster.xp, monster.gold))
                                    return True
                        else:
                            print("Miss!")

            elif fight_move[0] == "flee":
                print("\nYou attempt to flee!")
                roll = random.randint(1, 20) + player.a
                if roll >= 5:
                    print("\nYou 'tactically retreat' from the %s\n" % monster.name)
                    return False
                else:
                    print("\nYou fail to escape from the %s!\n" % monster.name)
                    monster_damage = random.randint(1, monster.damage)
                    print("The %s hits you for %d damage. You resist %d damage."
                          % (monster.name, monster_damage, player.inventory.dr))
                    total_damage = monster_damage - player.inventory.dr
                    if total_damage > 0:
                        player.current_hp -= (total_damage)
                        if player.current_hp < 1:
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


#Starts game by showing the instructions
show_instructions()

intro = True

# Declare main vars
current_location = 1
preview_location = 0

# Game runs while player is alive
while player.current_hp > 0:
    if intro == True:
        player.create_character()
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
            if "iid" in location_list.location[current_location] and move[1].lower() \
                    in (item_list.items[iid]['name']).lower():
                player.inventory.add_item(Item(item_list.items[iid]['name'], item_list.items[iid]['type'],
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
            elif 'mid' in location_list.location[current_location] and move[1].lower() \
                    in (monster_list.monsters[mid]['name']).lower():
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
                player.inventory.print_inventory()
            elif move[1].lower() == 'character' or move[1] == 'sheet' or move[1] == 'char':
                player.show_character()
            elif move[1].lower() == 'journal':
                player.journal.print_journal()
            else:
                print("Not a valid 'show' command")

        elif move[0].lower() == 'look':
            show_status()

        elif move[0].lower() == 'rest':
            if 'mid' in location_list.location[current_location]:
                print("\nYou cannot rest with enemies nearby!")
            else:
                print("\nYou rest for 8 hours...")
                player.current_hp = player.max_hp

        elif move[0].lower() == 'instructions' or move[0].lower() == 'help':
                show_instructions()

        elif move[0].lower() == 'quit' or move[0].lower() == 'exit':
            quit(1)

        else:
            print("\nNot a valid move! Type 'instructions' to see valid moves.\n")
    except IndexError:
        print("\nNot a valid move! Type 'instructions' to see valid moves.\n")


print("\nGAME OVER")
quit(1)
