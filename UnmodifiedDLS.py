from utilities import findPath
from Node import Node
from collections import deque



def DepthLimitedSearch(Graph, initialState, depthlimit):
    states = deque()
    states.append(Node(None, initialState))
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
            states.append(Node(actualState, successors[i]))
            i = i - 1
    return None