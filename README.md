# Python Calculator

## Console Calculator
Prompts the user for 2 numbers and an operator, it calculates the results. 

```bash
python console_calculator.py
```

## File Read Calculator
Reads the `calc.txt` file, gets the result of each calculation and prints the sum of all numbers.

```bash
python file_read_calculator.py
```

## File Navigator
Reads the `file_navigator.txt` file. It starts at line 1 and goes to the line number given or the line number of the result of the calculation

```bash
python file_navigator.py
```

### Utils
Contains functions that are imported and used in each script

```bash
from utils import calculator

print(calculator(10, 25, 'x'))
```