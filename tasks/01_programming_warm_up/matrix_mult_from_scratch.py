#!/usr/bin/env python3
import unittest


def matrix_dot_matrix(x, y):
    # Implement an algorithm of multiplication itself using loops and lists
    # https://github.com/korobool/hlll_course/blob/master/tasks/programming_warm_up.md
    try:
        c = []
        # X is an n×m matrix and Y is an m×p matrix
        n = len(x)
        m = len(x[0])
        p = len(y[0])
        if m != len(y):
            print('The product XY is not defined')
            return None
        # naive algorithm with computational complexity O(n^{3})
        # Algo improvements (e.g. Strassen algorithm) are out of scope
        for i in range(n):
            c.append([])
            for j in range(p):
                c[i].append(sum(x[i][r]*y[r][j] for r in range(m)))
        return c
    except Exception as e:
        print(e)
        return None


class TestProduct(unittest.TestCase):

    # Negative tests
    def test_product_not_matrix(self):
        self.assertIsNone(matrix_dot_matrix([], [[1]]), 'Should be None')

    def test_product_strings(self):
        self.assertIsNone(matrix_dot_matrix([[1]], [['1']]), 'Should be None')

    def test_product_not_defined(self):
        self.assertIsNone(matrix_dot_matrix([[1, 2], [3]], [[4], [5]]), 'Should be None')

    def test_product_wrong_shape(self):
        self.assertIsNone(matrix_dot_matrix([[1]], [[1], [2]]), 'Should be None')

    # Positive tests
    def test_product_E1(self):
        E1 = [[1]]
        self.assertEqual(matrix_dot_matrix(E1, E1), E1, f'Should be {E1}')

    def test_product_E2_float(self):
        E2 = [[1., 0], [0, 1]]
        m = [[1, 2.], [3., 4]]
        self.assertEqual(matrix_dot_matrix(E2, m), m, f'Should be {m}')

    def test_product_2x1_dot_1x1(self):
        result = [[3], [6]]
        self.assertEqual(matrix_dot_matrix([[1], [2]], [[3]]), result, f'Should be {result}')

    def test_product_1x2_dot_2x1(self):
        result = [[11]]
        self.assertEqual(matrix_dot_matrix([[1, 2]], [[3], [4]]), result, f'Should be {result}')

    def test_product_2x2_dot_2x2(self):
        result = [[19, 22], [43, 50]]
        self.assertEqual(matrix_dot_matrix([[1, 2], [3, 4]], [[5, 6], [7, 8]]), result, f'Should be {result}')

    def test_product_3x3_dot_3x4(self):
        result = [[55, 65, 49, 5], [57, 68, 72, 12], [90, 107, 111, 21]]
        self.assertEqual(matrix_dot_matrix(
            [[1, 7, 3], [3, 5, 6], [6, 8, 9]],
            [[1, 1, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]),
            result,
            f'Should be {result}')


if __name__ == '__main__':
    unittest.main()
