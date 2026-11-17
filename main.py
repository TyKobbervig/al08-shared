from collections import deque

from network_support import (
    validate_request,
    record_step,
)


def breadth_first(graph, start):
    """
    Perform breadth-first traversal from start.
    Return (order, trace, edges_examined).
    """
    validate_request(graph, start)

    order = []
    trace = []
    edges_examined = 0

    discovered = {start}
    frontier = deque([start])

    while frontier:
        node = frontier.popleft()
        order.append(node)

        for neighbor in graph[node]:
            edges_examined += 1

            if neighbor not in discovered:
                discovered.add(neighbor)
                frontier.append(neighbor)

        record_step(trace, node, frontier, discovered)

    return order, trace, edges_examined


def depth_first(graph, start):
    """
    Perform depth-first traversal from start.
    Return (order, trace, edges_examined).
    """
    validate_request(graph, start)

    order = []
    trace = []
    edges_examined = 0

    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            edges_examined += 1

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

        record_step(trace, node, stack, visited)

    return order, trace, edges_examined


def reconstruct_path(parents, goal):
    """
    Follow parent links back to start and return the route.
    """
    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path


def shortest_hop_path(graph, start, goal, blocked=()):
    """
    Return the fewest-hop route using BFS.
    Return (path, parents) or (None, parents).
    """
    blocked = set(blocked)

    validate_request(graph, start, goal, blocked)

    if start in blocked or goal in blocked:
        return None, {}

    if start == goal:
        return [start], {start: None}

    parents = {start: None}
    frontier = deque([start])

    while frontier:
        node = frontier.popleft()

        for neighbor in graph[node]:
            if neighbor in blocked:
                continue

            if neighbor not in parents:
                parents[neighbor] = node
                frontier.append(neighbor)

                if neighbor == goal:
                    return reconstruct_path(parents, goal), parents

    return None, parents