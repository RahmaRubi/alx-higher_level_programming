#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    if(n != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        if (operator not in ("+", "-", "*", "/")):
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            if operator == "+":
                res = a + b
            elif operator == "-":
                res = a - b
            elif operator == "*":
                res = a * b
            elif operator == "/" and b != 0:
                res = a / b
            else:
                exit(1)
            print("{} {} {} = {}".format(a, operator, b, res))
