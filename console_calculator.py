from utils import calculator

def get_user_number(ordinal: str):
    number = None

    while number is None:
        try:
            number = int(input(f"Enter the {ordinal} number: "))
        except ValueError:
            number = None
    return number

def get_user_operator():
    operators = ['x', '+', '-', '/']
    operator = None

    while operator is None:
        user_input = input('Enter the operator: ')

        if user_input in operators:
            operator = user_input
    
    return operator

def run():

    number_1 = get_user_number('first')
    number_2 = get_user_number('second')
    operator = get_user_operator()

    return calculator(number_1, number_2, operator)

print(run())