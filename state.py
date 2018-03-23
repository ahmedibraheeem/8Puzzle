from heuistic import *


class State:
    GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ORDER = 3

    def __init__(self, current_state):
        self.positions = current_state
        self.parent = None
        self.move = None
        self.depth = 0

    def __eq__(self, other):
        if isinstance(other, State) and self.positions == other.positions:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(tuple(self.positions))

    def ret(self):
        return self.positions

    def is_goal_state(self):
        return self.positions == State.GOAL_STATE

    def clone(self):
        return State(list(self.positions))

    def get_next_state(self, move):
        next_state = self.clone()
        slide_index = next_state.positions.index(0)
        if move == 'Right':
            if slide_index % State.ORDER == State.ORDER - 1:
                return None
            next_state.swap_elements(slide_index, slide_index + 1)
        elif move == 'Left':
            if slide_index % State.ORDER == 0:
                return None
            next_state.swap_elements(slide_index, slide_index - 1)
        elif move == 'Up':
            if slide_index < State.ORDER:
                return None
            next_state.swap_elements(slide_index, slide_index - 3)
        elif move == 'Down':
            if slide_index > len(next_state.positions) - 1 - State.ORDER:
                return None
            next_state.swap_elements(slide_index, slide_index + 3)
        else:
            return None
        return next_state

    def swap_elements(self, index1, index2):
        temp = self.positions[index1]
        self.positions[index1] = self.positions[index2]
        self.positions[index2] = temp

    def get_neighbour(self, move):
        state = self.get_next_state(move)
        if state is not None:
            state.parent = self
            state.move = move
            state.depth = self.depth + 1
        return state

    def add_neighbour(self, neighbours, move):
        state = self.get_neighbour(move)
        if state is not None:
            neighbours.append(state)

    def get_neighbours(self):
        neighbours = []
        self.add_neighbour(neighbours, 'Up')
        self.add_neighbour(neighbours, 'Down')
        self.add_neighbour(neighbours, 'Left')
        self.add_neighbour(neighbours, 'Right')
        return neighbours


class AstState(State):
    def __init__(self, current_state):
        super().__init__(current_state)
        self.cost = 0

    def compute_cost(self):
        cost = 0
        for idx, pos in enumerate(self.positions):
            if pos != 0:
                cost += LOOK_UP.get(pos).get(idx)
        return cost

    def clone(self):
        return AstState(list(self.positions))

    def get_neighbour(self, move):
        state = self.get_next_state(move)
        if state is not None:
            state.parent = self
            state.move = move
            state.depth = self.depth + 1
            state.cost = state.depth + state.compute_cost()
        return state

    def __lt__(self, other):
        return self.cost < other.cost
