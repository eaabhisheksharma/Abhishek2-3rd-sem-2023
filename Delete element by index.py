# Input a list of elements
elements = [int(x) for x in input("Enter a list of elements separated by spaces: ").split()]

# Input the index to delete
index_to_delete = int(input("Enter the index to delete (0-based index): "))

# Check if the index is valid
if 0 <= index_to_delete < len(elements):
    deleted_element = elements.pop(index_to_delete)
    print(f"Deleted element at index {index_to_delete}: {deleted_element}")
    print("Updated list:", elements)
else:
    print("Invalid index. Please enter a valid index within the range [0, length of the list - 1].")
