class Solution:
    # 322. Coin Change
    # https://leetcode.com/problems/coin-change/

    # You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    # Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    # You may assume that you have an infinite number of each kind of coin.

    # Example 1:
    # Input: coins = [1,2,5], amount = 11
    # Output: 3
    # Explanation: 11 = 5 + 5 + 1

    # Example 2:
    # Input: coins = [2], amount = 3
    # Output: -1

    # Example 3:
    # Input: coins = [1], amount = 0
    # Output: 0

    # Constraints:

    # 1 <= coins.length <= 12
    # 1 <= coins[i] <= 2^31 - 1
    # 0 <= amount <= 104

    ##
    # Solution:
    # 1-dimensional DP with least-coins-to-i as state.
    def coin_change(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if min(coins) > amount:
            return -1

        least = [0] + [float("inf")] * (amount)

        for c in coins:
            if c <= amount:
                least[c] = 1

        print(least)

        for i in range(amount + 1):
            for c in coins:
                if i - c > 0 and least[i - c] + 1 < least[i]:
                    least[i] = least[i - c] + 1

        if least[amount] == float("inf"):
            return -1
        else:
            return least[amount]
