from node import Board
from time import clock
from Algorithms import dfs
from Algorithms import bfs
from Algorithms import aStar

if __name__ == "__main__":
    state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]])

    userinput = input("[1]dfs    [2]bfs  [3]A*(Manhattan Distance)  [4]A*(Euclidean Distance) :-->")

    try:
        val = int(userinput)
        print("....\n")
    except ValueError:
        print("try again")

    if userinput == '1':
        before = clock()
        x = dfs(state)
        after = clock()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
    elif userinput == '2':
        before = clock()
        x = bfs(state)
        after = clock()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
    elif userinput == '3':
        before = clock()
        state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]], algo='a* manhattan')
        x = aStar(state)
        after = clock()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
    elif userinput == '4':
        before = clock()
        state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]], algo='a* eculidean')
        x = aStar(state)
        after = clock()
        print('process', x[0])
        print('tree depth', x[2])
        print('time took ', after - before, ' seconds')
