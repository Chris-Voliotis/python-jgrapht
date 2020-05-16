import time

from . import backend


def barabasi_albert_graph(graph, m0, m, n, seed=None):
    """Barabási-Albert growth and preferential attachment graph generator.
 
    The generator is described in the paper: A.-L. Barabási and R. Albert. Emergence of scaling in
    random networks. Science, 286:509-512, 1999.
 
    The generator starts with a complete graph of :math:`m_0` nodes and grows the network by adding
    :math:`n - m_0` additional nodes. The additional nodes are added one by one and each of them is
    connected to :math:`m` previously added nodes, where the probability of connecting to a node is
    proportional to its degree.
 
    Note that the Barabàsi-Albert model is designed for undirected networks. Nevertheless, this
    generator also works with directed networks where the probabilities are proportional to the sum
    of incoming and outgoing degrees. For a more general discussion see the paper: M. E. J. Newman.
    The Structure and Function of Complex Networks. SIAM Rev., 45(2):167--256, 2003.

    :param graph: the graph to alter
    :param m0: number of initial nodes
    :param m: number of edges of each new node added during the network growth
    :param n: final number of nodes
    :param seed: seed for the random number generator. If None the system time is used
    :raise ValueError: in case of invalid parameters
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_barabasi_albert(graph.handle, m0, m, n, seed)


def barabasi_albert_forest(graph, t, n, seed=None):
    """Barabási-Albert growth and preferential attachment forest generator.
 
    The general graph generator is described in the paper: A.-L. Barabási and R. Albert. Emergence of
    scaling in random networks. Science, 286:509-512, 1999.

    The generator starts with a :math:`t` isolated nodes and grows the network by adding
    :math:`n - t` additional nodes. The additional nodes are added one by one and each of them is
    connected to one previously added node, where the probability of connecting to a node is
    proportional to its degree.
 
    Note that this Barabàsi-Albert generator only works on undirected graphs.

    :param graph: the graph to alter. Must be undirected.
    :param t: number of initial isolated nodes.
    :param n: final number of nodes
    :param seed: seed for the random number generator. If None the system time is used
    :raise ValueError: In case of invalid parameters    
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_barabasi_albert_forest(graph.handle, t, n, seed)


def complete_graph(graph, n):
    """Generates a complete graph of any size.

    A complete graph is a graph where every vertex shares an edge with every other vertex.
    If it is a directed graph, then edges must always exist in both directions.

    :param graph: the graph to alter, which should be empty
    :param n: the number of vertices.
    """
    backend.jgrapht_generate_complete(graph.handle, n)


def complete_bipartite_graph(graph, a, b):
    """Generate a complete bipartite graph.

    :param graph: the graph to alter
    :param a: size of the first partition
    :param b: size of the second partition
    """
    backend.jgrapht_generate_bipartite_complete(graph.handle, a, b)


def empty_graph(graph, n):
    """Generate an empty graph of any size.
    
    The `empty graph <https://mathworld.wolfram.com/EmptyGraph.html>`_ is a graph 
    with a certain number of vertices and no edges.

    :param g: the graph to alter, which should be empty
    :param n: number of vertices
    """
    backend.jgrapht_generate_empty(graph.handle, n)


def gnm_random_graph(graph, n, m, loops=False, multiple_edges=False, seed=None):
    r"""Create a random graph based on the :math:`G(n, M)` Erdős–Rényi model. 
 
    In the :math:`G(n, M)` model, a graph is chosen uniformly at random from the collection
    of all graphs which have :math:`n` nodes and :math:`M` edges. For example, in the 
    :math:`G(3, 2)` model, each of the three possible graphs on three vertices and two edges
    are included with probability :math:`\frac{1}{3}`.
 
    The implementation creates the vertices and then randomly chooses an edge and tries to
    add it. If the add fails for any reason (an edge already exists and multiple edges are
    not allowed) it will just choose another and try again. The performance therefore varies
    significantly based on the probability of successfully constructing an acceptable edge.
 
    The implementation tries to guess the number of allowed edges based on the following. If
    self-loops or multiple edges are allowed and requested, the maximum number of edges is
    the maximum integer value. Otherwise the maximum for undirected graphs with :math:`n`
    vertices is :math:`\frac{n(n-1)}{2}` while for directed :math:`n(n-1)`.

    :param graph: the graph to alter
    :param n: the number of nodes
    :param m: the number of edges
    :param loops: whether to create self-loops
    :param multiple_edges: whether to create multiple edges
    :param seed: seed for the random number generator. If None then the system time is used
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_gnm_random(graph.handle, n, m, loops, multiple_edges, seed)


def gnp_random_graph(graph, n, p, loops=False, seed=None):
    r"""Create a random graph based on the :math:`G(n, p)` Erdős–Rényi model.
 
    In the :math:`G(n, p)` model, a graph is constructed by connecting nodes randomly.
    Each edge is included in the graph with probability :math:`p` independent from every
    other edge. The complexity of the generator is :math:`\mathcal{O}(n^2)` where :math:`n`
    is the number of vertices.

    :param graph: the graph to alter
    :param n: the number of nodes
    :param p: probability of edge existence
    :param loops: whether to create self-loops
    :param seed: seed for the random number generator. If None then the system time is used
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_gnp_random(graph.handle, n, p, loops, seed)


def ring_graph(graph, n):
    """Generate a ring graph.

    If the graph is directed, then all edges follow the ring consistently.

    :param graph: the graph to alter
    :param n: the number of vertices
    """
    backend.jgrapht_generate_ring(graph.handle, n)


def scalefree_graph(graph, n, seed=None):
    """Generate directed or undirected scale-free graphs of any size. 

    The generated graphs are connected and contains a large number of vertices with 
    small degrees and only a small number of vertices with large degree.

    :param graph: the graph to alter
    :param n: the number of vertices
    :param seed: seed for the random number generator. If None then the system time is used
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_scalefree(graph.handle, n, seed)


def watts_strogatz_graph(graph, n, k, p, add_instead_of_rewire=False, seed=None):
    r"""Watts-Strogatz small-world graph generator.

    The generator is described in the paper: 
     
     * D. J. Watts and S. H. Strogatz. Collective dynamics of small-world networks.
       Nature 393(6684):440--442, 1998.

    .. note::
    
        The following paragraph from the paper describes the construction.

        "The generator starts with a ring of :math:`n` vertices, each connected to its :math:`k`
        nearest neighbors (:math:`k` must be even). Then it chooses a vertex and the edge that
        connects it to its nearest neighbor in a clockwise sense. With probability :math:`p`, it
        reconnects this edge to a vertex chosen uniformly at random over the entire ring with
        duplicate edges forbidden; otherwise it leaves the edge in place. The process is repeated
        by moving clock-wise around the ring, considering each vertex in turn until one lap is
        completed. Next, it considers the edges that connect vertices to their second-nearest
        neighbors clockwise. As before, it randomly rewires each of these edges with probability
        :math:`p`, and continues this process, circulating around the ring and proceeding outward
        to more distant neighbors after each lap, until each edge in the original lattice has been
        considered once. As there are :math:`\frac{nk}{2}` edges in the entire graph, the rewiring
        process stops after :math:`\frac{k}{2}`. For :math:`p=0`, the original ring is unchanged;
        as :math:`p` increases, the graph becomes increasingly disordered until for :math:`p=1`,
        all edges are rewired randomly. For intermediate values of :math:`p`, the graph is a
        small-world network: highly clustered like a regular graph, yet with small characteristic
        path length, like a random graph."

    The authors require :math:`n \gg k \gg \ln(n) \gg 1` and specifically
    :math:`k \gg \ln(n)` guarantees that a random graph will be connected.

    Through the parameters the model can be slightly changed into adding shortcut edges
    instead of re-wiring. This variation was proposed in the paper:

     * M. E. J. Newman and D. J. Watts, Renormalization group analysis of the small-world
       network model, Physics Letters A, 263, 341, 1999.

    :param graph: the graph to alter
    :param n: the number of vertices
    :param k: connect each node to its :math:`k` nearest neighbors in a ring
    :param p: probabilityof re-wiring each edge
    :param add_instead_of_rewire: whether to add shortcut edges instead of re-wiring
    :param seed: seed for the random number generator. If None then the system time is used
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_watts_strogatz(
        graph.handle, n, k, p, add_instead_of_rewire, seed
    )


def kleinberg_smallworld_graph(graph, n, p, q, r, seed=None):
    r"""Kleinberg's small-world graph generator.

    The generator is described in the paper: J. Kleinberg, The Small-World Phenomenon: An Algorithmic
    Perspective, in Proc. 32nd ACM Symp. Theory of Comp., 163-170, 2000.

    The basic structure is a a two-dimensional grid and allows for edges to be directed. It begins
    with a set of nodes (representing individuals in the social network) that are identified with the
    set of lattice points in an :math:`n \times n` square. For a universal constant :math:`p \geq 1`, 
    the node :math:`u` has a directed edge to every other node within lattice distance :math:`p`
    (these are its local contacts). For universal constants :math:`q \geq 0` and :math:`r \geq 0`,
    we also construct directed edges from :math:`u` to :math:`q` other nodes (the long-range contacts)
    using independent random trials; the i-th directed edge from :math:`u` has endpoint :math:`v` with
    probability proportional to :math:`1/d(u,v)^r` where :math:`d(u,v)` is the lattice distance
    from :math:`u` to :math:`v`.

    :param g: the graph to populate
    :param n: generate set of lattice points in a :math:`n` by :math:`n` square
    :param p: lattice distance for which each node is connected to every other node in the lattice (local connections)
    :param q: how many long-range contacts to add for each node
    :param r: probability distribution parameter which is a basic structural parameter measuring how widely "networked" the underlying society of nodes is
    :param seed: seed for the random number generator
    :raises ValueError: in case of invalid parameters
    """
    if seed is None:
        seed = int(time.time())

    backend.jgrapht_generate_kleinberg_smallworld(graph.handle, n, p, q, r, seed)
