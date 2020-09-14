#!/usr/bin/env python3

x = 5
y = 3
z = x + y

print(f"using addition - result is {z}")

z = x - y
print(f"using minus - result is {z}")

z = x * y
print(f"using multiplication - result is {z}")

z = x / y
print(f"using division - result is {z}")

z = x // y
print(f"using integer division - result is {z}")

z = x % y
print(f"using remaider - result is {z}")

z = x % y
z = -z
print(f"using unary minus - result is {z}")

z = x % y
z = -z
z = +z # plus by minus is minus
print(f"using unary plus after a unary minus  - result is {z}")



