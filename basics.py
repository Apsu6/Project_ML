"""This file will contain my trials to understanding basic DSA in python.

A function that finds the minimum value."""


def find_minimum(nums):
    """Return the minimum value in the given iterable of numbers.

    Args:
        nums (iterable): An iterable of comparable numeric values.

    Returns:
        The smallest value in nums, or None if nums is empty.
    """
    if len(nums) == 0:
        return None

    min_val = float("inf")
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


lst = [3, -1, 4, 1, 5, 9, 2, 6, 50]
print(find_minimum(lst))
