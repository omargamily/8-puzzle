class Board:
    def __init__(self, State=None):
        self.State = State
        self.id = ''.join(map(str, self.State))
        GoalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.goalid = ''.join(map(str, GoalState))
        
        if (self.state!=None):
            self.g = State.g+1
        else:
            self.g = 0
    
    def getpath(self):
        state,path =self,[]
        while state:
            path.append(state)
            state = Board.State
        yield from reversed(path)

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

    def getIndex(self, v):
        for i, x in enumerate(self.State):
            if v in x:
                return [i, x.index(v)]

    def copy(self):
        duplicate = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.State[i][j])
            duplicate.append(row)
        return duplicate

    def getNeighbors(self):
        i, j = self.getIndex(0)
        neighbors = []

        if j + 1 < 3:
            right = self.copy()
            right[i][j], right[i][j + 1] = right[i][j + 1], right[i][j]
            neighbors.append(Board(right))
        if j - 1 > -1:
            left = self.copy()
            left[i][j], left[i][j - 1] = left[i][j - 1], left[i][j]
            neighbors.append(Board(left))
        if i - 1 > -1:
            up = self.copy()
            up[i][j], up[i - 1][j] = up[i - 1][j], up[i][j]
            neighbors.append(Board(up))
        if i + 1 < 3:
            down = self.copy()
            down[i][j], down[i + 1][j] = down[i + 1][j], down[i][j]
            neighbors.append(Board(down))

        return neighbors
