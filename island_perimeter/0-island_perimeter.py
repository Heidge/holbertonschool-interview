#!/usr/bin/python3
"""
Method that calculates the perimeter of an island completely surrounded by water
"""


def island_perimeter(grid):
    """
    Method that calculates the perimeter of an island completely surrounded by water
    """
    i, j = 1, 1
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if grid[i-1][j] == 0:
                    perimeter += 1
                if grid[i][j-1] == 0:
                    perimeter += 1
                if grid[i+1][j] == 0:
                    perimeter += 1
                if grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
