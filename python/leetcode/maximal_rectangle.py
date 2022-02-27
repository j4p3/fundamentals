class Solution:
    # 85. Maximal Rectangle
    # https://leetcode.com/problems/maximal-rectangle/
    # Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

    # Example 1:
    # Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # Output: 6
    # Explanation: The maximal rectangle is shown in the above picture.

    # Example 2:
    # Input: matrix = [["0"]]
    # Output: 0

    # Example 3:
    # Input: matrix = [["1"]]
    # Output: 1

    # Constraints:
    # rows == matrix.length
    # cols == matrix[i].length
    # 1 <= row, cols <= 200
    # matrix[i][j] is '0' or '1'.

    ##
    def maximal_rectangle(self, matrix: list[list[str]]) -> int:
        # initialize result, dp state
        largest_rect = 0
        widths = [0] * (len(matrix) + 1)

        for x in range(len(matrix[0])):
            # first pass: populate dp state, widths (could do outside too)
            for y in range(len(matrix)):
                if matrix[y][x] == '1':
                    # reuse previous column's width when continuing
                    widths[y] = widths[y] + 1
                else:
                    widths[y] = 0
            
            # initialize inner loop state: boundaries of rectangles
            indeces = [-1]
            for y in range(len(widths)):
                # for each level of step-down:
                while widths[y] < widths[indeces[-1]]:
                    width = widths[indeces.pop()]
                    # diff location of step-down & location of step-up
                    height = y - 1 - indeces[-1]
                    largest_rect = max(largest_rect, width * height)
                indeces.append(y)
        
        return largest_rect






    def max_rect_sol(self, matrix):
        # guard
        if not matrix or not matrix[0]:
            return 0
        
        # initialize width int & height-tracking list of that width (+1?)
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0

        # iterate through raw matrix
        for row in matrix:
            
            # populate integer heights
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0

            stack = [-1]

            # iterate through height list indeces
            for i in range(n + 1):

                # when height decreases (or at end)
                # for every step-down
                while height[i] < height[stack[-1]]:
                    # multiply the height of the step-down
                    h = height[stack.pop()]
                    # by the index at which it started
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                
                # and store current height
                stack.append(i)
        return ans
