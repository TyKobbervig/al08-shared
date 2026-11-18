"""Optional AL08 starter: model Monday, traversals Tuesday, routes Thursday."""

from collections import deque
from network_support import validate_request, record_step
from app_runner import run

STAGE = 3
MY_RESTRICTION = "A"  # Set this to your instructor-issued case in your personal copy.

# TUESDAY — Complete each algorithm separately on the fresh common fixture.
def breadth_first(graph, start):
    validate_request(graph, start)

    queue = deque([start])
    discovered = {start}
    order = []
    trace = []
    edge_count = 0

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            edge_count += 1

            if neighbor not in discovered:
                discovered.add(neighbor)
                queue.append(neighbor)
            record_step(trace, current, queue, discovered)

    return order, trace, edge_count

def depth_first(graph, start):
    validate_request(graph, start)

    stack = [start]
    visited = set()
    order = []
    trace = []
    edge_count = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue
        visited.add(current)
        order.append(current)

        for neighbor in reversed(graph[current]):
            edge_count += 1

            if neighbor not in visited:
                stack.append(neighbor)
        record_step(trace, current, stack, visited)

    return order, trace, edge_count

def reconstruct_path(parents, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path


def shortest_hop_path(graph, start, goal, blocked=()):

    blocked_nodes = set(blocked)
    validate_request(graph, start, goal, blocked_nodes)

    if start in blocked_nodes or goal in blocked_nodes:
        return None, {}

    parents = {start: None}
    queue = deque([start])

    while queue: 
        current = queue.popleft()

        if current == goal:
            return reconstruct_path(parents, goal), parents

        for neighbor in graph[current]:
            if neighbor not in parents and neighbor not in blocked_nodes:
                parents[neighbor] = current
                queue.append(neighbor)

    return None, parents  

def main():
    """Run only the selected completed stage using supplied presentation."""
    run(STAGE, breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION)


if __name__ == "__main__":
    main()
