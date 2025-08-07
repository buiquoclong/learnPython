from scipy.optimize import minimize_scalar
from scipy.optimize import differential_evolution

# Định nghĩa hàm mục tiêu 1 biến: (x - 3)^2 + 5
def quadratic_function(x):
    return (x - 3) ** 2 + 5

# Định nghĩa hàm mục tiêu 2 biến: x^2 + y^2 (vector x gồm 2 phần tử)
def global_objective(x):
    return x[0] ** 2 + x[1] ** 2

# Tối ưu hàm một biến bằng thuật toán minimize_scalar
result_minimize_scalar = minimize_scalar(quadratic_function)
print("Optimal Solution: ", result_minimize_scalar.x)   # Giá trị x tối ưu
print("Minimum Value: ", result_minimize_scalar.fun)    # Giá trị hàm tại x tối ưu

# Tối ưu hàm đa biến bằng thuật toán tiến hóa khác biệt (differential evolution)
# Phạm vi tìm kiếm cho mỗi biến là từ -2 đến 2
result_differential_evolution = differential_evolution(global_objective, [(-2, 2), (-2, 2)])
print("Global Optimal Solution: ", result_differential_evolution.x)  # Nghiệm tối ưu (x, y)
print("Global Minimum Value: ", result_differential_evolution.fun)   # Giá trị hàm tại nghiệm tối ưu
