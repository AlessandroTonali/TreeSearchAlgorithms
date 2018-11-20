from BreadthFirst import BreadthFirstSearch
from DepthFirst import DepthFirstSearch
from UniformCost import UniformCostSearch
from UnmodifiedDLS import DepthLimitedSearch
from IDS import IterativeDeepeningSearch
from AStar import AstarSearch
from MonteCarlo import MCS

def BFS(graph, initialState):
    return BreadthFirstSearch(graph, initialState)

def DFS(graph, initialState):
    return DepthFirstSearch(graph, initialState)

def UCS(valuedGraph, initialState):
    return UniformCostSearch(valuedGraph, initialState)

def DLS(graph, initialState, depthLimit):
    return DepthLimitedSearch(graph, initialState, depthLimit)

def IDS(graph, initialState):
    return IterativeDeepeningSearch(graph, initialState)

def Astar(ValuedGraph, initialState, heuristic):
    return AstarSearch(ValuedGraph, initialState, heuristic)

def MCTS(valuedGraph, state, budget):
    return MCS(valuedGraph, state, budget)





































