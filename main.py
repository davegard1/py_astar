import numpy as np
from typing import Callable
from Node import Node

def hfun(cur: Node, goal: Node):

    x1, y1 = cur.xy
    x2, y2 = goal.xy

    return np.sqrt( (x2 - x1)**2 +  (y2 - y1)**2  )
    # return np.sqrt( (goal.x - cur.x)**2 +  (goal.y - cur.y)**2  )

def printset(set):

    for node in set:
        print('Node location {}'.format(node.xy)) 

def printmap(map):

    for k,v in map.items():
        print('Node location {}, value: {}'.format(k.xy, v)) 

# Function to find minimum f score in the open set
def findminscore(set):

    # Initialize as the first
    index = 0
    cur = set[0]

    for index, node in enumerate(set):
        
        if node.get_score() <= cur.get_score():
            cur = node
            cur_index = index
    
    return cur_index, cur

# Function to get the path from start to goal
def getpath(lastnode):

    # Initialize with last node
    path = [lastnode]

    # Loop until node didn't come from anywhere (start)
    while lastnode.camefrom:

        # Add to path
        path.append(lastnode.camefrom)

        # update last node
        lastnode = lastnode.camefrom

    # Reverse path (so start -> finish)
    reversed(path)

    return path


def Astar(start: Node, goal: Node, h: Callable, grid ):

    # Test
    global visited
    global openSet

    # Initialize open set with the starting node
    start.g = 0
    start.h = h(start, goal)
    openSet = [start]
    
    # Initialize visited map
    visited = {start.xy: start}


    # Main solve loop
    while len(openSet) != 0:

        # Get the lowest fScore value
        # cur = min(fScore, key= openSet[:])
        cur_index, cur = findminscore(openSet)


        # print('Current location ({}, {})'.format(list(cur.xy)))
        # printset(openSet)
        # printmap(fScore)

        # Check if current is goal
        if cur == goal:
            print("Done")
            return 1, getpath(cur)

        # Remove cur from open set
        # openSet.remove(cur)
        openSet.pop(cur_index)
        cur.closed = True
        # closedSet.append(cur)

        # Get neighbors
        neighbors = cur.neighbors(grid)

        # Loop through neighbors
        for neighbor_pos in neighbors:

            # Neighbor is a tuple of positions, need to convert into nodes
            # Check to see if visited

            # If not visited add to visited
            if neighbor_pos not in visited:
                neighbor = visited[neighbor_pos] = Node(neighbor_pos)
            else:
                neighbor = visited[neighbor_pos] 

            if neighbor.closed:
                continue           

            
            # Temporary gscore
            tempg = cur.g + cur.dist(neighbor)

            if tempg < neighbor.g:

                # print('Nieghbor location ({}, {})'.format(neighbor.x, neighbor.y))

                neighbor.camefrom = cur
                neighbor.g = tempg
                neighbor.h = h(neighbor, goal)

                if neighbor not in openSet:
                    openSet.append(neighbor)
        
        
        #add it to the close set, and add currents neighbors


    print("Failed")
    return -1



nrows = 5
ncols = 6
grid = [[(i,j) for j in range(ncols)] for i in range(nrows)]


start = Node(grid[0][0])

goal = Node(grid[4][5])


status, path = Astar(start, goal, hfun, grid )
