# Function to add two matrices
def matrix_addition(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Return None if the matrices cannot be added

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# Input the dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input the first matrix
matrix1 = []
print("Enter elements for the first matrix:")
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix1.append(row)

# Input the second matrix
matrix2 = []
print("Enter elements for the second matrix:")
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix2.append(row)

# Perform matrix addition
result = matrix_addition(matrix1, matrix2)

# Display the result
if result is None:
    print("Matrices have different dimensions and cannot be added.")
else:
    print("Result of matrix addition:")
    for row in result:
        print(" ".join(map(str, row)))
