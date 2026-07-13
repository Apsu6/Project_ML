"""This file will contain my trials to understanding basic DSA in python.


A function that finds the minimum value, O(n) time complexity, where n is
the number of elements in the input iterable. We iterate through all
elements to find the minimum value."""


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
# print(find_minimum(lst))

# Next example will demonstrate O(n^2).


def name_matches(firstn, lastn, fulln):
    """Check if the full name matches any combination of first and last names.

    Args:
        firstn (iterable): An iterable of first names.
        lastn (iterable): An iterable of last names.
        fulln (str): The full name to match.

    Returns:
        True if a combination of first and last names matches fulln, False.
    """
    for name1 in firstn:
        for name2 in lastn:
             if f"{name1} {name2}" == fulln:
                return True
    return False


# print(name_matches(["John", "Olive", "Jane"], ["Doe"],"John Doe"))
# Returns True


# Example that shows O(nm) time complexity


def get_avg_brand_follower(all_handles, brand_names):
    """Return the average number of handles per account that contain brand_names.

    Args:
        all_handles (iterable of iterables): Collection of handle lists per account.
        brand_names (str): Substring to search for in each handle (e.g. 'brand').

    Returns:
        float: Average count of matching handles per account. Returns 0.0 if
        all_handles is empty.
    """
    if not all_handles:
        return 0.0

    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_names in handle:
                count += 1

    avg = count / len(all_handles)
    return avg


all_handles1 = [
    ["@brand1", "@brand2", "@brand3"],
    ["@brand4", "@brand5"],
    ["@brand6", "@brand7", "@brand8", "@brand9"],
     ["@brand10", "@brand11", "@brand12", "@brand13"]]

brand_names1 = "brand"

# print(get_avg_brand_follower(all_handles1, brand_names1))


# Example that shows o(log n) time complexity


def binary_search(arr, target):
    
    lowest = 0
    highest = len(arr) - 1

    while lowest <= highest:
        mid = (lowest + highest) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lowest = mid + 1
        else:
            highest = mid - 1

    return False


binary_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(binary_search(binary_arr, 7))
# Returns 6

