import numpy as np

class Node():
    def __init__(self, state, parent, index):
        self.state = state
        self.parent = parent  # parent node
        self.index = index  # index of the node in the tree

    def moveDown(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[0][0] == 2: # check if empty tile at edge
            return False
        else:
            bottom = self.state[emptyTile[0] + 1, emptyTile[1]]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = bottom
            childNode[emptyTile[0] + 1, emptyTile[1]] = 0
            return childNode, bottom

    def moveUp(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[0][0] == 0: # check if empty tile at edge
            return False
        else:
            up = self.state[emptyTile[0] - 1, emptyTile[1]]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = up
            childNode[emptyTile[0] - 1, emptyTile[1]] = 0
            return childNode, up

    def moveRight(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[1][0] == 2: # check if empty tile at edge
            return False
        else:
            right = self.state[emptyTile[0], emptyTile[1] + 1]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = right
            childNode[emptyTile[0], emptyTile[1] + 1] = 0
            return childNode, right

    def moveLeft(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[1][0] == 0: # check if empty tile at edge
            return False
        else:
            left = self.state[emptyTile[0], emptyTile[1] - 1]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = left
            childNode[emptyTile[0], emptyTile[1] - 1] = 0
            return childNode, left

    def bfs(self, goal):
        open('Nodes.txt', 'w').close() # clearing files
        open('NodesInfo.txt', 'w').close()
        visited = []
        visited = set(visited)
        toBeVisited = []
        toBeVisited.append(self)
        f = open("Nodes.txt", "a+")
        f2 = open("NodesInfo.txt", "a+")
        countMax = 1
        while(len(toBeVisited)!=0):
            count = 0
            visitingNode = toBeVisited.pop(0)
            node = visitingNode.state
            toWrite = str(np.transpose(node).reshape(1, 9)[0])
            f.write(toWrite[1:len(toWrite) - 1] + '\n')
            f2.write(str(visitingNode.index) + ' ' + str(
            0 if visitingNode.parent == None else visitingNode.parent.index) + '\n')
            if(tuple(node.reshape(1, 9)[0]) in visited): # check if node alredy visited
                continue
            else:
                if(np.array_equal(node, goal)): # check if goal found
                    f.close()
                    f2.close()
                    return visitingNode
                # create all possible children
                if(visitingNode.moveUp()):
                    new, up = visitingNode.moveUp()
                    if not (tuple(new.reshape(1, 9)[0]) in visited):
                        count += 1
                        toBeVisited.append(Node(new, visitingNode, countMax+count))
                if(visitingNode.moveDown()):
                    new, down = visitingNode.moveDown()
                    if not (tuple(new.reshape(1, 9)[0]) in visited):
                        count += 1
                        toBeVisited.append(Node(new, visitingNode, countMax + count))
                if(visitingNode.moveRight()):
                    new, right = visitingNode.moveRight()
                    if not (tuple(new.reshape(1, 9)[0]) in visited):
                        count += 1
                        toBeVisited.append(Node(new, visitingNode, countMax + count))
                if(visitingNode.moveLeft()):
                    new, left = visitingNode.moveLeft()
                    if not (tuple(new.reshape(1, 9)[0]) in visited):
                        count += 1
                        toBeVisited.append(Node(new, visitingNode, countMax + count))
                visited.add(tuple(visitingNode.state.reshape(1, 9)[0]))
                countMax = countMax + count
        f.close()
        f2.close()
        return False


def solvabilityCheck(root):
    root = root.reshape(1,9)[0]
    count = 0
    for i in range(8):
        for j in range(i,9):
            if(root[i] != 0 and root[j] != 0 and root[i] > root[j]):
                count += 1
    if(count % 2 == 0):
        return True
    else:
        return False

def generate_path(node, root):
    while (not np.array_equal(node.state, root)):
        f = open("nodePath.txt", "r+")
        content = f.read()
        f.seek(0, 0)
        toWrite = str(np.transpose(node.state).reshape(1, 9)[0])
        f.write(toWrite[1:len(toWrite) - 1] + '\n' + content)
        f.close()
        node = node.parent
    f = open("nodePath.txt", "r+")
    content = f.read()
    f.seek(0, 0)
    toWrite = str(np.transpose(node.state).reshape(1, 9)[0])
    f.write(toWrite[1:len(toWrite) - 1] + '\n' + content)
    f.close()

def main():
    # start node
    root = np.array([[1,0,3],[4,2,5],[7,8,6]])
    # goal node
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    if not solvabilityCheck(root):
        print("Not solvable!")
    else:
        startNode = Node(root, None, 1)
        node = startNode.bfs(goal)
        open('nodePath.txt', 'w').close()
        print("Found path")
        generate_path(node, root)


if __name__ == '__main__':
    main()