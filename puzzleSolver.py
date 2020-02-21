import numpy as np

class Node():
    def __init__(self, state, parent, index):
        self.state = state
        self.parent = parent  # parent node
        self.index = index  # index of the node in the tree

    def moveDown(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[0][0] == 2:
            return False
        else:
            bottom = self.state[emptyTile[0] + 1, emptyTile[1]]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = bottom
            childNode[emptyTile[0] + 1, emptyTile[1]] = 0
            return childNode, bottom

    def moveUp(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[0][0] == 0:
            return False
        else:
            up = self.state[emptyTile[0] - 1, emptyTile[1]]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = up
            childNode[emptyTile[0] - 1, emptyTile[1]] = 0
            return childNode, up

    def moveRight(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[1][0] == 2:
            return False
        else:
            right = self.state[emptyTile[0], emptyTile[1] + 1]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = right
            childNode[emptyTile[0], emptyTile[1] + 1] = 0
            return childNode, right

    def moveLeft(self):
        emptyTile = np.where(self.state == 0)
        if emptyTile[1][0] == 0:
            return False
        else:
            left = self.state[emptyTile[0], emptyTile[1] - 1]
            childNode = self.state.copy()
            childNode[emptyTile[0], emptyTile[1]] = left
            childNode[emptyTile[0], emptyTile[1] - 1] = 0
            return childNode, left




if __name__ == '__main__':
    main()