from queue import PriorityQueue


def search(init_state):
    frontier = PriorityQueue()
    explored = set()
    frontier.put(init_state)
    max_depth = 0
    while not frontier.empty():
        state = frontier.get()
        if state not in explored:
            explored.add(state)
            if state.is_goal_state():
                return state, len(explored), max_depth
            for neighbour in state.get_neighbours():
                max_depth = max(max_depth, neighbour.depth)
                frontier.put(neighbour)
    return None
