from queue import deque


def search(init_state):
    frontier = list()
    frontier_copy = set()
    explored = set()
    frontier.append(init_state)
    frontier_copy.add(init_state)
    max_depth = 0
    while frontier:
        state = frontier.pop()
        frontier_copy.remove(state)
        if state.is_goal_state():
            return state, len(explored), max_depth
        explored.add(state)
        for neighbour in reversed(state.get_neighbours()):
            if neighbour not in explored and neighbour not in frontier_copy:
                max_depth = max(max_depth, neighbour.depth)
                frontier.append(neighbour)
                frontier_copy.add(neighbour)
    return None
