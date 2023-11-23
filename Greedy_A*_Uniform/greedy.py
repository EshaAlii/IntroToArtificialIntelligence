#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Comments:
# The entirety of this code was created by utilizing prior code and changing up implementation to better fit the
# Greedy Search pseudocode provided to us in PA1spec.pdf. Essentially what differentiated this code from my prior one
# was the initial node initialization and the frontier initialization. This specific algorithm is one that was familiar
# to me given my prior knowledge in CSE 100 with Greedy Algorithms. I did make sure to search up the the Greedy
# Search algorithm in terms of how it is implemented in AI to ensure that I was not mistaking the algorithm. However,
# from what I saw, it seemed to fall mostly in line with how I learnt Greedy algorithms functioned.
#
#
# Citations:
# PA1Spec.pdf -> Greedy Search pseudocode that was provided
# PA1Spec.pdf -> A* Search pseudocode that was provided
# PA1Spec.pdf -> Uniform Cost Search pseudocode that was provided
# PASpec.pdf -> action_cost = road cost = gas amount
# https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/ -> Review on Greedy Search
# https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/ -> Review on Uniform Cost Search
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ -> Review on Dijkstra (for ucost)
# https://blog.finxter.com/python-__delitem__-magic-method/ -> Utilizing front_init.__delitem__(child)
# https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html -> Understanding of Heuristic + A* search
# https://brilliant.org/wiki/a-star-search/#heuristics -> Understanding + Overestimation of Heuristic
# Conversation with Nick Mount and Andrew Mouillesseaux on Heuristic Function Concept + how to go about implementing it
#
#
# Acknowledgements:
# Nick Mount -> Helped understand concept behind Heuristic Function
# Andrew Mouillesseaux -> Helped understand concept behind Heuristic Function + how to go about implementing it
#
#
# Esha Sarfraz - September 29, 2023
#

from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    # Create the node with the initial state of the problem
    initial = Node(problem.start, h_eval=h.h_cost(problem.start), h_fun=h)

    # If the node reaches the goal state (aka the node's location is equivalent to our goal location)
    if problem.is_goal(initial.loc):

        # We will return the initial node
        return initial

    # Initialize our frontier to contain our node (Priority Queue that sorts by h(n) cost)
    front_init = Frontier(initial, sort_by='h')

    # Initialize our reached set
    reached_set = set()

    # Add our initial node's location to our reached set
    reached_set.add(initial.loc)

    # While the frontier isn't empty
    while front_init.is_empty() is False:

        # Pop or "remove"  our leaf node and save that as our extracted node
        extracted = front_init.pop()

        # If the node reaches the goal state (aka the node's location is equivalent to our goal location)
        if problem.is_goal(extracted.loc):

            # We will return the extracted node
            return extracted

        # Expand the node
        expanded = extracted.expand(problem)

        # For each child node in the expanded node
        for child in expanded:

            # If repeat check is True
            if repeat_check is True:

                # If the location of our child node isn't in line with any of those in our reached set...
                if child.loc not in reached_set:

                    # Add the child to the frontier
                    front_init.add(child)

                    # Add our child node's location to our reached set
                    reached_set.add(child.loc)

            # Otherwise if our repeat check is False
            elif repeat_check is False:

                # Add the child to the frontier
                front_init.add(child)

    # Return Failure
    return None
