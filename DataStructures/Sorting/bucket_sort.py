import math

ls = [40, 10, 30, 80, 70, 20, 60, 90, 50, 100]

buckets_count = math.floor(math.sqrt(len(ls)))

buckets = []

for i in range(buckets_count):
    buckets.append([])

max = ls[0]
for i in ls[1:]:
    if i > max:
        max = i

divisor = buckets_count/max

for i in ls:
    index = math.floor(divisor * i)
    if index >= 3:
        index = 2
    buckets[index].append(i)

print(buckets)
