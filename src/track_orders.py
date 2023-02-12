class TrackOrders:
    _orders: list

    def __init__(self):
        self._orders = []

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        for register in self._orders:
            if register["customer"] == customer:
                register["order"].append(order)
                register["day"].append(day)
                break
        else:
            self._orders.append(
                {"customer": customer, "order": [order], "day": [day]}
            )

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
