import unittest


def triple_step_with_memo_helper(n, memo):
    if n < 0:
        return 0
    else:
        if memo[n]:
            return memo[n]
        elif n == 0:
            memo[n] = 1
            return 1
        else:
            memo[n] = triple_step_with_memo_helper(n - 1, memo) + triple_step_with_memo_helper(n - 2, memo) + triple_step_with_memo_helper(n - 3, memo)
            return memo[n]


def triple_step_with_memo(n):
    memo = [None] * 100
    return triple_step_with_memo_helper(n, memo)


def triple_step(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


def get_robot_path_helper(maze, row, column, path, failed_points):
    if column < 0 or row < 0 or not maze[row][column]:
        return False

    if (row, column) in failed_points:
        return False

    is_at_origin = (row == 0 and column == 0)
    if is_at_origin or get_robot_path_helper(maze, row, column - 1, path, failed_points) or get_robot_path_helper(maze, row - 1, column, path, failed_points):
        path.append((row, column))
        return True

    failed_points.append((row, column))
    return False


def get_robot_path(maze):
    if not maze or len(maze) == 0:
        return None
    path = []
    failed_points = []
    if get_robot_path_helper(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


class Test(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(1, triple_step(1))
        self.assertEqual(2, triple_step(2))
        self.assertEqual(4, triple_step(3))
        self.assertEqual(7, triple_step(4))
        self.assertEqual(1, triple_step_with_memo(1))
        self.assertEqual(2, triple_step_with_memo(2))
        self.assertEqual(4, triple_step_with_memo(3))
        self.assertEqual(7, triple_step_with_memo(4))

    def test_robot_path(self):
        maze = [[1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [0, 1, 0, 1, 1],
                [0, 1, 0, 0, 1],
                [0, 1, 1, 1, 1]]
        self.assertEqual([(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)], get_robot_path(maze))


if __name__ == '__main__':
    unittest.main()
