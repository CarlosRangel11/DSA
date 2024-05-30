import numpy as np
from time import perf_counter



# Multiplying square matrices
# Places the multiplied results of A, B, into C
def matrix_multiply(A, B, C, n):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n): 
                C[i][j] += A[i][k] * B[k][j]


def matrix_multiply_recursive(A, B, C, n):
    # base case
    if n == 1:
        print(f"A: \n{A}")
        print(f"A at n = {n}: {A[0, 0]}")
        C[0, 0] += A[0, 0] * B[0, 0]
        return
    
    # Divide
    # partition A, B, & C into n/2 x n/2 submatrices
    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid: mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    C11 = C[:mid, :mid]
    C12 = C[:mid, mid:]
    C21 = C[mid:, :mid]
    C22 = C[mid:, mid:]

    # conquer
    matrix_multiply_recursive(A11, B11, C11, mid)
    matrix_multiply_recursive(A11, B12, C12, mid)

    matrix_multiply_recursive(A21, B11, C21, mid)
    matrix_multiply_recursive(A21, B12, C22, mid)

    matrix_multiply_recursive(A12, B21, C11, mid)
    matrix_multiply_recursive(A12, B22, C12, mid)

    matrix_multiply_recursive(A22, B21, C21, mid)
    matrix_multiply_recursive(A22, B22, C22, mid)


 
n = 4

A = np.random.randint(100, size=(n,n), dtype=np.int64)
B = np.random.randint(100, size=(n,n), dtype=np.int64)
C = np.zeros((n,n), dtype=np.int64)

_A = A.copy()
_B = B.copy()
_C = C.copy()

print(f"""
##############################################################
Matrix Multiply on square matrix n x n where n = {n}
""")


start = perf_counter()
matrix_multiply(_A, _B, _C, n)
end = perf_counter()

print(f"{_A}\n\n{_B}\n\n{_C}\n\nmultiplied in {end-start} time!")


_A = A.copy()
_B = B.copy()
_C = C.copy()

print(f"{len(_A)} & {len(_B)} & {len(_C)}")

print(f"""
##############################################################
Recursive Matrix Multiply on square matrix n x n where n = {n}
""")


start = perf_counter()
matrix_multiply_recursive(_A, _B, _C, n)
end = perf_counter()

print(f"{C}\n\nmultiplied in {end-start} time!")