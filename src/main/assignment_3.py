import numpy as np

def gaussian_elimination(A, b):
    n = len(A)
    Aug = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float)))  # Ensure float type

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(Aug[r, i]))
        Aug[[i, max_row]] = Aug[[max_row, i]]  # Swap rows
        for j in range(i + 1, n):
            factor = Aug[j, i] / Aug[i, i]
            Aug[j] -= factor * Aug[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Aug[i, -1] - np.dot(Aug[i, i + 1:n], x[i + 1:])) / Aug[i, i]
    return x


def lu_factorization(A):
    n = len(A)
    L = np.eye(n)
    U = A.astype(float)
    
    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            U[j] -= factor * U[i]
            L[j, i] = factor
    
    determinant = np.prod(np.diag(U))
    return L, U, determinant

def is_diagonally_dominant(A):
    for i in range(len(A)):
        if abs(A[i, i]) < sum(abs(A[i, :])) - abs(A[i, i]):
            return False
    return True

def is_positive_definite(A):
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False

if __name__ == "__main__":
    A1 = np.array([[2, -1, 1], [1, 3, 1], [-1, 5, 4]])
    b1 = np.array([6, 0, -3])
    solution = gaussian_elimination(A1, b1)
    print(solution)
    
    A2 = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
    L, U, det = lu_factorization(A2)
    print("\n",det)
    print("\n", L)
    print("\n", U)
    
    A3 = np.array([[9, 0, 5, 2, 1], [3, 9, 1, 2, 1], [0, 1, 7, 2, 3],
                   [4, 2, 3, 12, 2], [3, 2, 4, 0, 8]])
    print("\n", is_diagonally_dominant(A3))
    
    A4 = np.array([[2, 2, 1], [2, 3, 0], [1, 0, 2]])
    print("\n", is_positive_definite(A4))
