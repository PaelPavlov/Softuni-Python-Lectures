rows_count = int(input())

# matrix = []
flattened = []

for i in range(rows_count):
    row_data = [int(el) for el in input().split(", ")]
    flattened.extend(row_data)

    # matrix.append(row_data)


# flattened = []

# for row in matrix:
#     for el in row:
#         flattened.append(el)

# print(flattened)
print(flattened)