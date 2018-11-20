from copy import deepcopy
from heapq import heappush
from heapq import heappop
from ValuedNode import ValuedNode
from Node import Node
from utilities import findPath


def UniformCostSearch(valuedGraph, initialState):
    if valuedGraph.isGoal(initialState):
        return [[initialState], 0]
    states = []
    heappush(states, (0,Node(None, initialState)))
    visited = set()
    visited.add(initialState)
    i = 0
    addingNodes = valuedGraph.successors(initialState)
    if not isinstance(addingNodes[0], tuple):
        while len(states) != 0:
            popped = heappop(states)
            actualCost = popped[0]
            actualState = popped[1]
            if valuedGraph.isGoal(actualState.getState()):
                return [findPath(actualState), actualCost]
            addingNodes = valuedGraph.successors(actualState.state)
            if addingNodes == None:
                continue
            while i < len(addingNodes):
                if addingNodes[i] in visited:
                    i = i + 1
                    continue
                visited.add(addingNodes[i])
                heappush(states, (actualCost + 1, Node(actualState, addingNodes[i])))
                i = i + 1
            i = 0
        print("no solution found")
        return None


    while len(states) > 0:
        popped = heappop(states)
        actualCost = popped[0]
        actualState = popped[1]
        if valuedGraph.isGoal(actualState.getState()):
            return [findPath(actualState), actualCost]
        addingNodes = valuedGraph.successors(actualState.state)
        if addingNodes == None:
            continue
        while i < len(addingNodes):
            if addingNodes[i][1] in visited:
                i = i + 1
                continue
            visited.add(addingNodes[i][1])
            heappush(states,(actualCost + addingNodes[i][0], Node(actualState,addingNodes[i][1])))
            i = i + 1
        i = 0
    print("No solution found")
    return None