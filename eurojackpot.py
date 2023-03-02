"""Module simulates eurojackpot lottery
"""
import random
from typing import List
import inquirer

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


def choose_unique_from_range(numbers_range: List[int], required_selections: int) -> List[int]:
    """
    Multiple selection from given list of choices.
    To make a choose use 'space' and 'enter' keys on your keyboard.
    With 'space' key, choices are selected(unselected).
    With 'enter' key, choices are confirmed.
    After confirmation, returned list must equal to number of required_selections parameter.

    Parameters
    ----------
    numbers_range : List[int]
        List of numbers participating in the lottery
    required_selections : int
        Number of selections to make

    Returns
    -------
    List[int]
        List of chosen numbers
    """
    name = "lottery"

    questions = [
    inquirer.Checkbox(name=name,
                        message=f"Please choose {required_selections} numbers from the range below. For the process use your keyboard. You can select(unselect) values with the space key. Confirm your choices with the enter key.",
                        choices=numbers_range,
                        ),
    ]
    answers = inquirer.prompt(questions)
    selected_choices = answers[name]

    assert len(selected_choices) == required_selections, f"You've selected {selected_choices} options. Please choose {required_selections}"

    return selected_choices
