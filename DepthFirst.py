from collections import deque
from copy import deepcopy

from Node import Node
from utilities import findPath

def DepthFirstSearch(Graph, initialState):
    if Graph.isGoal(initialState):
        return [[initialState], 0]
    states = deque()
    states.appendleft(Node(None, initialState))
    visited = set()
    while len(states) > 0:
        actualstate = states.popleft()
        if actualstate.getState() in visited:
            continue
        visited.add(actualstate.getState())
        if Graph.isGoal(actualstate.getState()):  # if it is a final state the job is done
            return [findPath(actualstate),len(findPath(actualstate)) - 1]
        successors = Graph.successors(actualstate.getState())
        if successors == None:
            continue
        i = len(successors) - 1
        while i >= 0:
            states.appendleft(Node(actualstate,successors[i]))
            i = i - 1
    print("no solutuion found")
    return False
