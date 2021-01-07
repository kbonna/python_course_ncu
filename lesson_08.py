# Benefits of unit testing:
#
# 1. Safe and confident refactoring
# 2. Improve quality of code
# 3. Find bugs early
# 4. Provides documentation
# 5. Forces to think about design
# 6. Reduce development cost in the long run

import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be 0")
    return a / b


def adjacent_element_product(array):
    products = [array[i] * array[i + 1] for i in range(len(array) - 1)]
    return max(products)


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(5, 100), 105)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(5, 100), -95)

    def test_multiply(self):
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(3, -5), -15)
        # self.assertEqual(multiply(0.1, 3), 3)

    def test_divide(self):
        self.assertEqual(divide(5, 1), 5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(1, 2), 0.5)

        with self.assertRaises(ValueError):
            divide(1, 0)


class TestArrayFunctions(unittest.TestCase):
    def test_adjacent_element_product(self):
        self.assertEqual(adjacent_element_product([1, 2]), 2)
        self.assertEqual(adjacent_element_product([1, 1, 1, 1]), 1)
        self.assertEqual(adjacent_element_product([1, 2, 3, 4, 5]), 20)
        self.assertEqual(adjacent_element_product([0, 1, 0, 1]), 0)
        self.assertEqual(adjacent_element_product([0, 1, 0, 1]), 0)


if __name__ == "__main__":
    unittest.main()
