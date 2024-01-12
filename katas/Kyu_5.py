from functools import lru_cache
from itertools import product

# ---------------------------------------------------------------------------------------------------------------------
# Description:
#
# Write an algorithm that takes an array and moves all the zeros to the end,
# preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3])
# returns [1, 1, 2, 1, 3, 0, 0]
# ---------------------------------------------------------------------------------------------------------------------


def move_zeros(array: list) -> list:

    return [elt for elt in array if elt] + [0] * array.count(0)

# ---------------------------------------------------------------------------------------------------------------------
# Description:
#
# The Fibonacci sequence is traditionally used to explain tree recursion.
#
# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# This algorithm serves well its educative purpose, but it's tremendously inefficient, not only because of recursion,
# but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2))
# recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).
# This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much.
# You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars
# you will most likely get a code timeout before any answers.
# Refactor the code to use a cache to avoid timeouts or tree recursion limit
# ---------------------------------------------------------------------------------------------------------------------


@lru_cache(None)
def fibonacci(n: int) -> int:

    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------------------------------------------------------------------------------------------------
# Description:
#
# In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was
# believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right
# half. Here are examples of such numbers:
#
# 003111    #             3 = 1 + 1 + 1
# 813372    #     8 + 1 + 3 = 3 + 7 + 2
# 17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number.
# 56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
#
# Such tickets were either eaten after being used or collected for bragging rights.
#
# Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal
# representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty
# strings or strings which don't represent a decimal number.
# ---------------------------------------------------------------------------------------------------------------------

def luck_check(st: str) -> bool:

    if not len(st) or not st.isnumeric():
        raise Exception("This is not a valid input string")

    # in case of odd numbers of caracters -> remove central caracter
    if len(st) % 2 != 0:
        st = st[0:int(len(st)/2)] + st[int(len(st)/2) + 1:]

    mid = len(st) // 2
    # check sum of left part vs sum of right part
    return sum([int(c) for c in st[:mid]]) == sum([int(c) for c in st[mid:]])

# ---------------------------------------------------------------------------------------------------------------------
# Description:
#
# A Man and his Umbrellas
#
# Each morning a man walks to work, and each afternoon he walks back home.
#
# If it is raining in the morning, and he has an umbrella at home, he takes an umbrella for the journey, so he doesn't
# get wet, and stores it at work. Likewise, if it is raining in the afternoon, and he has an umbrella at work, he takes
# an umbrella for the journey home.
#
# Given an array of the weather conditions, your task is to work out the minimum number of umbrellas he needs to start
# with in order that he never gets wet. He can start with some umbrellas at home and some at work, but the output is a
# single integer, the minimum total number.
#
# The input is an array/list of consecutive half-day weather forecasts. So, e.g. the first value is the 1st day's
# morning weather and the second value is the 1st day's afternoon weather. The options are:
#
# Without umbrella:
#     "clear",
#     "sunny",
#     "cloudy",
#     "overcast",
#     "windy".
#
# With umbrella:
#     "rainy",
#     "thunderstorms".
#
# e.g. for three days, 6 values:
# weather = ["rainy", "cloudy", "sunny", "sunny", "cloudy", "thunderstorms"]
#
# N.B. He never takes an umbrella if it is not raining.
# Examples:
#
#     minUmbrellas(["rainy", "clear", "rainy", "cloudy"])
#     should return 2
#
#     Because on the first morning, he needs an umbrella to take, and he leaves it at work. So on the second morning,
#     he needs a second umbrella.
#
#     minUmbrellas(["sunny", "windy", "sunny", "clear"])
#     should return 0
#     Because it doesn't rain at all
#
#     minUmbrellas(["rainy", "rainy", "rainy", "rainy", "thunderstorms", "rainy"])
#     should return 1
#     Because he only needs 1 umbrella which he takes on every journey.
#
# ---------------------------------------------------------------------------------------------------------------------


def min_umbrellas(weather: list[str]) -> int:

    umbrella_home = umbrella_work = 0
    home = True

    for cond in weather:
        if cond in ["rainy", "thunderstorms"]:
            if home:
                umbrella_work += 1
                umbrella_home = max(0, umbrella_home - 1)
            else:
                umbrella_home += 1
                umbrella_work = max(0, umbrella_work - 1)
        home = not home

    return umbrella_home + umbrella_work

# ---------------------------------------------------------------------------------------------------------------------
# Description:
#
# You will receive an uncertain amount of integers in a certain order k1, k2, ..., kn.
#
# You form a new number of n digits in the following way: you take one of the possible digits of the first given number,
# k1, then the same with the given number k2, repeating the same process up to kn, and you concatenate these obtained
# digits(in the order that were taken) obtaining the new number. As you can see, we have many possibilities.
#
# Let's see the process above explained with three given numbers:
#
# k1 = 23, k2 = 17, k3 = 89
# Digits Combinations   Obtained Number
#   ('2', '1', '8')           218    <---- Minimum
#   ('2', '1', '9')           219
#   ('2', '7', '8')           278
#   ('2', '7', '9')           279
#   ('3', '1', '8')           318
#   ('3', '1', '9')           319
#   ('3', '7', '8')           378
#   ('3', '7', '9')           379    <---- Maximum
#              Total Sum =   2388   (8 different values)
#
# We need the function that may work in this way:
# proc_seq(23, 17, 89) == [8, 218, 379, 2388]
#
# See this special case and deduce how the function should handle the cases which have many repetitions.
# proc_seq(22, 22, 22, 22) == [1, 2222] # we have only one obtained number, the minimum, maximum and total sum coincide
#
# The sequence of numbers will have numbers of n digits only. Numbers formed by leading zeroes will be discarded.
# proc_seq(230, 15, 8) == [4, 218, 358, 1152]
#
# You will never receive the number 0 and all the numbers will be in valid format.
# ---------------------------------------------------------------------------------------------------------------------


def proc_seq(*args: tuple[int]) -> list[int]:
    lst_dgts = set(int(''.join(tup)) for tup in product(*(str(elt) for elt in args)) if tup[0] != '0')

    if len(lst_dgts) == 1:
        return [1, list(lst_dgts)[0]]
    else:
        return [len(lst_dgts), min(lst_dgts), max(lst_dgts), sum(lst_dgts)]
