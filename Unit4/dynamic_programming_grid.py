# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

visited = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]

def compute_value_recurse(value, node_y, node_x, node_value):
    next_value = node_value + cost_step
    neighbors = []
    for (y,x) in delta:
        new_x = node_x + x
        new_y = node_y + y
        neighbor = (new_y, new_x)
        if new_x >= 0 and new_y >= 0 and (new_x) < len(grid[0]) and (new_y) < len(grid) and grid[new_y][new_x] == 0 and value[new_y][new_x] > next_value:
            neighbors.append(neighbor)
    if (len(neighbors) == 0): return

    for n in neighbors:
        if value[n[0]][n[1]] > next_value:
            value[n[0]][n[1]] = next_value
    map(lambda neighbor: compute_value_recurse(value, neighbor[0], neighbor[1], next_value), neighbors)

def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    value2 = compute_value_recurse(value, goal[0], goal[1], 0)

    return value #make sure your function returns a grid of values as demonstrated in the previous video.

value = compute_value()
for row in value:
    print row




