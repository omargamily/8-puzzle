from node import Board
rom collections import deque

def dfs(initialState):
    count = 0
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop()
        explored.append(state.id)

        count += 1
        print(count)
        state.printState()

        if state.compare():
            return True, state

        for neighbor in state.getNeighbors():
            if not neighbor.id in explored:
                frontier.append(neighbor)

    return False, state


def bfs (initialState):
    step = 0
    d = 0
    frontier = deque([initialState])
    explored = set()
    explored.add(initialState.id)
    
    while frontier:
        state = frontier.popleft()
        
        step= step+1
        print(step)
        state.printState()
        
        
        if state.compare():
            return True,[state.getpath(),d]
        
        for neighbor in state.getNeighbors():
            if not(neighbor.id  in explored):
                frontier.append(neighbor)
                explored.add(neighbor.id)
                if neighbor.g > d:
                    d = neighbor.g
