# Potentialbarriere und Tunneleffekt


```python
from sympy import *
init_printing()

# Symbols
A1, B1, A2, B2, A3, k, q, a = symbols("A1 B1 A2 B2 A3 k q a")

# Equations
eq1 = Eq(A1 + B1, A2 + B2)           
eq2 = Eq(k * (A1 - B1), q * (A2 - B2))
eq3 = Eq(A2 * exp(I * q * a) + B2 * exp(-I * q * a), A3 * exp(I * k * a))
eq4 = Eq(q * (A2 * exp(I * q * a) - B2 * exp(-I * q * a)), k * A3 * exp(I * k * a))

# Find the solution 
solve((eq1, eq2, eq3, eq4), (B1, A2, B2, A3))
```

![](solution.png)

