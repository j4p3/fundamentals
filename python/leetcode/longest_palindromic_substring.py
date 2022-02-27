class Solution:
    # 5. Longest Palindromic Substring

    # https://leetcode.com/problems/longest-palindromic-substring/
    # Given a string s, return the longest palindromic substring in s.
    # Example 1:
    # Input: s = "babad"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.
    # Example 2:
    # Input: s = "cbbd"
    # Output: "bb"
    def longest_palindrome(self, input: str) -> str:
        pal_state = [[0] * len(input) for _ in input]
        longest = input[0]

        # Base case: initial state
        for i in range(len(input)):
            pal_state[i][i] = True

        # General case
        for i in range(len(input)):
            for j in range(i):
                if input[j] == input[i]:
                    if i - j == 1 or pal_state[j + 1][i - 1] == True:
                        pal_state[j][i] = True
                        if i + 1 - j > len(longest):
                            longest = input[j : i + 1]

        return longest
