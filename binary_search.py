from typing import List
from random import randint

def binary_search(nums: List[int], n: int) -> bool:
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_num = nums[mid]

        if n == mid_num:
            return True
        elif n < mid_num:
            hi = mid - 1
        else:
            lo = mid + 1

    return False

number_of_nums = 50
max_number = 100
numbers = [randint(0, max_number) for _ in range(number_of_nums)]
numbers.sort()

how_many_searches = 10
to_search = [randint(0, max_number) for _ in range(how_many_searches)]
for n in to_search:
    print(f"Found {n}:\t{binary_search(numbers, n)}")
