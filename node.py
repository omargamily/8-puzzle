class Board:
    def __init__(self, State=None):
        self.State = State
        self.GoalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def compare(self):
        if self.State == self.GoalState:
            return True
        return False

    def printState(self):
        output = ''
        for row in range(3):
            for NumInRow in range(3):
                output = output + str(self.State[row][NumInRow]) + ' '
            output = output + '\n'
        print(output)

    def getIndex(self, v):
        for i, x in enumerate(self.State):
            if v in x:
                return [i, x.index(v)]

    def getNeighbors(self):
        i, j = self.getIndex(0)
        neighbors = []

        if j + 1 < 3:
            right = self.State[:]
            right[i][j], right[i][j + 1] = right[i][j + 1], right[i][j]
            neighbors.append(right)
        if j - 1 > -1:
            left = self.State[:]
            left[i][j], left[i][j - 1] = left[i][j - 1], left[i][j]
            neighbors.append(left)
        if i - 1 > -1:
            up = self.State[:]
            up[i][j], up[i - 1][j] = up[i - 1][j], up[i][j]
            neighbors.append(up)
        if i + 1 < 3:
            down = self.State[:]
            down[i][j], down[i + 1][j] = down[i + 1][j], down[i][j]
            neighbors.append(down)

        return neighbors
