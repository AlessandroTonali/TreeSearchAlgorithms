
from heapq import heappop
from heapq import heappush
from copy import deepcopy
from Node import Node
from utilities import findPath


def AstarSearch(valuedGraph, initialState, heuristic):

    visited = set()
    visited.add(initialState)
    states = []
    heappush(states, (0 + heuristic(initialState), 0, Node(None, initialState)))
    i = 0
    popped = heappop(states)
    actualState = popped[2]
    addingNodes = valuedGraph.successors(actualState.state)
    heappush(states, (0 + heuristic(initialState), 0, Node(None, initialState)))
    if not isinstance(addingNodes[0], tuple):
        while len(states) > 0:
            popped = heappop(states)
            actualState = popped[2]
            actualCost = popped[1]
            if valuedGraph.isGoal(actualState.state):
                return [findPath(actualState), actualCost]
            addingNodes = valuedGraph.successors(actualState.state)
            if addingNodes == None:
                continue
            while i < len(addingNodes):
                if addingNodes[i] in visited:
                    i = i + 1
                    continue
                visited.add(addingNodes[i])
                heappush(states, (actualCost + 1 + heuristic(addingNodes[i]), actualCost + 1,
                                    Node(actualState, addingNodes[i])))

                i = i + 1
            i = 0
        print("no Solution found")
        return None

    while len(states) > 0:
        popped = heappop(states)
        actualState = popped[2]
        actualCost = popped[1]
        if valuedGraph.isGoal(actualState.state):
            return [findPath(actualState), actualCost]
        addingNodes = valuedGraph.successors(actualState.state)
        if addingNodes == None:
            continue
        while i < len(addingNodes):
            if addingNodes[i][1] in visited:
                i = i+1
                continue
            visited.add(addingNodes[i][1])
            heappush(states,(actualCost + addingNodes[i][0] + heuristic(addingNodes[i][1]),
                             actualCost + addingNodes[i][0],
                             Node(actualState, addingNodes[i][1])))

            i = i + 1
        i = 0
    print("no Solution found")
    return None
