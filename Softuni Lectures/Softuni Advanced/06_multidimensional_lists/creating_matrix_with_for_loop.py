# matrix = []

# for row in range(4):
#     row_data = []
#     for col in range(1, 7):
#         row_data.append(col)
#     matrix.append(row_data)

# print(matrix)

###################################
matrix = []

matrix = [[0 for j in range(2)] for i in range(3)]
print(matrix)

#####################################

#going thru matrix indexes

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        print(matrix[row_index[col_index]])

###########################