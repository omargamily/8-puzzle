from collections import deque


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

def bfs(initialState):
    step = 0
    frontier = deque([initialState])
    explored = []

    while frontier:
        state = frontier.popleft()
        explored.append(state.id)

        step = step + 1
        print(step)
        state.printState()

        if state.compare():
            return True, state

        for neighbor in state.getNeighbors():
            if not (neighbor.id in explored):
                frontier.append(neighbor)
