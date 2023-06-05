def validMountainArray(arr):
    if len(arr) < 3:
        return False

    n = len(arr)
    peak_index = arr.index(max(arr))

    if peak_index == 0 or peak_index == n - 1:
        return False

    for i in range(peak_index):
        if arr[i] >= arr[i + 1]:
            return False

    for i in range(peak_index, n - 1):
        if arr[i] <= arr[i + 1]:
            return False

    return True

# Example usage
arr = [2, 1]
result = validMountainArray(arr)
print(result) 
