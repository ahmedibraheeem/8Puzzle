from queue import Queue


def search(init_state):
    frontier = Queue()
    explored = set()
    frontier.put(init_state)
    max_depth = 0
    while not frontier.empty():
        state = frontier.get()
        if state not in explored:
            if state.is_goal_state():
                return state, len(explored), max_depth
            explored.add(state)
            for neighbour in state.get_neighbours():
                max_depth = max(max_depth, neighbour.depth)
                frontier.put(neighbour)
    return None
