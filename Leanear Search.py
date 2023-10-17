# Leanear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

# Input a list of elements
arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

# Input the target value to search for
target = int(input("Enter the target value to search: "))

# Perform linear search
index = linear_search(arr, target)

if index != -1:
    print(f"Target value {target} found at index {index}.")
else:
    print(f"Target value {target} not found in the list.")
