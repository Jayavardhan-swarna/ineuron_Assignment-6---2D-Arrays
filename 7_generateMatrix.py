def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    num = 1

    while num <= n * n:
        # Traverse top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Traverse left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

# Example usage
n = 3
result = generateMatrix(n)
print(result) 
