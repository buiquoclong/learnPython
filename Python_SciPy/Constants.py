# Nhập thư viện constants từ scipy để sử dụng các hằng số vật lý và toán học
from scipy import constants

# Lấy một số hằng số vật lý phổ biến
speed_of_light = constants.speed_of_light              # Tốc độ ánh sáng trong chân không (m/s)
gravitation_constants = constants.gravitational_constant  # Hằng số hấp dẫn (m^3/kg/s^2)
boltzman_constants = constants.k                        # Hằng số Boltzmann (J/K)

# In ra giá trị các hằng số vật lý
print("Speed Of Light: ", speed_of_light)
print("Gravitation constants: ", gravitation_constants)
print("Boltzman constants: ", boltzman_constants)

# Lấy các hằng số toán học
pi = constants.pi                   # Số Pi ≈ 3.14159
euler_gamma = constants.euler_gamma # Hằng số Euler-Mascheroni ≈ 0.5772
golden_ration = constants.golden    # Tỷ lệ vàng ≈ 1.618

# In ra các hằng số toán học
print(pi)
print(euler_gamma)
print(golden_ration)

# Lấy các hằng số quy đổi đơn vị độ dài và tốc độ
mile_to_meter = constants.mile     # 1 dặm = 1609.344 mét
inch_to_meter = constants.inch     # 1 inch = 0.0254 mét
knot_to_mps = constants.knot       # 1 hải lý/giờ = 0.514444 m/s

# In ra các hằng số quy đổi đơn vị
print(mile_to_meter)
print(inch_to_meter)
print(knot_to_mps)
