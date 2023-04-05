#!/usr/bin/python3
import unittest


class TestListLength(unittest.TestCase):

    def test_empty_list(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_list_of_string(self):
        my_list = ["product of", "Aminta left", "Fatou", "Djibril"]
        self.assertEqual(max_integer(my_list), "product of")

    def test_list_of_integers(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_list_of_floats(self):
        my_list = [6.4, 6.1, 6.7, 6.5]
        self.assertEqual(max_integer(my_list), 6.7)


if __name__ == "__main__":
    unittest.main()
