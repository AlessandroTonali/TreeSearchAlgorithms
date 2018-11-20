
class ValuedNode:
    def __init__(self, cost, father, state):
        self.father = father
        self.state = state
        self.cost = cost

    def __lt__(self, other):
        if isinstance(other, ValuedNode):
            return self.cost <= other.cost
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, ValuedNode):
            return self.cost >= other.cost
        return NotImplemented