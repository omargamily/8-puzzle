from collections import deque


def dfs(initialState):
    count = 0
    currentDepth = 0
    frontier = [initialState]
    explored = []

    while frontier:
        state = frontier.pop()
        explored.append(state.id)

        count += 1
        print(count)
        state.printState()

        if state.compare():
            state.getMoves()
            return True, state, currentDepth

        for neighbor in state.getNeighbors():
            if not neighbor.id in explored:
                frontier.append(neighbor)
                if neighbor.depth > currentDepth:
                    currentDepth = neighbor.depth

    return False, state


def bfs(initialState):
    step = 0
    frontier = deque([initialState])
    explored = []
    currentDepth = 0

    while frontier:

        state = frontier.popleft()
        explored.append(state.id)

        step = step + 1
        print(step)
        state.printState()

        if state.compare():
            return True, state, currentDepth

        for neighbor in state.getNeighbors():
            if not (neighbor.id in explored):
                frontier.append(neighbor)
                if neighbor.depth > currentDepth:
                    currentDepth = neighbor.depth

    return False, state


def aStar(initialState):
    step = 0
    frontier = deque([initialState])
    explored = []
    currentDepth = 0

    while frontier:
        # sort according to least f
        frontier = deque(sorted(list(frontier), key=lambda state: state.f))

        # pop least f ( at the left)
        state = frontier.popleft()

        explored.append(state.id)

        step = step + 1
        print(step)
        state.printState()

        if state.compare():
            return True, state, currentDepth

        for neighbor in state.getNeighbors():
            if not neighbor.id in explored:
                frontier.appendleft(neighbor)
                if neighbor.depth > currentDepth:
                    currentDepth = neighbor.depth

    return False, state
