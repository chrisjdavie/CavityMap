'''
Solving the Cavity Map problem from hackerrank

https://www.hackerrank.com/challenges/cavity-map

---------------

Problem Statement

You are given a square map of size nxn. Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).

You need to find all the cavities on the map and depict them with the uppercase character X.

Input Format

The first line contains an integer, n, denoting the size of the map. Each of the following n lines contains n positive digits without spaces. Each digit (1-9) denotes the depth of the appropriate area.

Constraints 
1<=n<=100
Output Format

Output n lines, denoting the resulting map. Each cavity should be replaced with character X.

---------------

Created on 30 Dec 2015

@author: chris
'''
import copy

# Load in the grid

grid = []
N = input()
for _ in range(N):
    grid.append(map(int,list(raw_input().strip())))


# Find the coords for cavities

coordsToX = []
for i, gridRow in enumerate(grid[1:-1]):
    for j, x in enumerate(gridRow[1:-1]):
        I = i + 1
        J = j + 1
        cavity = True
        for iOff in range(-1,2,2):
            if x <= grid[I+iOff][J]:
                cavity = False            
        for jOff in range(-1,2,2):
            if x <= grid[I][J+jOff]:
                cavity = False
                    
        if cavity:
            coordsToX.append([I,J])


# Replace the coords with X

gridOutput = copy.copy(grid)
for coords in coordsToX:
    gridOutput[coords[0]][coords[1]] = 'X'


# Output in required format

for row in gridOutput:
    rowOp = map(str,row)
    print ''.join(rowOp)


        