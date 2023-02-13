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

    def get_quantity_of_a_products_by_client(self, customer, product):
        return self._orders[customer]["products"].count(product)

    def get_days_never_visited_per_customer(self, customer):
        return self._worked_days.difference(
            set(self._orders[customer]["days"])
        )

    def __get_all_days(self):
        days = []
        for key in self._orders.values():
            days.extend(key["days"])
        return days

    def get_busiest_day(self):
        days = self.__get_all_days()
        return max(days, key=days.count)

    def get_least_busy_day(self):
        days = self.__get_all_days()
        return min(days, key=days.count)
