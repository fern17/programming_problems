import unittest

# Given an N*M matrix, if an (i,j) index is zero, all the i row and j column should be converted to zero


def zero_matrix(matrix):
    if len(matrix) == 0:
        return matrix
    if len(matrix[0]) == 0:
        return matrix
    zero_column = -1
    zero_row = -1
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                if zero_row == -1:
                    zero_row = i
                if zero_column == -1:
                    zero_column = j
                matrix[zero_row][j] = 0
                matrix[i][zero_column] = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if i == zero_row or j == zero_column:
                continue
            if (zero_row != -1 and matrix[zero_row][j] == 0) or (zero_column != -1 and matrix[i][zero_column] == 0):
                matrix[i][j] = 0
    if zero_row != -1:
        for j in range(0, len(matrix[0])):
            matrix[zero_row][j] = 0
    if zero_column != -1:
        for i in range(0, len(matrix)):
            matrix[i][zero_column] = 0

    return matrix


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([[]], zero_matrix([[]]))
        self.assertEqual([[1]], zero_matrix([[1]]))
        self.assertEqual([[0]], zero_matrix([[0]]))
        self.assertEqual([[0, 0]], zero_matrix([[1, 0]]))
        self.assertEqual([[0, 0]], zero_matrix([[0, 1]]))
        self.assertEqual([[0, 0], [0, 0]], zero_matrix([[0, 1], [1, 0]]))
        self.assertEqual([[0, 0, 0], [0, 5, 0], [0, 0, 0]], zero_matrix([[0, 2, 3], [4, 5, 6], [7, 8, 0]]))
        self.assertEqual([[0, 0, 0], [4, 0, 6], [7, 0, 9]], zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    unittest.main()
