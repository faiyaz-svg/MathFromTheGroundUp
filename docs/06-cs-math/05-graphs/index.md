# Graphs

Dots and connections: vertices and edges, degrees, paths and trees, bipartite graphs, colouring, matching and planar drawings.

1. [Graph basics](01-graph-basics.md)
2. [Paths, connectivity and trees](02-paths-connectivity-and-trees.md)
3. [Bipartite graphs, colouring and planar graphs](03-bipartite-coloring-and-planar-graphs.md)

## Cheat sheet

### Graph basics

A simple graph $G = (V, E)$ has a finite nonempty vertex set $V$ and an edge set $E$ of 2-element subsets of $V$ (no loops, no parallel edges). A multigraph allows both. A digraph has ordered pairs (arrows), and is the same thing as a relation on $V$.

| Graph | Vertices | Edges | Degrees |
|---|---|---|---|
| $K_n$ | $n$ | $\frac{n(n-1)}{2}$ | all $n - 1$ |
| $C_n$ ($n \ge 3$) | $n$ | $n$ | all 2 |
| $P_n$ | $n$ | $n - 1$ | 1, 1, rest 2 |
| $K_{m,n}$ | $m + n$ | $mn$ | $n$ and $m$ |
| $Q_n$ | $2^n$ | $n \cdot 2^{n-1}$ | all $n$ |

- Handshake lemma: $\sum_v \deg(v) = 2\lvert E \rvert$. So the number of odd-degree vertices is even. In a digraph, $\sum \deg^+ = \sum \deg^- = \lvert E \rvert$.
- Isomorphism: a bijection that keeps edges and non-edges. Invariants: number of vertices and edges, degree sequence, number of triangles, cycle lengths, connectivity. One differing invariant shows two graphs are not isomorphic; agreeing invariants prove nothing.
- Adjacency matrix: $\Theta(\lvert V \rvert^2)$ space, $\Theta(1)$ edge test, symmetric for undirected graphs, row sums are degrees. Adjacency list: $\Theta(\lvert V \rvert + \lvert E \rvert)$ space, edge test costs the degree. Use lists for sparse graphs. In Python, a dict mapping each vertex to a set of neighbours.
- There are $2^{n(n-1)/2}$ graphs on $n$ named vertices, and 1, 2, 4, 11, 34 up to isomorphism for $n = 1, \dots, 5$.

Main mistakes:

- Sum of degrees equals $\lvert E \rvert$ (it is $2\lvert E \rvert$).
- Counting the edges of $K_n$ as $n^2$ or $n(n-1)$.
- Treating a drawing as the graph: crossings are not vertices.
- Concluding "isomorphic" from equal degree sequences.

### Paths, connectivity and trees

| Term | Repeats allowed |
|---|---|
| walk | vertices and edges |
| trail | vertices, not edges |
| path | neither |
| cycle | closed, length at least 3, no repeated vertex except start = end |

- Every walk from $u$ to $v$ contains a path from $u$ to $v$ (shortest walk argument). "Is connected to" is an equivalence relation; its classes are the components. $c(G) \ge \lvert V \rvert - \lvert E \rvert$.
- Distance $d(u, v)$ is the length of a shortest path, $\infty$ between components.
- BFS from $s$: layers $L_k$ are the vertices at distance $k$. Time $\Theta(\lvert V \rvert + \lvert E \rvert)$ with lists. Parents give a shortest path and a spanning tree. It counts edges, not weights.
- Euler circuit exists iff the graph is connected and every degree is even. An Euler trail that is not closed exists iff exactly two degrees are odd. A Hamilton cycle (every vertex once) has no such test.
- Tree: connected with no cycles. For $n$ vertices, equivalent: tree; unique path between every pair; connected with $n - 1$ edges; acyclic with $n - 1$ edges. Every tree with $n \ge 2$ has at least two leaves. Degrees add up to $2(n - 1)$.
- Rooted tree: parent, child, depth, height. Binary tree of height $h$ has at most $2^{h+1} - 1$ vertices.
- Spanning tree: a tree containing every vertex; every connected graph has one, with $n - 1$ edges. $K_n$ has $n^{n-2}$, $C_n$ has $n$.
- Kruskal: sort edges by weight, add an edge if its ends are in different components, skip it otherwise. Cut property: a lightest edge crossing a cut can be added to a partial minimum spanning tree.
- Walks of length $k$ from $u$ to $v$ are counted by the entry $(u, v)$ of $A^k$.

Main mistakes:

- Thinking $n - 1$ edges alone makes a tree (a triangle plus an isolated vertex has 3 edges on 4 vertices).
- Calling a closed walk along one edge and back a cycle.
- Skipping a Kruskal edge because it touches a used vertex; the test is same component.
- Using BFS for weighted shortest paths.

### Bipartite graphs, colouring and planar graphs

- Bipartite: the vertices split into two parts and every edge crosses. A graph is bipartite iff it has no odd cycle. Test: BFS with two colours (parity of distance); a same-coloured edge gives an odd cycle. Bipartite with $n$ vertices has at most $\lfloor n^2 / 4 \rfloor$ edges.
- Matching: edges with no shared vertex. Hall's theorem: a bipartite graph with parts $X, Y$ has a matching saturating $X$ iff $\lvert N(S) \rvert \ge \lvert S \rvert$ for every $S \subseteq X$. A bad set $S$ proves no matching exists. Every $k$-regular bipartite graph ($k \ge 1$) has a perfect matching.
- Proper colouring: adjacent vertices get different colours. $\chi(G)$ is the fewest colours.

| Graph | $\chi$ |
|---|---|
| $K_n$ | $n$ |
| even cycle, tree, $K_{m,n}$ | 2 |
| odd cycle | 3 |
| no edges | 1 |

- To prove $\chi = k$: give a $k$-colouring and a reason $k - 1$ fail (a $K_k$ subgraph, or an odd cycle for $k = 3$).
- Greedy colouring uses at most $\Delta + 1$ colours in any order, so $\chi \le \Delta + 1$. The order can make it worse than $\chi$.
- Planar: some drawing has no crossings. Euler: connected plane graph has $V - E + F = 2$ (with $c$ components, $1 + c$). Simple connected planar, $V \ge 3$: $E \le 3V - 6$, and $E \le 2V - 4$ with no triangles. So $K_5$ and $K_{3,3}$ are not planar. Every planar graph has a vertex of degree at most 5 and is 6-colourable. Four colour theorem: 4 colours suffice (stated).

Main mistakes:

- Using $E \le 3V - 6$ to prove planarity. It only rules graphs out.
- Deciding a graph is non-planar from one drawing with crossings.
- Applying $V - E + F = 2$ to a disconnected graph.
- Believing greedy colouring is optimal.
