import operator  # functions for operators, allows code reuse


# provides truth table
def truth_options():
    a_opts = [1, 0]
    b_opts = [1, 0]
    return [(a, b) for a in a_opts for b in b_opts]  # double for permutes options


# provides equivalent function lookup for bitwise operators
def bitwise_options(op):
    ops = {'&': operator.and_,
           '|': operator.or_,
           '^': operator.xor}
    return ops[op]


# control/eval for bitwise operators
def bitwise_eval(op, op2=""):
    if op2 == "":
        op_func = bitwise_options(op)
        print(f"Bitwise {op}")
        for a, b in truth_options():
            print(f"{a} {op} {b} is {op_func(a, b)}")
    else:
        op2_func = bitwise_options(op2)
        print(f"Bitwise {op}")
        for a, b in truth_options():
            print(f"{op}({a} {op2} {b}) is {(1, 0)[op2_func(a, b)]}")  # opposite: index 0 returns 1, index 1 return 0
    print()

def method1():
    bitwise_eval("&")
    bitwise_eval("NAND", "&")
    bitwise_eval("|")
    bitwise_eval("NOR", "|")
    bitwise_eval("^")

def method2():
    truth_table = [[1,1], [1,0], [0,1], [0,0]]
    for a, b in truth_table:
        print(f"and {a} & {b}: {a & b}")
    for a, b in truth_table:
        print(f"nand ~({a} & {b}): {((a & b) + 1) % 2}") # warning: ~ negates entire integer
    for a, b in truth_table:
        print(f"or {a} | {b}: {a | b}")
    for a, b in truth_table:
        print(f"nor ~({a} | {b}): {((a | b) + 1) % 2}")  # warning: ~ negates entire integer
    for a, b in truth_table:
        print(f"xor {a} ^ {b}: {a ^ b}")


# bitwise evaluation vs truth table
if __name__ == "__main__":
    print("***** Method 1 *****")
    method1()
    print("***** Method 2 *****")
    method2()

