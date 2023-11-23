#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.

from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    # Create the node with the initial state of the problem
    initial = Node(problem.start, h_eval=h.h_cost(problem.start), h_fun=h)

    # If the node reaches the goal state (aka the node's location is equivalent to our goal location)
    if problem.is_goal(initial.loc):

        # We will return the initial node
        return initial

    # Initialize our frontier to contain our node (Priority Queue that sorts by f(n) cost)
    front_init = Frontier(initial, sort_by='f')

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

                # If the location of our child node is in line with any of those in our reached set...
                if child.loc in reached_set:

                    # And if the child node is in the frontier and had a higher cost
                    if child in front_init and (front_init[child] > child.value('f')):

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
