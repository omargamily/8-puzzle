from node import Board


def dfs(initialState):
    count = 0
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop()
        count += 1
        state.printState()
        print(count)
        explored.append(state)
        if state.compare():
            return True, state

        for neighbor in state.getNeighbors():
            if neighbor not in list(set().union(frontier, explored)):
                frontier.append(Board(neighbor))

    return False, state
