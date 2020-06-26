from sympy import symbols, dsolve, Function

v = Function('v')
c, r, t = symbols('C R t')

a = c * v(t).diff(t)
a += v(t)/r

print(dsolve(a, v(t)))
