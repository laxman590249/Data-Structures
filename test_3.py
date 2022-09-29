data = [0,1,0,3,12, 1, 2, 3]

def moveZeroTOlast(input_data):
    position_number = 0
    for i in range(len(input_data)):
        if input_data[i] != 0:
            input_data[position_number], input_data[i] = input_data[i], input_data[position_number]

            position_number += 1
    print(input_data)

print(moveZeroTOlast(data))