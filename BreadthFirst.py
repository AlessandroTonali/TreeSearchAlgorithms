from copy import deepcopy
from collections import deque
from Node import Node
from utilities import findPath

def BreadthFirstSearch(Graph, initialState):
    if Graph.isGoal(initialState):
        return [[initialState], 0]
    states = deque()
    states.append(Node(None , initialState))
    visited = set()
    visited.add(initialState)
    while len(states) > 0:
        actualstate = states.popleft()
        if Graph.isGoal(actualstate.getState()):  # if it is a final state the job is done
            return [findPath(actualstate),len(findPath(actualstate)) - 1]
        successors = Graph.successors(actualstate.getState())
        i = 0
        if successors == None:
            continue
        while i < len(successors):
            if successors[i] in visited:
                i = i+ 1
                continue

            visited.add(successors[i])
            states.append(Node(actualstate,successors[i]))
            i = i + 1


    print("no solutuion found")
    return False