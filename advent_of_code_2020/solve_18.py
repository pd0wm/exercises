#!/usr/bin/env python3

# Number wehre - is actually *
class Num1:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Num1(self.n + other.n)

    def __sub__(self, other):
        return Num1(self.n * other.n)

# Number where + and * are swapped
class Num2:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Num2(self.n * other.n)

    def __mul__(self, other):
        return Num2(self.n + other.n)


def eval_expr(expr, k="Num1"):
    new_expr = ""

    # Wrap all numbers in custom class
    for c in expr:
        if c.isdigit():
            new_expr += f"{k}({c})"
        else:
            new_expr += c

    if k == "Num1":
        new_expr = new_expr.replace('*', '-')
    else:
        new_expr = new_expr.replace('+', '-').replace('*', '+').replace('-', '*')
    return(eval(new_expr).n)


solution_01 = 0
solution_02 = 0
with open('input_18') as f:
    for expr in f:
        solution_01 += eval_expr(expr)
        solution_02 += eval_expr(expr, "Num2")

print(solution_01)
print(solution_02)
