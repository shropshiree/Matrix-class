from vector import MyVector
import copy
import os


class MyMatrix:
    def __init__(self, rows):
        # [[1,2,3]] - matrix 1xn
        if rows == [[]] or rows == []:
            raise RuntimeError("Matrix can't be empty")
        if isinstance(rows, list) and all(isinstance(x, list) for x in rows):
            for nest_list in rows:
                if all((isinstance(x, (int, float)) and len(nest_list) == len(rows[0])) for x in nest_list):
                    self.__row = len(rows)
                    self.__col = len(rows[0])
                else:
                    raise RuntimeError("Matrix must be in form of double list: [[1,2], [3,4]] with int or floats")
        else:
            raise RuntimeError("Matrix must be in form of double list: [[1,2], [3,4]] with int or floats")

        self.__rows = rows
        self.__cols = self.update_cols()

    @classmethod
    def load_from_file(cls, path):
        # can only load expected format
        try:
            filesize = os.path.getsize(path)
            if filesize == 0:
                raise RuntimeError("File is empty!")
            f = open(path, "r")
            f1 = f.readlines()
            # if the matrix isn't square - row col
            dim = f1[0][18:-1].split(" ")
            row = int(dim[0])
            col = int(dim[1]) if len(dim) == 2 else row

            rows = [[0] * col for i in range(row)]

            for i in range(2, len(f1)):
                tmp = f1[i].split('\t')
                row_tmp = int(tmp[0])
                col_tmp = int(tmp[1])
                try:
                    val = float(tmp[2])
                except ValueError:
                    raise RuntimeError("You must give int/float to matrix")
                rows[row_tmp][col_tmp] = val
            f.close()
            return MyMatrix(rows)
        except FileNotFoundError:
            raise RuntimeError("Path does not exists!")

    def save_to_file(self, file):
        f = open(file, "w")
        f.write("Matrix Dimension= %d %d\n" % (self.__row, self.__col))
        f.write("List of entries: I, J, A(I, J)\n")
        for i in range(self.__row):
            for j in range(self.__col):
                f.write("%d\t%d\t%f\n" % (i, j, self[i][j]))
        f.close()

    @classmethod
    def create_from_cols(cls, cols):
        # 1 column in list
        if isinstance(cols[0], (int, float)):
            cols = [cols]
        rows = [list(t) for t in zip(*cols)]
        return MyMatrix(rows)

    def join_mat_vec(self, other):
        if (self.__col != self.__row) or (self.__row != len(other)):
            raise RuntimeError("Matrix must be squared - n-dim and vector must be n-length")

        cols = copy.deepcopy(self.__cols)
        cols.append(other.values)
        rows = [list(t) for t in zip(*cols)]
        return MyMatrix(rows)

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def __eq__(self, other):
        if self.__rows == other.__rows:
            return True
        else:
            return False

    def __getitem__(self, idx):
        return self.__rows[idx]

    def __setitem__(self, idx, value):
        self.__rows[idx] = value
        return self.__rows[idx]

    def update_cols(self):
        return [list(t) for t in zip(*self.__rows)]

    def __repr__(self):
        res = ''
        for i in range(self.__row):
            for j in range(self.__col):
                res = res + str(self[i][j]) + "\t"
            res += "\n"
        return res

    def __add__(self, other):
         if isinstance(other, MyMatrix):
             if (self.__row != other.__row) or (self.__col != other.__col):
                 raise RuntimeError('Matrices must have the same dimensions!')
             rows = [0] * self.__row
             for i in range(self.__row):
                 rows[i] = [sum(t) for t in zip(self[i], other[i])]
             return MyMatrix(rows)

         else:
             raise RuntimeError('Adding is not supported for this type!')

    def __iadd__(self, other):
        tmp = self + other
        self.__rows = tmp.__rows
        self.__cols = tmp.__cols
        return self

    def __sub__(self, other):
         if isinstance(other, MyMatrix):
             if (self.__row != other.__row) or (self.__col != other.__col):
                 raise RuntimeError('Matrices must have the same dimensions!')
             rows = [0] * self.__row
             for i in range(self.__row):
                 rows[i] = [t[0] - t[1] for t in zip(self[i], other[i])]
             return MyMatrix(rows)

         else:
             raise RuntimeError('Substracting is not supported for this type!')

    def __isub__(self, other):
         tmp = self - other
         self.__rows = tmp.__rows
         self.__cols = tmp.__cols
         return self

    def __mul__(self, other):

         if isinstance(other, MyMatrix):
             if self.__col != other.__row:
                 raise RuntimeError('Columns of the first matrix must be equal to rows of other matrix')
             row = self.__row
             col = other.__col
             rows = [[0] * col for i in range(row)]

             for i in range(self.__row):
                 for j in range(other.__col):
                     rows[i][j] = sum([t[0] * t[1] for t in zip(self[i], other.__cols[j])])

         elif isinstance(other, (int, float)):
             rows = list()
             row = self.__row
             col = self.__col
             for i in range(self.__row):
                 rows.append([other * el for el in self[i]])

         elif isinstance(other, MyVector):
             vec = MyMatrix.create_from_cols(other[:])
             return MyVector(*(self * vec).__cols[:])

         else:
             raise RuntimeError('Multiplying is not supported for this type!')

         return MyMatrix(rows)

     # int/float * matrix
    __rmul__ = __mul__

    def __imul__(self, other):
         tmp = self * other
         self.__row = tmp.__row
         self.__col = tmp.__col
         self.__rows = tmp.__rows
         self.__cols = tmp.__cols
         return self

    def transpose(self):
         # create new matrix
         rows = self.update_cols()
         return MyMatrix(rows)

    def self_transpose(self):
         # returns self
         self.__rows, self.__cols = self.__cols, self.__rows
         self.__row, self.__col = self.__col, self.__row
         return self

    def reduce_rows(self):
        mat = copy.deepcopy(self)
        nr = mat.get_row()
        nc = mat.get_col()
        # num of swaps and operations
        s, op = 0, 0

        for r in range(nr):
            if all(mat[r][c] == 0 for c in range(nc)):
                # all zeroes row to the lowest one
                mat[r], mat[nr] = mat[nr], mat[r]
                s += 1
                nr -= 1

        p = 0
        while p < nr and p < nc:
            r = 1
            if mat[p][p] == 0:
                while mat[r][p] == 0:
                    r += 1
                mat[p], mat[p + r] = mat[p + r], mat[p]
                s += 1

            for r in range(1, nr-p):
                x = mat[p + r][p] / mat[p][p]
                for c in range(p, nc):
                    mat[p + r][c] -= mat[p][c] * x
                op += 1
            p += 1

        return mat, s, op

    def compute_determinant(self):
        # only for square matrix
        if self.__col != self.__row:
            raise RuntimeError("Matrix must be squared in order to compute the determinant")
        tmp = self.reduce_rows()
        s = tmp[1]
        mat_reduce = tmp[0]
        det = (-1)**s
        for i in range(mat_reduce.__row):
            det = det * mat_reduce[i][i]
        return det



#
# # Loading from file
# path = 'C:/Users/wikis/PycharmProjects/Project_ISEG/Matrix_file_10.txt'
# mat_10 = MyMatrix.load_from_file(path)
# assert mat_10.get_col() == 11
# assert mat_10.get_row() == 11

# try:
#     path = 'C:/Users/wikis/PycharmProjects/Project_ISEG/Nonexist.txt'
#     mat_wrong = MyMatrix.load_from_file(path)
# except RuntimeError as err:
#     print(err)
# try:
#     path = 'C:/Users/wikis/PycharmProjects/Project_ISEG/empty_file.txt'
#     mat_empty = MyMatrix.load_from_file(path)
# except RuntimeError as err:
#     print(err)
#
# # init - double array
# test1 = [[1, 2, 9, 5], [3, 3, 4, 8], [1, 2, 3, 9], [1, 2, 3, 4]]
# test2 = [[1, 2], [3, 4]]
# test3 = [[4, 2], [8, 1]]
# test4 = [[1, 2], [3, 4], [5, 6]]
# test5 = [[1, 2, 3], [4, 5, 6]]
#
# mat1 = MyMatrix(test1)
# mat2 = MyMatrix(test2)
# mat3 = MyMatrix(test3)
# mat4 = MyMatrix(test4)
# mat5 = MyMatrix(test5)
#
# print(mat1)
# print(mat1.get_row())
# print(mat1.get_col())
#
# # empty
# try:
#     # or other options
#     a = MyMatrix(5)
# except RuntimeError as err:
#     print(err)
#
# # adding
# print("First matrix")
# print(mat2)
# print("Second matrix")
# print(mat3)
# mat = mat2 + mat3
# print("Sum")
# print(mat)
#
# print("id before adding")
# print(id(mat2))
# mat2 += mat3
# print("id after adding")
# print(id(mat2))
#
# # subtracting
# print("First matrix")
# print(mat2)
# print("Second matrix")
# print(mat3)
# mat = mat2 - mat3
# print("Subtract")
# print(mat)
#
# print("id before subtracting")
# print(id(mat2))
# mat2 -= mat3
# print("id after subtracting")
# print(id(mat2))
#
# # multiplying
# print("First matrix")
# print(mat2)
# print("Second matrix")
# print(mat3)
# mat = mat2 * mat3
# print("Multiply")
# print(mat)
#
# print("Matrix")
# print(mat2)
# print("Number")
# print(2.5)
# mat = mat2 * 2.5
# print("Multiply")
# print(mat)
#
# print("id before multiplying")
# print(id(mat2))
# mat2 *= mat3
# print("id after multiplying")
# print(id(mat2))
#
# # transpose
# print("Matrix")
# print(mat2)
# mat = mat2.transpose()
# print("Transpose")
# print(mat)
#
# print("id before transpose")
# print(id(mat2))
# mat2.self_transpose()
# print("id after transpose")
# print(id(mat2))
#
# # row reducing
# print("Matrix")
# print(mat1)
# print("Row reducing")
# mat = mat1.reduce_rows()[0]
# print(mat)
#
# # det
# print("Matrix")
# print(mat2)
# print("Determinant")
# print(round(mat2.compute_determinant(), 2))