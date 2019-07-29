from node import Board
import random
from Algorithms import dfs
from Algorithms import dfs
from Algorithms import bfs
import timeit

if __name__ == "__main__":
    initialSate = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    random.shuffle(initialSate)

    state = Board([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    
    userinput = input ("[1]dfs    [2]bfs  [3]A*(Manhattan Distance)  [4]A*(Euclidean Distance) :-->")
    try:
        val = int(userinput)
        print ("....\n")
    except ValueError:
        print ("try again")
        

    if userinput == '1':
        start = timeit.default_timer()
        x = dfs(state)
        stop = timeit.default_timer()
        print('process',x[0])
        print('Time: ', stop - start)
    else:
        start = timeit.default_timer()
        x =bfs(state)
        stop = timeit.default_timer()
        print('process',x[0])
        print('Time: ', stop - start)
