## 8-puzzle AI solver using BFS DFS AST
## Ahmad Ibrahim
# USEAGE:
An AI program to solve the 8-puzzle game using python

In the command line:


```markdown
$ python driver.py <method> <board>
```
where method: ‘bfs’, ‘dfs’ or ‘ast’ eg.

## METHOD:
<html>
bfs - breadth-first search <br/>
dfs - depth-first search ast <br/>
A* search, in this case using the total Manhattan Distance heuristic <br/>
</html>
```markdown
$ python driver.py ast 0,2,5,6,3,4,1,7,8
```
represents the board 0 2 5 6 3 4 1 7 8 where 0 is the blank space

This implementation treats the goal state as: 1 2 3 4 5 6 7 8 0 (some have the zero at top left)

## RETURNS:
```markdown
path_to_goal:
cost_of_path: 
nodes_expanded: 
fringe_size:
max_fringe_size: 
search_depth :
max_search_depth:
running_time:
```
