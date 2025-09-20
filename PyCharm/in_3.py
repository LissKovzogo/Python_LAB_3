import math

n = int(input("Value of n? "))
divisors = []
for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
        divisors.append(n//i)
        divisors.append(i)

print(f"Делители числа {n}: {divisors}")