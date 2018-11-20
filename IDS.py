from UnmodifiedDLS import DepthLimitedSearch

def IterativeDeepeningSearch(Graph, initialState):
    i = 0
    while True:
        result = DepthLimitedSearch(Graph, initialState, i)
        if result != None:
            return  result
        i = i + 1