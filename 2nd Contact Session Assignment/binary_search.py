def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate midpoint
        mid = (low + high) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half and make the low above mid
        elif target > arr[mid]:
            low = mid + 1
        # If target is smaller, ignore right half and make the high below mid
        else:
            high = mid - 1

    # if target wasn't found return -1
    return -1

data = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Index of 7: {binary_search(data, 7)}")
print(f"Index of 10: {binary_search(data, 10)}")
