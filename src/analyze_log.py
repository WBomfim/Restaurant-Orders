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


def analyze_log(path_to_file):
    data = format_data(path_to_file)
    products, days, clients = get_information_from_data(data)
    return print(products, days, clients)
