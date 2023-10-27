# Function to multiply two matrices
def matrix_multiplication(matrix1, matrix2):
    # Check if the matrices can be multiplied (columns of matrix1 = rows of matrix2)
    if len(matrix1[0]) != len(matrix2):
        return None  # Return None if the matrices cannot be multiplied

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Input the dimensions of the matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Input the first matrix
matrix1 = []
print("Enter elements for the first matrix:")
for i in range(rows1):
    row = [int(x) for x in input().split()]
    matrix1.append(row)

# Input the second matrix
matrix2 = []
print("Enter elements for the second matrix:")
for i in range(rows2):
    row = [int(x) for x in input().split()]
    matrix2.append(row)

# Perform matrix multiplication
result = matrix_multiplication(matrix1, matrix2)

# Display the result
if result is None:
    print("Matrices cannot be multiplied due to incompatible dimensions.")
else:
    print("Result of matrix multiplication:")
    for row in result:
        print(" ".join(map(str, row)))
