from itertools import groupby
import re


# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# The purpose of this kata is to write a program that can do some algebra.
#
# Write a function expand that takes in an expression with a single, one character variable, and expands it.
# The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single
# character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable.
# If a = -1, a "-" will be placed in front of the variable.
#
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients
# of the term, x is the original one character variable that was passed in the original expression and b, d, and f,
# are the powers that x is being raised to in each term and are in decreasing order.
#
# If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one,
# the coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included.
# If the power of the term is 0, only the coefficient should be included. If the power of the term is 1, the caret and
# power should be excluded.
# Examples:
#
# expand("(x+1)^2")      # returns "x^2+2x+1"
# expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
# expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
# expand("(-2a-4)^0")    # returns "1"
# expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
# expand("(r+0)^203")    # returns "r^203"
# expand("(-x-1)^2")     # returns "x^2+2x+1"
# ----------------------------------------------------------------------------------------------------------------------
class BinomExpansion:
    def __init__(self, a: int, b: int, var: str, n: int):
        self.expr = [(a, 1), (b, 0)]
        self.n = n
        self.var = var

    def expand(self):

        if not self.n:
            return "1"

        expand = self.expr

        # multiply (ax+b) n times : multiply factors and add powers to get polynomial decomposition
        for i in range(1, self.n):
            expand = [(t1[0] * t2[0], t1[1] + t2[1]) for t1 in expand for t2 in self.expr if t1[0] * t2[0] != 0]

        # group by power and add factors to simplify expression (ex 2x^1 -3x^1 = -x^1)
        # using tuples it gives (2, 1) + (-3, 1) = (-1, 1)
        res = []
        for l in [list(g) for _, g in groupby(sorted(expand, key=lambda x: x[1], reverse=True), lambda x: x[1])]:
            res.append((sum([tup[0] for tup in l]), l[0][1]))

        # build final raw expression
        expr = ''.join(["+" + str(tup[0]) + self.var + "^" + str(tup[1]) for tup in res])

        # final cleaning : remove or convert unnecessary signs ('+-', '^1', '1x', '-1x', '+x^0', '-x^0', 'x^0')
        for sub1, sub2 in zip(['+-', '^1', f'+1{self.var}', f'-1{self.var}', f'+{self.var}^0', f'-{self.var}^0', f'{self.var}^0'],
                              ['-', '', f'+{self.var}', f'-{self.var}', '+1', '-1', '']):
            expr = expr.replace(sub1, sub2)

        # remove initial caracter '+' if needed
        return expr[1:] if expr.startswith('+') else expr


def expand(expr: str) -> str:

    pattern = r"\((?P<a>-{0,1}\d{0,})(?P<variable>[a-zA-Z])(?P<b>(-|\+)\d+)\)\^(?P<power>\d+)"
    match = re.search(pattern, expr)

    if match:
        dic_expr = match.groupdict()
        a, b, var, n = dic_expr['a'], int(dic_expr['b']), dic_expr['variable'], int(dic_expr['power'])
        a = -1 if a == '-' else int(1 if a == "" else a)

    return BinomExpansion(a, b, var, n).expand()
