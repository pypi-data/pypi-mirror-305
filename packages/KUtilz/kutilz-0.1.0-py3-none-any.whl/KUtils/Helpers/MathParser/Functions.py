from KUtils.Typing import *
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy import Number, solve, Eq
import math

class MathFunc:
    def __init__(self, literal: str):
        self.expr = parse_expr(literal)
        self.variables = set(map(lambda x: x.name, self.expr.free_symbols))

    def evaluate(self, vals:Dict[str, Number]=None, strict=True)->Number:
        if strict and len(self.variables) != 0:
            assert vals is not None and set(vals.keys()) == set(self.variables)        
        
        return self.expr.evalf(subs=vals)
    
    def solve(self, y: Number, known:Dict[str, Number]=None)->Dict[str, Number]:
        expr = self.expr
        if known is not None:
            expr = expr.evalf(subs=known)
        
        sol = solve(Eq(expr, y), dict=True)
        ret = {}
        for item in sol:
            ret.update(item)

        for key, val in ret.items():
            if math.isnan(val):
                raise ValueError(f'Solving for {self.expr} has failed with result {key}={val}.')
        return ret
    
    @property
    def var_count(self):
        return len(self.variables)

if __name__ == '__main__':
    f = MathFunc('2*x+y')
    # print(f.evaluate(vals=dict(y=5)))
    sol = f.solve(y=20, known=dict(y=10))
    print(sol)
