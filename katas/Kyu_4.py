from functools import lru_cache
from itertools import groupby
import re


# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.
#
# Example:
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
#
# The output expected would be:
#
# apples, pears
# grapes
# bananas
#
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
# ----------------------------------------------------------------------------------------------------------------------


def strip_comments(strng: str, markers: list[str]) -> str:

    # backslash is chr(92), used to avoid using '\\' in f-string
    marks = f"[{'|'.join([chr(92) + mark for mark in markers])}]"
    return ''.join([re.sub(f'\\s*{marks}.*', '', line, 1) for line in strng.splitlines(True)]) \
        if len(markers) else strng

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Snail Sort
#
# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
# ----------------------------------------------------------------------------------------------------------------------


def snail(arr: list) -> list[int]:
    final_lst = []
    while len(arr):
        final_lst += arr.pop(0)
        arr = list(zip(*arr))[::-1]  # Rotate matrix
    return final_lst

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all
# the interval lengths. Overlapping intervals should only be counted once.
#
# Intervals:
# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always
# be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
#
# Overlapping Intervals
# List containing overlapping intervals:
#
# [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ]
#
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5],
# which has a length of 4.
#
# Examples:
#
# sumIntervals( [
#    [1, 2],
#    [6, 10],
#    [11, 15]
# ] ) => 9
#
# sumIntervals( [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ] ) => 7
#
# sumIntervals( [
#    [1, 5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ] ) => 19
#
# sumIntervals( [
#    [0, 20],
#    [-100000000, 10],
#    [30, 40]
# ] ) => 100000030
#
# Tests with large intervals
# Your algorithm should be able to handle large intervals. All tested intervals are subsets of
# the range [-1000000000, 1000000000].
# ----------------------------------------------------------------------------------------------------------------------


def sum_of_intervals(intervals: list) -> int:

    inter = sorted(intervals)
    i = 0
    while i < len(inter) - 1:
        if inter[i][0] <= inter[i + 1][0] <= inter[i][1]:
            if not (inter[i][0] <= inter[i + 1][1] <= inter[i][1]):
                inter[i] = [inter[i][0], inter[i + 1][1]]
            inter.pop(i + 1)
        else:
            i += 1

    return sum([elt[1] - elt[0] for elt in inter])

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Write a class called User that is used to calculate the amount that a user will progress through a ranking system
# similar to the one Codewars uses.
#
# Business Rules:
#     A user starts at rank -8 and can progress all the way to 8.
#     There is no 0 (zero) rank. The next rank after -1 is 1.
#     Users will complete activities. These activities also have ranks.
#     Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
#     The progress earned from the completed activity is relative to what the user's current rank is compared to the
#     rank of the activity
#     A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded
#     to the next level
#     Any remaining progress earned while in the previous rank will be applied towards the next rank's progress
#     (we don't throw any progress away). The exception is if there is no other rank left to progress towards
#     (Once you reach rank 8 there is no more progression).
#     A user cannot progress beyond rank 8.
#     The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8.
#     Any other value should raise an error.
#
# The progress is scored like so:
#     Completing an activity that is ranked the same as that of the user's will be worth 3 points
#     Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
#     Any activities completed that are ranking 2 levels or lower than the user's ranking will be ignored
#     Completing an activity ranked higher than the current user's rank will accelerate the rank progression.
#     The greater the difference between rankings the more the progression will be increased.
#     The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.
#
# Logic Examples:
#
#     If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
#     If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
#     If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
#     If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user
#     being upgraded to rank -7 and having earned 60 progress towards their next rank
#     If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
#
# Code Usage Examples:
#
# user = User()
# user.rank # => -8
# user.progress # => 0
# user.inc_progress(-7)
# user.progress # => 10
# user.inc_progress(-5) # will add 90 progress
# user.progress # => 0 # progress is now zero
# user.rank # => -7 # rank was upgraded to -7
#
# Note: Codewars no longer uses this algorithm for its own ranking system. It uses a pure Math based solution
# that gives consistent results no matter what order a set of ranked activities are completed at.
# ----------------------------------------------------------------------------------------------------------------------


class User:

    NEXT_LEVEL = 100

    def __init__(self):
        self._ranks = [i for i in range(-8, 9) if i]
        self._rank_order = 0
        self._curr_rank = self._ranks[self._rank_order]
        self._progress = 0

    @property
    def rank(self) -> int:
        return self._curr_rank

    @property
    def progress(self) -> int:
        return self._progress

    def inc_progress(self, activity_rnk: int) -> None:

        if activity_rnk not in self._ranks:
            raise Exception("argument is not a valid activity ranking")

        if self.rank == max(self._ranks):
            return

        diff_rnk = self._ranks.index(activity_rnk) - self._ranks.index(self._curr_rank)

        if diff_rnk <= -2:
            return
        elif diff_rnk == -1:
            progress = 1
        elif diff_rnk == 0:
            progress = 3
        else:
            progress = 10 * diff_rnk ** 2

        self._inc_ranking(progress)

    def _inc_ranking(self, progress: int) -> None:

        self._progress += progress

        while self._progress >= self.NEXT_LEVEL:
            if self.rank < max(self._ranks):
                self._progress -= self.NEXT_LEVEL
                self._rank_order += 1
                self._curr_rank = self._ranks[self._rank_order]
            if self.rank == max(self._ranks):
                self._progress = 0

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# How many ways can you make the sum of a number?
#
# From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)
#
#     In number theory and combinatorics, a partition of a positive integer n, also called an integer partition,
#     is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands
#     are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be
#     partitioned in five distinct ways:
#
# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1
#
# Examples
# Basic
#
# exp_sum(1) # 1
# exp_sum(2) # 2  -> 1+1 , 2
# exp_sum(3) # 3 -> 1+1+1, 1+2, 3
# exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
# exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
#
# exp_sum(10) # 42
#
# Explosive
#
# exp_sum(50) # 204226
# exp_sum(80) # 15796476
# exp_sum(100) # 190569292
# ----------------------------------------------------------------------------------------------------------------------


@lru_cache(None)
def exp_sum(n: int) -> int:

    # Implementation of MacMahon's recurrence relation : https://mathworld.wolfram.com/PartitionFunctionP.html
    # see formula https://math.stackexchange.com/questions/1192906/1-2-3-5-7-11-15-22-30-42-56-77-101-135-176-231
    # -partition-numbers-what-is
    if n < 0:
        return 0
    elif n in [0, 1]:
        return 1

    func_args = list(filter(lambda p: p >= 0, [n - sum(range(k, k - int(k / 2 + 0.5), -1)) for k in range(1, n + 1)]))
    return sum([result * (-1) ** int(k/2) for k, result in enumerate(list(map(exp_sum, func_args)))])

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Write a function which makes a list of strings representing all the ways you can balance n pairs of parentheses
# Examples
#
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
# ----------------------------------------------------------------------------------------------------------------------


def balanced_parens(n: int) -> list[str]:

    cpt = 0
    balanced_par = None
    while cpt <= n:
        balanced_par = build_list_of_parens(balanced_par, cpt)
        cpt += 1

    return balanced_par


def build_list_of_parens(lst_par: None, n) -> list[str]:

    if n == 0:
        return ['']
    if n == 1:
        return ['()']

    res = []
    for elt in lst_par:
        res += [''.join([elt[:i], '()', elt[i:]]) for i in range(len(elt))]

    return sorted(list(set(res)))

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values
# will be tested for each function.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
# any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
# Examples
#
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
# 1000 -> "M"
#  400 -> "CD"
#   90 -> "XC"
#   40 -> "XL"
#    1 -> "I"
#
# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CD"      -> 400
# "XC"      -> 90
# "XL"      -> 40
# "I"       -> 1
# ----------------------------------------------------------------------------------------------------------------------


class RomanNumerals:
    r_to_d = {'': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    d_to_r = {val: key for key, val in r_to_d.items()}

    @staticmethod
    def to_roman(decimal_nb: int) -> str:

        power = len(str(decimal_nb)) - 1
        roman_nb = ''
        for dec_dgt in [int(dec_dgt) for dec_dgt in str(decimal_nb)]:
            if dec_dgt in [5, 6, 7, 8]:
                roman_nb += RomanNumerals.d_to_r[5 * 10 ** power] + RomanNumerals.d_to_r[10 ** power] * (dec_dgt - 5)
            elif dec_dgt in [4, 9]:
                roman_nb += RomanNumerals.d_to_r[10 ** power] + RomanNumerals.d_to_r[(dec_dgt + 1) * 10 ** power]
            else:
                roman_nb += RomanNumerals.d_to_r[10 ** power] * dec_dgt
            power -= 1

        return roman_nb

    @staticmethod
    def from_roman(roman_nb: str) -> int:
        decimal_nb = 0
        prev_rom_dgt = ''
        for rom_dgt in reversed(roman_nb):
            if rom_dgt == 'X' and prev_rom_dgt in ['C', 'L']:
                decimal_nb -= RomanNumerals.r_to_d[rom_dgt]
            elif rom_dgt == 'I' and prev_rom_dgt in ['V', 'X']:
                decimal_nb -= RomanNumerals.r_to_d[rom_dgt]
            elif rom_dgt == 'C' and prev_rom_dgt in ['D', 'M']:
                decimal_nb -= RomanNumerals.r_to_d[rom_dgt]
            else:
                decimal_nb += RomanNumerals.r_to_d[rom_dgt]
            prev_rom_dgt = rom_dgt

        return decimal_nb

# ----------------------------------------------------------------------------------------------------------------------
# Description:
#
# Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account
# the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.
#
# s1 = "A aaaa bb c"
# s2 = "& aaa bbb c d"
#
# s1 has 4 'a', 2 'b', 1 'c'
# s2 has 3 'a', 3 'b', 1 'c', 1 'd'
#
# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
# consider letters when the maximum of their occurrences is less than or equal to 1.
#
# We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
# string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because
# the maximum for b is 3.
#
# The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum
# if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they
# appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.
#
# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
# order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits -
# more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".
#
# Hopefully other examples can make this clearer.
#
# s1 = "my&friend&Paul has heavy hats! &"
# s2 = "my friend John has many many friends &"
# mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
#
# s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
# s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
# mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
#
# s1="Are the kids at home? aaaaa fffff"
# s2="Yes they are here! aaaaa fffff"
# mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
# ----------------------------------------------------------------------------------------------------------------------


def mix(s1: str, s2: str) -> str:
    # k -> key ('a', 'b', ...)
    # v -> value (number of occurrences per key)
    # g -> group
    # substring means '1:aaa', '2:eeee', '=rr', ...

    s1 = ''.join(sorted([c for c in s1 if c.isalpha() and c.islower()]))
    s2 = ''.join(sorted([c for c in s2 if c.isalpha() and c.islower()]))

    # build a list of tuples (k, substring, v), sorted by k, filter occurrences > 1 only
    lst_grp = sorted(([(k, f"1:{k*v}", v) for k, v in {k: len(list(g)) for k, g in groupby(s1)}.items() if v > 1] +
                      [(k, f"2:{k*v}", v) for k, v in {k: len(list(g)) for k, g in groupby(s2)}.items() if v > 1]))

    # build a filtered list of tuples (substrings, v): keep max occurrences for each letter, substitute '1' or '2'
    # with '=' in case of equality between s1 and s2
    lst_max = []
    for lst in [list(g) for _, g in groupby(lst_grp, lambda x: x[0])]:
        lst_max.append(('=' + lst[0][1][1:], lst[0][2]) if (len(lst) > 1 and lst[0][2] == lst[1][2])
                       else max([elt for elt in lst], key=lambda x: x[2])[1:])

    # build final list of substrings only: sort by decreasing order of occurrences, in case of equality of occurrences
    # sort then by ascending lexicographic order
    lst_sorted = []
    for _, g in groupby(sorted(lst_max, key=lambda x: x[1], reverse=True), lambda x: x[1]):
        lst_sorted += [x[0] for x in sorted(list(g), key=lambda x: x[0])]

    return '/'.join(lst_sorted)
