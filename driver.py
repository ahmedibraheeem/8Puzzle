#this program is created by Ahmad Ibrahim
#https://github.com/ahmedibraheeem/8Puzzle

from bfs import search as bfs_search
from dfs import search as dfs_search
from ast import search as ast_search
from state import *
import sys
import time


def main(argv):
    output_file = open('output.txt', 'w')
    search_output = None
    if len(argv) != 3:
        print('Usage:   driver_3.py < search-algo (bfs | dfs | ast) > <initial_state>')
        print('Example: driver_3.py bfs 0,8,7,6,5,4,3,2,1')
        sys.exit(2)
    else:
        search_algorithm = argv[1]
        init_state = argv[2].split(",")
        init_state = [int(x) for x in init_state]
        if set(init_state) != set(State.GOAL_STATE):
            print('Invalid initial state, the initial sequence should contain '
                  'at-least and at-most a single occurrence of numbers '
                  'between 0 to 8 ordered in random sequence')
            sys.exit(2)
        else:
            start_time = time.clock()
            if search_algorithm.lower() == 'bfs':
                search_output = bfs_search(State(init_state))
            elif search_algorithm.lower() == 'dfs':
                search_output = dfs_search(State(init_state))
            elif search_algorithm.lower() == 'ast':
                search_output = ast_search(AstState(init_state))
            else:
                print('Invalid search algorithm, the program accepts only bfs or dfs or ast as the search algorithm')
                sys.exit(2)
            end_time = time.clock()

            if search_output is not None:
                state = search_output[0]
                links = []
                state_depth = state.depth
                while state.parent is not None:
                    links = [state.move] + links
                    state = state.parent
                print("path_to_goal:", links, file=output_file)
                print("cost_of_path:", state_depth, file=output_file)
                print("nodes_expanded:", search_output[1], file=output_file)
                print("search_depth:", state_depth, file=output_file)
                print("max_search_depth:", search_output[2], file=output_file)
                print("running_time:", end_time - start_time, file=output_file)
    output_file.close()

if __name__ == "__main__":
    main(sys.argv)
