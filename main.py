import numpy as np

def print_hi(name):
    print(f'Hi, {name}')

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
    print("here")

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
