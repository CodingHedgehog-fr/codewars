from unittest import TestCase
from katas.Kyu_5 import (move_zeros,
                         fibonacci,
                         luck_check,
                         min_umbrellas,
                         proc_seq)


class TestKyu5(TestCase):
    """TestKyu5 class aims at unit testing Kyu_5.py module"""

    def test_move_zeros(self):

        self.assertEqual(move_zeros([1, 0, 1, 2, 0, 1, 3]), [1, 1, 2, 1, 3, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 2, 0, 1, 3]), [2, 1, 3, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0, 0, 2, 0, 1, 3]), [2, 1, 3, 0, 0, 0, 0])
        self.assertEqual(move_zeros([1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])
        self.assertEqual(move_zeros([1, 0, 0, 0, 0, 0, 2]), [1, 2, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                         [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([]), [])

    def test_fibonacci(self):

        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(70), 190392490709135)
        self.assertEqual(fibonacci(60), 1548008755920)
        self.assertEqual(fibonacci(50), 12586269025)

    def test_luck_check(self):

        self.assertEqual(luck_check('5555'), True)
        self.assertEqual(luck_check('003111'), True)
        self.assertEqual(luck_check('543970707'), False)
        self.assertEqual(luck_check('439924'), False)
        self.assertEqual(luck_check('943294329932'), False)
        self.assertEqual(luck_check('000000'), True)
        self.assertEqual(luck_check('454319'), True)
        self.assertEqual(luck_check('1233499943'), False)
        self.assertEqual(luck_check('935336'), False)
        self.assertRaises(Exception, luck_check, '6F43E8')
        self.assertRaises(Exception, luck_check, '1234 ')
        self.assertRaises(Exception, luck_check, '124-21')
        self.assertRaises(Exception, luck_check, '124X212')

    def test_min_umbrellas(self):
        self.assertEqual(min_umbrellas(["cloudy"]), 0)
        self.assertEqual(min_umbrellas(["rainy", "rainy", "rainy", "rainy"]), 1)
        self.assertEqual(min_umbrellas(["overcast", "rainy", "clear", "thunderstorms"]), 2)
        self.assertEqual(min_umbrellas(['rainy', 'sunny', 'cloudy', 'sunny', 'windy', 'thunderstorms',
                                        'thunderstorms', 'windy', 'thunderstorms', 'sunny', 'windy', 'thunderstorms',
                                        'cloudy', 'thunderstorms', 'cloudy', 'thunderstorms', 'windy', 'thunderstorms',
                                        'thunderstorms', 'windy', 'windy', 'cloudy', 'thunderstorms', 'cloudy',
                                        'thunderstorms', 'sunny', 'thunderstorms', 'cloudy', 'sunny', 'cloudy',
                                        'thunderstorms', 'sunny', 'rainy', 'cloudy', 'thunderstorms', 'thunderstorms',
                                        'sunny', 'cloudy', 'thunderstorms', 'windy', 'sunny', 'thunderstorms', 'rainy',
                                        'sunny', 'thunderstorms', 'thunderstorms', 'thunderstorms', 'thunderstorms',
                                        'cloudy', 'rainy', 'rainy', 'thunderstorms', 'cloudy', 'windy', 'thunderstorms',
                                        'thunderstorms', 'sunny', 'windy', 'rainy', 'sunny', 'windy', 'rainy', 'windy',
                                        'windy', 'thunderstorms', 'windy', 'rainy', 'sunny', 'windy', 'thunderstorms',
                                        'rainy', 'thunderstorms', 'thunderstorms', 'rainy', 'rainy', 'rainy',
                                        'thunderstorms', 'rainy', 'thunderstorms', 'thunderstorms', 'thunderstorms',
                                        'rainy', 'thunderstorms', 'thunderstorms', 'rainy', 'thunderstorms', 'windy',
                                        'thunderstorms', 'rainy', 'thunderstorms', 'windy', 'windy', 'sunny', 'cloudy',
                                        'windy', 'thunderstorms', 'thunderstorms', 'rainy', 'sunny',
                                        'thunderstorms']), 8)
        self.assertEqual(min_umbrellas(['windy', 'clear', 'rainy', 'windy', 'sunny', 'rainy', 'clear', 'cloudy',
                                        'clear', 'windy', 'windy', 'clear', 'windy', 'sunny', 'clear', 'sunny', 'sunny',
                                        'windy', 'clear', 'windy', 'sunny', 'sunny', 'clear', 'clear', 'windy', 'rainy',
                                        'clear', 'sunny', 'clear', 'windy', 'windy', 'clear', 'sunny', 'cloudy',
                                        'clear', 'thunderstorms', 'clear', 'windy', 'sunny', 'thunderstorms', 'sunny',
                                        'rainy', 'cloudy', 'sunny', 'sunny', 'clear', 'clear', 'windy', 'windy',
                                        'sunny', 'clear', 'thunderstorms', 'clear', 'sunny', 'sunny', 'windy', 'windy',
                                        'clear', 'cloudy', 'sunny', 'windy', 'sunny', 'clear', 'sunny', 'sunny',
                                        'clear', 'clear', 'clear', 'clear', 'cloudy', 'clear', 'clear', 'rainy',
                                        'clear', 'sunny', 'sunny', 'cloudy', 'clear', 'rainy', 'sunny', 'sunny',
                                        'clear', 'windy', 'sunny', 'windy', 'rainy', 'cloudy', 'clear', 'clear',
                                        'rainy', 'windy', 'clear', 'windy', 'rainy', 'sunny', 'windy', 'windy', 'clear',
                                        'sunny', 'clear']), 7)
        self.assertEqual(min_umbrellas(['clear', 'cloudy', 'cloudy', 'cloudy', 'clear', 'sunny', 'cloudy', 'sunny',
                                        'cloudy', 'clear']), 0)

    def test_proc_seq(self):

        self.assertEqual(proc_seq(23, 17, 89), [8, 218, 379, 2388])
        self.assertEqual(proc_seq(22, 22, 22, 22), [1, 2222])
        self.assertEqual(proc_seq(230, 15, 8), [4, 218, 358, 1152])
        self.assertEqual(proc_seq(4312, 9440, 3616, 1218, 9152, 8178, 8234, 6575, 6267),
                         [46656, 101111252, 496898877, 13860641773440])
