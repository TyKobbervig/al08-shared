"""Optional AL08 starter: model Monday, traversals Tuesday, routes Thursday."""

from collections import deque
from network_support import validate_request, record_step
from app_runner import run

STAGE = 2
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


# THURSDAY — Save parents during BFS, then follow one chain backward.
def reconstruct_path(parents, goal):
    """Return start-to-goal order by following the BFS parent chain."""
    # Begin at goal and collect names until the parent is None.
    # Reverse the new list before returning it; preserve parents.
    raise NotImplementedError("Complete parent-chain reconstruction.")


def shortest_hop_path(graph, start, goal, blocked=()):
    """Return a permitted fewest-hop path and parents, or None with parent state."""
    blocked_nodes = set(blocked)
    validate_request(graph, start, goal, blocked_nodes)
    # A blocked start or goal returns None and an empty dictionary.
    # Begin parents with start: None and a queue containing start.
    # Process the queue; on reaching goal, return the reconstructed path and parents.
    # For a neighbor not in parents and not blocked, save its first parent and enqueue.
    # If the queue runs out, return None and the parents collected.
    raise NotImplementedError("Complete BFS with parents and blocked nodes.")


def main():
    """Run only the selected completed stage using supplied presentation."""
    run(STAGE, breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION)


if __name__ == "__main__":
    main()
