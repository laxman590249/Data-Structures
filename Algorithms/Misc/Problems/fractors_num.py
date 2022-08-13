
n = 330
l = []

for i in range(1, n//2):
    if n == 1:
        break
    if n % i == 0:
        l.append(i)
        n = n // i

print(l)