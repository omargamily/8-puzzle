from node import Board
import random
from Algorithms import dfs

if __name__ == "__main__":
    initialSate = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    random.shuffle(initialSate)

    state = Board(initialSate)

    print(state.GoalState)
    x = dfs(state)
    print('process',x[0])
    print('state',x[1].printState())
