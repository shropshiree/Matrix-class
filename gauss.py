from matrix import MyMatrix
from vector import MyVector
import time


# returns x 7.99999 - operations on floats
def gauss(matrix, vector):
    # Ax = b
    # A - matrix, x and b vectors
    # 1. reduce rows of matrix and vec
    mat = matrix.join_mat_vec(vector)
    tmp = mat.reduce_rows()
    mat_reduce = tmp[0]
    num_of_swaps = tmp[1]
    num_of_ope = tmp[2]
    # 2. computing x
    x = list()
    n = len(vector)
    # appending the last x
    x.append(1 / mat_reduce[n - 1][n - 1] * mat_reduce[n - 1][n])
    # appending other x
    for k in range(n - 2, -1, -1):
        tmp = sum(mat_reduce[k][i] * x[abs(i - (n - 1))] for i in range(k + 1, n))
        x.append(1 / mat_reduce[k][k] * (mat_reduce[k][n] - tmp))
    x.reverse()
    return MyVector(x), num_of_swaps, num_of_ope


def round_vec_x(x):
    return MyVector([round(el, 5) for el in x])


def check_gauss(A, x, b):
    # error because of operations on floats
    error = 0.0000001
    res = A * x
    sub = [t[0] - t[1] for t in zip(res[:], b[:])]
    for i in range(len(sub)):
        if abs(sub[i]) > error:
            return False
    return True


def display_result(n):
    try:
        start_time = time.time()
        path = str('Matrix_file_%d.txt' % n)
        A = MyMatrix.load_from_file(path)
        print("Matrix %d x %d" % (A.get_row(), A.get_col()))
        b = MyVector.random_vector(n+1)
        result = gauss(A, b)
        print("Number of swaps: ", result[1])
        print("Number of operations: ", result[2])
        print("Time consumption: ", time.time() - start_time, "s")
        print("Checking: ", check_gauss(A, result[0], b))
        print("--------------------------------------------------------")
    except RuntimeError as err:
        print(err)


a = MyMatrix([[1,5],[0,0]])
b = MyVector([5,0])
gauss(a,b)
# display_result(10)
# display_result(20)
# display_result(40)
# display_result(80)
# display_result(160)
# display_result(320)
# display_result(640)
# display_result(1280)
# display_result(2560)
# display_result(5120)


# mat = MyMatrix([[1,0,5,8], [1,0,8,9], [5,8,0,9], [8,9,7,0]])
# b = MyVector([1,2,3,4])
# x = gauss(mat, b)[0]
# print(check_gauss(mat, x, b))