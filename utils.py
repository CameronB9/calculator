def calculator(number_1: int, number_2: int, operator: str) -> int:

    operator_map = {
        'x': number_1 * number_2,
        '+': number_1 + number_2,
        '-': number_1 - number_2,
        '/': number_1 / number_2
    }

    if operator not in operator_map.keys():
        print("Invalid operator")
        return
    
    return operator_map[operator]


def open_file(filename: str):
    with open(filename, mode="r") as f:
        return f.read().splitlines()


def parse_line(line: str):
    items = line.split(' ')
    return tuple(items)