from node import Board


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
