class InventoryControl:
    _current_inventory = dict
    _current_dishes = dict

    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
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
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self._current_dishes = {
            "hamburguer", "pizza", "misto-quente", "coxinha"
        }

    def handle_index_of_dishes(self, igredient):
        if (self._current_inventory[igredient]
                == self.MINIMUM_INVENTORY[igredient]):
            for dish in self.INGREDIENTS:
                if igredient in self.INGREDIENTS[dish]:
                    self._current_dishes.discard(dish)

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if (self._current_inventory[ingredient]
                    < self.MINIMUM_INVENTORY[ingredient]):
                self._current_inventory[ingredient] += 1
                self.handle_index_of_dishes(ingredient)
            else:
                return False

    def get_quantities_to_buy(self):
        return self._current_inventory

    def get_available_dishes(self):
        return set(self._current_dishes)
