#TASK01

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




# TASK02

input = open('F:\Spring 2022\CSE 422\Lab\Assignment01\input1.txt')
lines = input.readlines()

a = int(lines[0])
b = int(lines[1])
grid = []

for i in range(2, a + 2):
    str = lines[i].strip()
    grid.append(str.split(' '))

ac = []
alive = 0
for i in range(a):
    for j in range(b):
        if grid[i][j] == 'A':
            ac.append((i, j))
        elif grid[i][j] == 'H':
            alive += 1

time = -1
ab = len(ac)

while not len(ac) == 0:
    # print(ac)
    if ac[0][0] > 0 and grid[ac[0][0] - 1][ac[0][1]] == 'H':
        ac.append((ac[0][0] - 1, ac[0][1]))
        grid[ac[0][0] - 1][ac[0][1]] = 'A'
        alive -= 1

    if ac[0][0] < a - 1 and grid[ac[0][0] + 1][ac[0][1]] == 'H':
        ac.append((ac[0][0] + 1, ac[0][1]))
        grid[ac[0][0] + 1][ac[0][1]] = 'A'
        alive -= 1

    if ac[0][1] < b - 1 and grid[ac[0][0]][ac[0][1] + 1] == 'H':
        ac.append((ac[0][0], ac[0][1] + 1))
        grid[ac[0][0]][ac[0][1] + 1] = 'A'
        alive -= 1

    if ac[0][1] > 0 and grid[ac[0][0]][ac[0][1] - 1] == 'H':
        ac.append((ac[0][0], ac[0][1] - 1))
        grid[ac[0][0]][ac[0][1] - 1] = 'A'
        alive -= 1

    ab -= 1
    ac.remove(ac[0])
    if ab == 0:
        time += 1
        ab = len(ac)

print("Time:", time, "minutes")
if alive == 0:
    print("No one survived")
else:
    print(alive, "survived")
# print(grid)
