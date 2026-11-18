"""Optional focused check starting points; expand them across the week."""

from network_support import validate_model
from network_data import GRAPH
from main import breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION

TEST_STAGE = 2  # Raise to 2 Tuesday and 3 Thursday after completing those tests.


def test_model():
    assert validate_model({"A": ["B"], "B": ["A"]}) == []
    assert validate_model({"A": ["Missing"]})

    broken_graph = {node: neighbors.copy() for node, neighbors in GRAPH.items()}
    broken_graph["Reception"].remove("Entrance")
    assert validate_model(broken_graph)

    broken_graph["Reception"].append("Entrance")
    assert validate_model(broken_graph) == []


def test_traversals():
    """Check independent expectations before trying the full workshop fixture."""
    tiny = {"A": ["B", "C"], "B": ["A"], "C": ["A"], "D": []}
    expected_bfs = ["A", "B", "C"]
    expected_dfs = ["A", "B", "C"]

    original = {node: neighbors.copy() for node, neighbors in tiny.items()}

    bfs_order, bfs_trace, bfs_edges = breadth_first(tiny, "A")
    dfs_order, dfs_trace, dfs_edges = depth_first(tiny, "A")

    assert bfs_order == expected_bfs
    assert dfs_order == expected_dfs

    assert len(bfs_order) == len(set(bfs_order))
    assert len(dfs_order) == len(set(dfs_order))

    assert bfs_edges == 4
    assert dfs_edges == 4

    assert tiny == original


def test_paths_and_personal_case():
    """Check route boundaries and your issued blocked-node result independently."""
    # Check a small known path, start=goal, disconnected goal, and a blocked endpoint.
    # Import the supplied workshop data and use MY_RESTRICTION for your personal case.
    # Check exact expected endpoints/hops or None, consecutive connections, no blocked
    # rooms in a returned route, and unchanged source data.
    raise NotImplementedError("Add Thursday's path and personal-case checks.")


if __name__ == "__main__":
    test_model()
    if TEST_STAGE >= 2:
        test_traversals()
    if TEST_STAGE >= 3:
        test_paths_and_personal_case()
    print("AL08 Checks Passed")
