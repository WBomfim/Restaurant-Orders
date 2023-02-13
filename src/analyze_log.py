from track_orders import TrackOrders


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


def get_and_format_data(path_to_file):
    lines = read_file(path_to_file)
    return [tuple(line.split(",")) for line in lines]


def analyze_log(path_to_file):
    orders = TrackOrders()

    data = get_and_format_data(path_to_file)

    for client, product, day in data:
        orders.add_new_order(client, product, day)

    informations = [
        orders.get_most_ordered_dish_per_customer("maria"),
        orders.get_quantity_of_a_products_by_client("arnaldo", "hamburguer"),
        orders.get_never_ordered_per_customer("joao"),
        orders.get_days_never_visited_per_customer("joao")
    ]

    write_file("data/mkt_campaign.txt", informations)
