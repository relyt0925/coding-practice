"""
You are given a robot that starts at the top-left corner of a grid with dimensions m x n. The robot can only move either down or right at any point in time. The goal is for the robot to reach the bottom-right corner of the grid.

Given the dimensions of the board m and n, write a function to return the number of unique paths the robot can take to reach the bottom-right corner.
"""

class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        # Your code goes here
        dp_array = [[0] * m for _ in range(n)]

        for i in range(m):
            dp_array[0][i] = 1
        for i in range(n):
            dp_array[i][0] = 1

        for rowItr in range(1,n):
            for colItr in range(1,m):
                dp_array[rowItr][colItr] = dp_array[rowItr-1][colItr] + dp_array[rowItr][colItr-1]
        return dp_array[n-1][m-1]
        pass