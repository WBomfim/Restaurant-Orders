def read_file(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file) as file:
            return list(file.read().splitlines())

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def format_data(path_to_file):
    lines = read_file(path_to_file)
    return [tuple(line.split(",")) for line in lines]


def get_information_from_data(data):
    products = set()
    days = set()
    clients = {}

    for client, product, day in data:
        products.add(product)
        days.add(day)

        if client not in clients:
            clients[client] = {"products": [], "days": []}

        clients[client]["products"].append(product)
        clients[client]["days"].append(day)

    return products, days, clients


def product_most_asked_by_client(client):
    products = {
        product: client["products"].count(product)
        for product in client["products"]
    }
    return max(products, key=products.get)


def quantity_of_order_of_a_products_by_client(client, product):
    return client["products"].count(product)


def analyze_log(path_to_file):
    data = format_data(path_to_file)
    products, days, clients = get_information_from_data(data)
    test = quantity_of_order_of_a_products_by_client(clients["maria"], "hamburguer")
    return print(test)
