

length = [0, 1, 2, 3, 4, 5, 6, 7, 8]
price = [0, 3, 5, 8, 9, 10, 17, 17, 20]

n = len(length)
price_matrix = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j < i:
            price_matrix[i][j] = price_matrix[i-1][j]
        else:
            price_matrix[i][j] = max(price_matrix[i-1][j],  price[i]+price_matrix[i][j-i])

print(price_matrix)


