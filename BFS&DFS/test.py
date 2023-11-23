
from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):

    initial = Node(problem.start)

    if problem.is_goal(initial.loc):
        return initial

    front_init = Frontier(initial, False)

    reached_set = set()

    reached_set.add(initial.loc)

    while front_init.is_empty() is False:

        extracted = front_init.pop()

        if problem.is_goal(extracted.loc):
            return extracted

        expanded = extracted.expand(problem)

        for child in expanded:
            if repeat_check is True:

                if child.loc not in reached_set:

                    front_init.add(child)

                    reached_set.add(child.loc)

            elif repeat_check is False:

                front_init.add(child)

    return None