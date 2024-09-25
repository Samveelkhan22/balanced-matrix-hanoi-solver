# balanced 0-1 matrices
# Task: Compute the number of balanced matrices for matrices of order 2, 4, 6, and 8

from itertools import combinations

def permutations(n):
    ones = list(combinations(list(range(n)),n//2))
    ans = []
    for o in ones:
        case = []
        for i in range(n):
            if (i in o):
                case.append(1)
            else:
                case.append(0)
        ans.append(case)
    return ans

def check(mat):
    n = len(mat[0])
    for j in range(n):
        acc0, acc1 = 0, 0
        for i in range(len(mat)):
            if (mat[i][j] == 1):
                acc1 += 1
            elif (mat[i][j] == 0):
                acc0 += 1
            if (acc0 > (n//2)) or (acc1 > n//2):
                return False
    return True

def layer(r, mat, perm, ans):
    for p in perm:
        mat.append(p)
        if check(mat):
            if (r+1 == len(p)):
                ans += 1
            else:
                ans = layer(r+1, mat, perm, ans)
        mat.pop()
    return ans

def balanced01mat_for_n(n):
    print(f"\nComputing the number of balanced matrices for matrix order {n}")
    perm = permutations(n)
    ans = layer(0, [], perm, 0)
    print(f"The number of balanced matrices for order {n} is {ans}")
    return ans

def run_balanced_matrices():
    orders = [2, 4, 6, 8]
    for n in orders:
        balanced01mat_for_n(n)

# Sequentially call the function for orders 2, 4, 6, and 8
run_balanced_matrices()

#Remarks
# Order 2: The number of balanced matrices is 2.
# Order 4: The number of balanced matrices is 90.
# Order 6: The number of balanced matrices is 297,200.
# Order 8: The number of balanced matrices is expected to be in the range of billions, but the exact value would require extended computation due to the exponential growth.