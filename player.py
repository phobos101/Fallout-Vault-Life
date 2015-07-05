__author__ = 'rob'

s = p = e = c = i = a = l = 5

class Inventory(object):

    def __init__(self):
        self.items = {}
        self.armor = 'None'
        self.dr = 0
        self.attack = 4
        self.bonus = 0
        self.weapon = 'Fists'

    def add_item(self, item):
        self.items[item.itemid] = item
        if 'weapon' in item.type:
            self.weapon = item.name
            self.attack = item.damage
            self.bonus = item.bonus
            print('\nNew Weapon: %s' % self.weapon)
            print('New Attack: %d' % self.attack)
        elif 'armor' in item.type:
            self.armor = item.name
            self.dr += item.armor
            print('New Armor: %s' % self.armor)
            print('New DR: %d' % self.dr)

    def drop_item(self, item):
        del self.items[item]

    def print_inventory(self):
        print("\n----------------------------------")
        print("Caps: %d" % current_caps)
        print("----------------------------------")
        if len(self.items) > 0:
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
        if len(self.journal) > 0:
            print('\t'.join(['Name', 'Gold reward', 'XP reward', 'Description', 'Progress']))
            for quest in self.journal.values():
                print('\t'.join(
                    [str(x) for x in [quest.name, quest.gold, quest.xp, quest.description, quest.progress]]))
        else:
            print("Your journal is empty")
        print("----------------------------------\n")


def show_character():
    print("\n----------------------------------")
    print('''Defense:
        HP: %d/%d
        DR: %d
        Armor: %s

    Offense:
        Attack: 1-%d
        Weapon: %s

    Progress:
        Level: %d
        XP: %d
        XP required for lvl %d: %d
        Kills: %d
    ''' % (current_hp, max_hp, inventory.dr, inventory.armor, inventory.attack, inventory.weapon, current_level,
           current_xp, (current_level+1), (1000 - current_xp), total_kills))
    print("----------------------------------\n")


def create_character():
    global max_hp, current_hp, name, gender, s, p, e, c, i, a, l

    name = input("Please enter your characters name\n> ").lower()

    age = 0
    while age < 18 or age > 35:
        age = eval(input("Please enter your characters age (18 - 35)\n> "))

    gender_check = False
    while gender_check == False:
        gender = input("Please enter your gender (male/female)\n> ").lower()
        if gender == 'male' or gender == 'female':
            gender_check = True

    print("\n----------------------------------")
    print('''S.P.E.C.I.A.L Attributes
----------------------------------
S - Strength:     5
P - Perception:   5
E - Endurance:    5
C - Charisma :    5
I - Intelligence: 5
A - Agility:      5
L - Luck:         5
    ''')
    print("----------------------------------")

    total_points = 40
    points_to_distribute = total_points - (s + p + e + c + i + a + l)
    special_check = False

    print("You have %s points to distribute!" % points_to_distribute)
    print("----------------------------------\n")

    while special_check == False:
        s = eval(input("Please enter your characters strength (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)
        print("You have %d points remaining\n" % (points_to_distribute))

        p = eval(input("Please enter your characters perception (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)
        print("You have %d points remaining\n" % (points_to_distribute))

        e = eval(input("Please enter your characters endurance (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)
        print("You have %d points remaining\n" % (points_to_distribute))

        c = eval(input("Please enter your characters charisma (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)
        print("You have %d points remaining\n" % (points_to_distribute))

        i = eval(input("Please enter your characters intelligence (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)
        print("You have %d points remaining\n" % (points_to_distribute))

        a = eval(input("Please enter your characters agility (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)
        print("You have %d points remaining\n" % (points_to_distribute))

        l = eval(input("Please enter your characters luck (1 - 10)\n> "))
        points_to_distribute = total_points - (s + p + e + c + i + a + l)

        if points_to_distribute == 0:
            print("\n----------------------------------")
            print('''S.P.E.C.I.A.L Attributes:
            S - Strength:     %d
            P - Perception:   %d
            E - Endurance:    %d
            C - Charisma :    %d
            I - Intelligence: %d
            A - Agility:      %d
            L - Luck:         %d
            ''' % (s, p, e, c, i, a, l))
            print("----------------------------------\n")

            happy = input("Are you happy with your S.P.E.C.I.A.L assignment? (y/n)\n> ").lower()
            if happy == 'y' or happy == 'yes':
                max_hp = 90 + (e * 20) + (current_level * 10)
                current_hp = max_hp
                special_check = True

        elif points_to_distribute < 0:
            print("\nYou have assigned too many points! Please try again\n")
            s = p = e = c = i = a = l = 5

        elif points_to_distribute > 0:
            print("\nYou have unused points to distribute! Please try again\n")
            s = p = e = c = i = a = l = 5

    if age < 23 and gender == 'male':
        print('''\n
Hi %s, and welcome to vault 204! As a young %d year old man you have spent your entire life living
in safety and security in one of the great vault-tec vaults. Your current work assignment is working on the
nuclear fusion reactor as a junior maintenance man. The day started like any other...
        ''' % (name.capitalize(), age))

    elif age >=23 and age < 30 and gender == 'male':
        print('''\n
Hi %s, and welcome to vault 204! As a %d year old man you have spent your entire life living in
safety and security in one of the great vault-tec vaults. Your current work assignment is working on the
nuclear fusion reactor as a reactor technician. The day started like any other...
        ''' % (name.capitalize(), age))

    elif age >= 30 and gender == 'male':
        print('''\n
Hi %s, and welcome to vault 204! As a %d year old man you have spent your entire life living in
safety and security in one of the great vault-tec vaults. Your current work assignment is working on the
nuclear fusion reactor as a nuclear specialist. The day started like any other...
        ''' % (name.capitalize(), age))

    elif age < 23 and gender == 'female':
        print('''\n
Hi %s, and welcome to vault 204! As a young %d year old woman you have spent your entire life living
in safety and security in one of the great vault-tec vaults. Your current work assignment is working on the
nuclear fusion reactor as a junior maintenance woman. The day started like any other...
        ''' % (name.capitalize(), age))
    elif age >=23 and age < 30 and gender == 'female':
        print('''\n
Hi %s, and welcome to vault 204! As a %d year old woman you have spent your entire life living in
safety and security in one of the great vault-tec vaults. Your current work assignment is working on the
nuclear fusion reactor as a reactor technician. The day started like any other...
        ''' % (name.capitalize(), age))

    elif age >= 30 and gender == 'female':
        print('''\n
Hi %s, and welcome to vault 204! As a %d year old woman you have spent your entire life living in
safety and security in one of the great vault-tec vaults. Your current work assignment is working on the
nuclear fusion reactor as a nuclear specialist. The day started like any other...
        ''' % (name.capitalize(), age))


inventory = Inventory()
journal = Journal()

current_caps = 10
total_kills = 0
current_xp = 0
current_level = 1
current_hp = 50