from node import Board
from Algorithms import dfs
from Algorithms import bfs
from Algorithms import aStar
import time

if __name__ == "__main__":
    state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]])

    userinput = input("[1]dfs    [2]bfs  [3]A*(Manhattan Distance)  [4]A*(Euclidean Distance) :-->")

    if userinput == '1':
        before = time.time()
        x = dfs(state)
        after = time.time()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
    elif userinput == '2':
        before = time.time()
        x = bfs(state)
        after = time.time()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
    elif userinput == '3':
        before = time.time()
        state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]], algo='a* manhattan')
        x = aStar(state)
        after = time.time()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
    elif userinput == '4':
        before = time.time()
        state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]], algo='a* eculidean')
        x = aStar(state)
        after = time.time()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
