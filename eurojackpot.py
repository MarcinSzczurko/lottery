"""Module simulates eurojackpot lottery
"""
import random
from typing import List
import inquirer

# numbers available during eurojackpot lottery
pool_of_numbers_1_to_50 = list(range(1,51))
pool_of_numbers_1_to_12 = list(range(1,13))


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


def choose_numbers(randomly: bool = True) -> List[int]:
    """
    Selection of numbers participating in the lottery.

    There are 2 pools of numbers and from each, unique numbers are selected.
    Numbers can duplicate, but not within a single pool.

    Pool 1: numbers from 1 to 50
    Pool 2: numbers from 1 to 12

    Parameters
    ----------
    randomly : bool, optional
        If set to True (default), then numbers are selected by random method.
        If set to False, numbers are selected by the user:
            - multiple selection from the list of given choices.
            - with 'space' key on keyboard, choices are selected(unselected).
            - with 'enter' key on keyboard, choices are confirmed.

    Returns
    -------
    List[int]
        List of chosen numbers
    """
    if randomly:
        chosen_numbers_pool_1 = random.sample(pool_of_numbers_1_to_50, k=5)
        chosen_numbers_pool_2 = random.sample(pool_of_numbers_1_to_12, k=2)
    else:
        chosen_numbers_pool_1 = choose_unique_from_range(pool_of_numbers_1_to_50, 5)
        chosen_numbers_pool_2 = choose_unique_from_range(pool_of_numbers_1_to_12, 2)

    all_chosen_numbers = chosen_numbers_pool_1 + chosen_numbers_pool_2

    return all_chosen_numbers
