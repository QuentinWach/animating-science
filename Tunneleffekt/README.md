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




$$\left \{ A_{2} : \frac{2 A_{1} k \left(k + q\right)}{- k^{2} e^{2 i a q} + k^{2} + 2 k q e^{2 i a q} + 2 k q - q^{2} e^{2 i a q} + q^{2}}, \quad A_{3} : \frac{4 A_{1} k q e^{i a \left(- k + q\right)}}{- k^{2} e^{2 i a q} + k^{2} + 2 k q e^{2 i a q} + 2 k q - q^{2} e^{2 i a q} + q^{2}}, \quad B_{1} : - \frac{A_{1} \left(k^{2} e^{2 i a q} - k^{2} - q^{2} e^{2 i a q} + q^{2}\right)}{- k^{2} e^{2 i a q} + k^{2} + 2 k q e^{2 i a q} + 2 k q - q^{2} e^{2 i a q} + q^{2}}, \quad B_{2} : - \frac{2 A_{1} k \left(k - q\right) e^{2 i a q}}{- k^{2} e^{2 i a q} + k^{2} + 2 k q e^{2 i a q} + 2 k q - q^{2} e^{2 i a q} + q^{2}}\right \}$$

