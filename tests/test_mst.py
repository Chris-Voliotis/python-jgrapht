import pytest

import jgrapht.graph as graph
import jgrapht.algorithms.mst as mst

def build_graph():
    g = graph.Graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    for i in range(0, 10):
        g.add_vertex()

    e01 = g.add_edge(0, 1)
    e02 = g.add_edge(0, 2)
    e03 = g.add_edge(0, 3)
    e04 = g.add_edge(0, 4)
    e05 = g.add_edge(0, 5)
    e06 = g.add_edge(0, 6)
    e07 = g.add_edge(0, 7)
    e08 = g.add_edge(0, 8)
    e09 = g.add_edge(0, 9)

    e12 = g.add_edge(1, 2)
    e23 = g.add_edge(2, 3)
    e34 = g.add_edge(3, 4)
    e45 = g.add_edge(4, 5)
    e56 = g.add_edge(5, 6)
    e67 = g.add_edge(6, 7)
    e78 = g.add_edge(7, 8)
    e89 = g.add_edge(8, 9)
    e91 = g.add_edge(9, 1)

    return g

def test_kruskal():
    g = build_graph()
    mst_w, mst_edges = mst.mst_kruskal(g)
    assert mst_w == 9.0
    expected = set([0, 1, 2, 3, 4, 5, 6, 7, 8])
    solution = set(mst_edges)
    assert expected <= solution
    assert solution <= expected


def test_prim():
    g = build_graph()
    mst_w, mst_edges = mst.mst_prim(g)
    assert mst_w == 9.0
    expected = set([0, 1, 2, 3, 4, 5, 6, 7, 8])
    solution = set(mst_edges)
    assert expected <= solution
    assert solution <= expected


def test_boruvka():
    g = build_graph()
    mst_w, mst_edges = mst.mst_boruvka(g)
    assert mst_w == 9.0
    expected = set([0, 1, 2, 3, 4, 5, 6, 7, 8])
    solution = set(mst_edges)
    assert expected <= solution
    assert solution <= expected
