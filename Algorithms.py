def dfs(initialState):
    frontier = [initialState]
    explored = []
    while frontier:
        state = frontier.pop()
        explored.append(state)

        if state.compare():
            return True,state

        for neighbor in state.getNeighbors():
            if neighbor not in frontier and neighbor not in explored:
                newState = state.swap(neighbor)
                frontier.append(newState)
        return False