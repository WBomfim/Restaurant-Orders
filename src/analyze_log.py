def read_file(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file) as file:
            return list(file.read().splitlines())

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def write_file(path_to_file, informations):
    content = "\n".join([str(information) for information in informations])

    with open(path_to_file, "w") as file:
        file.write(content)


def format_data(path_to_file):
    lines = read_file(path_to_file)
    return [tuple(line.split(",")) for line in lines]


def get_information_from_data(data):
    products_available = set()
    worked_days = set()
    clients = {}

    for client, product, day in data:
        products_available.add(product)
        worked_days.add(day)

        if client not in clients:
            clients[client] = {"products": [], "days": []}

        clients[client]["products"].append(product)
        clients[client]["days"].append(day)

    return products_available, worked_days, clients


def product_most_asked_by_client(client):
    products = {
        product: client["products"].count(product)
        for product in client["products"]
    }
    return max(products, key=products.get)


def quantity_of_order_of_a_products_by_client(client, product):
    return client["products"].count(product)


def products_never_asked_by_client(products_available, client):
    return products_available.difference(set(client["products"]))


def days_never_went_by_client(worked_days, client):
    return worked_days.difference(set(client["days"]))


def analyze_log(path_to_file):
    data = format_data(path_to_file)
    products_available, worked_days, clients = get_information_from_data(data)

    informations = [
        product_most_asked_by_client(clients["maria"]),

        quantity_of_order_of_a_products_by_client(
            clients["arnaldo"], "hamburguer"
        ),

        products_never_asked_by_client(products_available, clients["joao"]),

        days_never_went_by_client(worked_days, clients["joao"]),
    ]

    write_file("data/mkt_campaign.txt", informations)
