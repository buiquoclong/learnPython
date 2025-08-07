# Nhập các thư viện cần thiết
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

# Tạo một ma trận numpy đại diện cho trọng số cạnh của đồ thị (0: không có cạnh)
array = np.array([
    [0, -1, 0, 1],  # Hàng 0
    [1, 1, 1, 1],   # Hàng 1
    [2, 1, 1, 1],   # Hàng 2
    [0, 1, 0, 1],   # Hàng 3
])

# Chuyển ma trận numpy sang dạng ma trận thưa CSR (Compressed Sparse Row) để xử lý hiệu quả hơn
new_array = csr_matrix(array)

# Tìm số lượng thành phần liên thông trong đồ thị và phân nhóm các đỉnh theo thành phần
print(connected_components(new_array))
# Kết quả trả về tuple: (số thành phần liên thông, mảng đánh dấu thành phần của từng đỉnh)

# Tính đường đi ngắn nhất từ đỉnh 0 tới các đỉnh khác sử dụng thuật toán Dijkstra
# return_predecessors=True để trả về cả mảng các đỉnh trước trên đường đi ngắn nhất
print(dijkstra(new_array, return_predecessors=True, indices=0))

# Tính tất cả cặp đường đi ngắn nhất trong đồ thị sử dụng thuật toán Floyd-Warshall
print(floyd_warshall(new_array, return_predecessors=True))

# Tính đường đi ngắn nhất từ đỉnh 0 sử dụng thuật toán Bellman-Ford (cho phép trọng số âm)
print(bellman_ford(new_array, return_predecessors=True, indices=0))

# Thực hiện duyệt đồ thị theo chiều sâu (DFS) bắt đầu từ đỉnh 1
print(depth_first_order(new_array, 1))

# Thực hiện duyệt đồ thị theo chiều rộng (BFS) bắt đầu từ đỉnh 1
print(breadth_first_order(new_array, 1))
