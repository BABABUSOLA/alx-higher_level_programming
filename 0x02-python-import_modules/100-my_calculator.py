#!/usr/bin/python3
if __name__ == "__main__":
    """Print version of calculator"""
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]

    op_arr = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in list(op_arr.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, op, b, op_arr[op](a, b)))
