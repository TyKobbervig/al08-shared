"""Optional focused check starting points; expand them across the week."""

from network_support import validate_model
from network_data import GRAPH
from main import breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION

TEST_STAGE = 3


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
    tiny = {"A": ["B"], "B": ["A", "C"], "C": ["B"], "D": []}
    original_tiny = {node: neighbors.copy() for node, neighbors in tiny.items()}

    path, parents = shortest_hop_path(tiny, "A", "C")
    assert path == ["A", "B", "C"]

    path, parents = shortest_hop_path(tiny, "A", "A")
    assert path == ["A"]

    path, parents = shortest_hop_path(tiny, "A", "D")
    assert path is None

    path, parents = shortest_hop_path(tiny, "A", "C", {"C"})
    assert path is None
    assert parents == {}

    assert tiny == original_tiny

    original_graph = {node: neighbors.copy() for node, neighbors in GRAPH.items()}

    case_a_path, case_a_parents = shortest_hop_path(GRAPH, "Entrance", "Loading", {"Office"})
    assert case_a_path == [
        "Entrance",
        "Reception",
        "Hallway",
        "Assembly",
        "Inspection",
        "Packing",
        "Loading",
    ]
    assert len(case_a_path) - 1 == 6
    assert "Office" not in case_a_path

    case_b_path, case_b_parents = shortest_hop_path(GRAPH, "Entrance", "Loading", {"Office", "Packing"})
    assert case_b_path is None

    case_c_path, case_c_parents = shortest_hop_path(GRAPH, "Entrance", "Loading", {"Packing"})
    assert case_c_path == ["Entrance", "Reception", "Office", "Loading"]
    assert len(case_c_path) - 1 == 3
    assert "Packing" not in case_c_path

    for path in (case_a_path, case_c_path):
        for first, second in zip(path, path[1:]):
            assert second in GRAPH[first]

    assert GRAPH == original_graph
    assert MY_RESTRICTION == "A"


if __name__ == "__main__":
    test_model()
    if TEST_STAGE >= 2:
        test_traversals()
    if TEST_STAGE >= 3:
        test_paths_and_personal_case()
    print("AL08 Checks Passed")
