from math import sqrt, pow


class Board:
    def ManhattanHeuristic(self):
        h = 0
        for currentX in range(3):
            for currentY in range(3):
                goalX, goalY = map(int, self.getIndex(self.State[currentX][currentY], purpose='heuristics'))
                h = h + abs(currentX - goalX) + abs(currentY - goalY)
        return h

    def EuclideanHeuristic(self):
        h = 0
        for currentX in range(3):
            for currentY in range(3):
                goalX, goalY = map(int, self.getIndex(self.State[currentX][currentY], purpose='heuristics'))
                h = h + sqrt(pow(currentX - goalX, 2) + pow(currentY - goalY, 2))
        return h

    def __init__(self, State=None, parent=None, algo='dfs'):
        self.algo = algo
        self.State = State
        self.id = ''.join(map(str, self.State))
        self.GoalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.goalid = ''.join(map(str, self.GoalState))
        self.parent = parent

        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1
        if algo == 'a* manhattan':
            self.f = self.depth + self.ManhattanHeuristic()
        elif algo == 'a* eculidean':
            self.f = self.depth + self.EuclideanHeuristic()

    def getIndex(self, v, purpose):
        if purpose == 'heuristics':
            for i in range(3):
                for j in range(3):
                    if self.GoalState[i][j] == v:
                        return i, j
        if purpose == 'general':
            for i, x in enumerate(self.State):
                if v in x:
                    return [i, x.index(v)]

    def compare(self):
        if self.id == self.goalid:
            return True
        return False

    def printState(self):
        output = ''
        for row in range(3):
            for NumInRow in range(3):
                output = output + str(self.State[row][NumInRow]) + ' '
            output = output + '\n'
        print(output)

    def copy(self):
        duplicate = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.State[i][j])
            duplicate.append(row)
        return duplicate

    def getNeighbors(self):
        i, j = self.getIndex(0, 'general')
        neighbors = []

        if j + 1 < 3:
            right = self.copy()
            right[i][j], right[i][j + 1] = right[i][j + 1], right[i][j]
            newRight = Board(right, parent=self, algo=self.algo)
            neighbors.append(newRight)

        if j - 1 > -1:
            left = self.copy()
            left[i][j], left[i][j - 1] = left[i][j - 1], left[i][j]
            newLeft = Board(left, parent=self, algo=self.algo)
            neighbors.append(newLeft)
        if i - 1 > -1:
            up = self.copy()
            up[i][j], up[i - 1][j] = up[i - 1][j], up[i][j]
            newUp = Board(up, parent=self, algo=self.algo)
            neighbors.append(newUp)
        if i + 1 < 3:
            down = self.copy()
            down[i][j], down[i + 1][j] = down[i + 1][j], down[i][j]
            newDown = Board(down, parent=self, algo=self.algo)
            neighbors.append(newDown)

        return neighbors

    def getParent(self):
        return self.parent
