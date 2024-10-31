import unittest
from simplemath4test.simplemath4test import add, subtract


class TestSimpleMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, 4), -2)


if __name__ == "__main__":
    unittest.main()
