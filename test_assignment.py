from copy import deepcopy

from network_data import GRAPH
from network_support import validate_model

from main import (
    breadth_first,
    depth_first,
    reconstruct_path,
    shortest_hop_path,
)


def test_bfs_reaches_11_rooms():
    order, trace, edges = breadth_first(GRAPH, "Entrance")

    assert len(order) == 11
    assert "Annex" not in order
    assert edges == 26


def test_dfs_reaches_11_rooms():
    order, trace, edges = depth_first(GRAPH, "Entrance")

    assert len(order) == 11
    assert "Annex" not in order
    assert edges == 26


def test_annex_only():
    order, trace, edges = breadth_first(GRAPH, "Annex")

    assert order == ["Annex"]
    assert edges == 0


def test_baseline_path():
    path, parents = shortest_hop_path(
        GRAPH,
        "Entrance",
        "Loading",
    )

    assert path == [
        "Entrance",
        "Reception",
        "Office",
        "Loading",
    ]


def test_start_equals_goal():
    path, parents = shortest_hop_path(
        GRAPH,
        "Entrance",
        "Entrance",
    )

    assert path == ["Entrance"]


def test_annex_unreachable():
    path, parents = shortest_hop_path(
        GRAPH,
        "Entrance",
        "Annex",
    )

    assert path is None


def test_case_a():
    path, parents = shortest_hop_path(
        GRAPH,
        "Entrance",
        "Loading",
        ["Office"],
    )

    assert path == [
        "Entrance",
        "Reception",
        "Hallway",
        "Assembly",
        "Inspection",
        "Packing",
        "Loading",
    ]


def test_case_b():
    path, parents = shortest_hop_path(
        GRAPH,
        "Entrance",
        "Loading",
        ["Office", "Packing"],
    )

    assert path is None


def test_case_c():
    path, parents = shortest_hop_path(
        GRAPH,
        "Entrance",
        "Loading",
        ["Packing"],
    )

    assert path == [
        "Entrance",
        "Reception",
        "Office",
        "Loading",
    ]


def test_graph_unchanged():
    original = deepcopy(GRAPH)

    breadth_first(GRAPH, "Entrance")
    depth_first(GRAPH, "Entrance")
    shortest_hop_path(GRAPH, "Entrance", "Loading")

    assert GRAPH == original


def test_broken_connection_detection():
    broken = deepcopy(GRAPH)

    broken["Reception"].remove("Entrance")

    errors = validate_model(broken)

    assert len(errors) > 0


if __name__ == "__main__":
    test_bfs_reaches_11_rooms()
    test_dfs_reaches_11_rooms()
    test_annex_only()
    test_baseline_path()
    test_start_equals_goal()
    test_annex_unreachable()
    test_case_a()
    test_case_b()
    test_case_c()
    test_graph_unchanged()
    test_broken_connection_detection()

    print("All tests passed.")