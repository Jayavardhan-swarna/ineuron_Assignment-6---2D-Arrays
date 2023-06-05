def findPermutation(s):
    n = len(s)
    perm = [0] * (n + 1)
    stack = []

    for i in range(n):
        if s[i] == 'I':
            stack.append(i + 1)
            while stack:
                perm[i + 1] = stack.pop()
                i += 1
        else:
            stack.append(i + 1)

    stack.append(n + 1)
    while stack:
        perm[n] = stack.pop()
        n -= 1

    return perm

# Example usage
s = "IDID"
permutation = findPermutation(s)
print(permutation) 
