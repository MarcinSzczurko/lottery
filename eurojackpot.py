"""Module simulates eurojackpot lottery
"""
import random
from typing import List

# numbers available during eurojackpot lottery
pool_of_numbers_1_to_50 = list(range(1,51))
pool_of_numbers_1_to_12 = list(range(1,13))


def choose_random() -> List[int]:
    """
    Random selection of 7 numbers:
        - from the pool of numbers range from 1 to 50, 5 unique numbers are chosen
        - from the pool of numbers range from 1 to 12, 2 unique numbers are chosen

    Returns
    -------
    List[int]
        List of drawn numbers
    """
    drawn_numbers_1_to_50 = random.sample(pool_of_numbers_1_to_50, k=5)
    drawn_numbers_1_to_12 = random.sample(pool_of_numbers_1_to_12, k=2)

    all_drawn_numbers = drawn_numbers_1_to_50 + drawn_numbers_1_to_12

    return all_drawn_numbers
