import math

def main():
    N = int(input())
    red_orange = int(input())
    red_green = int(input())
    orange_red = int(input())
    orange_green = int(input())
    green_red = int(input())
    green_orange = int(input())

    items = [red_orange, red_green, orange_red, orange_green, green_red, green_orange]

    total_ways = pow(3, N)
    index = -1
    index_0 = []

    for i in items:
        index += 1
        if i == 0:
            ways = (N - 1) * pow(3, N-2)
            total_ways = total_ways - ways
            index_0.append(index)
            if index == 2:
                if items[0] == 0:
                    w = (N-2)*pow(3,N-3)
                    total_ways = total_ways + w
            elif index == 3:
                if items[0] == 0:
                    w = (N-2)*pow(3,N-3)
                    total_ways = total_ways + w
            elif index == 4:
                if items[1] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
                if items[3] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
                if items[0] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
            elif index == 5:
                if items[1] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
                if items[2] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
                if items[3] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
                if items[4] == 0:
                    w = (N-2)*pow(3, N-3)
                    total_ways = total_ways + w
        elif i < N:
            pair = N-(i*2)
            ways = (pair-1) * pow(3, pair-2)
            total_ways = total_ways - ways

    print(int(total_ways))

main()