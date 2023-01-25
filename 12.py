from functools import reduce

n = int(input("input number: "))

print(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))