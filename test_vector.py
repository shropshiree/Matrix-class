from vector import MyVector
import unittest


class TestLoadFromFile(unittest.TestCase):
    '''Tests for method load_from_file from class MyVector'''

    # testing if vector is read properly
    def test_load_from_file(self):
        result = MyVector.load_from_file('file.txt')
        self.assertEqual(result.values, [1.0, 2.0, 3.0])

    # testing if vector with two-digit number is read properly
    def test_load_twoDigits(self):
        result = MyVector.load_from_file('twoDigits.txt')
        self.assertEqual(result.values, [10.0, 20.0, 30.0])

    # testing reading from file with wrong value (one string which is omitted)
    def test_values(self):
        with self.assertRaises(RuntimeError):
            result = MyVector.load_from_file('wrongValues.txt')


    # testing loading empty file
    def test_empty_file(self):
        with self.assertRaises(RuntimeError):
            result = MyVector.load_from_file('empty_file.txt')

    # testing loading from file which does not exist
    def test_not_exist(self):
        with self.assertRaises(RuntimeError):
            result = MyVector.load_from_file('nonExist.txt')


class TestSaveToFile(unittest.TestCase):
    '''Tests for method save_to_file from class MyVector'''

    # testing if vector is save properly
    def test_save_to_file(self):
        v1 = MyVector([1, 2, 3])
        result = v1.save_to_file('save.txt')
        check = MyVector.load_from_file('save.txt')
        self.assertEqual(check.values, [1.0, 2.0, 3.0])

    # testing if vector is save properly
    def test_save_digit(self):
        v1 = MyVector([10, 20, 30])
        result = v1.save_to_file('twoDigits_save.txt')
        check = MyVector.load_from_file('twoDigits_save.txt')
        self.assertEqual(check.values, [10.0, 20.0, 30.0])

    # testing saving empty list
    def test_save_empty(self):
        v1 = MyVector([])
        with self.assertRaises(RuntimeError):
            result = v1.save_to_file('empty_save.txt')


class TestAdd(unittest.TestCase):
    '''Tests for method __add__ from class MyVector'''

    def setUp(self):
        """This function creates objects which will be used in all tests"""
        self.vector1 = MyVector([1, 2, 3])
        self.vector2 = MyVector([4, 5, 6])
        self.vector3 = MyVector([1, 2, 3, 4, 5])
        self.vector4 = MyVector([])
        self.vector5 = MyVector([6, 7, 8, 9, 10])

    # testing the sum of 2 vectors with lengths equal to 3
    def test_add_vector3(self):
        result = self.vector1 + self.vector2
        self.assertEqual(result.values, [5, 7, 9])

    # testing the sum of 2 vectors with lengths equal to 5
    def test_add_vector5(self):
        result = self.vector3 + self.vector5
        self.assertEqual(result.values, [7, 9, 11, 13, 15])

    # testing the sum of 2 vectors with lengths equal to 3 for method __iadd__
    def test_iadd_vector3(self):
        self.vector1 += self.vector2
        self.assertEqual(self.vector1.values, [5, 7, 9])

    # testing the sum of 2 vectors with lengths equal to 5 for method __iadd__
    def test_iadd_vector5(self):
        self.vector3 += self.vector5
        self.assertEqual(self.vector3.values, [7, 9, 11, 13, 15])

    # testing the sum of vector and number
    def test_add_number(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 + 5

    # testing the sum of vector and string
    def test_add_string(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 + 'f'

    # testing the sum of vector and empty list
    def test_add_empty(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 + self.vector4

    # testing the sum of vectors with another lengths
    def test_add_lengths(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 + self.vector3



class TestMul(unittest.TestCase):
    '''Tests for method __mul__ from class MyVector'''

    def setUp(self):
        """This function creates objects which will be used in all tests"""
        self.vector1 = MyVector([1, 2, 3])
        self.vector2 = MyVector([4, 5, 6])
        self.vector3 = MyVector([1, 2, 3, 4, 5])
        self.vector4 = MyVector([])
        self.vector5 = MyVector([6, 7, 8, 9, 10])

    # testing the multiplication of 2 vectors with lenghts equal to 3
    def test_mul_vector3(self):
        result = self.vector1 * self.vector2
        self.assertEqual(result.values, [4, 10, 18])

    # testing the multiplication of 2 vectors with lenghts equal to 5
    def test_mul_vector5(self):
        result = self.vector3 * self.vector5
        self.assertEqual(result.values, [6, 14, 24, 36, 50])

    # testing the multiplication of vector and number
    def test_mul_number(self):
        result = self.vector1 * 5
        self.assertEqual(result.values, [5, 10, 15])

    # testing the multiplication of 2 vectors with lenghts equal to 3 for __imul__ method
    def test_imul_vector3(self):
            self.vector1 *= self.vector2
            self.assertEqual(self.vector1.values, [4, 10, 18])

    # testing the multiplication of 2 vectors with lenghts equal to 5 for __imul__ method
    def test_imul_vector5(self):
            self.vector3 *= self.vector5
            self.assertEqual(self.vector3.values, [6, 14, 24, 36, 50])

    # testing the multiplication of vector and number for __imul__ method
    def test_imul_number(self):
        self.vector1 *= 5
        self.assertEqual(self.vector1.values, [5, 10, 15])


    # testing the multiplication of vector and string
    def test_mul_string(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 * 'f'

    # testing the multiplication of vector and empty list
    def test_mul_empty(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 * self.vector4

    # testing the multiplication of vectors with another lengths
    def test_mul_lengths(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1 * self.vector3


class TestInnerProduct(unittest.TestCase):
    '''Tests for method inner_product from class MyVector'''

    def setUp(self):
        """This function creates objects which will be used in all tests"""
        self.vector1 = MyVector([1, 2, 3])
        self.vector2 = MyVector([4, 5, 6])
        self.vector3 = MyVector([1, 2, 3, 4, 5])
        self.vector4 = MyVector([])
        self.vector5 = MyVector([6, 7, 8, 9, 10])

    # testing the inner product of 2 vectors with length = 3
    def test_innerproduct_vectors3(self):
        result = self.vector1.inner_product(self.vector2)
        self.assertEqual(result.values, [32])

    # testing the inner product of 2 vectors with length = 5
    def test_innerproduct_vectors5(self):
        result = self.vector3.inner_product(self.vector5)
        self.assertEqual(result.values, [130])

    # testing the inner product of vector and number
    def test_innerproduct_number(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.inner_product(5)

    # testing the inner product of vector and string
    def test_innerproduct_string(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.inner_product('f')

    # testing the inner product of vector and empty list
    def test_innerproduct_empty(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.inner_product(self.vector4)

    # testing the inner product of vectors with another lengths
    def test_innerproduct_another_lenghts(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.inner_product(self.vector3)



class TestCrossProduct(unittest.TestCase):
    '''Tests for method cross_product from class MyVector'''

    def setUp(self):
        """This function creates objects which will be used in all tests"""
        self.vector1 = MyVector([1, 2, 3])
        self.vector2 = MyVector([4, 5, 6])
        self.vector3 = MyVector([1, 2, 3, 4, 5])
        self.vector4 = MyVector([])
        self.vector5 = MyVector([6, 7, 8, 9, 10])

    # testing the cross product of 2 vectors with length = 3
    def test_crossproduct_vectors3(self):
        result = self.vector1.cross_product(self.vector2)
        self.assertEqual(result.values, [-3, 6, -3])

    # testing the cross product of vector and number
    def test_crossproduct_number(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.cross_product(5)

    # testing the cross product of vector and string
    def test_crossproduct_string(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.cross_product('f')

    # testing the cross product of vector and empty list
    def test_crossproduct_empty(self):
        with self.assertRaises(RuntimeError):
            result = self.vector1.cross_product(self.vector4)

    # testing the cross product of 2 vectors with length = 5
    def test_crossproduct_vectors5(self):
        with self.assertRaises(RuntimeError):
            result = self.vector3.cross_product(self.vector5)


class TestRandomVector(unittest.TestCase):
    '''Tests for method random_vectors from class MyVector'''

    # testing if empty list is possible
    def test_empty_vector(self):
        with self.assertRaises(RuntimeError):
            result = MyVector.random_vector(0)


if __name__ == '__main__':
    unittest.main()