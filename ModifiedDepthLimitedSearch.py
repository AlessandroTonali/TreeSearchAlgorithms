from collections import deque
from copy import deepcopy
from Node import Node
from utilities import findPath



def DepthLimitedSearch(Graph, initialState, depthlimit):
    states = deque()
    states.append(Node(None, initialState))
    visited = set()
    while len(states) > 0:
        actualState = states.popleft()
        if len(findPath(actualState)) > depthlimit:
            continue
        if Graph.isGoal(actualState.getState()):  # if it is a final state the job is done
            return [findPath(actualState),len(findPath(actualState)) - 1]
        successors = Graph.successors(actualState.getState())
        if successors == None:
            continue
        else:
            i = len(successors) - 1
        while i >= 0:
            if successors[i].state in visited:
                continue
            visited.add(successors[i].state)
            states.append(Node(actualState, successors[i]))
            i = i - 1
    return None