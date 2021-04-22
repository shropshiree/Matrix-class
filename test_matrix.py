import unittest
from matrix import MyMatrix


class LoadingFromFile(unittest.TestCase):
    def test_normal_load(self):
        path = 'Matrix_file_10.txt'
        mat_10 = MyMatrix.load_from_file(path)
        self.assertIsInstance(mat_10, MyMatrix)

    def test_non_exist(self):
        path = 'Nonexist.txt'
        with self.assertRaises(RuntimeError):
            mat_wrong = MyMatrix.load_from_file(path)

    def test_file_empty(self):
        path = 'empty_file.txt'
        with self.assertRaises(RuntimeError):
            mat_empty = MyMatrix.load_from_file(path)


class InitMatrix(unittest.TestCase):
    def test_normal_square(self):
        test1 = [[1, 2, 9, 5], [3, 3, 4, 8], [1, 2, 3, 9], [1, 2, 3, 4]]
        mat1 = MyMatrix(test1)
        self.assertEqual(mat1.get_row(), 4)
        self.assertEqual(mat1.get_col(), 4)

    def test_normal_nonsquare(self):
        test4 = [[1, 2], [3, 4], [5, 6]]
        mat4 = MyMatrix(test4)
        self.assertEqual(mat4.get_row(), 3)
        self.assertEqual(mat4.get_col(), 2)

    def test_int(self):
        with self.assertRaises(RuntimeError):
            mat_bad = MyMatrix(5)

    def test_emptylist(self):
        with self.assertRaises(RuntimeError):
            mat_bad = MyMatrix([])

    def test_emptydbllist(self):
        with self.assertRaises(RuntimeError):
            mat_bad = MyMatrix([[]])

    def test_not_good_rows(self):
        with self.assertRaises(RuntimeError):
            mat_bad = MyMatrix([['a', 'b'], ['c', 'd']])


class SaveToFile(unittest.TestCase):
    def save_normal(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        mat3.save_to_file("test.txt")
        mat = MyMatrix.load_from_file("test.txt")
        self.assertEqual(mat3, mat)

class Adding(unittest.TestCase):
    def test_normal_add(self):
        test2 = [[1, 2], [3, 4]]
        test3 = [[4, 2], [8, 1]]
        mat2 = MyMatrix(test2)
        mat3 = MyMatrix(test3)
        self.assertEqual(mat2 + mat3, MyMatrix([[5, 4], [11, 5]]))

    def test_normal_iadd(self):
        mat2 = MyMatrix([[1, 2], [3, 4]])
        mat3 = MyMatrix([[4, 2], [8, 1]])
        id1 = id(mat2)
        mat2 += mat3
        id2 = id(mat2)
        self.assertEqual(id1, id2)

    def test_add_not_matrix(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        with self.assertRaises(RuntimeError):
            wrong = mat3 + 5

    def test_add_wrong_matrix(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        mat4 = MyMatrix([[1, 2, 3]])
        with self.assertRaises(RuntimeError):
            wrong = mat3 + mat4


class Subtracting(unittest.TestCase):
    def test_normal_sub(self):
        test2 = [[1, 2], [3, 4]]
        test3 = [[4, 2], [8, 1]]
        mat2 = MyMatrix(test2)
        mat3 = MyMatrix(test3)
        self.assertEqual(mat2 - mat3, MyMatrix([[-3, 0], [-5, 3]]))

    def test_normal_isub(self):
        mat2 = MyMatrix([[1, 2], [3, 4]])
        mat3 = MyMatrix([[4, 2], [8, 1]])
        id1 = id(mat2)
        mat2 -= mat3
        id2 = id(mat2)
        self.assertEqual(id1, id2)

    def test_sub_not_matrix(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        with self.assertRaises(RuntimeError):
            wrong = mat3 - 5

    def test_sub_wrong_matrix(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        mat4 = MyMatrix([[1, 2, 3]])
        with self.assertRaises(RuntimeError):
            wrong = mat3 - mat4


class Multiplying(unittest.TestCase):
    def test_normal_mul_matrix(self):
        test2 = [[1, 2]]
        test3 = [[1, 2], [3, 4]]
        mat2 = MyMatrix(test2)
        mat3 = MyMatrix(test3)
        self.assertEqual(mat2 * mat3, MyMatrix([[7, 10]]))

    def test_normal_mul_int(self):
        test3 = [[1, 2], [3, 4]]
        mat3 = MyMatrix(test3)
        self.assertEqual(mat3 * 2, MyMatrix([[2, 4], [6, 8]]))

    def test_normal_rmul_int(self):
        test3 = [[1, 2], [3, 4]]
        mat3 = MyMatrix(test3)
        self.assertEqual(2 * mat3, MyMatrix([[2, 4], [6, 8]]))

    def test_normal_imul(self):
        mat2 = MyMatrix([[1, 2], [3, 4]])
        mat3 = MyMatrix([[4, 2], [8, 1]])
        id1 = id(mat2)
        mat2 *= mat3
        id2 = id(mat2)
        self.assertEqual(id1, id2)

    def test_mul_bad_instance(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        with self.assertRaises(RuntimeError):
            wrong = mat3 * 'ab'

    def test_mul_wrong_matrix(self):
        mat3 = MyMatrix([[4, 2], [8, 1]])
        mat4 = MyMatrix([[1, 2, 3]])
        with self.assertRaises(RuntimeError):
            wrong = mat3 * mat4


class Transpose(unittest.TestCase):
    def test_normal_tran(self):
        mat2 = MyMatrix([[1, 2], [3, 4]])
        mat = mat2.transpose()
        self.assertEqual(mat, MyMatrix([[1, 3], [2, 4]]))

    def test_normal_itran(self):
        mat2 = MyMatrix([[1, 2], [3, 4]])
        id1 = id(mat2)
        mat2.self_transpose()
        id2 = id(mat2)
        self.assertEqual(id1, id2)


class Determinant(unittest.TestCase):
    def test_det_good(self):
        mat2 = MyMatrix([[1, 2], [3, 4]])
        det = mat2.compute_determinant()
        self.assertEqual(det, -2.0)

    def test_det_nonsquare(self):
        mat2 = MyMatrix([[1, 2], [3, 4], [5, 6]])
        with self.assertRaises(RuntimeError):
            det = mat2.compute_determinant()


if __name__ == '__main__':
    unittest.main()

