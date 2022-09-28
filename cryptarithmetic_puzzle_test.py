# File: cryptarithmetic_puzzle_test.py

from unittest import TestCase, main
from cryptarithmetic_puzzle import solve_cryptarithmetic_puzzle


class TestCryptarithmetic(TestCase):

    def test_cryptarithmetic_puzzle_1(self):
        self.assertEqual(
            {'X': 1, 'Y': 2, 'Z': 8},
            solve_cryptarithmetic_puzzle(['x', 'y', 'z'], 'xx'))

    def test_cryptarithmetic_puzzle_2(self):
        self.assertEqual(
            {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5,
             'F': 7, 'G': 8, 'H': 9, 'I': 3, 'J': 6},
            solve_cryptarithmetic_puzzle(['A', 'B', 'C', 'D',
                                          'E', 'F', 'G', 'H'],
                                         'IJ'))

    def test_cryptarithmetic_puzzle_3(self):
        self.assertEqual(
            {'A': 1, 'B': 9, 'C': 8},
            solve_cryptarithmetic_puzzle(['ab', 'bc', 'ca'], 'abc'))

    def test_cryptarithmetic_puzzle_4(self):
        self.assertEqual(
            {'X': 1, 'Y': 9, 'Z': 8},
            solve_cryptarithmetic_puzzle(['xx', 'yy', 'zz'], 'xyz'))

    def test_cryptarithmetic_puzzle_5(self):
        self.assertEqual(
            {'X': 9, 'Y': 1, 'Z': 8},
            solve_cryptarithmetic_puzzle(['xxxx', 'yyyy', 'zzzz'],
                                         'yxxxz'))

    def test_cryptarithmetic_puzzle_6(self):
        self.assertEqual(
            {'X': 1, 'Y': 9, 'Z': 8},
            solve_cryptarithmetic_puzzle(['xxxx', 'yyyy', 'zzzz'],
                                         'xyyyz'))

    def test_cryptarithmetic_puzzle_7(self):
        self.assertIsNone(
            solve_cryptarithmetic_puzzle(['x', 'y', 'z'], 'xxx'))

    def test_cryptarithmetic_puzzle_8(self):
        self.assertIsNone(
            solve_cryptarithmetic_puzzle(['x', 'y', 'z'], 'xyz'))

    def test_cryptarithmetic_puzzle_9(self):
        self.assertEqual(
            {'E': 0, 'I': 2, 'L': 3, 'S': 6, 'U': 9, 'V': 5, 'Y': 4},
            solve_cryptarithmetic_puzzle(['i', 'luv', 'u'], 'yes'))

    def test_cryptarithmetic_puzzle_10(self):
        self.assertEqual(
            {'A': 7, 'E': 8, 'G': 9, 'P': 1},
            solve_cryptarithmetic_puzzle(['egg', 'egg'], 'page'))

    def test_cryptarithmetic_puzzle_11(self):
        self.assertEqual(
            {'A': 0, 'D': 4, 'H': 7, 'M': 3, 'R': 1, 'T': 5, 'Y': 9},
            solve_cryptarithmetic_puzzle(['math', 'myth'], 'hard'))

    def test_cryptarithmetic_puzzle_12(self):
        self.assertEqual(
            {'F': 1, 'I': 3, 'M': 4, 'N': 7, 'S': 0, 'U': 6, 'W': 2},
            solve_cryptarithmetic_puzzle(['fun', 'sun'], 'swim'))

    def test_cryptarithmetic_puzzle_13(self):
        self.assertEqual(
            {'D': 5, 'E': 1, 'N': 0, 'O': 6, 'V': 3},
            solve_cryptarithmetic_puzzle(['odd', 'odd'], 'even'))

    def test_cryptarithmetic_puzzle_14(self):
        self.assertEqual(
            {'F': 0, 'O': 2, 'R': 4, 'T': 1, 'U': 6, 'W': 3},
            solve_cryptarithmetic_puzzle(['two', 'two'], 'four'))

    def test_cryptarithmetic_puzzle_15(self):
        self.assertEqual(
            {'A': 0, 'F': 1, 'L': 3, 'W': 4, 'Y': 5},
            solve_cryptarithmetic_puzzle(['fly', 'fly', 'fly'],
                                         'away'))

    def test_cryptarithmetic_puzzle_16(self):
        self.assertEqual(
            {'A': 1, 'E': 8, 'H': 2, 'L': 3, 'P': 0, 'T': 9},
            solve_cryptarithmetic_puzzle(['EAT', 'THAT'], 'APPLE'))

    def test_cryptarithmetic_puzzle_17(self):
        self.assertEqual(
            {'G': 8, 'O': 1, 'T': 2, 'U': 0},
            solve_cryptarithmetic_puzzle(['to', 'go'], 'out'))

    def test_cryptarithmetic_puzzle_18(self):
        self.assertEqual(
            {'D': 1, 'E': 5, 'M': 0, 'N': 3,
             'O': 8, 'R': 2, 'S': 7, 'Y': 6},
            solve_cryptarithmetic_puzzle(['SEND', 'MORE'], 'MONEY'))


if __name__ == '__main__':
    main()