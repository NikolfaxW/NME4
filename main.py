import numpy as np
import itertools


def print_hi(name):
    print(f'Hi, {name}')

def factroial(n):
    result = 1
    for i in  range(1,n + 1):
        result *= i
    return result


def get_submatrix(A, i_of_line, j_of_column):#works
    result = np.delete(A,i_of_line, 0)
    result = np.delete(result, j_of_column, 1)
    return result

def count_determinant_by_cofactor_method(A):
    n = A.shape[0]
    if(n == 1):
        return A[0,0]
    else:
        det = 0.
        for i in range(n):
            subdet = count_determinant_by_cofactor_method(get_submatrix(A,0,i))
            sign = pow(-1, 2+i)
            det += sign * A[0,i] * subdet
        return det

def count_determinant_by_permutation_definition(A):
    n = A.shape[1]
    permutations = generate_permutations(n)
    result = 0;
    number_of_perm = factroial(n)
    for i in range(number_of_perm):
        temp = pow(-1, count_inversions(permutations[i]))
        for j in range(n):
            temp *= A[j,permutations[i][j] - 1]
        result +=temp
    return result



def generate_permutations(n):
    nums = list(range(1, n + 1))
    permutations = list(itertools.permutations(nums))
    return permutations

def count_inversions(perm):
    inversions = 0
    n = len(perm)
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return inversions


if __name__ == '__main__':
    A = np.array([
        [2., 1., -2., -1.],
        [1., -1., -1., 1.],
        [4., 2., 2., 1.],
        [8., 1., 1., 2.]])

    result_np = np.linalg.det(A)
    print("By np.linalg.det(A) function we got:", result_np) #det A = 27

    result_cof = count_determinant_by_cofactor_method(A)
    print("By cofactor method we got:", result_cof)
    if  np.allclose(result_cof, result_np):
        print("The result of count_determinant_by_cofactor_method(A) function \033[92mIS CLOSE\033[0m to np.linalg.det(A)")
    else:
        print("The result of count_determinant_by_cofactor_method(A) function \033[91mIS NOT CLOSE\033[0m to np.linalg.det(A)")

    result_perm = count_determinant_by_permutation_definition(A)
    print("By the permutation definitions we got:",result_perm)
    if np.allclose(result_perm, result_np):
        print(
            "The result of count_determinant_by_permutation_definition(A) function \033[92mIS CLOSE\033[0m to np.linalg.det(A)")
    else:
        print(
            "The result of count_determinant_by_permutation_definition(A) function \033[91mIS NOT CLOSE\033[0m to np.linalg.det(A)")