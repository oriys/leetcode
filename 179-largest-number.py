from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(x) for x in nums]
        str_nums.sort(key=cmp_to_key(lambda x,y: int(x + y) - int(y + x)), reverse=True)
        return ''.join(str_nums) if str_nums[0] != '0' else '0'