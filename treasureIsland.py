"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""
from collections import deque

def maxStepsToTreasure(M):
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque()
    visited = set()
    q.append((0,0))
    visited.add((0,0))
    steps = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()
            x = node[0]
            y = node[1]

            if M[x][y]=='X':
                return steps

            for d in dirs:
                newX, newY = x+d[0], y+d[1]
                if newX >= 0 and newX <= len(M)-1 and newY >=0 and newY <=len(M[0])-1:
                    if M[newX][newY]!='D':
                        if (newX,newY) not in visited:
                            q.append((newX,newY))
                            visited.add((newX,newY))
        steps+=1
    return steps



M = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['X', 'D', 'D', 'O']]

steps = maxStepsToTreasure(M)
print(steps)
