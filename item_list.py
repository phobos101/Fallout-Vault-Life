__author__ = 'Rob'
"""
Items
ID           Name              Value
1            rusty sword       10
100          ale               1

Monsters
ID           Name
1            weak goblin
"""

class Items(object):
    def __init__(self, iid):
        self.iid = iid

    def item_list(self, iid):
        all_items = {
            1: {"name" : "Sword",
                "desc": "A rusty looking sword",
                "dmg": 5,
                "arm": 1,
                "val": 10},
            }

        return all_items[iid]
        #When calling items inventory.add_item(Items.item_list(iid))
