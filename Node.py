
class Node:
    def __init__(self, father, state):
        self.father = father
        self.state = state

    def getState(self):
        return self.state
    def getFather(self):
        return self.father

    def __gt__(self, other):
        if isinstance(other, Node):
            return True
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Node):
            return True
        return NotImplemented