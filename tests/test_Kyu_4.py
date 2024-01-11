from unittest import TestCase
from katas.Kyu_4 import (strip_comments,
                         snail,
                         sum_of_intervals,
                         User,
                         exp_sum,
                         balanced_parens)


class TestKyu4(TestCase):
    """Testutils class aims at unit testing Kyu_4.py module"""

    def test_strip_comments(self):

        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                         "apples, pears\ngrapes\nbananas")
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
                         'apples, pears\ngrapes\nbananas')
        self.assertEqual(strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !#apples', ['#', '!']),
                         'apples, pears\ngrapes\nbananas')
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas #!apples', ['#', '!']),
                         'apples, pears\ngrapes\nbananas')
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\navocado @apples', ['@', '!']),
                         'apples, pears # and bananas\ngrapes\navocado')
        self.assertEqual(strip_comments('apples, pears § and bananas\ngrapes\navocado *apples', ['*', '§']),
                         'apples, pears\ngrapes\navocado')
        self.assertEqual(strip_comments('\tapples, pears § and bananas\ngrapes\navocado *apples', ['*', '§']),
                         '\tapples, pears\ngrapes\navocado')
        self.assertEqual(strip_comments('  apples, pears § and bananas\ngrapes\navocado *apples', ['*', '§']),
                         '  apples, pears\ngrapes\navocado')
        self.assertEqual(strip_comments('', ['#', '!']), '')
        self.assertEqual(strip_comments('#', ['#', '!']), '')
        self.assertEqual(strip_comments('\n§', ['#', '§']), '\n')
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', []),
                         'apples, pears # and bananas\ngrapes\nbananas !apples')

    def test_snail(self):

        self.assertEqual(snail([[]]), [])
        self.assertEqual(snail([[1]]), [1])
        self.assertEqual(snail([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]),
                         [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertEqual(snail([[1, 2, 3],
                                [8, 9, 4],
                                [7, 6, 5]]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(snail([[1,  2,  3,  4,  5],
                                [6,  7,  8,  9, 10],
                                [11, 12, 13, 14, 15],
                                [16, 17, 18, 19, 20],
                                [21, 22, 23, 24, 25]]),
                         [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12,
                          13])
        self.assertEqual(snail([[1,  2,  3,  4,  5,  6],
                                [20, 21, 22, 23, 24,  7],
                                [19, 32, 33, 34, 25,  8],
                                [18, 31, 36, 35, 26,  9],
                                [17, 30, 29, 28, 27, 10],
                                [16, 15, 14, 13, 12, 11]]),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                          25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])

    def test_sum_of_intervals(self):

        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
        self.assertEqual(sum_of_intervals([(1, 2), (6, 10), (11, 15)]), 9)
        self.assertEqual(sum_of_intervals([(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)]), 19)
        self.assertEqual(sum_of_intervals([(1, 4), (3, 8), (10, 13), (5, 10), (7, 12), (11, 20)]), 19)
        self.assertEqual(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
        self.assertEqual(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)

    def _test_ranking_and_progress(self, user, rank, expected_rank, expected_progress):
        if rank:
            user.inc_progress(rank)
        self.assertEqual(user.rank, expected_rank, "After applying rank of " + str(rank))
        self.assertEqual(user.progress, expected_progress, "After applying rank of " + str(rank))

    def test_class_user(self):
        user = User()
        self._test_ranking_and_progress(user, -8, -8, 3)

        user = User()
        self._test_ranking_and_progress(user, -7, -8, 10)

        user = User()
        self._test_ranking_and_progress(user, -6, -8, 40)

        user = User()
        self._test_ranking_and_progress(user, -5, -8, 90)

        user = User()
        self._test_ranking_and_progress(user, -4, -7, 60)

        user = User()
        self._test_ranking_and_progress(user, 1, -2, 40)
        self._test_ranking_and_progress(user, 1, -2, 80)
        self._test_ranking_and_progress(user, 1, -1, 20)
        self._test_ranking_and_progress(user, 1, -1, 30)
        self._test_ranking_and_progress(user, 1, -1, 40)
        self._test_ranking_and_progress(user, 2, -1, 80)
        self._test_ranking_and_progress(user, 2, 1, 20)
        self._test_ranking_and_progress(user, -1, 1, 21)
        self._test_ranking_and_progress(user, 3, 1, 61)
        self._test_ranking_and_progress(user, 8, 6, 51)
        self._test_ranking_and_progress(user, 8, 6, 91)
        self._test_ranking_and_progress(user, 8, 7, 31)
        self._test_ranking_and_progress(user, 8, 7, 41)
        self._test_ranking_and_progress(user, 8, 7, 51)
        self._test_ranking_and_progress(user, 8, 7, 61)
        self._test_ranking_and_progress(user, 8, 7, 71)
        self._test_ranking_and_progress(user, 8, 7, 81)
        self._test_ranking_and_progress(user, 8, 7, 91)
        self._test_ranking_and_progress(user, 8, 8, 0)
        self._test_ranking_and_progress(user, 8, 8, 0)

        # in case of invalid ranking, should raise an exception
        self.assertRaises(Exception, user.inc_progress, 9)
        self.assertRaises(Exception, user.inc_progress, -9)
        self.assertRaises(Exception, user.inc_progress, 0)

    def test_exp_sum(self):

        self.assertEqual(exp_sum(1), 1, 'Testing for 1')
        self.assertEqual(exp_sum(2), 2, 'Testing for 2')
        self.assertEqual(exp_sum(3), 3, 'Testing for 3')
        self.assertEqual(exp_sum(4), 5, 'Testing for 4')
        self.assertEqual(exp_sum(5), 7, 'Testing for 5')
        self.assertEqual(exp_sum(20), 627, 'Testing for 20')
        self.assertEqual(exp_sum(30), 5604, 'Testing for 30')
        self.assertEqual(exp_sum(40), 37338, 'Testing for 40')
        self.assertEqual(exp_sum(43), 63261, 'Testing for 43')
        self.assertEqual(exp_sum(60), 966467, 'Testing for 60')
        self.assertEqual(exp_sum(70), 4087968, 'Testing for 70')
        self.assertEqual(exp_sum(90), 56634173, 'Testing for 90')
        self.assertEqual(exp_sum(200), 3972999029388, 'Testing for 200')
        self.assertEqual(exp_sum(275), 1520980492851175, 'Testing for 275')

    def test_balanced_parens(self):

        self.assertEqual(balanced_parens(0), [""])
        self.assertEqual(balanced_parens(1), ["()"])
        self.assertEqual(balanced_parens(2), sorted(["(())", "()()"]))
        self.assertEqual(balanced_parens(3), sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]))
        self.assertEqual(balanced_parens(6), sorted(['(((((())))))', '((((()()))))', '((((())())))', '((((()))()))',
                                                     '((((())))())', '((((()))))()', '(((()(()))))', '(((()()())))',
                                                     '(((()())()))', '(((()()))())', '(((()())))()', '(((())(())))',
                                                     '(((())()()))', '(((())())())', '(((())()))()', '(((()))(()))',
                                                     '(((()))()())', '(((()))())()', '(((())))(())', '(((())))()()',
                                                     '((()((()))))', '((()(()())))', '((()(())()))', '((()(()))())',
                                                     '((()(())))()', '((()()(())))', '((()()()()))', '((()()())())',
                                                     '((()()()))()', '((()())(()))', '((()())()())', '((()())())()',
                                                     '((()()))(())', '((()()))()()', '((())((())))', '((())(()()))',
                                                     '((())(())())', '((())(()))()', '((())()(()))', '((())()()())',
                                                     '((())()())()', '((())())(())', '((())())()()', '((()))((()))',
                                                     '((()))(()())', '((()))(())()', '((()))()(())', '((()))()()()',
                                                     '(()(((()))))', '(()((()())))', '(()((())()))', '(()((()))())',
                                                     '(()((())))()', '(()(()(())))', '(()(()()()))', '(()(()())())',
                                                     '(()(()()))()', '(()(())(()))', '(()(())()())', '(()(())())()',
                                                     '(()(()))(())', '(()(()))()()', '(()()((())))', '(()()(()()))',
                                                     '(()()(())())', '(()()(()))()', '(()()()(()))', '(()()()()())',
                                                     '(()()()())()', '(()()())(())', '(()()())()()', '(()())((()))',
                                                     '(()())(()())', '(()())(())()', '(()())()(())', '(()())()()()',
                                                     '(())(((())))', '(())((()()))', '(())((())())', '(())((()))()',
                                                     '(())(()(()))', '(())(()()())', '(())(()())()', '(())(())(())',
                                                     '(())(())()()', '(())()((()))', '(())()(()())', '(())()(())()',
                                                     '(())()()(())', '(())()()()()', '()((((()))))', '()(((()())))',
                                                     '()(((())()))', '()(((()))())', '()(((())))()', '()((()(())))',
                                                     '()((()()()))', '()((()())())', '()((()()))()', '()((())(()))',
                                                     '()((())()())', '()((())())()', '()((()))(())', '()((()))()()',
                                                     '()(()((())))', '()(()(()()))', '()(()(())())', '()(()(()))()',
                                                     '()(()()(()))', '()(()()()())', '()(()()())()', '()(()())(())',
                                                     '()(()())()()', '()(())((()))', '()(())(()())', '()(())(())()',
                                                     '()(())()(())', '()(())()()()', '()()(((())))', '()()((()()))',
                                                     '()()((())())', '()()((()))()', '()()(()(()))', '()()(()()())',
                                                     '()()(()())()', '()()(())(())', '()()(())()()', '()()()((()))',
                                                     '()()()(()())', '()()()(())()', '()()()()(())', '()()()()()()']))

