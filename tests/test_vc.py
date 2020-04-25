import pytest

import jgrapht.graph as graph
import jgrapht.algorithms.vertexcover as vc

def assert_same_set(set1, set2):
    assert set1 <= set2 and set2 <= set1

def build_graph():
    g = graph.Graph(directed=False, allowing_self_loops=True, allowing_multiple_edges=False, weighted=True)

    for i in range(0, 10):
        g.add_vertex()
    for i in range(1,10):
        g.add_edge(0, i)    

    vertex_weights = dict()
    vertex_weights[0] = 1000.0;   
    for i in range(1, 10):
        vertex_weights[i] = 1.0;

    return g, vertex_weights

def test_greedy():
    g, vertex_weights = build_graph()
    vc_weight, vc_vertices = vc.vertexcover_greedy(g)
    assert vc_weight == 1.0
    assert_same_set(set(vc_vertices), set([0]))


def test_greedy_with_weights():
    g, vertex_weights = build_graph()
    vc_weight, vc_vertices = vc.vertexcover_greedy(g, vertex_weights=vertex_weights)
    assert vc_weight == 9.0
    assert_same_set(set(vc_vertices), set([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def test_clarkson():
    g, vertex_weights = build_graph()
    vc_weight, vc_vertices = vc.vertexcover_clarkson(g)
    assert vc_weight == 1.0
    assert_same_set(set(vc_vertices), set([0]))


def test_clarkson_with_weights():
    g, vertex_weights = build_graph()
    vc_weight, vc_vertices = vc.vertexcover_clarkson(g, vertex_weights=vertex_weights)
    assert vc_weight == 9.0
    assert_same_set(set(vc_vertices), set([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def test_edgebased():
    g, vertex_weights = build_graph()
    vc_weight, vc_vertices = vc.vertexcover_edgebased(g)
    assert vc_weight == 2.0
    assert_same_set(set(vc_vertices), set([0, 1]))     



