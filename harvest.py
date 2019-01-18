############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    cantaloupe = MelonType('Cantaloupe', 'cant', 2005, 'peach green mix', True, True)
    cantaloupe.add_pairing('parma ham')

    musk = MelonType('Muskmelon', 'musk', 1998, 'green', True, True)
    musk.add_pairing('mint')
    
    casaba = MelonType('Casaba', 'cas', 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('Crenshaw', 'cren', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('Yellow Watermelon', 'yw', 2013, 'yellow', True, True)
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types.extend([cantaloupe, musk, casaba, crenshaw, yellow_watermelon])

    # for melon_type in all_melon_types:
    #     print(melon_type.pairings)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon_type in melon_types:
        print('{} pairs with'.format(melon_type.name))
        for pairing in melon_type.pairings:
            print('- {}'.format(pairing))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}

    for melon_type in melon_types:
        melon_type_dict[melon_type.code] = melon_type

    # print(melon_type_dict)
    return melon_type_dict
    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    # Fill in the rest

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by

    def is_sellable(self):

        return self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from_field != 3


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    yellow_watermelon1 = Melon("yw", 8, 7, 2, "Sheila")
    yellow_watermelon2 = Melon ("yw", 7, 10, 3, "Sheila")
    muskmelon = Melon("musk", 6, 7, 4, "Michael")

    print(melons_by_id)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



