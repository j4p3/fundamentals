class Solution:
    # 213. House Robber II
    # https://leetcode.com/problems/house-robber-ii/

    # You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
    # Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
  
    # Example 1:
    # Input: nums = [2,3,2]
    # Output: 3
    # Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    # Example 2:
    # Input: nums = [1,2,3,1]
    # Output: 4
    # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    # Total amount you can rob = 1 + 3 = 4.

    # Example 3:
    # Input: nums = [1,2,3]
    # Output: 3

    # Constraints:
    # 1 <= nums.length <= 100
    # 0 <= nums[i] <= 1000

    # Ideas:
    # * two lists? taking n[-1], vs not?
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        # 0: hit last, not first
        # 1: hit first, not last
        maximums = ((0, nums[0]),
                    (nums[1], nums[1]),
                    (nums[2], nums[2] + nums[0]))

        for i in nums[3:-1]:
            ((m3a, m3b),
             (m2a, m2b),
             (m1a, m1b)) = maximums

            maximums = ((m2a, m2b),
                        (m1a, m1b),
                        (i + max(m3a, m2a), i + max(m3b, m2b)))
        
        # last house: do not increment state which hit first house
        ((m3a, m3b),
         (m2a, m2b),
         (m1a, m1b)) = maximums

        maximums = ((m2a, m2b),
                    (m1a, m1b),
                    (nums[-1] + max(m3a, m2a), max(m3b, m2b)))
        
        maximums = [i for pair in maximums for i in pair]
        return max(maximums)
