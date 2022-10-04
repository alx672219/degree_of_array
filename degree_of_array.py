from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        leftmost, rightmost, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in leftmost: 
                leftmost[x] = i
            rightmost[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, rightmost[x] - leftmost[x] + 1)

        return ans