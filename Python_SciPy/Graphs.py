import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

array = np.array([
    [0, -1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [0, 1, 0, 1],
])

new_array = csr_matrix(array)
print(connected_components(new_array))

print(dijkstra(new_array, return_predecessors=True, indices=0))

print(floyd_warshall(new_array, return_predecessors=True))

print(bellman_ford(new_array, return_predecessors=True, indices=0))

print(depth_first_order(new_array, 1))

print(breadth_first_order(new_array, 1))