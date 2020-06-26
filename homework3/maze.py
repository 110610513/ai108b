import numpy as np

def printMap(map):
    for i in range(np.shape(map)[0]):
        for j in range(np.shape(map)[1]):
            if map[i][j] == 1:
                print('■ ', end='')
            elif map[i][j] == 0:
                print('  ', end='')
            else:
                print("{} ".format(map[i][j]), end='')
        print()

def dfs(array, start, goal):
    neighbors = np.array([(0, 1), (-1, 1), (-1, 0), (-1, -1),
                          (0, -1), (1, -1), (1, 0), (1, 1)])
    stack = []
    stack.append(start)
    step = 0

    while stack:
        step += 1
        print("\nStep: ", step)
        
        cNode = stack.pop()
        mapStats[cNode[0]][cNode[1]] = 2
        printMap(mapStats)

        if np.array_equal(cNode, goal):
            return

        for i in range(len(neighbors)):
            nNode = cNode + neighbors[i]

            v0 = nmap[nNode[0]][nNode[1]] == 0
            v1 = mapStats[nNode[0]][nNode[1]] == 0
            if v0 and v1:
                stack.append(nNode)
            else:
                pass
   
nmap = np.array([(1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                 (0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                 (1, 1, 1, 1, 1, 1, 1, 0, 1, 1),
                 (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
                 (1, 0, 1, 1, 0, 1, 1, 1, 1, 1),
                 (1, 0, 0, 1, 0, 1, 0, 0, 0, 1),
                 (1, 0, 1, 1, 0, 1, 0, 1, 0, 1),
                 (1, 0, 1, 1, 1, 1, 0, 1, 0, 1),
                 (1, 0, 0, 0, 0, 0, 0, 1, 0, 1),
                 (1, 1, 1, 1, 1, 1, 1, 1, 0, 1)])


mapStats = nmap.copy()

print("Map:")
printMap(nmap)

print("=============START=============")

start = np.array([1, 0])
goal = np.array([9, 8])
dfs(nmap, start, goal)
