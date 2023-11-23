#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Comments:
# The entirety of this code was created by utilizing prior code and changing up implementation to better fit the
# Uniform Cost Search pseudocode provided to us in PA1spec.pdf. Essentially what differentiated this code from my prior
# one was the frontier initialization, and checking if the child node was in the reached set as
# opposed to not in the reached set. Additionally some more differences include: checking if the child node was in the
# frontier and had a higher cost, deleting the node from the frontier if it was and adding the child to the frontier,
# and implementing an else statement (if the child node was NOT in the frontier) and adding our child node to the
# frontier, and the child node's location to the reached set. This specific algorithm is one that I was unfamiliar with
# # in terms of conceptual understanding and coding.  So I made sure to search up the the Uniform Cost Search algorithm
# to better my understanding of it overall.
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


def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # Create the node with the initial state of the problem
    initial = Node(problem.start)

    # If the node reaches the goal state (aka the node's location is equivalent to our goal location)
    if problem.is_goal(initial.loc):

        # We will return the initial node
        return initial

    # Initialize our frontier to contain our node (Priority Queue that sorts by g(n) cost)
    front_init = Frontier(initial, sort_by = 'g')

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
                if child.loc in reached_set:

                    # If the child node is in the frontier and had a higher cost
                    if (child in front_init) and (front_init[child] > child.value('g')):

                        # Remove the matching node from the frontier
                        front_init.__delitem__(child)

                        # Add our child node to our frontier
                        front_init.add(child)

                # Otherwise...
                else:

                    # Add our child node to our frontier
                    front_init.add(child)

                    # Add our child node's location to our reached set
                    reached_set.add(child.loc)

            # Otherwise if our repeat check is False
            elif repeat_check is False:

                # Add the child to the frontier
                front_init.add(child)


    return None
