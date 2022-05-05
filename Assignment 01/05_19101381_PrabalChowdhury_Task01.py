import numpy as np
infected = 0
input = open('F:\Spring 2022\CSE 422\Lab\Assignment01\input.txt')
lines = input.readlines()
grid = []
for i in lines:
    i = i.strip()
    str = i.split(' ')
    grid.append(str)


def dfs(i, j):
    global ab
    ab += 1
    visited[i][j] = True
    if i > 0 and grid[i - 1][j] == 'Y' and not (visited[i - 1][j]):
        dfs(i - 1, j)
    if i < a - 1 and grid[i + 1][j] == 'Y' and not (visited[i + 1][j]):
        dfs(i + 1, j)
    if j < b - 1 and grid[i][j + 1] == 'Y' and not (visited[i][j + 1]):
        dfs(i, j + 1)
    if j > 0 and grid[i][j - 1] == 'Y' and not (visited[i][j - 1]):
        dfs(i, j - 1)
    if i > 0 and j > 0 and grid[i - 1][j - 1] == 'Y' and not (visited[i - 1][j - 1]):
        dfs(i - 1, j - 1)
    if i < a - 1 and j < b - 1 and grid[i + 1][j + 1] == 'Y' and not (visited[i + 1][j + 1]):
        dfs(i + 1, j + 1)
    if i > 0 and j < b - 1 and grid[i - 1][j + 1] == 'Y' and not (visited[i - 1][j + 1]):
        dfs(i - 1, j + 1)
    if i < a - 1 and j > 0 and grid[i + 1][j - 1] == 'Y' and not (visited[i + 1][j - 1]):
        dfs(i + 1, j - 1)


a = len(grid)
b = len(grid[0])
ab = 0
visited = np.zeros((a, b))
visited = visited > 0

for i in range(a):
    for j in range(b):
        if grid[i][j] == 'Y' and not (visited[i][j]):
            ab = 0
            dfs(i, j)
            infected = max(infected, ab)



print(infected)
