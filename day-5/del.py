# Define a sample matrix as a list of lists
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Define the number of times you want to transpose the matrix
n = 2

# Function to transpose a matrix without using external libraries
def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create an empty matrix to store the result
    result = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    
    for i in range(num_rows):
        for j in range(num_cols):
            result[j][i] = matrix[i][j]
    
    return result

# Transpose the matrix 'n' times
for _ in range(n):
    matrix = transpose_matrix(matrix)

# Print the final transposed matrix
for row in matrix:
    print(row)
