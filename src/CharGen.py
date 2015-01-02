__author__ = 'Dark_Silencer_P'
__project__ = 'Character Generator'

"""
1/1/2015
Imma use classes here, mostly because I hate myself, but also cause bitches love class, so I gave that bitch a
class Bitch(object)
"""
"""
Notes:

    So I want the Merchant to stock ALL common items, and a random fraction of uncommons that will depend on the city,
    and a couple of rares depending on the city, again.
"""


class Character(object):
    # so let's make a class that will start as the archetype behind all the other character types.
    def __init__(self, name, job, sex, race, age):
        self.name = name
        self.job = job
        self.sex = sex
        self.race = race
        self.age = age

    def description(self):
        return "%s is a %s by trade, and is a %s %s. They are %s years old." % (
            self.name, self.job, self.sex, self.race, self.age)


class Merchant(Character):
    # I want every instance of the merchant to create its own inventory from "allitems".
    inventory = {}  # make it a dictionary to have the items and their quantities.
    price = {}  # price will be a dictionary with all the prices listed as items of the item keys.

    def get_inventory(self, allitems):
        pass
