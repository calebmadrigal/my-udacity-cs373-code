colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = []

def matrix_sum_func(func, matrix):
    if type(matrix) != list: return func(matrix)
    else: return sum(map(lambda x: matrix_sum_func(func,x), matrix))

def matrix_sum(matrix):
    return matrix_sum_func(lambda x: x, matrix)

def matrix_num_items(matrix):
    return matrix_sum_func(lambda x: 1, matrix)

def sense(belief_map, world, measurement):
    bm_update = []
    for row in range(len(world)):
        new_row = []
        for column in range(len(world[row])):
            hit = (world[row][column] == measurement)
            new_row.append(belief_map[row][column] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
        bm_update.append(new_row)

    # Normalize
    total = matrix_sum(bm_update)
    bm_update = [[c / total for c in r] for r in bm_update]

    return bm_update

def move(belief_map, world, move):
    bm_update = []
    for row in range(len(world)):
        new_row = []
        for column in range(len(world[row])):
            p = p_move * belief_map[ (row - move[0]) % len(belief_map) ][ (column - move[1]) % len(belief_map[row]) ]
            p += (1-p_move) * belief_map[row][column]
            new_row.append(p)
        bm_update.append(new_row)

    return bm_update

def localize(world, motions, measurements):
    num_places = matrix_num_items(world)
    belief_map = [[1./num_places for c in r] for r in world]

    for i in range(len(motions)):
        belief_map = move(belief_map, world, motions[i])
        belief_map = sense(belief_map, world, measurements[i])

    return belief_map        

p = localize(colors, motions, measurements)

#Your probability array must be printed 
#with the following code.

show(p)
