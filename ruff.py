from typing import Iterable

import os
<<<<<<< HEAD

=======
>>>>>>> 39d713e (restore python codes)

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )
