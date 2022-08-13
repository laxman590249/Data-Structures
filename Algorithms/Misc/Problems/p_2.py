

length = int(input())
line_segments = input().split()

set_l = set(line_segments)

result = 0

for i in set_l:
    count= line_segments.count(i)
    if count > 3:
        result += count + 1
    else:
        result += 1

print(result)





