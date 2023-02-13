class InventoryControl:
    _current_inventory = dict

    _INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }

    _MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._current_inventory = {
            ingredient: 0 for ingredient in self._MINIMUM_INVENTORY.keys()
        }

    def add_new_order(self, customer, order, day):
        for ingredient in self._INGREDIENTS[order]:
            if (self._current_inventory[ingredient]
                    < self._MINIMUM_INVENTORY[ingredient]):
                self._current_inventory[ingredient] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self._current_inventory

    def get_available_dishes(self):
        dishes = set(self._INGREDIENTS.keys())

        for ingredient in self._current_inventory.keys():
            if (self._current_inventory[ingredient]
                    == self._MINIMUM_INVENTORY[ingredient]):

                for dish, ingredients in self._INGREDIENTS.items():
                    if ingredient in ingredients:
                        dishes.discard(dish)

        return dishes
