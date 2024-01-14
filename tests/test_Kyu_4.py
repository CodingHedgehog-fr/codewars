from unittest import TestCase
from katas.Kyu_4 import (strip_comments,
                         snail,
                         sum_of_intervals,
                         User,
                         exp_sum,
                         balanced_parens,
                         RomanNumerals,
                         mix)


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

    def test_RomanNumerals(self):

        roman = RomanNumerals()
        self.assertEqual(RomanNumerals.to_roman(1000), 'M')
        self.assertEqual(RomanNumerals.to_roman(4), 'IV')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII')
        self.assertEqual(RomanNumerals.to_roman(1000), 'M')
        self.assertEqual(RomanNumerals.to_roman(786), 'DCCLXXXVI')
        self.assertEqual(RomanNumerals.to_roman(3499), 'MMMCDXCIX')
        self.assertEqual(RomanNumerals.to_roman(678), 'DCLXXVIII')

        self.assertEqual(RomanNumerals.from_roman('XXI'), 21)
        self.assertEqual(RomanNumerals.from_roman('I'), 1)
        self.assertEqual(RomanNumerals.from_roman('IV'), 4)
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008)
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666)

    def test_mix(self):

        self.assertEqual(mix("my&friend&Paul has heavy hats! &", "my friend John has many many friends &"),
                         "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")
        self.assertEqual(mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &",
                             "my frie n d Joh n has ma n y ma n y frie n ds n&"),
                         "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")
        self.assertEqual(mix("Are the kids at home? aaaaa fffff", "Yes they are here! aaaaa fffff"),
                         "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh")
        self.assertEqual(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        self.assertEqual(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"),
                         '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        self.assertEqual(mix("looping is fun but dangerous", "less dangerous than coding"),
                         "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        self.assertEqual(mix(" In many languages", " there's a pair of functions"),
                         "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        self.assertEqual(mix("Lords of the Fallen", "gamekult"),
                         "1:ee/1:ll/1:oo")
        self.assertEqual(mix("codewars", "codewars"), "")
        self.assertEqual(mix("A generation must confront the looming ", "codewarrs"),
                         "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


