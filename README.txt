In this repository you can find the following search algorithms:
	- Astar
	- Uniform cost search
	- Breadth first search
	- Iterative deepening search
	- Depth first search
	- Depth Limited Search
	- Montecarlo tree search

All the algorithms work using the following interface:
	- successor(state): a method returning a tuples with all the successors states of the state given in input
	- isGoal(state): a method returning true if the input state is a goal state false otherwise

All the algorithms are using graph search in order to speed up, only Depth first search, depth limited search and iterative deepening do't use, 
you can use the modified version in order to use them.

