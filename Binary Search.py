def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1 

# Input a sorted list of elements
arr = [int(x) for x in input("Enter a sorted list of numbers separated by spaces: ").split()]

# Input the target value to search for
target = int(input("Enter the target value to search: "))

# Perform binary search
index = binary_search(arr, target)

if index != -1:
    print(f"Target value {target} found at index {index}.")
else:
    print(f"Target value {target} not found in the list.")
