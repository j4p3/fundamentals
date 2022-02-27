class Solution:
    # 32. Longest Valid Parentheses
    # https://leetcode.com/problems/longest-valid-parentheses/
    # Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    # Example 1:
    # Input: s = "(()"
    # Output: 2
    # Explanation: The longest valid parentheses substring is "()".

    # Example 2:
    # Input: s = ")()())"
    # Output: 4
    # Explanation: The longest valid parentheses substring is "()()".

    # Example 3:
    # Input: s = ""
    # Output: 0

    # ((()()()()((
    # ())))(((()

    ##
    # Solution:
    # Model streaks with a stack of streak lengths. Not DP.
    # When a paren is opened, push current streak length into stack.
    # When a paren is closed, check stack for the most recently pushed streak length and save it
    # When an invalid close is performed, set streak to 0. There is no invalid open.
    def longest_valid_parentheses(self, s: str) -> int:
        longest = 0
        stack = []
        current = 0

        for i, c in enumerate(s):
            print(f"{i}: {c}")
            if c == "(":
                stack.append(current)
                current = 0
            else:
                if stack:
                    current += stack.pop() + 2
                    longest = max(longest, current)
                else:
                    current = 0


        return longest
