from utils import calculator, open_file, parse_line



def run():
    lines = open_file('calc.txt')

    results = []
    total = 0

    for line in lines:
        action, operator, number_1, number_2 = parse_line(line)
        results.append(calculator(int(number_1), int(number_2), operator))
    
    for result in results:
        total += result

    print(total)    

run()
