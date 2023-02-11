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


def analyze_log(path_to_file):
    data = format_data(path_to_file)
    for client, product, day in data:
        print(client)
