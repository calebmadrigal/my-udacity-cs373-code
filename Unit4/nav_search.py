# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def is_unexplored_node(node, grid):
    """ This assumes node is valid in grid. """
    return grid[node[0]][node[1]] == 0

def is_valid_node(node, grid):
    #print "node[0] = %d, node[1] = %d" % (node[0], node[1])
    return (node[0] >= 0 and node[1] >= 0 and node[0] < len(grid) and node[1] < len(grid[0]))

def get_neighbor_nodes(node, grid):
    neighbors = []
    for (move_y, move_x) in delta:
        possible_neighbor = [node[1] + move_y, node[2] + move_x]
        if is_valid_node(possible_neighbor, grid):
            neighbors.append(possible_neighbor)
    return neighbors

def get_unexplored_neighbors(node, grid):
    result = map(lambda new_node: [node[0]+1] + new_node, filter(lambda node: is_unexplored_node(node, grid), get_neighbor_nodes(node, grid)))
    return result

def mark_frontier(nodes, grid):
    for node in nodes:
        grid[node[1]][node[2]] = 2

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------    
    initial_node = [0, init[0], init[1]]
    unexpanded_nodes = [initial_node]
    
    while len(unexpanded_nodes) > 0:
        (node, unexpanded_nodes) = (unexpanded_nodes[0], unexpanded_nodes[1:])
        grid[node[1]][node[2]] = 2
        
        if node[1:] == goal:
            return node
        else:
            unexplored_neighbors = get_unexplored_neighbors(node, grid)
            mark_frontier(unexplored_neighbors, grid)
            unexpanded_nodes = unexpanded_nodes + unexplored_neighbors
            unexpanded_nodes.sort()
            if len(unexpanded_nodes) == 0:
                return "fail"

if __name__ == "__main__":
    print search()
