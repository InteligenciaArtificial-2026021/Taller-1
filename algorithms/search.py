from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fila = utils.Stack()

    inicio = problem.getStartState()

    fila.push((inicio, []))

    visitados = set()

    while not fila.isEmpty():
        estado, acciones = fila.pop()

        if problem.isGoalState(estado):
            return acciones

        if estado in visitados:
            continue
        visitados.add(estado)

        for sucesor, accion, _costo in problem.getSuccessors(estado):
            if sucesor not in visitados:
                fila.push((sucesor, acciones + [accion]))

              
    utils.raiseNotDefined()
    return [] 


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    cola = utils.Queue()
    inicio = problem.getStartState()

    cola.push((inicio, []))
    visitados = set()

    while not cola.isEmpty():
        estado, acciones = cola.pop()

        if problem.isGoalState(estado):
            return acciones

        if estado in visitados:
            continue
        visitados.add(estado)

        for sucesor, accion, _costo in problem.getSuccessors(estado):
            if sucesor not in visitados:
                cola.push((sucesor, acciones + [accion]))
                
    utils.raiseNotDefined()
    
    return []  
    


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    colaP = utils.PriorityQueue()
    inicio = problem.getStartState()

    colaP.push((inicio, [], 0), 0)

    mejor_costo = {inicio: 0}

    while not colaP.isEmpty():
        estado, acciones, costo = colaP.pop()

        if problem.isGoalState(estado):
            return acciones

        if costo > mejor_costo.get(estado, float("inf")):
            continue

        for sucesor, accion, paso_costo in problem.getSuccessors(estado):
            nuevo_costo = costo + paso_costo

            if nuevo_costo < mejor_costo.get(sucesor, float("inf")):
                mejor_costo[sucesor] = nuevo_costo
                colaP.push((sucesor, acciones + [accion], nuevo_costo), nuevo_costo)
    
    
    utils.raiseNotDefined()
    
    return []



def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    colaP = utils.PriorityQueue()
    inicio = problem.getStartState()


    colaP.push((inicio, [], 0), heuristic(inicio, problem))

    mejor_g = {inicio: 0}

    while not colaP.isEmpty():
        estado, acciones, g = colaP.pop()

        if problem.isGoalState(estado):
            return acciones

        if g > mejor_g.get(estado, float("inf")):
            continue

        for sucesor, accion, paso_costo in problem.getSuccessors(estado):
            nuevo_g = g + paso_costo

            if nuevo_g < mejor_g.get(sucesor, float("inf")):
                mejor_g[sucesor] = nuevo_g
                f = nuevo_g + heuristic(sucesor, problem)
                colaP.push((sucesor, acciones + [accion], nuevo_g), f)

    utils.raiseNotDefined()

    return []
    


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
