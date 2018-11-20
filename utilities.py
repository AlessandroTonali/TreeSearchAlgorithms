from Node import Node
from collections import deque


def findPath(node):
    path = []
    actualNode = node
    while actualNode.getFather() != None:
        path.insert(0, actualNode.getState())
        actualNode = actualNode.getFather()
    path.insert(0,actualNode.getState())
    return path