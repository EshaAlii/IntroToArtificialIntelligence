#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.

import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem

        # PLACE ANY INITIALIZATION CODE HERE

        # Set our map as our problem map
        self.map = problem.map

        # Set our goal as our problem goal
        self.goal = problem.goal

        # Initialize our max mpg to be 0
        self.max_mpg = 0.0

        # For each location in the problem map
        for location in self.map.locations():

            # For each connection at each location + roads at that location
            for connection in self.map.connection_dict:

                # Get the road cost or amount of gas from the location to the connection of that location
                gas_amount = problem.action_cost(location, connection)

                # Set our current distance equal to the euclidean distance between that location and its connection
                current_distance = problem.map.euclidean_distance(location, connection)

                # If our road cost/gas amount is not Null
                if gas_amount is not None:

                    # Calculate our current mpg to the current distance over the road cost/gas amount
                    current_mpg = current_distance / gas_amount

                    # If our current mpg is greater than the max mpg we want
                    if current_mpg > self.max_mpg:

                        # We set our max mpg as our current mpg
                        self.max_mpg = current_mpg


    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE

            # Find our euclidean distance between our location and our problem goal
            euclidean_distance = self.map.euclidean_distance(loc, self.goal)

            # Set our time cost value equal to the euclidean distance divided by our maximum mpg
            value = euclidean_distance / self.max_mpg

            # Return our time cost value
            return value
