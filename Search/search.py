# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    """

    visited = set()  
    stack = util.Stack() 

    stack.push((problem.getStartState(), [])) 
    while not stack.isEmpty():
        node, actions = stack.pop()  
        if problem.isGoalState(node):
            return actions 
        if node not in visited:
            visited.add(node)
            for next, action,cost in  problem.getSuccessors(node) :
                stack.push((next, actions + [action])) 

    return [] 





def breadthFirstSearch(problem: SearchProblem):

    visited = set()
    queue = util.Queue()

    queue.push(( problem.getStartState(), []))
    visited.add(problem.getStartState())
    
    while not queue.isEmpty():
        node, actions = queue.pop()
        if problem.isGoalState(node):
            return actions
        for next, action, cost in problem.getSuccessors(node):
            if next not in visited:
                queue.push((next, actions + [action]))
                visited.add(next)
    
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
