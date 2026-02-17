# 7. Recursive Search
def linear_search(arr, target, index=0):
    # When the list is at the end it returns -1
    if index == len(arr):
        return -1

    # Returns the index of the target when found
    if arr[index] == target:
        return index

    return linear_search(arr, target, index + 1)

NUM_ARRAY = []

# Input the length of the number list
LENGTH_OF_NUMBERS = int(input("Enter the length of the list of numbers: "))

# Input the list of numbers
print("Enter the list of numbers: ")
for i in range(LENGTH_OF_NUMBERS):
    num = int(input())
    NUM_ARRAY.append(num)

# Enter the number to search for
target_num = int(input("Enter the target number: "))
print(NUM_ARRAY)

found_index = linear_search(NUM_ARRAY, target_num)

if found_index != -1:
    print(f"Element {target_num} found at index: {found_index}")
else:
    print(f"Element {target_num} not found in the list.")

