from node import Board
def dfs(initialState):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop()
        explored.append(state)
        if state.compare():
            return True, state

        for neighbor in state.getNeighbors():
            if neighbor not in list(set().union(frontier,explored)):
                newState = Board(state.swap(neighbor))
                frontier.append(newState)


    return False,state
