import sys
input = sys.stdin.readline


def check(grid):
    possible = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j] != '_':
                possible[i][j] = []
            else:
                for k in range(9):
                    if grid[i][k] != '_' and int(grid[i][k]) in possible[i][j]:
                        possible[i][j].remove(int(grid[i][k]))
                    if grid[k][j] != '_' and int(grid[k][j]) in possible[i][j]:
                        possible[i][j].remove(int(grid[k][j]))
                for k in range(3):
                    for l in range(3):
                        if grid[i - (i % 3) + k][j - (j % 3) + l] != '_' and int(
                                grid[i - (i % 3) + k][j - (j % 3) + l]) in possible[i][j]:
                            possible[i][j].remove(int(grid[i - (i % 3) + k][j - (j % 3) + l]))
    minlen = 9
    ind = []
    for i in range(9):
        for j in range(9):
            if 0 < len(possible[i][j]) < minlen:
                minlen = len(possible[i][j])
                ind = [i, j]
    grid[ind[0]][ind[1]] = possible[ind[0]][ind[1]][0]
    return grid


grid = [input().split() for _ in range(9)]
while any('_' in grid[i] for i in range(9)):
    grid = check(grid)
print(grid)
