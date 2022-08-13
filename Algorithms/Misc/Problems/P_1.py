line_1 = input().split()
array_size = int(line_1[0])
element = int(line_1[1])
array = []

line_2 = input().split()
for i in line_2:
    array.append(int(i))

number_of_cases = int(input())

for i in range(number_of_cases):
    line = input().split()

    if int(line[0])==1:
        l = int(line[1])-1
        r = int(line[2])-1
        value = int(line[3])
        splitted = array[l:r+1]
        try:
            index = splitted.index(value)
            print(index+l+1)
        except:
            print(-1)
    else:
        index = int(line[1])
        value = int(line[2])
        array[index-1] = value
