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
                return i, x.index(v)

    def getNeighbors(self):
        zero = self.getIndex(0)
        directions = []
        neighbors = []
        if zero[1] + 1 < 3:
            right = (zero[0], zero[1] + 1)
            directions.append(right)
        if zero[1] - 1 > -1:
            left = (zero[0], zero[1] - 1)
            directions.append(left)
        if zero[0] - 1 > -1:
            up = (zero[0] - 1, zero[1])
            directions.append(up)
        if zero[0] + 1 < 3:
            down = (zero[0] + 1, zero[1])
            directions.append(down)

        for i in directions:
            if self.State[i[0]][i[1]]:
                neighbors.append(self.State[i[0]][i[1]])
        return neighbors

    def swap(self, num):
        zero = self.getIndex(0)
        number = self.getIndex(num)
        l = self.State

        temp = l[zero[0]][zero[1]]
        l[zero[0]][zero[1]] = l[number[0]][number[1]]
        l[number[0]][number[1]] = temp

        return l
