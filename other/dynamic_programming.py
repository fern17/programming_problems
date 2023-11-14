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
    """A child is running up a staircase with N steps. He can jump either 1, 2 or 3 steps. Calculate how many possible ways
    can the child climb the staircase"""
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
    """Write a function to help a robot find its way in a maze. There could be some cells where the robot cannot walk"""
    if not maze or len(maze) == 0:
        return None
    path = []
    failed_points = []
    if get_robot_path_helper(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


def product_without_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    half = smaller >> 1
    half_prod = product_without_product_helper(half, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger


def product_without_product(a, b):
    """Write a function to calculate the product of two numbers without using the product operator"""
    smaller, bigger = (a, b) if (a < b) else (b, a)
    return product_without_product_helper(smaller, bigger)


def hanoi_helper(n, tower_origin, tower_destination, tower_buffer):
    if n <= 0:
        return
    hanoi_helper(n - 1, tower_origin, tower_buffer, tower_destination)
    tower_destination.append(tower_origin.pop())
    hanoi_helper(n - 1, tower_buffer, tower_destination, tower_origin)


def hanoi(n):
    """Solve the classic Towers of Hanoi problem for any value of N"""
    tower_origin = [i for i in range(1, n + 1)]
    tower_buffer = []
    tower_destination = []
    hanoi_helper(n, tower_origin, tower_destination, tower_buffer)
    return tower_destination


def all_permutations(s):
    """Write a method to compute all permutations of a string with unique characters"""
    if not s:
        return ['']
    perms = []
    if len(s) == 0:
        perms.append('')
        return perms
    head = s[0]
    tail = s[1:]
    tail_perms = all_permutations(tail)
    for word in tail_perms:
        for j in range(len(word) + 1):
            sp = word[0:j] + head + word[j:]
            perms.append(sp)
    return perms


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

    def test_product(self):
        self.assertEqual(56, product_without_product(8, 7))
        self.assertEqual(64, product_without_product(8, 8))
        self.assertEqual(2425, product_without_product(25, 97))

    def test_hanoi(self):
        self.assertEqual([1, 2, 3], hanoi(3))
        self.assertEqual([1, 2, 3, 4], hanoi(4))
        self.assertEqual([1, 2, 3, 4, 5], hanoi(5))

    def test_all_permutations(self):
        self.assertEqual(['a'], all_permutations('a'))
        self.assertEqual(['ab', 'ba'], all_permutations('ab'))
        self.assertEqual(['abc', 'bac', 'bca', 'acb', 'cab', 'cba'], all_permutations('abc'))


if __name__ == '__main__':
    unittest.main()
