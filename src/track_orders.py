class TrackOrders:
    _orders: dict
    _products_available: set
    _worked_days: set

    def __init__(self):
        self._orders = {}
        self._products_available = set()
        self._worked_days = set()

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        self._products_available.add(order)
        self._worked_days.add(day)

        if customer not in self._orders:
            self._orders[customer] = {"products": [], "days": []}

        self._orders[customer]["products"].append(order)
        self._orders[customer]["days"].append(day)

    def get_most_ordered_dish_per_customer(self, customer):
        products = self._orders[customer]["products"]
        return max(products, key=products.count)

    def get_never_ordered_per_customer(self, customer):
        return self._products_available.difference(
            set(self._orders[customer]["products"])
        )

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
