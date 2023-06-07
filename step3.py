from utils import calculator, open_file, parse_line
from math import floor

def get_next_line(item: tuple):
    if 'calc' in list(item):
        operator, number_1, number_2 = item[2:]
        return floor(calculator(int(number_1), int(number_2), operator))
    elif len(item) == 2:
        return floor(int(item[1]))
    else:
        return None


def run():
    lines = open_file('step3.txt')

    visited = []
    results = []

    prev_statement = lines[0]
    prev_statement_index = get_next_line(parse_line(prev_statement))

    while True:
        visited.append(prev_statement)
        results.append(prev_statement_index)
        
        next_statement = lines[prev_statement_index]
        next_statement_index = get_next_line(parse_line(next_statement))

        if next_statement in visited:
            print(f'Already seen {next_statement}, quitting!')
            break

        prev_statement = next_statement
        prev_statement_index = next_statement_index
    print(visited)
    print(results)

    '''
    visited = [0]

    prev_line = 0

    while True:
        next_line = get_next_line(parse_line(lines[prev_line]))
        print(f"Going to line {next_line}")

        if next_line in visited:
            print(f'Already visited {next_line}, exiting program')
            break

        visited.append(next_line)


        prev_line = next_line
    
    print(visited)
    '''




run()


