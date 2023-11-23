#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS AND ACKNOWLEDGMENTS
#
# Comments:
# The entirety of this code is similar to DFS in structure, utilizing the Generic Search Pseudocode provided to us.
# The primary difference between the two is the simple fact that, when the frontier was initialized, I changed the
# secondary input to True, rather than False, to implement a Stack Structure rather than a Queue structure.
# Additionally, I implemented a set in python, rather than an array, to follow in line with the pseudocode provided.
# Most of my understanding of the code came from the pseudocode, and my background knowledge in CSE 100 on
# the provided DFS and BFS algorithms (although I did utilize reviews). There was a point where I was confused as to
# how the initialization of the Frontier functioned. I was under the impression that False initialized a Stack, however
# that was a misunderstanding on my end and speaking with Dulce Karina allowed me to see the error in my logic.
# Additionally, I recall not utilizing repeat check initially, as that was not implemented within the Pseudocode.
# I spoke to Ernesto, unsure of how I would implement the repeat check, as he was also stuck on this issue as well.
# Eventually, after overlooking the pseudocode, we came to the conclusion that implementing it within the for loop
# would make the most sense, given that there could be cases where there is a repeated child node in the reached_set.
#
#
# Citations:
# PA0Spec.pdf -> Generic Search Slide pseudocode that was provided
# BFS Review -> https://www.youtube.com/watch?v=HZ5YTanv5QE
# DFS Review -> https://www.youtube.com/watch?v=Urx87-NMm6c
# Sets in Python -> https://www.w3schools.com/python/python_sets.asp
# Review on For loops in Python -> https://wiki.python.org/moin/ForLoop
# Discussion on Frontier Initialization (determining Stack vs Queue) ->  Dulce Karina Pimentel-Hurlburt
# Discussion on Repeat Check Implementation logic (determining how to use it) -> Ernesto Reyes
#
#
# Acknowledgements:
# Dulce Karina Pimentel-Hurlburt
# Ernesto Reyes
#
#
#
# Esha Sarfraz - September 29, 2022


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
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

    # Initialize our frontier to contain our node (True makes it a Stack)
    front_init = Frontier(initial, True) # DFS utilizes a Stack Structure

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
