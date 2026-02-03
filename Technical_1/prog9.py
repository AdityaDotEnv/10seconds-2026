def fun(i, j):
    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0"):
        return False
    if grid[i][j]=="e":
        return True
    grid[i][j] = "0"
    return fun(i + 1, j) or fun(i - 1, j) or  fun(i, j + 1) or fun(i, j - 1) 


grid = [
    ["s", "1", "1", "0"],
    ["1", "0", "1", "0"],
    ["1", "0", "1", "0"],
    ["0", "0", "1", "e"]
]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "s":
            if fun(i, j) ==True:
                print("True")
                exit